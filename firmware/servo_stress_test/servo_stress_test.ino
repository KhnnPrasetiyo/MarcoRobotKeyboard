/*
 * Diagnostic & Stress Test Firmware - NanoKeyboardController Servos
 * 
 * firmware ini dirancang khusus untuk mendeteksi batas kemampuan daya PSU/Regulator Anda.
 * 
 * Cara Penggunaan:
 * 1. Buka folder 'servo_stress_test' di Arduino IDE (file -> open -> pilih servo_stress_test.ino).
 * 2. Upload ke Arduino Nano Anda.
 * 3. Buka Serial Monitor (Baudrate: 115200).
 * 4. Pilihlah tipe pengetesan:
 *    '1' -> Uji Coba Sekuensial (Satu per satu - Arus paling rendah)
 *    '2' -> Uji Coba Bersamaan (Staggered Attach + Gerakan Menyapu Perlahan)
 *    '3' -> Uji Coba Stress Test (Semua bergerak cepat bersamaan - Arus maksimal)
 */

#include <Servo.h>

const int NUM_SERVOS = 6;
const int SERVO_PINS[NUM_SERVOS] = {2, 3, 4, 5, 6, 7};
const char* SERVO_NAMES[NUM_SERVOS] = {
  "1. LEFT (D2)", 
  "2. RIGHT (D3)", 
  "3. UP (D4)", 
  "4. DOWN (D5)", 
  "5. SHIFT (D6)", 
  "6. A (D7)"
};

Servo servos[NUM_SERVOS];

// Pin LED
const int PIN_LED_STATUS = 11;
const int PIN_LED_SERVO = 12;

void setup() {
  Serial.begin(9600);
  while (!Serial) { ; } // Tunggu Serial siap
  
  pinMode(PIN_LED_STATUS, OUTPUT);
  pinMode(PIN_LED_SERVO, OUTPUT);
  
  digitalWrite(PIN_LED_STATUS, HIGH);
  digitalWrite(PIN_LED_SERVO, LOW);
  
  Serial.println(F("\n=============================================="));
  Serial.println(F("    ARDUINO NANO SERVO DIAGNOSTIC & STRESS    "));
  Serial.println(F("=============================================="));
  Serial.println(F("Pilih tes dengan mengetik angka lalu tekan Enter:"));
  Serial.println(F("  '1' -> Tes Sekuensial (Servo bergerak satu-persatu)"));
  Serial.println(F("  '2' -> Tes Bersamaan Aman (Staggered Attach + Sweep Lambat)"));
  Serial.println(F("  '3' -> Tes Stress Maksimal (Semua servo hentakan serentak)"));
  Serial.println(F("=============================================="));
  
  digitalWrite(PIN_LED_STATUS, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    
    // Abaikan newline atau spasi
    if (cmd == '\r' || cmd == '\n' || cmd == ' ') return;
    
    if (cmd == '1') {
      runSequentialTest();
    }
    else if (cmd == '2') {
      runSafeConcurrentTest();
    }
    else if (cmd == '3') {
      runStressTest();
    }
    else {
      Serial.print(F("Perintah tidak dikenal: '"));
      Serial.print(cmd);
      Serial.println(F("' (Gunakan '1', '2', atau '3')"));
    }
  }
}

// -----------------------------------------------------------------
// TES 1: Sekuensial (Menguji satu-persatu servo secara bergiliran)
// -----------------------------------------------------------------
void runSequentialTest() {
  Serial.println(F("\n>>> [MEMULAI TES 1] SEKUENSIAL (Satu per Satu) <<<"));
  Serial.println(F("Daya yang dibutuhkan sangat minimal."));
  digitalWrite(PIN_LED_STATUS, HIGH);
  
  for (int i = 0; i < NUM_SERVOS; i++) {
    Serial.print(F("Mengaktifkan & Menggerakkan: "));
    Serial.println(SERVO_NAMES[i]);
    
    // Attach servo aktif
    servos[i].attach(SERVO_PINS[i]);
    digitalWrite(PIN_LED_SERVO, HIGH);
    delay(100);
    
    // Gerakan tekan (45 derajat)
    servos[i].write(45);
    delay(600);
    
    // Gerakan kembali (90 derajat)
    servos[i].write(90);
    delay(600);
    
    // Detach kembali agar hemat daya
    servos[i].detach();
    digitalWrite(PIN_LED_SERVO, LOW);
    delay(100);
  }
  
  digitalWrite(PIN_LED_STATUS, LOW);
  Serial.println(F(">>> [TES 1 SELESAI] Jika berhasil tanpa restart, sistem kontrol pin berfungsi normal. <<<"));
}

// -----------------------------------------------------------------
// TES 2: Bersamaan Aman (Staggered Attach + Slow Sweep)
// -----------------------------------------------------------------
void runSafeConcurrentTest() {
  Serial.println(F("\n>>> [MEMULAI TES 2] BERSAMAAN AMAN (Staggered + Slow Sweep) <<<"));
  Serial.println(F("Menyalakan servo bergantian lalu digerakkan perlahan untuk meredam lonjakan arus."));
  digitalWrite(PIN_LED_STATUS, HIGH);
  
  // 1. Staggered Attach (Menghindari lonjakan daya inisialisasi)
  for (int i = 0; i < NUM_SERVOS; i++) {
    Serial.print(F("Attach: "));
    Serial.println(SERVO_NAMES[i]);
    servos[i].attach(SERVO_PINS[i]);
    servos[i].write(90); // Pastikan default di atas
    delay(150);          // Jeda agar arus stabil sebelum servo berikutnya di-attach
  }
  digitalWrite(PIN_LED_SERVO, HIGH);
  delay(500);
  
  // 2. Slow Sweep Bersamaan (Gerakan menyapu perlahan ke 45)
  Serial.println(F("Menggerakkan semua servo serentak secara perlahan..."));
  for (int angle = 90; angle >= 45; angle--) {
    for (int i = 0; i < NUM_SERVOS; i++) {
      servos[i].write(angle);
    }
    delay(25); // Kecepatan menyapu (25ms per derajat)
  }
  delay(1000);
  
  // Kembali perlahan ke 90
  for (int angle = 45; angle <= 90; angle++) {
    for (int i = 0; i < NUM_SERVOS; i++) {
      servos[i].write(angle);
    }
    delay(25);
  }
  delay(1000);
  
  // Detach semua
  for (int i = 0; i < NUM_SERVOS; i++) {
    servos[i].detach();
  }
  digitalWrite(PIN_LED_SERVO, LOW);
  digitalWrite(PIN_LED_STATUS, LOW);
  Serial.println(F(">>> [TES 2 SELESAI] Sukses meredam shock beban kelistrikan! <<<"));
}

// -----------------------------------------------------------------
// TES 3: Stress Test (Semua Bergerak Hentakan Serentak)
// -----------------------------------------------------------------
void runStressTest() {
  Serial.println(F("\n>>> [MEMULAI TES 3] STRESS TEST MAKSIMAL (Gerak Hentakan Serentak) <<<"));
  Serial.println(F("Peringatan: Ini akan mengonsumsi daya puncak ekstrem dari PSU Anda!"));
  delay(1000);
  
  digitalWrite(PIN_LED_STATUS, HIGH);
  
  // Attach semua servo secara cepat
  Serial.println(F("Mengaktifkan seluruh servo secara bersamaan..."));
  for (int i = 0; i < NUM_SERVOS; i++) {
    servos[i].attach(SERVO_PINS[i]);
  }
  digitalWrite(PIN_LED_SERVO, HIGH);
  delay(300);
  
  // Hentakan pertama (Langsung ke 45 derajat secepatnya)
  Serial.println(F("HENTAKAN 1: Semua servo langsung lompat ke 45 derajat..."));
  for (int i = 0; i < NUM_SERVOS; i++) {
    servos[i].write(45);
  }
  delay(1200);
  
  // Hentakan kedua (Kembali ke 90 derajat secepatnya)
  Serial.println(F("HENTAKAN 2: Semua servo langsung lompat ke 90 derajat..."));
  for (int i = 0; i < NUM_SERVOS; i++) {
    servos[i].write(90);
  }
  delay(1200);
  
  // Detach semua
  for (int i = 0; i < NUM_SERVOS; i++) {
    servos[i].detach();
  }
  digitalWrite(PIN_LED_SERVO, LOW);
  digitalWrite(PIN_LED_STATUS, LOW);
  Serial.println(F(">>> [TES 3 SELESAI] PSU Anda terbukti luar biasa kuat jika berhasil melewati ini! <<<"));
}
