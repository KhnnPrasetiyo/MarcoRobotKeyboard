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
let serialPort = null;
let serialWriter = null;
let serialReader = null;
let keepReading = false;
let serialConnected = false;
let selectedActionIndex = null;
let testerActive = false;

// Simulation State Variables
let simRunning = false;
let simTimeoutId = null;
let simStepIndex = 0;

/* ==========================================
   WEB SERIAL CONNECTION MANAGEMENT
   ========================================== */
async function connectSerial() {
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

    if (state === "STOPPED" || state === "IDLE" || state === "EMERGENCY_STOP") {
      stepRow.classList.add("hidden");
    }
  } 
  else if (line.startsWith("STEP:")) {
    const stepInfo = line.replace("STEP:", "").trim();
    stepRow.classList.remove("hidden");
    stepText.innerText = stepInfo;
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
    
    portText.innerHTML = "Status Port: <b>TERBUNGKUS (Serial OTG)</b>";
    
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
  });
  document.getElementById("btn-start").addEventListener("click", () => {
    sendSerialCommand("START");
  });
  document.getElementById("btn-stop").addEventListener("click", () => {
    sendSerialCommand("STOP");
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

  document.getElementById("btn-refresh-validation").addEventListener("click", () => {
    renderValidationTab();
  });

  // Initial runs
  renderCalibrationTab();
  renderPatternTab();
  updateEstimatedDuration();
  renderValidationTab();

  // Resize canvas event
  window.addEventListener("resize", initSimCanvas);
  
});
