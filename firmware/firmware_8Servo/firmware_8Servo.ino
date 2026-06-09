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
const int NUM_SERVOS = 8;
const int SERVO_PINS[NUM_SERVOS] = {2, 3, 4, 5, 6, 7, 8, 9};

// Buttons (Internal pull-up)
const int PIN_START_BTN = A0;
const int PIN_STOP_BTN = A1;
const int PIN_ESTOP_BTN = A2;

// LEDs
const int PIN_LED_STATUS = A3;
const int PIN_LED_SERVO = A4;

// EEPROM Constants
const byte EEPROM_MAGIC = 0xAC; // Bumped: settings layout +1 byte (random_skip_enabled)
const int MAX_PATTERNS = 150;

// Supported Action Types
enum ActionType {
  NONE_ACT = 0,
  LEFT = 1,
  RIGHT = 2,
  UP = 3,
  DOWN = 4,
  A = 5,
  SHIFT = 6,
  ALT = 7,
  SPACE = 8,
  BLINK_LEFT = 9,
  BLINK_RIGHT = 10,
  BLINK_UP = 11,
  BLINK_DOWN = 12
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
  uint16_t blink_init_delay;
  uint16_t blink_hold_delay;
  uint16_t blink_release_delay;
  byte random_skip_enabled; // 50% chance to skip one BLINK + pair per loop
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

// Skip mask: which actions to skip in the current loop iteration
bool skipMask[MAX_PATTERNS];

// Executor State Machine Variables
int currentActionIndex = 0;
int currentLoopIteration = 0;
unsigned long stepTimer = 0;
bool isPressingPhase = false;
bool actionActuated = false;
bool shiftActuated = false;
bool shiftReleased = false;
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
      settings.blink_init_delay = 120;
      settings.blink_hold_delay = 200;
      settings.blink_release_delay = 120;
      settings.random_skip_enabled = 0;
      patternLength = 0;
      for (int i = 0; i < MAX_PATTERNS; i++) skipMask[i] = false;
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

    high = EEPROM.read(addr++);
    low = EEPROM.read(addr++);
    settings.blink_init_delay = (high << 8) | low;

    high = EEPROM.read(addr++);
    low = EEPROM.read(addr++);
    settings.blink_hold_delay = (high << 8) | low;

    high = EEPROM.read(addr++);
    low = EEPROM.read(addr++);
    settings.blink_release_delay = (high << 8) | low;

    settings.random_skip_enabled = EEPROM.read(addr++);

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

  void saveHexConfigFromSerial() {
    // Write Magic Byte first
    int addr = 0;
    EEPROM.update(addr++, EEPROM_MAGIC);
    
    bool success = true;
    unsigned long writeStartMs = millis();
    
    // Skip any leading spaces
    while (true) {
      int next = Serial.peek();
      if (next == ' ') {
        Serial.read();
      } else {
        break;
      }
    }
    
    while (true) {
      // Wait for at least 2 characters or a newline/carriage return
      while (Serial.available() < 2) {
        if (Serial.available() > 0) {
          char nextChar = Serial.peek();
          if (nextChar == '\n' || nextChar == '\r') {
            break;
          }
        }
        if (millis() - writeStartMs > 3000) { // 3 seconds timeout
          success = false;
          break;
        }
      }
      if (!success) break;
      
      // Check if we hit the end of the line
      if (Serial.available() > 0 && (Serial.peek() == '\n' || Serial.peek() == '\r')) {
        // Read out all newlines/carriage returns
        while (Serial.available() > 0 && (Serial.peek() == '\n' || Serial.peek() == '\r')) {
          Serial.read();
        }
        break;
      }
      
      char c1 = Serial.read();
      char c2 = Serial.read();
      
      // Convert c1 and c2 from hex to byte
      byte val = 0;
      if (c1 >= '0' && c1 <= '9') val += (c1 - '0') << 4;
      else if (c1 >= 'A' && c1 <= 'F') val += (c1 - 'A' + 10) << 4;
      else if (c1 >= 'a' && c1 <= 'f') val += (c1 - 'a' + 10) << 4;
      else { success = false; break; }
      
      if (c2 >= '0' && c2 <= '9') val += (c2 - '0');
      else if (c2 >= 'A' && c2 <= 'F') val += (c2 - 'A' + 10);
      else if (c2 >= 'a' && c2 <= 'f') val += (c2 - 'a' + 10);
      else { success = false; break; }
      
      EEPROM.update(addr++, val);
      writeStartMs = millis();
    }
    
    if (success) {
      Serial.println(F("[EEPROM] Configuration saved. Reloading..."));
      loadConfig();
      Serial.println(F("OK"));
    } else {
      Serial.println(F("ERROR: Write failed or invalid hex"));
    }
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
    
    // Print Settings (16 bytes)
    for (int i = 0; i < 16; i++) {
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
      servos[i].write(calibration[i].up_angle); // Set up angle before attach to prevent snapping/jitter
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
  const unsigned long COMBO_INITIAL_DELAY = 80; // Jeda penekanan awal arah sebelum shift (dalam ms)

  // --------------------------------------------------------
  // buildSkipMask: dipanggil di awal setiap loop iterasi.
  // Dengan peluang 50%, memilih SATU aksi BLINK secara acak
  // untuk di-skip, beserta pasangannya (arah berlawanan).
  // --------------------------------------------------------
  void buildSkipMask() {
    for (int i = 0; i < patternLength; i++) skipMask[i] = false;
    if (!settings.random_skip_enabled || patternLength == 0) return;

    // 50% chance to skip this loop
    if (random(0, 100) >= 50) return;

    // Fixed 50% vertical vs horizontal mode
    bool verticalMode = random(0, 100) < 50; // 50% chance vertical

    if (verticalMode) {
        // Collect indices of vertical blink actions (UP/DOWN)
        int vertIdx[MAX_PATTERNS];
        int vertCount = 0;
        for (int i = 0; i < patternLength; i++) {
            byte t = pattern[i].type;
            if (t == BLINK_UP || t == BLINK_DOWN) {
                vertIdx[vertCount++] = i;
            }
        }
        if (vertCount == 0) return;
        int chosen = vertIdx[random(0, vertCount)];
        byte ct = pattern[chosen].type;
        if (ct == BLINK_UP) {
            // Skip chosen UP and nearest DOWN partner
            skipMask[chosen] = true;
            Serial.print(F("[DEBUG-SKIP] Skipping BLINK UP index "));
            Serial.println(chosen);
            bool found = false;
            for (int i = chosen + 1; i < patternLength; i++) {
                if (pattern[i].type == BLINK_DOWN) {
                    skipMask[i] = true;
                    Serial.print(F("[DEBUG-SKIP] Skipping paired DOWN index "));
                    Serial.println(i);
                    found = true;
                    break;
                }
            }
            if (!found) {
                for (int i = chosen - 1; i >= 0; i--) {
                    if (pattern[i].type == BLINK_DOWN) {
                        skipMask[i] = true;
                        Serial.print(F("[DEBUG-SKIP] Skipping paired DOWN index "));
                        Serial.println(i);
                        break;
                    }
                }
            }
        }
        // If DOWN selected, normal behavior (no skip)
    } else {
        // Horizontal mode
        int horizIdx[MAX_PATTERNS];
        int horizCount = 0;
        for (int i = 0; i < patternLength; i++) {
            byte t = pattern[i].type;
            if (t == BLINK_LEFT || t == BLINK_RIGHT) {
                horizIdx[horizCount++] = i;
            }
        }
        if (horizCount == 0) return;
        int chosen = horizIdx[random(0, horizCount)];
        byte ct = pattern[chosen].type;
        if (ct == BLINK_RIGHT) {
            // Skip all horizontal actions
            for (int i = 0; i < patternLength; i++) {
                if (pattern[i].type == BLINK_LEFT || pattern[i].type == BLINK_RIGHT) {
                    skipMask[i] = true;
                }
            }
            Serial.print(F("[DEBUG-SKIP] Skipping all horizontal, chosen RIGHT index "));
            Serial.println(chosen);
            // Keep nearest LEFT pair (forward then backward)
            bool kept = false;
            for (int i = chosen + 1; i < patternLength; i++) {
                if (pattern[i].type == BLINK_LEFT) {
                    skipMask[i] = false;
                    Serial.print(F("[DEBUG-SKIP] Keeping paired LEFT index "));
                    Serial.println(i);
                    kept = true;
                    break;
                }
            }
            if (!kept) {
                for (int i = chosen - 1; i >= 0; i--) {
                    if (pattern[i].type == BLINK_LEFT) {
                        skipMask[i] = false;
                        Serial.print(F("[DEBUG-SKIP] Keeping paired LEFT index "));
                        Serial.println(i);
                        break;
                    }
                }
            }
            // Chosen RIGHT remains skipped
        }
        // If LEFT selected, normal behavior (no skip)
    }
  }

  void stop() {
    if (currentState == STATE_RUNNING) {
      currentState = STATE_STOPPED;
      actionActuated = false;
      shiftActuated = false;
      shiftReleased = false;
      ServoManager::setAllUP();
      Serial.println(F("STATE:STOPPED"));
    }
  }

  void estop() {
    currentState = STATE_ESTOP;
    actionActuated = false;
    shiftActuated = false;
    shiftReleased = false;
    ServoManager::setAllUP();
    Serial.println(F("STATE:EMERGENCY_STOP"));
  }

  void start() {
    if (patternLength == 0) {
      Serial.println(F("[Executor] Cannot start. Empty pattern sequence."));
      return;
    }
    
    // Attach all servos and set them to their up_angle, then wait for them to settle
    ServoManager::attachAll();
    for (int i = 0; i < NUM_SERVOS; i++) {
      servos[i].write(calibration[i].up_angle);
    }
    delay(500); // 500ms delay to make sure all servos are physically ready
    
    currentState = STATE_RUNNING;
    currentActionIndex = 0;
    currentLoopIteration = 0;
    isPressingPhase = true;
    actionActuated = false;
    shiftActuated = false;
    shiftReleased = false;
    stepTimer = millis();
    buildSkipMask(); // Hitung skip mask untuk loop pertama
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

    unsigned long target_press_duration = active.press_duration;
    if (active.type >= BLINK_LEFT && active.type <= BLINK_DOWN) {
      target_press_duration = settings.blink_init_delay + settings.blink_hold_delay + settings.blink_release_delay;
    }

    if (isPressingPhase) {
      // Cek apakah aksi ini harus di-skip (fitur random skip)
      if (skipMask[currentActionIndex]) {
        // Lewati fase penekanan, langsung ke fase jeda
        isPressingPhase = false;
        actionActuated = false;
        shiftActuated = false;
        shiftReleased = false;
        stepTimer = now;
        currentTargetDelay = active.delay_duration;
        if (settings.random_delay_enabled) {
          currentTargetDelay = random(settings.random_delay_min, settings.random_delay_max + 1);
        }
        return;
      }

      // Actuating physical action
      if (!actionActuated) {
        if (active.type == NONE_ACT) {
          // Do nothing (pure delay phase)
        } else if (active.type >= BLINK_LEFT && active.type <= BLINK_DOWN) {
          // Step 1 of BLINK: Press Direction key first
          int raw_idx = active.type - BLINK_LEFT; // BLINK_LEFT=9 -> physical servo 0, etc.
          ServoManager::moveServo(raw_idx, calibration[raw_idx].press_angle);
          shiftActuated = false; // Shift is not pressed yet
          shiftReleased = false;
        } else {
          // Direct key press
          int raw_idx = active.type - 1;
          ServoManager::moveServo(raw_idx, calibration[raw_idx].press_angle);
        }
        actionActuated = true;
      }

      // Step 2 of BLINK (Non-blocking): Press Shift after settings.blink_init_delay
      if (active.type >= BLINK_LEFT && active.type <= BLINK_DOWN) {
        if (!shiftActuated && (now - stepTimer >= settings.blink_init_delay)) {
          ServoManager::moveServo(5, calibration[5].press_angle); // SHIFT (Servo index 5)
          shiftActuated = true;
        }
        // Step 3 of BLINK (Non-blocking): Release Shift after settings.blink_init_delay + settings.blink_hold_delay
        unsigned long release_time = settings.blink_init_delay + settings.blink_hold_delay;
        if (shiftActuated && !shiftReleased && (now - stepTimer >= release_time)) {
          ServoManager::moveServo(5, calibration[5].up_angle); // SHIFT (Servo index 5)
          shiftReleased = true;
        }
      }

      if (now - stepTimer >= target_press_duration) {
        // Shift to Delay / Release phase
        isPressingPhase = false;
        actionActuated = false;
        shiftActuated = false;
        shiftReleased = false;
        stepTimer = now;
        
        // Release all
        if (active.type == NONE_ACT) {
          // Do nothing
        } else if (active.type >= BLINK_LEFT && active.type <= BLINK_DOWN) {
          // Ensure SHIFT is released if not already
          ServoManager::moveServo(5, calibration[5].up_angle); // SHIFT (Servo index 5)
          int raw_idx = active.type - BLINK_LEFT; // BLINK_LEFT=9 -> physical servo 0, etc.
          ServoManager::moveServo(raw_idx, calibration[raw_idx].up_angle);
        } else {
          int raw_idx = active.type - 1;
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
          buildSkipMask(); // Hitung ulang skip mask untuk loop baru

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

  // Skip leading whitespace/newlines/carriage returns
  while (true) {
    int next = Serial.peek();
    if (next == -1) return; // No more data
    if (next == ' ' || next == '\n' || next == '\r' || next == '\t') {
      Serial.read(); // Consume it
    } else {
      break;
    }
  }
  
  if (Serial.available() <= 0) return;

  // Read command word (until space or newline, max 20 chars)
  char cmd[20];
  int cmdLen = 0;
  unsigned long startMs = millis();
  
  while (cmdLen < 19) {
    if (Serial.available() > 0) {
      char c = Serial.read();
      if (c == ' ' || c == '\n' || c == '\r' || c == '\t') {
        break;
      }
      cmd[cmdLen++] = c;
    } else {
      if (millis() - startMs > 100) { // 100ms timeout
        break;
      }
    }
  }
  cmd[cmdLen] = '\0';
  
  if (cmdLen == 0) return;

  if (strcmp(cmd, "WRITE_CONFIG") == 0) {
    EEPROMManager::saveHexConfigFromSerial();
  } 
  else {
    // For all other commands, read the rest of the line (which is guaranteed to be short)
    String rest = Serial.readStringUntil('\n');
    rest.trim();
    
    if (strcmp(cmd, "PING") == 0) {
      Serial.println(F("PONG"));
    }
    else if (strcmp(cmd, "SEED") == 0) {
      long seed = rest.toInt();
      randomSeed(seed);
      Serial.println(F("OK"));
    }
    else if (strcmp(cmd, "TEST_SERVO") == 0) {
      int space = rest.indexOf(' ');
      if (space != -1) {
        int idx = rest.substring(0, space).toInt();
        int angle = rest.substring(space + 1).toInt();
        ServoManager::moveServo(idx, angle);
        Serial.println(F("OK"));
      } else {
        Serial.println(F("ERROR: Invalid TEST_SERVO syntax"));
      }
    }
    else if (strcmp(cmd, "READ_CONFIG") == 0) {
      EEPROMManager::dumpConfig();
    }
    else if (strcmp(cmd, "TEST_BLINK") == 0) {
      int servoIdx = -1;
      if (rest == "LEFT")       servoIdx = 0;
      else if (rest == "RIGHT") servoIdx = 1;
      else if (rest == "UP")    servoIdx = 2;
      else if (rest == "DOWN")  servoIdx = 3;

      if (servoIdx >= 0 && servoIdx < 4) {
        ServoManager::attachAll();
        servos[servoIdx].write(calibration[servoIdx].press_angle);
        delay(settings.blink_init_delay);
        servos[5].write(calibration[5].press_angle); // SHIFT is servo 5
        delay(settings.blink_hold_delay);
        servos[5].write(calibration[5].up_angle); // SHIFT is servo 5
        delay(settings.blink_release_delay);
        servos[servoIdx].write(calibration[servoIdx].up_angle);
        delay(200);
        ServoManager::setAllUP();
        Serial.println(F("OK"));
      } else {
        Serial.println(F("ERROR: Invalid direction for TEST_BLINK"));
      }
    }
    else if (strcmp(cmd, "START") == 0) {
      PatternExecutor::start();
    }
    else if (strcmp(cmd, "STOP") == 0) {
      PatternExecutor::stop();
    }
    else if (strcmp(cmd, "ESTOP") == 0) {
      PatternExecutor::estop();
    }
    else if (strcmp(cmd, "STATUS") == 0) {
      if (currentState == STATE_RUNNING) Serial.println(F("STATE:RUNNING"));
      else if (currentState == STATE_STOPPED) Serial.println(F("STATE:STOPPED"));
      else if (currentState == STATE_ESTOP) Serial.println(F("STATE:EMERGENCY_STOP"));
      else Serial.println(F("STATE:IDLE"));
    }
    else if (strcmp(cmd, "PUZZLE_SEQ") == 0) {
      ServoManager::attachAll();
      
      // Reset all direction servos (0 to 3: LEFT, RIGHT, UP, DOWN) to UP angle first
      for (int i = 0; i < 4; i++) {
        servos[i].write(calibration[i].up_angle);
      }
      delay(500); // Wait for them to settle
      
      int dirCount = 0;
      int startIdx = 0;
      int restLen = rest.length();
      
      for (int scan = 0; scan <= restLen && dirCount < 4; scan++) {
        if (scan == restLen || rest.charAt(scan) == ',') {
          String token = rest.substring(startIdx, scan);
          token.trim();
          
          int servoIdx = -1;
          if (token == "LEFT")       servoIdx = 0;
          else if (token == "RIGHT") servoIdx = 1;
          else if (token == "UP")    servoIdx = 2;
          else if (token == "DOWN")  servoIdx = 3;
          
          if (servoIdx >= 0 && servoIdx < 4) {
            Serial.print(F("PUZZLE_STEP:"));
            Serial.println(token);
            servos[servoIdx].write(calibration[servoIdx].press_angle);
            delay(350);  // Hold press for 350ms
            
            servos[servoIdx].write(calibration[servoIdx].up_angle);
            delay(650);  // Wait 650ms before next step
          }
          
          dirCount++;
          startIdx = scan + 1;
        }
      }
      
      // Reset all to UP and detach
      ServoManager::setAllUP();
      Serial.println(F("PUZZLE_DONE"));
    }
    else {
      Serial.println(F("ERROR: Unknown Command"));
    }
  }
}

// ==========================================
// CORE SETUP & LOOP
// ==========================================
byte lastResetCause = 0;

void setup() {
  // Read MCUSR first thing before it is modified
  lastResetCause = MCUSR;
  MCUSR = 0; // Clear it for next time

  Serial.begin(9600);
  while (!Serial) { ; } // wait for serial port to connect
  delay(800); // Beri waktu buffer serial PC untuk sinkronisasi setelah reset!

  Serial.println(F("\n========================================="));
  Serial.println(F("[System] Checking last reset source..."));
  if (lastResetCause & (1 << PORF)) {
    Serial.println(F("[System] Last Reset: Power-on (Baru pertama kali dinyalakan)."));
  }
  else if (lastResetCause & (1 << BORF)) {
    Serial.println(F("[System] Last Reset: BROWN-OUT RESET (⚠️ TEGANGAN DROP / KURANG ARUS!)."));
  }
  else if (lastResetCause & (1 << EXTRF)) {
    Serial.println(F("[System] Last Reset: External Reset (PC terhubung / Tombol Reset ditekan)."));
  }
  else if (lastResetCause & (1 << WDRF)) {
    Serial.println(F("[System] Last Reset: Watchdog Timer Reset."));
  }
  else {
    Serial.print(F("[System] Last Reset: Code 0x"));
    Serial.println(lastResetCause, HEX);
  }
  Serial.println(F("========================================="));

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
