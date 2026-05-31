/* ==========================================
   STATE MANAGEMENT & CORE MODELLING
   ========================================== */
class ServoConfig {
  constructor(name, pin, up_angle = 90, press_angle = 45) {
    this.name = name;
    this.pin = pin;
    this.up_angle = up_angle;
    this.press_angle = press_angle;
  }
}

class RobotProfile {
  constructor() {
    this.servos = [
      new ServoConfig("LEFT", 2, 90, 45),
      new ServoConfig("RIGHT", 3, 90, 45),
      new ServoConfig("UP", 4, 90, 45),
      new ServoConfig("DOWN", 5, 90, 45),
      new ServoConfig("SHIFT", 6, 90, 45),
      new ServoConfig("A", 7, 90, 45),
    ];
    this.pattern = [];
    this.loop_mode = "INFINITY"; // "INFINITY" or "CUSTOM"
    this.loop_count = 1;
    this.random_delay_enabled = false;
    this.random_delay_min = 100;
    this.random_delay_max = 1000;
    this.auto_start = false;
  }
}

// Global active instances
const profile = new RobotProfile();
const actionTypesList = [
  "NONE", "LEFT", "RIGHT", "UP", "DOWN", "A",
  "BLINK_LEFT", "BLINK_RIGHT", "BLINK_UP", "BLINK_DOWN"
];

// UI Key coordinates mapping (canvas positioning)
const servosUI = {
  "LEFT": { x: 90, y: 150, color: "#1e90ff", label: "LEFT (D2)", pressed: false },
  "RIGHT": { x: 250, y: 150, color: "#2ed573", label: "RIGHT (D3)", pressed: false },
  "UP": { x: 170, y: 70, color: "#ffa502", label: "UP (D4)", pressed: false },
  "DOWN": { x: 170, y: 150, color: "#ff4757", label: "DOWN (D5)", pressed: false },
  "SHIFT": { x: 90, y: 220, color: "#9b59b6", label: "SHIFT (D6)", pressed: false },
  "A": { x: 250, y: 220, color: "#f1c40f", label: "A (D7)", pressed: false }
};

// State Variables
let isCordova = false;
let serialPort = null;
let serialWriter = null;
let serialReader = null;
let keepReading = false;
let serialConnected = false;
let selectedActionIndex = null;
let testerActive = false;
let activeTab = "dashboard";

// Listen to Cordova's deviceready event to switch to native mode
document.addEventListener("deviceready", () => {
  isCordova = true;
  logToConsole("Platform native Android (Cordova) terdeteksi!");
}, false);

// Buffer for incoming Cordova USB Serial data streams
let cordovaInputBuffer = "";

function handleIncomingCordovaData(str) {
  cordovaInputBuffer += str;
  while (cordovaInputBuffer.includes("\n")) {
    const parts = cordovaInputBuffer.split("\n");
    const line = parts.shift().trim();
    cordovaInputBuffer = parts.join("\n");
    
    if (line) {
      logToConsole(`RX: ${line}`);
      handleIncomingSerialLine(line);
    }
  }
}

// Simulation State Variables
let simRunning = false;
let simTimeoutId = null;
let simStepIndex = 0;

// QWERTY Keyboard Layout & Variables
const keyboardLayout = [
  // --- Row 0: F-Row ---
  { label: "Esc", x: 0.0, y: 0.0, w: 1.0, h: 1.0, keysym: "Escape" },
  { label: "F1", x: 2.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F1" },
  { label: "F2", x: 3.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F2" },
  { label: "F3", x: 4.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F3" },
  { label: "F4", x: 5.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F4" },
  { label: "F5", x: 6.5, y: 0.0, w: 1.0, h: 1.0, keysym: "F5" },
  { label: "F6", x: 7.5, y: 0.0, w: 1.0, h: 1.0, keysym: "F6" },
  { label: "F7", x: 8.5, y: 0.0, w: 1.0, h: 1.0, keysym: "F7" },
  { label: "F8", x: 9.5, y: 0.0, w: 1.0, h: 1.0, keysym: "F8" },
  { label: "F9", x: 11.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F9" },
  { label: "F10", x: 12.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F10" },
  { label: "F11", x: 13.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F11" },
  { label: "F12", x: 14.0, y: 0.0, w: 1.0, h: 1.0, keysym: "F12" },
  { label: "PrtSc", x: 15.5, y: 0.0, w: 1.0, h: 1.0, keysym: "Print" },
  { label: "ScrLk", x: 16.5, y: 0.0, w: 1.0, h: 1.0, keysym: "Scroll_Lock" },
  { label: "Pause", x: 17.5, y: 0.0, w: 1.0, h: 1.0, keysym: "Pause" },

  // --- Row 1 ---
  { label: "~", x: 0.0, y: 1.3, w: 1.0, h: 1.0, keysym: "grave" },
  { label: "1", x: 1.0, y: 1.3, w: 1.0, h: 1.0, keysym: "1" },
  { label: "2", x: 2.0, y: 1.3, w: 1.0, h: 1.0, keysym: "2" },
  { label: "3", x: 3.0, y: 1.3, w: 1.0, h: 1.0, keysym: "3" },
  { label: "4", x: 4.0, y: 1.3, w: 1.0, h: 1.0, keysym: "4" },
  { label: "5", x: 5.0, y: 1.3, w: 1.0, h: 1.0, keysym: "5" },
  { label: "6", x: 6.0, y: 1.3, w: 1.0, h: 1.0, keysym: "6" },
  { label: "7", x: 7.0, y: 1.3, w: 1.0, h: 1.0, keysym: "7" },
  { label: "8", x: 8.0, y: 1.3, w: 1.0, h: 1.0, keysym: "8" },
  { label: "9", x: 9.0, y: 1.3, w: 1.0, h: 1.0, keysym: "9" },
  { label: "0", x: 10.0, y: 1.3, w: 1.0, h: 1.0, keysym: "0" },
  { label: "-", x: 11.0, y: 1.3, w: 1.0, h: 1.0, keysym: "minus" },
  { label: "=", x: 12.0, y: 1.3, w: 1.0, h: 1.0, keysym: "equal" },
  { label: "Backspace", x: 13.0, y: 1.3, w: 2.0, h: 1.0, keysym: "BackSpace" },
  { label: "Ins", x: 15.5, y: 1.3, w: 1.0, h: 1.0, keysym: "Insert" },
  { label: "Home", x: 16.5, y: 1.3, w: 1.0, h: 1.0, keysym: "Home" },
  { label: "PgUp", x: 17.5, y: 1.3, w: 1.0, h: 1.0, keysym: "Prior" },
  { label: "Num", x: 19.0, y: 1.3, w: 1.0, h: 1.0, keysym: "Num_Lock" },
  { label: "/", x: 20.0, y: 1.3, w: 1.0, h: 1.0, keysym: "KP_Divide" },
  { label: "*", x: 21.0, y: 1.3, w: 1.0, h: 1.0, keysym: "KP_Multiply" },
  { label: "-", x: 22.0, y: 1.3, w: 1.0, h: 1.0, keysym: "KP_Subtract" },

  // --- Row 2 ---
  { label: "Tab", x: 0.0, y: 2.3, w: 1.5, h: 1.0, keysym: "Tab" },
  { label: "Q", x: 1.5, y: 2.3, w: 1.0, h: 1.0, keysym: "q" },
  { label: "W", x: 2.5, y: 2.3, w: 1.0, h: 1.0, keysym: "w" },
  { label: "E", x: 3.5, y: 2.3, w: 1.0, h: 1.0, keysym: "e" },
  { label: "R", x: 4.5, y: 2.3, w: 1.0, h: 1.0, keysym: "r" },
  { label: "T", x: 5.5, y: 2.3, w: 1.0, h: 1.0, keysym: "t" },
  { label: "Y", x: 6.5, y: 2.3, w: 1.0, h: 1.0, keysym: "y" },
  { label: "U", x: 7.5, y: 2.3, w: 1.0, h: 1.0, keysym: "u" },
  { label: "I", x: 8.5, y: 2.3, w: 1.0, h: 1.0, keysym: "i" },
  { label: "O", x: 9.5, y: 2.3, w: 1.0, h: 1.0, keysym: "o" },
  { label: "P", x: 10.5, y: 2.3, w: 1.0, h: 1.0, keysym: "p" },
  { label: "[", x: 11.5, y: 2.3, w: 1.0, h: 1.0, keysym: "bracketleft" },
  { label: "]", x: 12.5, y: 2.3, w: 1.0, h: 1.0, keysym: "bracketright" },
  { label: "\\", x: 13.5, y: 2.3, w: 1.5, h: 1.0, keysym: "backslash" },
  { label: "Del", x: 15.5, y: 2.3, w: 1.0, h: 1.0, keysym: "Delete" },
  { label: "End", x: 16.5, y: 2.3, w: 1.0, h: 1.0, keysym: "End" },
  { label: "PgDn", x: 17.5, y: 2.3, w: 1.0, h: 1.0, keysym: "Next" },
  { label: "7", x: 19.0, y: 2.3, w: 1.0, h: 1.0, keysym: "KP_7" },
  { label: "8", x: 20.0, y: 2.3, w: 1.0, h: 1.0, keysym: "KP_8" },
  { label: "9", x: 21.0, y: 2.3, w: 1.0, h: 1.0, keysym: "KP_9" },
  { label: "+", x: 22.0, y: 2.3, w: 1.0, h: 2.0, keysym: "KP_Add" },

  // --- Row 3 ---
  { label: "Caps", x: 0.0, y: 3.3, w: 1.75, h: 1.0, keysym: "Caps_Lock" },
  { label: "A", x: 1.75, y: 3.3, w: 1.0, h: 1.0, keysym: "a" },
  { label: "S", x: 2.75, y: 3.3, w: 1.0, h: 1.0, keysym: "s" },
  { label: "D", x: 3.75, y: 3.3, w: 1.0, h: 1.0, keysym: "d" },
  { label: "F", x: 4.75, y: 3.3, w: 1.0, h: 1.0, keysym: "f" },
  { label: "G", x: 5.75, y: 3.3, w: 1.0, h: 1.0, keysym: "g" },
  { label: "H", x: 6.75, y: 3.3, w: 1.0, h: 1.0, keysym: "h" },
  { label: "J", x: 7.75, y: 3.3, w: 1.0, h: 1.0, keysym: "j" },
  { label: "K", x: 8.75, y: 3.3, w: 1.0, h: 1.0, keysym: "k" },
  { label: "L", x: 9.75, y: 3.3, w: 1.0, h: 1.0, keysym: "l" },
  { label: ";", x: 10.75, y: 3.3, w: 1.0, h: 1.0, keysym: "semicolon" },
  { label: "'", x: 11.75, y: 3.3, w: 1.0, h: 1.0, keysym: "apostrophe" },
  { label: "Enter", x: 12.75, y: 3.3, w: 2.25, h: 1.0, keysym: "Return" },
  { label: "4", x: 19.0, y: 3.3, w: 1.0, h: 1.0, keysym: "KP_4" },
  { label: "5", x: 20.0, y: 3.3, w: 1.0, h: 1.0, keysym: "KP_5" },
  { label: "6", x: 21.0, y: 3.3, w: 1.0, h: 1.0, keysym: "KP_6" },

  // --- Row 4 ---
  { label: "Shift L", x: 0.0, y: 4.3, w: 2.25, h: 1.0, keysym: "Shift_L" },
  { label: "Z", x: 2.25, y: 4.3, w: 1.0, h: 1.0, keysym: "z" },
  { label: "X", x: 3.25, y: 4.3, w: 1.0, h: 1.0, keysym: "x" },
  { label: "C", x: 4.25, y: 4.3, w: 1.0, h: 1.0, keysym: "c" },
  { label: "V", x: 5.25, y: 4.3, w: 1.0, h: 1.0, keysym: "v" },
  { label: "B", x: 6.25, y: 4.3, w: 1.0, h: 1.0, keysym: "b" },
  { label: "N", x: 7.25, y: 4.3, w: 1.0, h: 1.0, keysym: "n" },
  { label: "M", x: 8.25, y: 4.3, w: 1.0, h: 1.0, keysym: "m" },
  { label: ",", x: 9.25, y: 4.3, w: 1.0, h: 1.0, keysym: "comma" },
  { label: ".", x: 10.25, y: 4.3, w: 1.0, h: 1.0, keysym: "period" },
  { label: "/", x: 11.25, y: 4.3, w: 1.0, h: 1.0, keysym: "slash" },
  { label: "Shift R", x: 12.25, y: 4.3, w: 2.75, h: 1.0, keysym: "Shift_R" },
  { label: "▲", x: 16.5, y: 4.3, w: 1.0, h: 1.0, keysym: "Up" },
  { label: "1", x: 19.0, y: 4.3, w: 1.0, h: 1.0, keysym: "KP_1" },
  { label: "2", x: 20.0, y: 4.3, w: 1.0, h: 1.0, keysym: "KP_2" },
  { label: "3", x: 21.0, y: 4.3, w: 1.0, h: 1.0, keysym: "KP_3" },
  { label: "Ent", x: 22.0, y: 4.3, w: 1.0, h: 2.0, keysym: "KP_Enter" },

  // --- Row 5 ---
  { label: "Ctrl L", x: 0.0, y: 5.3, w: 1.25, h: 1.0, keysym: "Control_L" },
  { label: "Win", x: 1.25, y: 5.3, w: 1.25, h: 1.0, keysym: "Win_L" },
  { label: "Alt L", x: 2.5, y: 5.3, w: 1.25, h: 1.0, keysym: "Alt_L" },
  { label: "Spacebar", x: 3.75, y: 5.3, w: 6.25, h: 1.0, keysym: "space" },
  { label: "Alt R", x: 10.0, y: 5.3, w: 1.25, h: 1.0, keysym: "Alt_R" },
  { label: "Win", x: 11.25, y: 5.3, w: 1.25, h: 1.0, keysym: "Win_R" },
  { label: "Menu", x: 12.5, y: 5.3, w: 1.25, h: 1.0, keysym: "Menu" },
  { label: "Ctrl R", x: 13.75, y: 5.3, w: 1.25, h: 1.0, keysym: "Control_R" },
  { label: "◀", x: 15.5, y: 5.3, w: 1.0, h: 1.0, keysym: "Left" },
  { label: "▼", x: 16.5, y: 5.3, w: 1.0, h: 1.0, keysym: "Down" },
  { label: "▶", x: 17.5, y: 5.3, w: 1.0, h: 1.0, keysym: "Right" },
  { label: "0", x: 19.0, y: 5.3, w: 2.0, h: 1.0, keysym: "KP_0" },
  { label: ".", x: 21.0, y: 5.3, w: 1.0, h: 1.0, keysym: "KP_Decimal" }
];

const keysymAliases = {
  "exclam": "1", "at": "2", "numbersign": "3", "dollar": "4", "percent": "5",
  "asciicircum": "6", "ampersand": "7", "asterisk": "8", "parenleft": "9", "parenright": "0",
  "underscore": "minus", "plus": "equal", "braceleft": "bracketleft", "braceright": "bracketright",
  "bar": "backslash", "colon": "semicolon", "quotedbl": "apostrophe", "less": "comma",
  "greater": "period", "question": "slash", "tilde": "grave", "asciitilde": "grave", "quoteleft": "grave",
  "KP_Home": "KP_7", "KP_Up": "KP_8", "KP_Prior": "KP_9", "KP_Left": "KP_4", "KP_Begin": "KP_5",
  "KP_Right": "KP_6", "KP_End": "KP_1", "KP_Down": "KP_2", "KP_Next": "KP_3", "KP_Insert": "KP_0",
  "KP_Delete": "KP_Decimal"
};

const keysPressed = {};
keyboardLayout.forEach(k => { keysPressed[k.keysym] = false; });

const keyToServo = {
  "Shift_L": 4, "a": 5, "Up": 2, "Left": 0, "Down": 3, "Right": 1
};

let testerQwertyActive = true;

// Neso & Time Tracker State Variables
let mobileWalletAddress = localStorage.getItem("mobileWalletAddress") || "";
let mobileSessionActive = false;
let mobileSessionStartTime = null;
let mobileInitialNeso = null;
let mobileInitialNxpc = null;
let mobileCurrentNeso = 0.0;
let mobileCurrentNxpc = 0.0;
let mobileRpcInterval = null;

/* ==========================================
   WEB SERIAL CONNECTION MANAGEMENT
   ========================================== */
async function connectSerial() {
  // --- MODE A: NATIVE ANDROID APK (CORDOVA) VIA USB OTG ---
  if (isCordova) {
    if (!window.serial) {
      logToConsole("Error: Plugin USB Serial native tidak ditemukan!");
      alert("Error: Driver serial native Android belum terpasang di APK ini.");
      return;
    }

    logToConsole("Mencari perangkat USB Serial OTG...");
    
    window.serial.requestPermission(
      function() {
        logToConsole("Izin akses USB OTG diberikan oleh pengguna.");
        logToConsole("Membuka port serial USB (115200 bps)...");
        
        window.serial.open(
          {
            baudRate: 115200,
            dtr: true // Diperlukan untuk memulai komunikasi Arduino
          },
          function() {
            serialConnected = true;
            updateConnectionUI(true);
            logToConsole("Koneksi serial USB OTG aktif pada baud rate 115200.");
            
            // Daftarkan callback baca data secara terus-menerus
            window.serial.registerReadCallback(
              function(data) {
                // Mengubah ArrayBuffer menjadi String
                const view = new Uint8Array(data);
                let str = "";
                for (let i = 0; i < view.length; i++) {
                  str += String.fromCharCode(view[i]);
                }
                handleIncomingCordovaData(str);
              },
              function(err) {
                logToConsole(`Error membaca serial USB: ${err}`);
              }
            );
            
            // Ping untuk verifikasi
            sendSerialCommand("PING");
          },
          function(error) {
            logToConsole(`Gagal membuka port USB OTG: ${error}`);
            alert("Gagal menyambung ke USB. Pastikan kabel OTG tercolok kuat ke Arduino Nano!");
            updateConnectionUI(false);
          }
        );
      },
      function(error) {
        logToConsole(`Akses USB ditolak: ${error}`);
        alert("Izin akses USB ditolak. Aplikasi membutuhkan izin ini untuk mengendalikan Arduino Nano.");
        updateConnectionUI(false);
      }
    );
    return;
  }

  // --- MODE B: WEB BROWSER (PWA / WEB SERIAL API) ---
  if (!("serial" in navigator)) {
    logToConsole("Mode Wi-Fi PC Bridge aktif. Semua perintah diteruskan nirkabel melalui PC Anda.");
    alert("Web Serial API tidak didukung pada browser mobile Anda.\n\nAplikasi secara otomatis beralih menggunakan Wi-Fi PC Bridge. Pastikan PC desktop Anda terhubung ke Arduino dan jalankan aplikasi desktop.");
    return;
  }

  try {
    serialPort = await navigator.serial.requestPort();
    await serialPort.open({ baudRate: 115200 });
    
    serialConnected = true;
    serialWriter = serialPort.writable.getWriter();
    
    // UI Updates
    updateConnectionUI(true);
    logToConsole("Koneksi serial terhubung pada baud rate 115200.");
    
    // Start Reading loop
    keepReading = true;
    readSerialLoop();
    
    // Ping to verify
    sendSerialCommand("PING");
  } catch (error) {
    logToConsole(`Gagal menyambungkan port: ${error.message}`);
    updateConnectionUI(false);
  }
}

async function disconnectSerial() {
  // --- DISCONNECT NATIVE ---
  if (isCordova) {
    if (window.serial) {
      window.serial.close(
        function() {
          logToConsole("Koneksi USB OTG diputus.");
          serialConnected = false;
          updateConnectionUI(false);
        },
        function(err) {
          logToConsole(`Error saat menutup serial USB: ${err}`);
          serialConnected = false;
          updateConnectionUI(false);
        }
      );
    } else {
      serialConnected = false;
      updateConnectionUI(false);
    }
    return;
  }

  // --- DISCONNECT WEB ---
  keepReading = false;
  if (serialReader) {
    try {
      await serialReader.cancel();
    } catch (e) {}
  }
  if (serialWriter) {
    try {
      serialWriter.releaseLock();
    } catch (e) {}
  }
  if (serialPort) {
    try {
      await serialPort.close();
    } catch (e) {}
  }
  
  serialConnected = false;
  serialPort = null;
  serialWriter = null;
  serialReader = null;
  
  updateConnectionUI(false);
  logToConsole("Koneksi serial terputus.");
}

async function sendSerialCommand(cmd) {
  // --- SEND NATIVE ---
  if (isCordova) {
    if (serialConnected && window.serial) {
      window.serial.write(
        cmd + "\n",
        function() {
          logToConsole(`TX (USB OTG): ${cmd}`);
        },
        function(err) {
          logToConsole(`Error mengirim perintah USB OTG: ${err}`);
          disconnectSerial();
        }
      );
    } else {
      logToConsole(`Gagal mengirim (Belum Terhubung): ${cmd}`);
    }
    return;
  }

  // --- SEND WEB / WI-FI ---
  if (serialConnected && serialWriter) {
    try {
      const encoder = new TextEncoder();
      const data = encoder.encode(cmd + "\n");
      await serialWriter.write(data);
      logToConsole(`TX (USB): ${cmd}`);
    } catch (error) {
      logToConsole(`Error mengirim perintah USB: ${error.message}`);
      disconnectSerial();
    }
  } else {
    // Fallback to Wi-Fi PC Bridge
    try {
      logToConsole(`TX (Wi-Fi): ${cmd}`);
      const res = await fetch(`/api/command?cmd=${encodeURIComponent(cmd)}`);
      const data = await res.json();
      if (data.status !== "ok") {
        logToConsole("Error: PC Bridge menolak perintah.");
      }
    } catch (error) {
      console.log(`Wi-Fi Bridge error: ${error.message}`);
    }
  }
}

async function readSerialLoop() {
  const decoder = new TextDecoder();
  let inputBuffer = "";
  
  while (serialPort && serialPort.readable && keepReading) {
    try {
      serialReader = serialPort.readable.getReader();
      while (keepReading) {
        const { value, done } = await serialReader.read();
        if (done) break;
        
        inputBuffer += decoder.decode(value);
        while (inputBuffer.includes("\n")) {
          const parts = inputBuffer.split("\n");
          const line = parts.shift().trim();
          inputBuffer = parts.join("\n");
          
          if (line) {
            logToConsole(`RX: ${line}`);
            handleIncomingSerialLine(line);
          }
        }
      }
    } catch (error) {
      logToConsole(`Read error: ${error.message}`);
      break;
    } finally {
      if (serialReader) {
        serialReader.releaseLock();
      }
    }
  }
}

function handleIncomingSerialLine(line) {
  const badgeText = document.getElementById("badge-text");
  const badge = document.getElementById("conn-status-badge");
  const statusText = document.getElementById("system-status-text");
  const stepRow = document.getElementById("step-progress-row");
  const stepText = document.getElementById("step-progress-text");

  if (line.startsWith("STATE:")) {
    const state = line.replace("STATE:", "").trim();
    statusText.innerText = `Aktif: ${state}`;
    statusText.className = "status-val text-orange";
    
    badgeText.innerText = `Aktif: ${state}`;
    badge.className = "status-badge active";

    if (state === "RUNNING") {
      if (!mobileSessionActive) {
        mobileSessionActive = true;
        mobileSessionStartTime = Date.now();
        mobileInitialNeso = null;
        mobileInitialNxpc = null;
        fetchMobileRpcBalance();
      }
    } else if (state === "STOPPED" || state === "IDLE" || state === "EMERGENCY_STOP") {
      mobileSessionActive = false;
      mobileSessionStartTime = null;
      stepRow.classList.add("hidden");
    }
  } 
  else if (line.startsWith("STEP:")) {
    const stepInfo = line.replace("STEP:", "").trim();
    stepRow.classList.remove("hidden");
    stepText.innerText = stepInfo;
    
    if (!mobileSessionActive) {
      mobileSessionActive = true;
      mobileSessionStartTime = Date.now();
      mobileInitialNeso = null;
      mobileInitialNxpc = null;
      fetchMobileRpcBalance();
    }
  }
  else if (line.startsWith("CONFIG_DUMP:")) {
    const hex = line.replace("CONFIG_DUMP:", "").trim();
    try {
      parseConfigHex(hex, profile);
      logToConsole(`Konfigurasi dibaca sukses: ${profile.pattern.length} aksi ditemukan.`);
      
      // Reload UI views
      renderCalibrationTab();
      renderPatternTab();
      updateEstimatedDuration();
      renderValidationTab();
      
      alert(`Konfigurasi sukses dibaca dari Arduino!\n\n• ${profile.pattern.length} aksi ditemukan\n• Mode: ${profile.loop_mode}`);
    } catch (e) {
      logToConsole(`Error parsing hex: ${e.message}`);
    }
  }
}

function updateConnectionUI(connected) {
  const btn = document.getElementById("btn-serial-connect");
  const badge = document.getElementById("conn-status-badge");
  const badgeText = document.getElementById("badge-text");
  const statusText = document.getElementById("system-status-text");
  const portText = document.getElementById("lbl-serial-com");
  
  const uploadBtn = document.getElementById("btn-eeprom-upload");
  const readBtn = document.getElementById("btn-eeprom-read");

  if (connected) {
    btn.innerText = "🔌 PUTUSKAN SAMBUNGAN ARDUINO";
    btn.className = "btn-ctrl btn-stop";
    
    badge.className = "status-badge connected";
    badgeText.innerText = "Terhubung";
    
    statusText.innerText = "Terhubung";
    statusText.className = "status-val text-green";
    
    if (isCordova) {
      portText.innerHTML = "Status Port: <b style='color:#2ed573'>TERHUBUNG (Kabel USB OTG)</b>";
    } else {
      portText.innerHTML = "Status Port: <b>TERBUNGKUS (Serial OTG)</b>";
    }
    
    uploadBtn.classList.remove("disabled");
    uploadBtn.disabled = false;
    readBtn.classList.remove("disabled");
    readBtn.disabled = false;
  } else {
    btn.innerText = "🔌 HUBUNGKAN ARDUINO NANO";
    btn.className = "btn-ctrl btn-start";
    
    badge.className = "status-badge disconnected";
    badgeText.innerText = "Terputus";
    
    statusText.innerText = "Terputus";
    statusText.className = "status-val text-red";
    
    portText.innerHTML = "Status Port: <b>Tidak Ada Sambungan</b>";
    
    uploadBtn.classList.add("disabled");
    uploadBtn.disabled = true;
    readBtn.classList.add("disabled");
    readBtn.disabled = true;
  }
}

/* ==========================================
   HEX ENCODING & DECODING (EEPROM PACKING)
   ========================================== */
function packProfileHex(profile) {
  const totalSize = 12 + 9 + 1 + (profile.pattern.length * 5);
  const buffer = new ArrayBuffer(totalSize);
  const view = new DataView(buffer);
  
  let offset = 0;
  
  // 1. Calibration (12 bytes)
  for (let i = 0; i < 6; i++) {
    const s = profile.servos[i];
    view.setUint8(offset++, s.up_angle);
    view.setUint8(offset++, s.press_angle);
  }
  
  // 2. Settings (9 bytes)
  view.setUint8(offset++, profile.auto_start ? 1 : 0);
  view.setUint8(offset++, profile.loop_mode === "CUSTOM" ? 1 : 0);
  view.setUint16(offset, parseInt(profile.loop_count), false); offset += 2;
  view.setUint8(offset++, profile.random_delay_enabled ? 1 : 0);
  view.setUint16(offset, parseInt(profile.random_delay_min), false); offset += 2;
  view.setUint16(offset, parseInt(profile.random_delay_max), false); offset += 2;
  
  // 3. Pattern Size (1 byte)
  view.setUint8(offset++, profile.pattern.length);
  
  // 4. Actions (5 bytes each)
  for (const action of profile.pattern) {
    let actIdx = actionTypesList.indexOf(action.action_type);
    if (actIdx === -1) actIdx = 0;
    view.setUint8(offset++, actIdx);
    view.setUint16(offset, parseInt(action.press_duration), false); offset += 2;
    view.setUint16(offset, parseInt(action.delay_duration), false); offset += 2;
  }
  
  // Convert to hex
  const bytes = new Uint8Array(buffer);
  let hex = "";
  for (const b of bytes) {
    hex += b.toString(16).padStart(2, "0").toUpperCase();
  }
  return hex;
}

function parseConfigHex(hexStr, profile) {
  const bytes = new Uint8Array(hexStr.match(/.{1,2}/g).map(byte => parseInt(byte, 16)));
  const buffer = bytes.buffer;
  const view = new DataView(buffer);
  
  let offset = 0;
  
  // 1. Calibration (12 bytes)
  for (let i = 0; i < 6; i++) {
    profile.servos[i].up_angle = view.getUint8(offset++);
    profile.servos[i].press_angle = view.getUint8(offset++);
  }
  
  // 2. Settings (9 bytes)
  profile.auto_start = view.getUint8(offset++) === 1;
  profile.loop_mode = view.getUint8(offset++) === 1 ? "CUSTOM" : "INFINITY";
  profile.loop_count = view.getUint16(offset, false); offset += 2;
  profile.random_delay_enabled = view.getUint8(offset++) === 1;
  profile.random_delay_min = view.getUint16(offset, false); offset += 2;
  profile.random_delay_max = view.getUint16(offset, false); offset += 2;
  
  // 3. Pattern Length (1 byte)
  const patternLength = view.getUint8(offset++);
  
  // 4. Actions
  profile.pattern = [];
  for (let i = 0; i < patternLength; i++) {
    if (offset + 4 >= bytes.length) break;
    const actIdx = view.getUint8(offset++);
    const pressDur = view.getUint16(offset, false); offset += 2;
    const delayDur = view.getUint16(offset, false); offset += 2;
    
    const actType = actionTypesList[actIdx] || "NONE";
    profile.pattern.push({
      action_type: actType,
      press_duration: pressDur,
      delay_duration: delayDur
    });
  }
}

/* ==========================================
   UI UTILITY LOGGING
   ========================================== */
function logToConsole(msg) {
  const box = document.getElementById("console-logs");
  const time = new Date().toLocaleTimeString();
  box.innerHTML += `<div><span style="color:#747d8c">[${time}]</span> ${msg}</div>`;
  box.scrollTop = box.scrollHeight;
}

/* ==========================================
   CALIBRATION TAB RENDERING
   ========================================== */
function renderCalibrationTab() {
  const container = document.getElementById("calibration-servos-container");
  container.innerHTML = "";

  profile.servos.forEach((servo, index) => {
    const card = document.createElement("div");
    card.className = "glass-card servo-card";
    card.innerHTML = `
      <h3>Servo ${index + 1}: ${servo.name} (Pin D${servo.pin})</h3>
      
      <!-- UP Row -->
      <div class="slider-row">
        <label>Sudut UP (°)</label>
        <input type="range" class="app-slider slider-up" min="0" max="180" value="${servo.up_angle}">
        <button class="btn-adjust btn-up-dec">-</button>
        <span class="val-bubble green up-label">${servo.up_angle}</span>
        <button class="btn-adjust btn-up-inc">+</button>
        <button class="btn-servo-test btn-up-test">Posisi UP</button>
      </div>

      <!-- PRESS Row -->
      <div class="slider-row">
        <label>Sudut PRESS (°)</label>
        <input type="range" class="app-slider slider-press" min="0" max="180" value="${servo.press_angle}">
        <button class="btn-adjust btn-press-dec">-</button>
        <span class="val-bubble orange press-label">${servo.press_angle}</span>
        <button class="btn-adjust btn-press-inc">+</button>
        <button class="btn-servo-test btn-press-test">Posisi PRESS</button>
      </div>

      <button class="btn-wide-test btn-seq-test">⚡ JALANKAN UJI TEKAN (SEQUENCE)</button>
    `;

    // Sliders & Adjusters setup
    const upSlider = card.querySelector(".slider-up");
    const upLabel = card.querySelector(".up-label");
    const pressSlider = card.querySelector(".slider-press");
    const pressLabel = card.querySelector(".press-label");

    // UP events
    const updateUp = (val) => {
      servo.up_angle = parseInt(val);
      upSlider.value = val;
      upLabel.innerText = val;
    };
    upSlider.addEventListener("input", (e) => updateUp(e.target.value));
    upSlider.addEventListener("change", (e) => {
      if (serialConnected) sendSerialCommand(`TEST_SERVO ${index} ${servo.up_angle}`);
    });
    card.querySelector(".btn-up-dec").addEventListener("click", () => {
      const val = Math.max(0, servo.up_angle - 1);
      updateUp(val);
      if (serialConnected) sendSerialCommand(`TEST_SERVO ${index} ${val}`);
    });
    card.querySelector(".btn-up-inc").addEventListener("click", () => {
      const val = Math.min(180, servo.up_angle + 1);
      updateUp(val);
      if (serialConnected) sendSerialCommand(`TEST_SERVO ${index} ${val}`);
    });
    card.querySelector(".btn-up-test").addEventListener("click", () => {
      sendSerialCommand(`TEST_SERVO ${index} ${servo.up_angle}`);
    });

    // PRESS events
    const updatePress = (val) => {
      servo.press_angle = parseInt(val);
      pressSlider.value = val;
      pressLabel.innerText = val;
    };
    pressSlider.addEventListener("input", (e) => updatePress(e.target.value));
    pressSlider.addEventListener("change", (e) => {
      if (serialConnected) sendSerialCommand(`TEST_SERVO ${index} ${servo.press_angle}`);
    });
    card.querySelector(".btn-press-dec").addEventListener("click", () => {
      const val = Math.max(0, servo.press_angle - 1);
      updatePress(val);
      if (serialConnected) sendSerialCommand(`TEST_SERVO ${index} ${val}`);
    });
    card.querySelector(".btn-press-inc").addEventListener("click", () => {
      const val = Math.min(180, servo.press_angle + 1);
      updatePress(val);
      if (serialConnected) sendSerialCommand(`TEST_SERVO ${index} ${val}`);
    });
    card.querySelector(".btn-press-test").addEventListener("click", () => {
      sendSerialCommand(`TEST_SERVO ${index} ${servo.press_angle}`);
    });

    // Sequence execution
    card.querySelector(".btn-seq-test").addEventListener("click", () => {
      logToConsole(`Menguji servo ${servo.name} (sekuensial)...`);
      sendSerialCommand(`TEST_SERVO ${index} ${servo.press_angle}`);
      setTimeout(() => {
        sendSerialCommand(`TEST_SERVO ${index} ${servo.up_angle}`);
      }, 250);
    });

    container.appendChild(card);
  });
}

/* ==========================================
   PATTERN BUILDER TAB RENDERING
   ========================================== */
function renderPatternTab() {
  const list = document.getElementById("pattern-actions-list");
  list.innerHTML = "";
  
  document.getElementById("pattern-summary-text").innerText = `${profile.pattern.length} Aksi`;

  profile.pattern.forEach((action, index) => {
    const item = document.createElement("div");
    item.className = `action-row-item ${selectedActionIndex === index ? 'selected' : ''}`;
    item.innerHTML = `
      <span class="idx">#${index + 1}</span>
      <span class="type">${action.action_type}</span>
      <span class="durs">${action.press_duration}ms / ${action.delay_duration}ms</span>
    `;

    item.addEventListener("click", () => {
      selectedActionIndex = index;
      // Re-render selection
      document.querySelectorAll(".action-row-item").forEach((el, i) => {
        el.className = `action-row-item ${selectedActionIndex === i ? 'selected' : ''}`;
      });
      openActionEditor(index);
    });

    list.appendChild(item);
  });
}

function openActionEditor(index) {
  const card = document.getElementById("action-editor-card");
  const action = profile.pattern[index];
  
  document.getElementById("editor-action-index").innerText = index + 1;
  
  // Load select types
  const typeSelect = document.getElementById("editor-action-type");
  typeSelect.innerHTML = "";
  actionTypesList.forEach(type => {
    const opt = document.createElement("option");
    opt.value = type;
    opt.innerText = type;
    if (type === action.action_type) opt.selected = true;
    typeSelect.appendChild(opt);
  });

  document.getElementById("editor-press-duration").value = action.press_duration;
  document.getElementById("editor-delay-duration").value = action.delay_duration;

  card.classList.remove("hidden");
}

function closeActionEditor() {
  document.getElementById("action-editor-card").classList.add("hidden");
}

function updateEstimatedDuration() {
  let totalMs = 0;
  profile.pattern.forEach(act => {
    totalMs += parseInt(act.press_duration) + parseInt(act.delay_duration);
  });

  const durationStr = totalMs / 1000;
  const dbText = document.getElementById("dashboard-duration-text");
  
  if (profile.pattern.length === 0) {
    dbText.innerText = "Pola Kosong";
    dbText.className = "status-val text-red";
    return;
  }

  if (profile.loop_mode === "INFINITY") {
    dbText.innerText = `${durationStr.toFixed(2)} dtk/siklus (∞)`;
    dbText.className = "status-val text-green";
  } else {
    const totalTime = durationStr * parseInt(profile.loop_count);
    dbText.innerText = `${totalTime.toFixed(2)} dtk (${profile.loop_count}x loop)`;
    dbText.className = "status-val text-green";
  }
}

/* ==========================================
   VALIDASI & SAFETY CHECKS
   ========================================== */
function renderValidationTab() {
  const box = document.getElementById("validation-issues-box");
  box.innerHTML = "";
  
  const issues = [];
  const warnings = [];

  // Empty check
  if (profile.pattern.length === 0) {
    issues.push("Aksi pola tidak boleh kosong! Robot tidak akan bisa berjalan.");
  }
  
  // Size limit check
  if (profile.pattern.length > 150) {
    issues.push("Aksi melebihi batas EEPROM Arduino! Max 150 aksi diperbolehkan.");
  }

  // Loop validation
  if (profile.loop_mode === "CUSTOM" && (parseInt(profile.loop_count) <= 0 || isNaN(profile.loop_count))) {
    issues.push("Jumlah loop kustom tidak valid! Harus minimal 1 loop.");
  }

  // Random Delay checks
  if (profile.random_delay_enabled) {
    const min = parseInt(profile.random_delay_min);
    const max = parseInt(profile.random_delay_max);
    if (min < 50) {
      issues.push("Batas minimum random delay terlalu cepat! Amankan di atas 50ms.");
    }
    if (min > max) {
      issues.push("Batas minimum random delay tidak boleh lebih besar dari batas maksimum!");
    }
    if (max - min < 100) {
      warnings.push("Jarak batas minimum dan maksimum random delay sangat sempit (disarankan beda > 100ms).");
    }
  }

  // Check actions durations
  profile.pattern.forEach((act, idx) => {
    if (act.press_duration < 100) {
      warnings.push(`Aksi #${idx + 1} (${act.action_type}): Durasi tekan di bawah 100ms mungkin terlalu cepat untuk sensor keyboard.`);
    }
    if (act.action_type.startsWith("BLINK_") && act.press_duration <= 150) {
      issues.push(`Aksi #${idx + 1} (${act.action_type}): Durasi tekan wajib di atas 150ms agar tombol SHIFT staggered sempat terpicu.`);
    }
  });

  // Render HTML
  if (issues.length === 0 && warnings.length === 0) {
    box.innerHTML = `<div class="warn-item text-green" style="text-align:center;font-weight:600;padding-top:15px;">✅ SEMUA BERHASIL DIVALIDASI!<br>Profil aman dan siap diunggah ke Arduino.</div>`;
    return;
  }

  issues.forEach(iss => {
    box.innerHTML += `<div class="warn-item critical">🔴 <b>Kesalahan Kritis:</b> ${iss}</div>`;
  });

  warnings.forEach(warn => {
    box.innerHTML += `<div class="warn-item warning">🟡 <b>Peringatan Keamanan:</b> ${warn}</div>`;
  });
}

/* ==========================================
   SIMULASI & TESTER CANVAS DRAW ENGINE
   ========================================== */
function initSimCanvas() {
  const canvas = document.getElementById("sim-canvas");
  const wrapper = canvas.parentElement;
  
  // Set logical pixels
  canvas.width = wrapper.clientWidth;
  canvas.height = wrapper.clientHeight;
  
  drawVirtualRig();
}

function drawVirtualRig() {
  const canvas = document.getElementById("sim-canvas");
  const ctx = canvas.getContext("2d");
  const cw = canvas.width;
  const ch = canvas.height;
  
  ctx.clearRect(0, 0, cw, ch);
  
  // Render header title
  ctx.fillStyle = "#a4b0be";
  ctx.font = "bold 10px sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("TAP TOMBOL KEYBOARD VIRTUAL BERIKUT", cw / 2, 25);

  // Auto spacing calculation
  const ox = (cw - 340) / 2;
  const oy = (ch - 260) / 2;

  for (const name in servosUI) {
    const key = servosUI[name];
    // Dynamic offsets
    const cx = key.x + ox;
    const cy = key.y + oy;
    
    // Draw Switch Footprint Outline
    ctx.strokeStyle = key.pressed ? "#ffffff" : "#57606f";
    ctx.lineWidth = key.pressed ? 2.5 : 1.5;
    ctx.fillStyle = key.pressed ? key.color : "#1c2430";
    
    ctx.beginPath();
    if (ctx.roundRect) {
      ctx.roundRect(cx - 35, cy - 30, 70, 60, 8);
    } else {
      ctx.rect(cx - 35, cy - 30, 70, 60);
    }
    ctx.fill();
    ctx.stroke();
    
    // Draw character label
    ctx.fillStyle = key.pressed ? "#ffffff" : "#a4b0be";
    ctx.font = "bold 13px sans-serif";
    ctx.fillText(name, cx, cy - 3);

    // Servo Actuator arm
    ctx.strokeStyle = key.pressed ? "#eccc68" : "#2f3542";
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(cx - 15, cy + 18);
    ctx.lineTo(cx + 15, cy + 18);
    ctx.stroke();
    
    // LED Pin labels
    ctx.fillStyle = "#57606f";
    ctx.font = "9px monospace";
    ctx.fillText(key.label, cx, cy + 45);
  }
}

/* ==========================================
   SIMULASI RUN TIME ENGINE
   ========================================== */
function runSimulationNextStep() {
  if (!simRunning) return;

  const totalSteps = profile.pattern.length;
  if (simStepIndex >= totalSteps) {
    if (profile.loop_mode === "INFINITY") {
      simStepIndex = 0;
      simTraceLog("=== Mengulang Loop Simulasi ===");
    } else {
      stopSimulation();
      return;
    }
  }

  const action = profile.pattern[simStepIndex];
  document.getElementById("lbl-sim-step").innerText = `Langkah: ${simStepIndex + 1} / ${totalSteps}`;
  document.getElementById("lbl-servo-state").innerText = "TEKAN";
  document.getElementById("lbl-servo-state").style.background = "#ffa502";

  // Reset pressed
  for (const name in servosUI) servosUI[name].pressed = false;

  // Staggered logic matching
  if (action.action_type.startsWith("BLINK_")) {
    const blinkKey = action.action_type.replace("BLINK_", "");
    simTraceLog(`[${action.action_type}] Menekan ${blinkKey} (staggered)...`);
    
    servosUI[blinkKey].pressed = true;
    drawVirtualRig();
    
    const staggerDelay = 150;
    if (action.press_duration > staggerDelay) {
      simTimeoutId = setTimeout(() => {
        if (!simRunning) return;
        simTraceLog(`[${action.action_type}] Menekan SHIFT (keduanya tertahan)`);
        servosUI[blinkKey].pressed = true;
        servosUI["SHIFT"].pressed = true;
        drawVirtualRig();
        
        // Schedule release
        const remaining = action.press_duration - staggerDelay;
        simTimeoutId = setTimeout(releaseAllServos, remaining);
      }, staggerDelay);
    } else {
      simTimeoutId = setTimeout(releaseAllServos, action.press_duration);
    }
  } else {
    if (action.action_type === "NONE") {
      simTraceLog(`[${action.action_type}] Jeda kosong (${action.press_duration}ms)`);
    } else {
      simTraceLog(`[${action.action_type}] Menekan ${action.action_type} (${action.press_duration}ms)`);
      servosUI[action.action_type].pressed = true;
    }
    drawVirtualRig();
    simTimeoutId = setTimeout(releaseAllServos, action.press_duration);
  }

  function releaseAllServos() {
    if (!simRunning) return;
    document.getElementById("lbl-servo-state").innerText = "UP";
    document.getElementById("lbl-servo-state").style.background = "rgba(255,255,255,0.1)";
    
    for (const name in servosUI) servosUI[name].pressed = false;
    drawVirtualRig();

    // Loop settings simulation
    let delayDuration = parseInt(action.delay_duration);
    if (profile.random_delay_enabled) {
      const min = parseInt(profile.random_delay_min);
      const max = parseInt(profile.random_delay_max);
      delayDuration = Math.floor(Math.random() * (max - min + 1)) + min;
      simTraceLog(`  Jeda (Diacak): ${delayDuration}ms`);
    } else {
      simTraceLog(`  Jeda: ${delayDuration}ms`);
    }

    document.getElementById("lbl-sim-delay").innerText = `Jeda: ${delayDuration}ms`;
    
    simTimeoutId = setTimeout(() => {
      simStepIndex++;
      runSimulationNextStep();
    }, delayDuration);
  }
}

function startSimulation() {
  if (profile.pattern.length === 0) {
    alert("Tambahkan aksi pola terlebih dahulu sebelum simulasi!");
    return;
  }
  simRunning = true;
  simStepIndex = 0;
  document.getElementById("btn-run-sim").innerText = "⏹ STOP SIMULASI";
  document.getElementById("btn-run-sim").className = "btn-ctrl btn-stop";
  
  const trace = document.getElementById("sim-log-trace");
  trace.classList.remove("hidden");
  trace.innerHTML = "<div>Simulasi dijalankan...</div>";
  
  runSimulationNextStep();
}

function stopSimulation() {
  simRunning = false;
  if (simTimeoutId) {
    clearTimeout(simTimeoutId);
    simTimeoutId = null;
  }
  document.getElementById("btn-run-sim").innerText = "▶ JALANKAN SIMULASI";
  document.getElementById("btn-run-sim").className = "btn-ctrl btn-start";
  
  document.getElementById("lbl-sim-step").innerText = "Langkah: - / -";
  document.getElementById("lbl-sim-delay").innerText = "Sisa jeda: 0ms";
  document.getElementById("lbl-servo-state").innerText = "UP";
  document.getElementById("lbl-servo-state").style.background = "rgba(255,255,255,0.1)";
  
  document.getElementById("sim-log-trace").classList.add("hidden");

  // Reset pressed states
  for (const name in servosUI) servosUI[name].pressed = false;
  drawVirtualRig();
}

function simTraceLog(msg) {
  const box = document.getElementById("sim-log-trace");
  box.innerHTML += `<div>${msg}</div>`;
  box.scrollTop = box.scrollHeight;
}

/* ==========================================
   CANVAS TAP COORDINATES PICKER FOR KEY TESTER
   ========================================== */
function handleCanvasTap(e, isPressed) {
  if (!testerActive) return;

  const canvas = document.getElementById("sim-canvas");
  const rect = canvas.getBoundingClientRect();
  
  // Calculate relative coordinate scales
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  
  const tapX = ((clientX - rect.left) / rect.width) * canvas.width;
  const tapY = ((clientY - rect.top) / rect.height) * canvas.height;

  // Spacing offsets
  const ox = (canvas.width - 340) / 2;
  const oy = (canvas.height - 260) / 2;

  // Search if hit key switch boundary box
  for (const name in servosUI) {
    const key = servosUI[name];
    const kcx = key.x + ox;
    const kcy = key.y + oy;

    if (tapX >= kcx - 35 && tapX <= kcx + 35 && tapY >= kcy - 30 && tapY <= kcy + 30) {
      // Key hit!
      if (key.pressed !== isPressed) {
        key.pressed = isPressed;
        drawVirtualRig();
        
        // Move hardware servo
        const sIdx = Object.keys(servosUI).indexOf(name);
        const sConf = profile.servos[sIdx];
        if (sConf) {
          const angle = isPressed ? sConf.press_angle : sConf.up_angle;
          sendSerialCommand(`TEST_SERVO ${sIdx} ${angle}`);
        }
      }
      break;
    }
  }
}

function toggleTesterState() {
  const btn = document.getElementById("btn-tester-switch");
  testerActive = !testerActive;
  
  if (testerActive) {
    stopSimulation(); // Turn off sim
    document.getElementById("sim-run-controls").classList.add("hidden");
    
    btn.innerText = "🟢 TESTER: ON";
    btn.className = "switch-btn on";
    
    logToConsole("Mode Tester Aktif. Sentuh tombol visual di layar untuk menggerakkan servo langsung.");
  } else {
    document.getElementById("sim-run-controls").classList.remove("hidden");
    
    btn.innerText = "🔴 TESTER: OFF";
    btn.className = "switch-btn off";
    
    // Release all physical servos for safety
    Object.keys(servosUI).forEach((name, idx) => {
      if (servosUI[name].pressed) {
        servosUI[name].pressed = false;
        const sConf = profile.servos[idx];
        if (sConf) sendSerialCommand(`TEST_SERVO ${idx} ${sConf.up_angle}`);
      }
    });
    drawVirtualRig();
    logToConsole("Mode Tester dimatikan.");
  }
}

/* ==========================================
   DOM LOADED INITIALIZATIONS & BINDINGS
   ========================================== */
document.addEventListener("DOMContentLoaded", () => {
  
  // Register Service Worker for offline PWA
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').then(() => {
      console.log('KBD Service Worker Registered!');
    }).catch(err => {
      console.warn('Service Worker registration deferred (non-secure origin):', err.message);
    });
  }

  // 1. Tab Navigation Routing
  document.querySelectorAll(".nav-item").forEach(btn => {
    btn.addEventListener("click", (e) => {
      const tabName = btn.getAttribute("data-tab");
      activeTab = tabName;
      
      // Nav highlight
      document.querySelectorAll(".nav-item").forEach(item => item.classList.remove("active"));
      btn.classList.add("active");
      
      // Panel showing
      document.querySelectorAll(".tab-panel").forEach(panel => panel.classList.remove("active"));
      document.getElementById(`tab-${tabName}`).classList.add("active");
      
      // Tab load updates
      if (tabName === "calibration") renderCalibrationTab();
      if (tabName === "pattern") renderPatternTab();
      if (tabName === "simulation") {
        setTimeout(initSimCanvas, 100);
      }
      if (tabName === "tester") {
        setTimeout(initTesterCanvas, 100);
      }
      if (tabName === "tracker") {
        fetchMobileRpcBalance();
      }
      if (tabName === "profiles") renderValidationTab();
    });
  });

  // 2. Serial connect button
  document.getElementById("btn-serial-connect").addEventListener("click", () => {
    if (serialConnected) disconnectSerial();
    else connectSerial();
  });

  // 3. E-stop buttons
  document.getElementById("btn-estop").addEventListener("click", () => {
    sendSerialCommand("ESTOP");
    logToConsole("⚠️ PERINTAH BERHENTI DARURAT DIKIRIM!");
    mobileSessionActive = false;
    mobileSessionStartTime = null;
  });
  document.getElementById("btn-start").addEventListener("click", () => {
    sendSerialCommand("START");
    if (!mobileSessionActive) {
      mobileSessionActive = true;
      mobileSessionStartTime = Date.now();
      mobileInitialNeso = null;
      mobileInitialNxpc = null;
      fetchMobileRpcBalance();
    }
  });
  document.getElementById("btn-stop").addEventListener("click", () => {
    sendSerialCommand("STOP");
    mobileSessionActive = false;
    mobileSessionStartTime = null;
  });

  // Clear logs button
  document.getElementById("btn-clear-log").addEventListener("click", () => {
    document.getElementById("console-logs").innerHTML = "";
  });

  // 4. Collapsible Settings Tab panel
  const toggleBtn = document.getElementById("btn-toggle-settings");
  toggleBtn.addEventListener("click", () => {
    const settingsPanel = document.getElementById("collapsible-settings");
    settingsPanel.classList.toggle("hidden");
    toggleBtn.classList.toggle("open");
  });

  // 5. Loop Mode setup
  const loopSelect = document.getElementById("loop-mode-select");
  loopSelect.addEventListener("change", (e) => {
    profile.loop_mode = e.target.value;
    const row = document.getElementById("loop-count-row");
    if (profile.loop_mode === "CUSTOM") row.classList.remove("hidden");
    else row.classList.add("hidden");
    updateEstimatedDuration();
  });
  document.getElementById("loop-count-input").addEventListener("input", (e) => {
    profile.loop_count = Math.max(1, parseInt(e.target.value) || 1);
    updateEstimatedDuration();
  });

  // 6. Random delay setups
  const randomToggle = document.getElementById("random-delay-toggle");
  randomToggle.addEventListener("change", (e) => {
    profile.random_delay_enabled = e.target.checked;
    const bounds = document.getElementById("random-delay-bounds");
    if (profile.random_delay_enabled) bounds.classList.remove("hidden");
    else bounds.classList.add("hidden");
  });
  document.getElementById("random-delay-min").addEventListener("input", (e) => {
    profile.random_delay_min = Math.max(50, parseInt(e.target.value) || 50);
  });
  document.getElementById("random-delay-max").addEventListener("input", (e) => {
    profile.random_delay_max = Math.max(50, parseInt(e.target.value) || 50);
  });

  // 7. Actions CRUD in Builder
  document.getElementById("btn-add-action").addEventListener("click", () => {
    profile.pattern.push({
      action_type: "NONE",
      press_duration: 200,
      delay_duration: 500
    });
    renderPatternTab();
    updateEstimatedDuration();
  });

  document.getElementById("btn-duplicate-action").addEventListener("click", () => {
    if (selectedActionIndex === null) {
      alert("Pilih aksi dari daftar terlebih dahulu!");
      return;
    }
    const origin = profile.pattern[selectedActionIndex];
    profile.pattern.splice(selectedActionIndex + 1, 0, {
      action_type: origin.action_type,
      press_duration: origin.press_duration,
      delay_duration: origin.delay_duration
    });
    selectedActionIndex++;
    renderPatternTab();
    updateEstimatedDuration();
  });

  document.getElementById("btn-delete-action").addEventListener("click", () => {
    if (selectedActionIndex === null) {
      alert("Pilih aksi yang ingin dihapus!");
      return;
    }
    if (confirm("Apakah Anda yakin ingin menghapus aksi terpilih?")) {
      profile.pattern.splice(selectedActionIndex, 1);
      selectedActionIndex = null;
      closeActionEditor();
      renderPatternTab();
      updateEstimatedDuration();
    }
  });

  document.getElementById("btn-move-up").addEventListener("click", () => {
    if (selectedActionIndex === null || selectedActionIndex === 0) return;
    const temp = profile.pattern[selectedActionIndex];
    profile.pattern[selectedActionIndex] = profile.pattern[selectedActionIndex - 1];
    profile.pattern[selectedActionIndex - 1] = temp;
    selectedActionIndex--;
    renderPatternTab();
  });

  document.getElementById("btn-move-down").addEventListener("click", () => {
    if (selectedActionIndex === null || selectedActionIndex >= profile.pattern.length - 1) return;
    const temp = profile.pattern[selectedActionIndex];
    profile.pattern[selectedActionIndex] = profile.pattern[selectedActionIndex + 1];
    profile.pattern[selectedActionIndex + 1] = temp;
    selectedActionIndex++;
    renderPatternTab();
  });

  // 8. Editor Changes bindings
  document.getElementById("editor-action-type").addEventListener("change", (e) => {
    if (selectedActionIndex !== null) {
      profile.pattern[selectedActionIndex].action_type = e.target.value;
      renderPatternTab();
    }
  });
  document.getElementById("editor-press-duration").addEventListener("input", (e) => {
    if (selectedActionIndex !== null) {
      profile.pattern[selectedActionIndex].press_duration = Math.max(50, parseInt(e.target.value) || 50);
      renderPatternTab();
      updateEstimatedDuration();
    }
  });
  document.getElementById("editor-delay-duration").addEventListener("input", (e) => {
    if (selectedActionIndex !== null) {
      profile.pattern[selectedActionIndex].delay_duration = Math.max(0, parseInt(e.target.value) || 0);
      renderPatternTab();
      updateEstimatedDuration();
    }
  });
  document.getElementById("btn-close-editor").addEventListener("click", closeActionEditor);

  // 9. Tester Toggle bindings
  document.getElementById("btn-tester-switch").addEventListener("click", toggleTesterState);

  // Simulation run triggers
  document.getElementById("btn-run-sim").addEventListener("click", () => {
    if (simRunning) stopSimulation();
    else startSimulation();
  });

  // Canvas Touches and Taps bindings
  const canvas = document.getElementById("sim-canvas");
  canvas.addEventListener("mousedown", (e) => handleCanvasTap(e, true));
  canvas.addEventListener("mouseup", (e) => handleCanvasTap(e, false));
  
  canvas.addEventListener("touchstart", (e) => {
    e.preventDefault();
    handleCanvasTap(e, true);
  }, { passive: false });
  canvas.addEventListener("touchend", (e) => {
    e.preventDefault();
    handleCanvasTap(e, false);
  }, { passive: false });

  // 10. EEPROM Upload & Read
  document.getElementById("btn-eeprom-upload").addEventListener("click", () => {
    if (!serialConnected) return;
    
    // Check validation first
    const issues = [];
    if (profile.pattern.length === 0) issues.push("Pola kosong");
    if (profile.pattern.length > 150) issues.push("Pola melebihi 150 aksi");
    if (profile.random_delay_enabled && profile.random_delay_min > profile.random_delay_max) issues.push("Batas random delay terbalik");

    if (issues.length > 0) {
      alert(`Upload dibatalkan karena kesalahan kritis:\n\n• ${issues.join("\n• ")}`);
      return;
    }

    if (confirm("Data EEPROM di Arduino akan ditimpa. Lanjutkan pengunggahan?")) {
      logToConsole("Memulai proses upload profil aktif ke EEPROM...");
      const hex = packProfileHex(profile);
      sendSerialCommand(`WRITE_CONFIG ${hex}`);
    }
  });

  document.getElementById("btn-eeprom-read").addEventListener("click", () => {
    if (!serialConnected) return;
    if (confirm("Konfigurasi aktif di aplikasi akan ditimpa dengan data Arduino. Lanjutkan?")) {
      sendSerialCommand("READ_CONFIG");
    }
  });

  // 11. Profiles JSON file load & save
  document.getElementById("btn-profile-save").addEventListener("click", () => {
    const jsonStr = JSON.stringify(profile, null, 2);
    
    // Copy to clipboard fallback (guaranteed to work everywhere, including Cordova)
    let copied = false;
    try {
      const el = document.createElement('textarea');
      el.value = jsonStr;
      document.body.appendChild(el);
      el.select();
      document.execCommand('copy');
      document.body.removeChild(el);
      copied = true;
    } catch (err) {
      console.warn("Gagal menyalin otomatis:", err);
    }

    try {
      const blob = new Blob([jsonStr], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      
      const a = document.createElement("a");
      a.href = url;
      a.download = "robot_profile.json";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      logToConsole("Profil berhasil diekspor ke file robot_profile.json.");
      
      if (copied) {
        alert("Konfigurasi profil berhasil diekspor ke file!\n\n(Salinan teks JSON juga otomatis disimpan di clipboard Anda sebagai cadangan).");
      } else {
        alert("Konfigurasi profil berhasil diekspor ke file!");
      }
    } catch (e) {
      logToConsole(`Gagal mengunduh berkas: ${e.message}`);
      if (copied) {
        alert("Unduhan berkas dinonaktifkan oleh lingkungan HP/APK.\n\nTenang! Konfigurasi profil Anda telah berhasil DISALIN ke clipboard Anda secara otomatis. Silakan tempelkan (paste) di aplikasi catatan Anda.");
      } else {
        alert("Gagal mengunduh berkas profil di browser/APK ini.");
      }
    }
  });

  document.getElementById("btn-profile-load").addEventListener("click", () => {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = ".json";
    
    input.addEventListener("change", (e) => {
      const file = e.target.files[0];
      if (!file) return;
      
      const reader = new FileReader();
      reader.onload = (evt) => {
        try {
          const loaded = JSON.parse(evt.target.result);
          
          // Re-populate profile active values
          profile.loop_mode = loaded.loop_mode || "INFINITY";
          profile.loop_count = loaded.loop_count || 1;
          profile.random_delay_enabled = loaded.random_delay_enabled || false;
          profile.random_delay_min = loaded.random_delay_min || 100;
          profile.random_delay_max = loaded.random_delay_max || 1000;
          profile.auto_start = loaded.auto_start || false;
          profile.pattern = loaded.pattern || [];
          
          if (loaded.servos) {
            loaded.servos.forEach((s, idx) => {
              if (profile.servos[idx]) {
                profile.servos[idx].up_angle = s.up_angle;
                profile.servos[idx].press_angle = s.press_angle;
              }
            });
          }

          // Reload UI views
          renderCalibrationTab();
          renderPatternTab();
          updateEstimatedDuration();
          renderValidationTab();
          
          logToConsole(`Profil berhasil dimuat dari file: ${file.name}`);
          alert("Profil sukses dimuat!");
        } catch (err) {
          alert("Gagal mem-parsing file JSON!");
        }
      };
      reader.readAsText(file);
    });
    
    input.click();
  });

  // --- LOCAL SLOTS STORAGE HANDLERS ---
  function updateSlotUI(slotNum) {
    const info = localStorage.getItem(`robot_profile_slot_info_${slotNum}`);
    const lbl = document.getElementById(`lbl-slot-${slotNum}`);
    const btnLoad = document.getElementById(`btn-slot-load-${slotNum}`);
    
    if (info) {
      if (lbl) {
        lbl.innerText = `Slot ${slotNum}: ${info}`;
        lbl.style.color = "var(--accent-green)";
      }
      if (btnLoad) {
        btnLoad.disabled = false;
        btnLoad.classList.remove("disabled");
      }
    } else {
      if (lbl) {
        lbl.innerText = `Slot ${slotNum}: Kosong`;
        lbl.style.color = "var(--text-muted)";
      }
      if (btnLoad) {
        btnLoad.disabled = true;
        btnLoad.classList.add("disabled");
      }
    }
  }

  function saveProfileToSlot(slotNum) {
    try {
      const jsonStr = JSON.stringify(profile);
      localStorage.setItem(`robot_profile_slot_${slotNum}`, jsonStr);
      
      const timestamp = new Date().toLocaleDateString() + ' ' + new Date().toLocaleTimeString();
      const infoText = `Aktif (${timestamp})`;
      localStorage.setItem(`robot_profile_slot_info_${slotNum}`, infoText);
      
      updateSlotUI(slotNum);
      logToConsole(`Profil disimpan ke Slot ${slotNum} HP.`);
      alert(`Profil berhasil disimpan ke Slot ${slotNum}!`);
    } catch (err) {
      alert(`Gagal menyimpan ke Slot ${slotNum}: ${err.message}`);
    }
  }

  function loadProfileFromSlot(slotNum) {
    try {
      const jsonStr = localStorage.getItem(`robot_profile_slot_${slotNum}`);
      if (!jsonStr) return;
      
      const loaded = JSON.parse(jsonStr);
      
      // Re-populate profile active values
      profile.loop_mode = loaded.loop_mode || "INFINITY";
      profile.loop_count = loaded.loop_count || 1;
      profile.random_delay_enabled = loaded.random_delay_enabled || false;
      profile.random_delay_min = loaded.random_delay_min || 100;
      profile.random_delay_max = loaded.random_delay_max || 1000;
      profile.auto_start = loaded.auto_start || false;
      profile.pattern = loaded.pattern || [];
      
      if (loaded.servos) {
        loaded.servos.forEach((s, idx) => {
          if (profile.servos[idx]) {
            profile.servos[idx].up_angle = s.up_angle;
            profile.servos[idx].press_angle = s.press_angle;
          }
        });
      }

      // Reload UI views
      renderCalibrationTab();
      renderPatternTab();
      updateEstimatedDuration();
      renderValidationTab();
      
      logToConsole(`Profil berhasil dimuat dari Slot ${slotNum} HP.`);
      alert(`Profil sukses dimuat dari Slot ${slotNum}!`);
    } catch (err) {
      alert(`Gagal memuat Slot ${slotNum}: ${err.message}`);
    }
  }

  // Bind Slot Save Buttons
  const sBtnSave1 = document.getElementById("btn-slot-save-1");
  const sBtnSave2 = document.getElementById("btn-slot-save-2");
  const sBtnSave3 = document.getElementById("btn-slot-save-3");
  if (sBtnSave1) sBtnSave1.addEventListener("click", () => saveProfileToSlot(1));
  if (sBtnSave2) sBtnSave2.addEventListener("click", () => saveProfileToSlot(2));
  if (sBtnSave3) sBtnSave3.addEventListener("click", () => saveProfileToSlot(3));

  // Bind Slot Load Buttons
  const sBtnLoad1 = document.getElementById("btn-slot-load-1");
  const sBtnLoad2 = document.getElementById("btn-slot-load-2");
  const sBtnLoad3 = document.getElementById("btn-slot-load-3");
  if (sBtnLoad1) sBtnLoad1.addEventListener("click", () => loadProfileFromSlot(1));
  if (sBtnLoad2) sBtnLoad2.addEventListener("click", () => loadProfileFromSlot(2));
  if (sBtnLoad3) sBtnLoad3.addEventListener("click", () => loadProfileFromSlot(3));

  // Initial slot UI refreshes
  updateSlotUI(1);
  updateSlotUI(2);
  updateSlotUI(3);

  document.getElementById("btn-refresh-validation").addEventListener("click", () => {
    renderValidationTab();
  });

  // 12. QWERTY Tester Event Bindings
  document.getElementById("btn-tester-qwerty-switch").addEventListener("click", () => {
    const btn = document.getElementById("btn-tester-qwerty-switch");
    testerQwertyActive = !testerQwertyActive;
    if (testerQwertyActive) {
      btn.innerText = "🟢 STATUS: AKTIF";
      btn.className = "switch-btn on";
    } else {
      btn.innerText = "🔴 STATUS: NONAKTIF";
      btn.className = "switch-btn off";
      keyboardLayout.forEach(k => { keysPressed[k.keysym] = false; });
      drawTesterKeys();
    }
  });

  const testerCanvas = document.getElementById("tester-canvas");
  if (testerCanvas) {
    testerCanvas.addEventListener("mousedown", (e) => handleTesterCanvasClick(e, true));
    testerCanvas.addEventListener("mouseup", (e) => handleTesterCanvasClick(e, false));
    testerCanvas.addEventListener("touchstart", (e) => {
      e.preventDefault();
      handleTesterCanvasClick(e, true);
    }, { passive: false });
    testerCanvas.addEventListener("touchend", (e) => {
      e.preventDefault();
      handleTesterCanvasClick(e, false);
    }, { passive: false });
  }

  // 13. Neso Tracker Event Bindings
  document.getElementById("btn-mobile-wallet-save").addEventListener("click", saveMobileWallet);
  document.getElementById("btn-mobile-wallet-delete").addEventListener("click", deleteMobileWallet);
  
  // Populate initial MetaMask address field
  document.getElementById("mobile-wallet-address").value = mobileWalletAddress;

  // Initial runs
  renderCalibrationTab();
  renderPatternTab();
  updateEstimatedDuration();
  renderValidationTab();

  // Setup QWERTY physical keyboard capture
  setupPhysicalKeyboardListeners();

  // Start Tracker digital clock loops
  updateMobileTrackerLoop();

  // Periodically query Henesys blockchain balance (every 10s)
  setInterval(() => {
    if (mobileWalletAddress) fetchMobileRpcBalance();
  }, 10000);

  // Resize canvas event
  window.addEventListener("resize", () => {
    initSimCanvas();
    initTesterCanvas();
  });
  
});

/* ==========================================
   PENGUJI TOMBOL QWERTY PROC DRAW ENGINE
   ========================================== */
function initTesterCanvas() {
  const canvas = document.getElementById("tester-canvas");
  if (!canvas) return;
  canvas.width = 800;
  canvas.height = 220;
  drawTesterKeys();
}

function drawTesterKeys() {
  const canvas = document.getElementById("tester-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const cw = canvas.width;
  const ch = canvas.height;

  ctx.clearRect(0, 0, cw, ch);

  const gap = 3;
  const paddingX = 10;
  const paddingY = 10;

  const uWidth = (cw - 2 * paddingX - 22 * gap) / 23.0;
  const keyH = (ch - 2 * paddingY - 5 * gap) / 6.3;

  keyboardLayout.forEach(k => {
    const keyX = paddingX + k.x * (uWidth + gap);
    const keyY = paddingY + k.y * (keyH + gap);
    const keyW = k.w * uWidth + (k.w - 1.0) * gap;
    const keyHActual = k.h * keyH + (k.h - 1.0) * gap;

    const isPressed = keysPressed[k.keysym];
    const isRobotKey = k.keysym in keyToServo;

    if (isPressed) {
      ctx.fillStyle = "#2ed573";
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
    } else if (isRobotKey) {
      ctx.fillStyle = "#1c2430";
      ctx.strokeStyle = "#ffa502";
      ctx.lineWidth = 2.5;
    } else {
      ctx.fillStyle = "#151b26";
      ctx.strokeStyle = "#2f3542";
      ctx.lineWidth = 1;
    }

    ctx.beginPath();
    if (ctx.roundRect) {
      ctx.roundRect(keyX, keyY, keyW, keyHActual, 4);
    } else {
      ctx.rect(keyX, keyY, keyW, keyHActual);
    }
    ctx.fill();
    ctx.stroke();

    if (isPressed) ctx.fillStyle = "#ffffff";
    else if (isRobotKey) ctx.fillStyle = "#ffa502";
    else ctx.fillStyle = "#a4b0be";

    const fontSz = k.label.length > 5 ? 7 : 9;
    ctx.font = `bold ${fontSz}px sans-serif`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(k.label, keyX + keyW / 2, keyY + keyHActual / 2);
  });
}

function handleTesterCanvasClick(e, isPressed) {
  if (!testerQwertyActive) return;
  const canvas = document.getElementById("tester-canvas");
  const rect = canvas.getBoundingClientRect();
  
  const clientX = e.touches ? e.touches[0].clientX : e.clientX;
  const clientY = e.touches ? e.touches[0].clientY : e.clientY;
  
  const clickX = ((clientX - rect.left) / rect.width) * canvas.width;
  const clickY = ((clientY - rect.top) / rect.height) * canvas.height;

  const gap = 3;
  const paddingX = 10;
  const paddingY = 10;
  const uWidth = (canvas.width - 2 * paddingX - 22 * gap) / 23.0;
  const keyH = (canvas.height - 2 * paddingY - 5 * gap) / 6.3;

  for (const k of keyboardLayout) {
    const keyX = paddingX + k.x * (uWidth + gap);
    const keyY = paddingY + k.y * (keyH + gap);
    const keyW = k.w * uWidth + (k.w - 1.0) * gap;
    const keyHActual = k.h * keyH + (k.h - 1.0) * gap;

    if (clickX >= keyX && clickX <= keyX + keyW && clickY >= keyY && clickY <= keyY + keyHActual) {
      if (keysPressed[k.keysym] !== isPressed) {
        keysPressed[k.keysym] = isPressed;
        drawTesterKeys();

        const sIdx = keyToServo[k.keysym];
        if (sIdx !== undefined) {
          const sConf = profile.servos[sIdx];
          if (sConf) {
            const angle = isPressed ? sConf.press_angle : sConf.up_angle;
            sendSerialCommand(`TEST_SERVO ${sIdx} ${angle}`);
          }
        }
      }
      break;
    }
  }
}

function setupPhysicalKeyboardListeners() {
  window.addEventListener("keydown", (e) => {
    if (!testerQwertyActive || activeTab !== "tester") return;
    
    if (e.key === "Tab" || e.key === " ") {
      e.preventDefault();
    }

    let keysym = e.key;
    if (keysym === "Control") keysym = e.location === 1 ? "Control_L" : "Control_R";
    if (keysym === "Shift") keysym = e.location === 1 ? "Shift_L" : "Shift_R";
    if (keysym === "Alt") keysym = e.location === 1 ? "Alt_L" : "Alt_R";
    if (keysym === "Meta") keysym = "Win_L";
    if (keysym === "ArrowUp") keysym = "Up";
    if (keysym === "ArrowDown") keysym = "Down";
    if (keysym === "ArrowLeft") keysym = "Left";
    if (keysym === "ArrowRight") keysym = "Right";
    if (keysym === "Enter") keysym = "Return";

    let targetKey = null;
    if (keysPressed[keysym] !== undefined) {
      targetKey = keysym;
    } else if (keysPressed[keysym.toLowerCase()] !== undefined) {
      targetKey = keysym.toLowerCase();
    } else if (keysymAliases[keysym] !== undefined) {
      targetKey = keysymAliases[keysym];
    } else if (keysymAliases[keysym.toLowerCase()] !== undefined) {
      targetKey = keysymAliases[keysym.toLowerCase()];
    }

    if (targetKey) {
      if (!keysPressed[targetKey]) {
        keysPressed[targetKey] = true;
        drawTesterKeys();

        const sIdx = keyToServo[targetKey];
        if (sIdx !== undefined) {
          const sConf = profile.servos[sIdx];
          if (sConf) {
            const angle = sConf.press_angle;
            sendSerialCommand(`TEST_SERVO ${sIdx} ${angle}`);
          }
        }
      }
    }
  });

  window.addEventListener("keyup", (e) => {
    if (!testerQwertyActive || activeTab !== "tester") return;

    let keysym = e.key;
    if (keysym === "Control") keysym = e.location === 1 ? "Control_L" : "Control_R";
    if (keysym === "Shift") keysym = e.location === 1 ? "Shift_L" : "Shift_R";
    if (keysym === "Alt") keysym = e.location === 1 ? "Alt_L" : "Alt_R";
    if (keysym === "Meta") keysym = "Win_L";
    if (keysym === "ArrowUp") keysym = "Up";
    if (keysym === "ArrowDown") keysym = "Down";
    if (keysym === "ArrowLeft") keysym = "Left";
    if (keysym === "ArrowRight") keysym = "Right";
    if (keysym === "Enter") keysym = "Return";

    const releasedKeys = [];
    if (keysPressed[keysym] !== undefined) releasedKeys.push(keysym);
    else if (keysPressed[keysym.toLowerCase()] !== undefined) releasedKeys.push(keysym.toLowerCase());
    else if (keysymAliases[keysym] !== undefined) releasedKeys.push(keysymAliases[keysym]);
    else if (keysymAliases[keysym.toLowerCase()] !== undefined) releasedKeys.push(keysymAliases[keysym.toLowerCase()]);

    if (keysym.includes("Shift")) {
      releasedKeys.push("Shift_L");
      releasedKeys.push("Shift_R");
    }

    releasedKeys.forEach(targetKey => {
      if (keysPressed[targetKey]) {
        keysPressed[targetKey] = false;
        drawTesterKeys();

        const sIdx = keyToServo[targetKey];
        if (sIdx !== undefined) {
          const sConf = profile.servos[sIdx];
          if (sConf) {
            const angle = sConf.up_angle;
            sendSerialCommand(`TEST_SERVO ${sIdx} ${angle}`);
          }
        }
      }
    });
  });
}

/* ==========================================
   PEMANTAUAN & PENDAPATAN TRACKER MODULE
   ========================================== */
function saveMobileWallet() {
  const addr = document.getElementById("mobile-wallet-address").value.trim();
  if (addr && (!addr.startsWith("0x") || addr.length !== 42)) {
    alert("Alamat wallet MetaMask tidak valid!\nAlamat harus diawali dengan '0x' dan memiliki panjang 42 karakter.");
    return;
  }
  mobileWalletAddress = addr;
  localStorage.setItem("mobileWalletAddress", addr);
  
  if (addr) {
    document.getElementById("mobile-earn-details").classList.remove("hidden");
    document.getElementById("lbl-mobile-wallet-warning").classList.add("hidden");
    logToConsole(`Metamask Wallet disimpan: ${addr.slice(0, 6)}...${addr.slice(-4)}`);
    alert("Alamat wallet MetaMask disimpan!");
  } else {
    document.getElementById("mobile-earn-details").classList.add("hidden");
    document.getElementById("lbl-mobile-wallet-warning").classList.remove("hidden");
    logToConsole("Alamat wallet MetaMask dihapus.");
    alert("Alamat wallet MetaMask dihapus!");
  }
  
  mobileInitialNeso = null;
  mobileInitialNxpc = null;
  fetchMobileRpcBalance();
}

function deleteMobileWallet() {
  document.getElementById("mobile-wallet-address").value = "";
  saveMobileWallet();
}

async function fetchMobileRpcBalance() {
  if (!mobileWalletAddress) return;
  const callData = "0x70a08231" + mobileWalletAddress.toLowerCase().replace("0x", "").padStart(64, "0");
  const payload = {
    jsonrpc: "2.0",
    method: "eth_call",
    params: [
      {
        to: "0x07E49Ad54FcD23F6e7B911C2068F0148d1827c08",
        data: callData
      },
      "latest"
    ],
    id: 1
  };

  const urls = ["https://henesys-rpc.msu.io", "https://subnets.avax.network/henesys/"];
  let success = false;
  let errorMsg = "";

  for (const url of urls) {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      if (response.ok) {
        const resData = await response.json();
        if (resData.result) {
          const hex = resData.result.replace("0x", "") || "0";
          const wei = BigInt("0x" + hex);
          const neso = Number(wei) / 1e18;
          const nxpc = neso / 100000.0;

          mobileCurrentNeso = neso;
          mobileCurrentNxpc = nxpc;
          success = true;

          if (mobileSessionActive && mobileInitialNeso === null) {
            mobileInitialNeso = neso;
            mobileInitialNxpc = nxpc;
          }
          break;
        } else {
          errorMsg = resData.error ? resData.error.message : "RPC Error";
        }
      } else {
        errorMsg = `HTTP ${response.status}`;
      }
    } catch (err) {
      errorMsg = err.message;
    }
  }

  const statusLbl = document.getElementById("lbl-mobile-rpc-status");
  if (success) {
    statusLbl.innerText = "● Terhubung ke Henesys Network";
    statusLbl.style.color = "var(--accent-green)";

    document.getElementById("lbl-mobile-bal-neso").innerText = `${mobileCurrentNeso.toLocaleString(undefined, { maximumFractionDigits: 0 })} NESO`;
    document.getElementById("lbl-mobile-bal-nxpc").innerText = `${mobileCurrentNxpc.toFixed(4)} NXPC`;

    if (mobileSessionActive && mobileInitialNeso !== null) {
      const earnedNeso = Math.max(0, mobileCurrentNeso - mobileInitialNeso);
      const earnedNxpc = Math.max(0.0, mobileCurrentNxpc - mobileInitialNxpc);
      document.getElementById("lbl-mobile-earn-neso").innerText = `+${earnedNeso.toLocaleString(undefined, { maximumFractionDigits: 0 })} NESO`;
      document.getElementById("lbl-mobile-earn-nxpc").innerText = `+${earnedNxpc.toFixed(4)} NXPC`;
    } else {
      document.getElementById("lbl-mobile-earn-neso").innerText = "+0 NESO";
      document.getElementById("lbl-mobile-earn-nxpc").innerText = "+0.0000 NXPC";
    }
  } else {
    statusLbl.innerText = `● Gangguan Koneksi Jaringan (${errorMsg})`;
    statusLbl.style.color = "var(--accent-red)";
  }
}

function updateMobileTrackerLoop() {
  if (mobileSessionActive) {
    const elapsed = Date.now() - mobileSessionStartTime;
    const hrs = Math.floor(elapsed / 3600000);
    const mins = Math.floor((elapsed % 3600000) / 60000);
    const secs = Math.floor((elapsed % 60000) / 1000);
    
    document.getElementById("lbl-mobile-timer").innerText = 
      `${hrs.toString().padStart(2, "0")}:${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
    document.getElementById("lbl-mobile-session-status").innerText = "🟢 ROBOT BERJALAN";
    document.getElementById("lbl-mobile-session-status").style.color = "var(--accent-green)";
  } else {
    document.getElementById("lbl-mobile-timer").innerText = "00:00:00";
    document.getElementById("lbl-mobile-session-status").innerText = "🔴 ROBOT BERHENTI";
    document.getElementById("lbl-mobile-session-status").style.color = "var(--accent-red)";
  }

  if (mobileWalletAddress) {
    document.getElementById("mobile-earn-details").classList.remove("hidden");
    document.getElementById("lbl-mobile-wallet-warning").classList.add("hidden");
  } else {
    document.getElementById("mobile-earn-details").classList.add("hidden");
    document.getElementById("lbl-mobile-wallet-warning").classList.remove("hidden");
  }

  setTimeout(updateMobileTrackerLoop, 1000);
}
