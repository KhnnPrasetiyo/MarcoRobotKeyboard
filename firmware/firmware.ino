/**
 * Arduino Nano Keyboard Robot Controller Firmware
 * 
 * Hardware:
 *   - Arduino Nano V3
 *   - 6 MG90S Servos
 *   - D2 = LEFT, D3 = RIGHT, D4 = UP, D5 = DOWN, D6 = SHIFT, D7 = A
 *   - D8 = START, D9 = STOP, D10 = EMERGENCY STOP
 *   - D11 = STATUS LED (Arduino), D12 = SERVO LED (Active movement indicator)
 */

#include <Servo.h>
#include <EEPROM.h>

// ==========================================
// PIN CONFIGURATION & CONSTANTS
// ==========================================
const int NUM_SERVOS = 6;
const int SERVO_PINS[NUM_SERVOS] = {2, 3, 4, 5, 6, 7};

// Buttons (Internal pull-up)
const int PIN_START_BTN = 8;
const int PIN_STOP_BTN = 9;
const int PIN_ESTOP_BTN = 10;

// LEDs
const int PIN_LED_STATUS = 11;
const int PIN_LED_SERVO = 12;

// EEPROM Constants
const byte EEPROM_MAGIC = 0xAB;
const int MAX_PATTERNS = 150;

// Supported Action Types
enum ActionType {
  NONE_ACT = 0,
  LEFT = 1,
  RIGHT = 2,
  UP = 3,
  DOWN = 4,
  A = 5,
  BLINK_LEFT = 6,
  BLINK_RIGHT = 7,
  BLINK_UP = 8,
  BLINK_DOWN = 9
};

// ==========================================
// DATA STRUCTURES
// ==========================================
struct ServoCalibration {
  byte up_angle;
  byte press_angle;
};

struct Action {
  byte type;
  uint16_t press_duration;
  uint16_t delay_duration;
};

struct RobotSettings {
  byte auto_start;
  byte loop_mode; // 0 = INFINITY, 1 = CUSTOM
  uint16_t loop_count;
  byte random_delay_enabled;
  uint16_t random_delay_min;
  uint16_t random_delay_max;
};

// ==========================================
// SYSTEM STATE
// ==========================================
enum SystemState {
  STATE_IDLE,
  STATE_RUNNING,
  STATE_STOPPED,
  STATE_ESTOP
};

SystemState currentState = STATE_IDLE;
ServoCalibration calibration[NUM_SERVOS];
RobotSettings settings;
int patternLength = 0;
Action pattern[MAX_PATTERNS];

Servo servos[NUM_SERVOS];
bool servosAttached = false;

// Executor State Machine Variables
int currentActionIndex = 0;
int currentLoopIteration = 0;
unsigned long stepTimer = 0;
bool isPressingPhase = false;
bool actionActuated = false;
bool shiftActuated = false;
unsigned long currentTargetDelay = 0;

// ==========================================
// EEPROM MANAGER
// ==========================================
namespace EEPROMManager {
  void loadConfig() {
    int addr = 0;
    byte magic = EEPROM.read(addr++);
    if (magic != EEPROM_MAGIC) {
      Serial.println(F("[EEPROM] Magic byte mismatch. Initializing default configuration."));
      // Default calibration
      for (int i = 0; i < NUM_SERVOS; i++) {
        calibration[i].up_angle = 90;
        calibration[i].press_angle = 45;
      }
      settings.auto_start = 0;
      settings.loop_mode = 0;
      settings.loop_count = 1;
      settings.random_delay_enabled = 0;
      settings.random_delay_min = 200;
      settings.random_delay_max = 1000;
      patternLength = 0;
      return;
    }

    // Load Calibration (12 bytes)
    for (int i = 0; i < NUM_SERVOS; i++) {
      calibration[i].up_angle = EEPROM.read(addr++);
      calibration[i].press_angle = EEPROM.read(addr++);
    }

    // Load Settings
    settings.auto_start = EEPROM.read(addr++);
    settings.loop_mode = EEPROM.read(addr++);
    
    byte high = EEPROM.read(addr++);
    byte low = EEPROM.read(addr++);
    settings.loop_count = (high << 8) | low;

    settings.random_delay_enabled = EEPROM.read(addr++);
    
    high = EEPROM.read(addr++);
    low = EEPROM.read(addr++);
    settings.random_delay_min = (high << 8) | low;

    high = EEPROM.read(addr++);
    low = EEPROM.read(addr++);
    settings.random_delay_max = (high << 8) | low;

    // Load Pattern Length
    patternLength = EEPROM.read(addr++);
    if (patternLength > MAX_PATTERNS) patternLength = MAX_PATTERNS;

    // Load Actions
    for (int i = 0; i < patternLength; i++) {
      pattern[i].type = EEPROM.read(addr++);
      
      high = EEPROM.read(addr++);
      low = EEPROM.read(addr++);
      pattern[i].press_duration = (high << 8) | low;

      high = EEPROM.read(addr++);
      low = EEPROM.read(addr++);
      pattern[i].delay_duration = (high << 8) | low;
    }
    Serial.println(F("[EEPROM] Configuration loaded successfully."));
  }

  void saveHexConfig(const String& hexData) {
    // Parse hex string back to bytes and write to EEPROM
    int len = hexData.length() / 2;
    int addr = 0;
    
    // Write Magic Byte first
    EEPROM.write(addr++, EEPROM_MAGIC);

    for (int i = 0; i < len; i++) {
      String byteHex = hexData.substring(i * 2, i * 2 + 2);
      byte val = strtol(byteHex.c_str(), NULL, 16);
      EEPROM.write(addr++, val);
    }
    Serial.println(F("[EEPROM] Configuration saved. Reloading..."));
    loadConfig();
  }

  void dumpConfig() {
    // Read entire stored EEPROM payload and print hex
    Serial.print(F("CONFIG_DUMP:"));
    int addr = 1; // Skip magic byte for clean direct config dump
    
    // Print Calibration (12 bytes)
    for (int i = 0; i < NUM_SERVOS * 2; i++) {
      byte val = EEPROM.read(addr++);
      if (val < 16) Serial.print('0');
      Serial.print(val, HEX);
    }
    
    // Print Settings (9 bytes)
    for (int i = 0; i < 9; i++) {
      byte val = EEPROM.read(addr++);
      if (val < 16) Serial.print('0');
      Serial.print(val, HEX);
    }
    
    // Print Pattern Length
    byte pLen = EEPROM.read(addr++);
    if (pLen < 16) Serial.print('0');
    Serial.print(pLen, HEX);

    // Print Actions
    for (int i = 0; i < pLen * 5; i++) {
      byte val = EEPROM.read(addr++);
      if (val < 16) Serial.print('0');
      Serial.print(val, HEX);
    }
    Serial.println();
  }
}

// ==========================================
// SERVO MANAGER
// ==========================================
namespace ServoManager {
  void attachAll() {
    if (servosAttached) return;
    for (int i = 0; i < NUM_SERVOS; i++) {
      servos[i].attach(SERVO_PINS[i]);
    }
    servosAttached = true;
    digitalWrite(PIN_LED_SERVO, HIGH);
  }

  void detachAll() {
    if (!servosAttached) return;
    for (int i = 0; i < NUM_SERVOS; i++) {
      servos[i].detach();
    }
    servosAttached = false;
    digitalWrite(PIN_LED_SERVO, LOW);
  }

  void moveServo(int index, byte angle) {
    if (index < 0 || index >= NUM_SERVOS) return;
    attachAll();
    servos[index].write(angle);
  }

  void setAllUP() {
    for (int i = 0; i < NUM_SERVOS; i++) {
      moveServo(i, calibration[i].up_angle);
    }
    // Briefly delay to let servos complete travel before detach
    delay(200);
    detachAll();
  }
}

// ==========================================
// PATTERN EXECUTOR (Non-blocking)
// ==========================================
namespace PatternExecutor {
  const unsigned long COMBO_INITIAL_DELAY = 150; // Jeda penekanan awal arah sebelum shift (dalam ms)

  void stop() {
    if (currentState == STATE_RUNNING) {
      currentState = STATE_STOPPED;
      actionActuated = false;
      ServoManager::setAllUP();
      Serial.println(F("STATE:STOPPED"));
    }
  }

  void estop() {
    currentState = STATE_ESTOP;
    actionActuated = false;
    ServoManager::setAllUP();
    Serial.println(F("STATE:EMERGENCY_STOP"));
  }

  void start() {
    if (patternLength == 0) {
      Serial.println(F("[Executor] Cannot start. Empty pattern sequence."));
      return;
    }
    currentState = STATE_RUNNING;
    currentActionIndex = 0;
    currentLoopIteration = 0;
    isPressingPhase = true;
    actionActuated = false;
    shiftActuated = false;
    stepTimer = millis();
    ServoManager::attachAll();
    Serial.println(F("STATE:RUNNING"));
    // Kirim progres langkah awal
    Serial.print(F("STEP:"));
    Serial.print(1);
    Serial.print(F("/"));
    Serial.println(patternLength);
  }

  void executeActiveStep() {
    if (currentState != STATE_RUNNING) return;

    Action active = pattern[currentActionIndex];
    unsigned long now = millis();

    if (isPressingPhase) {
      // Actuating physical action
      if (!actionActuated) {
        if (active.type == NONE_ACT) {
          // Do nothing (pure delay phase)
        } else if (active.type >= BLINK_LEFT && active.type <= BLINK_DOWN) {
          // Step 1 of BLINK: Press Direction key first
          int raw_idx = active.type - 6; // BLINK_LEFT=6 -> physical servo 0, etc.
          ServoManager::moveServo(raw_idx, calibration[raw_idx].press_angle);
          shiftActuated = false; // Shift is not pressed yet
        } else {
          // Direct key press
          int raw_idx = active.type - 1;
          if (active.type == A) {
            raw_idx = 5; // A corresponds to physical servo 5
          }
          ServoManager::moveServo(raw_idx, calibration[raw_idx].press_angle);
        }
        actionActuated = true;
      }

      // Step 2 of BLINK (Non-blocking): Press Shift after COMBO_INITIAL_DELAY
      if (active.type >= BLINK_LEFT && active.type <= BLINK_DOWN && !shiftActuated) {
        if (now - stepTimer >= COMBO_INITIAL_DELAY) {
          ServoManager::moveServo(4, calibration[4].press_angle); // SHIFT
          shiftActuated = true;
        }
      }

      if (now - stepTimer >= active.press_duration) {
        // Shift to Delay / Release phase
        isPressingPhase = false;
        actionActuated = false;
        shiftActuated = false;
        stepTimer = now;
        
        // Release all
        if (active.type == NONE_ACT) {
          // Do nothing
        } else if (active.type >= BLINK_LEFT && active.type <= BLINK_DOWN) {
          ServoManager::moveServo(4, calibration[4].up_angle); // SHIFT
          int raw_idx = active.type - 6; // BLINK_LEFT=6 -> physical servo 0, etc.
          ServoManager::moveServo(raw_idx, calibration[raw_idx].up_angle);
        } else {
          int raw_idx = active.type - 1;
          if (active.type == A) {
            raw_idx = 5; // A corresponds to physical servo 5
          }
          ServoManager::moveServo(raw_idx, calibration[raw_idx].up_angle);
        }

        // Hitung target delay SEKALI saat transisi ke fase jeda
        currentTargetDelay = active.delay_duration;
        if (settings.random_delay_enabled) {
          currentTargetDelay = random(settings.random_delay_min, settings.random_delay_max + 1);
        }
      }
    } else {
      // Delay phase (menggunakan currentTargetDelay yang sudah dihitung sekali)

      if (now - stepTimer >= currentTargetDelay) {
        // Move to next action item
        currentActionIndex++;
        if (currentActionIndex >= patternLength) {
          currentActionIndex = 0;
          currentLoopIteration++;
          
          if (settings.loop_mode == 1 && currentLoopIteration >= settings.loop_count) {
            // Completed custom loops
            stop();
            return;
          }
        }
        
        // Kirim progres langkah ke serial (jika PC terhubung)
        Serial.print(F("STEP:"));
        Serial.print(currentActionIndex + 1);
        Serial.print(F("/"));
        Serial.println(patternLength);

        isPressingPhase = true;
        stepTimer = now;
      }
    }
  }
}

// ==========================================
// SERIAL PROTOCOL HANDLER
// ==========================================
void handleSerial() {
  if (Serial.available() <= 0) return;

  String input = Serial.readStringUntil('\n');
  input.trim();
  if (input.length() == 0) return;

  if (input == F("PING")) {
    Serial.println(F("PONG"));
  } 
  else if (input.startsWith(F("TEST_SERVO"))) {
    // Format: TEST_SERVO <index> <angle>
    int firstSpace = input.indexOf(' ');
    int secondSpace = input.indexOf(' ', firstSpace + 1);
    if (firstSpace != -1 && secondSpace != -1) {
      int idx = input.substring(firstSpace + 1, secondSpace).toInt();
      int angle = input.substring(secondSpace + 1).toInt();
      ServoManager::moveServo(idx, angle);
      Serial.println(F("OK"));
    } else {
      Serial.println(F("ERROR: Invalid TEST_SERVO syntax"));
    }
  } 
  else if (input.startsWith(F("WRITE_CONFIG"))) {
    // Format: WRITE_CONFIG <hex>
    int space = input.indexOf(' ');
    if (space != -1) {
      String hexData = input.substring(space + 1);
      EEPROMManager::saveHexConfig(hexData);
      Serial.println(F("OK"));
    } else {
      Serial.println(F("ERROR: Missing config hex payload"));
    }
  } 
  else if (input == F("READ_CONFIG")) {
    EEPROMManager::dumpConfig();
  } 
  else if (input == F("START")) {
    PatternExecutor::start();
  } 
  else if (input == F("STOP")) {
    PatternExecutor::stop();
  } 
  else if (input == F("ESTOP")) {
    PatternExecutor::estop();
  } 
  else if (input == F("STATUS")) {
    if (currentState == STATE_RUNNING) Serial.println(F("STATE:RUNNING"));
    else if (currentState == STATE_STOPPED) Serial.println(F("STATE:STOPPED"));
    else if (currentState == STATE_ESTOP) Serial.println(F("STATE:EMERGENCY_STOP"));
    else Serial.println(F("STATE:IDLE"));
  } 
  else {
    Serial.println(F("ERROR: Unknown Command"));
  }
}

// ==========================================
// CORE SETUP & LOOP
// ==========================================
void setup() {
  Serial.begin(115200);
  while (!Serial) { ; } // wait for serial port to connect

  // Initialize random seed SEKALI di setup
  randomSeed(analogRead(A0));

  // Initialize Input Buttons
  pinMode(PIN_START_BTN, INPUT_PULLUP);
  pinMode(PIN_STOP_BTN, INPUT_PULLUP);
  pinMode(PIN_ESTOP_BTN, INPUT_PULLUP);

  // Initialize Outputs
  pinMode(PIN_LED_STATUS, OUTPUT);
  pinMode(PIN_LED_SERVO, OUTPUT);

  digitalWrite(PIN_LED_STATUS, LOW);
  digitalWrite(PIN_LED_SERVO, LOW);

  // Load EEPROM Calibration & Config
  EEPROMManager::loadConfig();

  // Reset servos to UP position
  ServoManager::setAllUP();

  // Auto Start if enabled
  if (settings.auto_start == 1) {
    PatternExecutor::start();
  }
}

void loop() {
  // Read Serial commands
  handleSerial();

  // Read hardware buttons (dengan debounce)
  if (digitalRead(PIN_ESTOP_BTN) == LOW && currentState != STATE_ESTOP) {
    delay(50);
    if (digitalRead(PIN_ESTOP_BTN) == LOW) {
      PatternExecutor::estop();
    }
  } 
  else if (digitalRead(PIN_START_BTN) == LOW && currentState != STATE_RUNNING) {
    // Debounce simple trigger
    delay(50);
    if (digitalRead(PIN_START_BTN) == LOW) {
      PatternExecutor::start();
    }
  } 
  else if (digitalRead(PIN_STOP_BTN) == LOW && currentState == STATE_RUNNING) {
    delay(50);
    if (digitalRead(PIN_STOP_BTN) == LOW) {
      PatternExecutor::stop();
    }
  }

  // Handle running loop execution
  if (currentState == STATE_RUNNING) {
    PatternExecutor::executeActiveStep();
    
    // Fast flash STATUS LED during execution
    digitalWrite(PIN_LED_STATUS, (millis() / 150) % 2);
  } else if (currentState == STATE_ESTOP) {
    // Rapid strobe warning
    digitalWrite(PIN_LED_STATUS, (millis() / 50) % 2);
  } else {
    // Gentle heartbeat breathing when idle
    digitalWrite(PIN_LED_STATUS, (millis() / 1000) % 2);
  }
}
