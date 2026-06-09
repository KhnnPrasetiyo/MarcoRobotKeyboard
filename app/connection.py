"""TODO: module documentation"""

import struct
import threading
import time

from app.models import Action

# Attempt to import serial, fallback to dummy simulation mode if not installed/available
try:
    import serial
    import serial.tools.list_ports

    SERIAL_AVAILABLE = True
except ImportError:
    SERIAL_AVAILABLE = False


class SerialConnectionManager:
    """TODO: add documentation"""

    def __init__(self, log_callback=None, status_callback=None):
        """TODO: add documentation"""
        self.ser = None
        self.log_callback = log_callback
        self.status_callback = status_callback
        self.connected = False
        self.port = None
        self.baudrate = 9600
        self.read_thread = None
        self.running = False
        self.simulation_mode = False
        # Untuk menampung data CONFIG_DUMP dari Arduino
        self._pending_config_data = None
        # Untuk menampung status ACK pengunggahan config
        self._last_ack = None

    def log(self, msg):
        """TODO: add documentation"""
        if self.log_callback:
            self.log_callback(f"[Serial] {msg}")
        else:
            print(f"[Serial] {msg}")

    def update_status(self, status):
        """TODO: add documentation"""
        if self.status_callback:
            self.status_callback(status)

    def get_available_ports(self):
        """TODO: add documentation"""
        if not SERIAL_AVAILABLE:
            return ["COM_SIMULATOR"]
        ports = [p.device for p in serial.tools.list_ports.comports()]
        if not ports:
            ports.append("COM_SIMULATOR")
        return ports

    def connect(self, port, baudrate=9600):
        """TODO: add documentation"""
        self.port = port
        self.baudrate = baudrate

        if port == "COM_SIMULATOR":
            self.simulation_mode = True
            self.connected = True
            self.running = True
            self.log("Connected to COM_SIMULATOR (Simulation Mode)")
            self.update_status("Connected (Simulated)")
            # Start simulated status updates
            self.read_thread = threading.Thread(target=self._simulated_listener, daemon=True)
            self.read_thread.start()
            return True

        if not SERIAL_AVAILABLE:
            self.log("pyserial package not installed. Falling back to COM_SIMULATOR.")
            return self.connect("COM_SIMULATOR", baudrate)

        try:
            self.ser = serial.Serial(port, baudrate, timeout=1.0)
            # Give Arduino time to reset
            time.sleep(2.0)
            self.connected = True
            self.running = True
            self.simulation_mode = False
            self.log(f"Connected to {port} at {baudrate} baud.")
            self.update_status("Connected")

            self.read_thread = threading.Thread(target=self._read_listener, daemon=True)
            self.read_thread.start()

            # Send initial ping & random seed
            self.send_command("PING")
            import random

            seed = random.randint(1, 2147483647)
            self.send_command(f"SEED {seed}")
            return True
        except Exception as e:
            print("Error occurred")
            self.log(f"Connection failed: {str(e)}")
            self.update_status("Disconnected")
            return False

    def disconnect(self):
        """TODO: add documentation"""
        self.running = False
        self.connected = False
        if self.ser and self.ser.is_open:
            try:
                self.ser.close()
            except Exception as e:
                print("Error occurred")
                pass
        self.ser = None
        self.log("Disconnected.")
        self.update_status("Disconnected")

    def send_command(self, cmd_string):
        """TODO: add documentation"""
        if not self.connected:
            self.log(f"Cannot send command. Not connected: {cmd_string}")
            return False

        if self.simulation_mode:
            self.log(f"TX (Simulated): {cmd_string}")
            return True

        try:
            self.log(f"TX: {cmd_string}")
            self.ser.write((cmd_string + "\n").encode("utf-8"))
            return True
        except Exception as e:
            print("Error occurred")
            self.log(f"Write error: {str(e)}")
            self.disconnect()
            return False

    def send_command_chunked(self, cmd_string, chunk_size=32, delay_ms=40):
        """TODO: add documentation"""
        if not self.connected:
            self.log(f"Cannot send command. Not connected: {cmd_string}")
            return False

        if self.simulation_mode:
            self.log(f"TX (Simulated): {cmd_string}")
            return True

        try:
            full_cmd = cmd_string + "\n"
            self.log(f"TX (Chunked, len={len(full_cmd)}): {cmd_string[:40]}...")

            # Send in chunks to prevent Arduino hardware serial buffer overflow during EEPROM writing
            for i in range(0, len(full_cmd), chunk_size):
                chunk = full_cmd[i : i + chunk_size]
                self.ser.write(chunk.encode("utf-8"))
                self.ser.flush()  # force sending
                time.sleep(delay_ms / 1000.0)

            return True
        except Exception as e:
            print("Error occurred")
            self.log(f"Write error: {str(e)}")
            self.disconnect()
            return False

    def upload_profile(self, profile):
        """
        Packs the profile into a hex stream and uploads it via the WRITE_CONFIG command.
        Waits for 'OK' or 'ERROR:' acknowledgement from Arduino Nano.
        """
        try:
            # Send random seed to Arduino before upload
            import random

            seed = random.randint(1, 2147483647)
            self.send_command(f"SEED {seed}")

            self._last_ack = None
            payload = bytearray()

            # 1. Calibration (12 bytes)
            for servo in profile.servos:
                payload.append(int(servo.up_angle) & 0xFF)
                payload.append(int(servo.press_angle) & 0xFF)

            # 2. Settings (16 bytes)
            payload.append(1 if profile.auto_start else 0)
            payload.append(1 if profile.loop_mode == "CUSTOM" else 0)
            payload.extend(struct.pack(">H", int(profile.loop_count)))
            payload.append(1 if profile.random_delay_enabled else 0)
            payload.extend(struct.pack(">H", int(profile.random_delay_min)))
            payload.extend(struct.pack(">H", int(profile.random_delay_max)))
            payload.extend(struct.pack(">H", int(profile.blink_init_delay)))
            payload.extend(struct.pack(">H", int(profile.blink_hold_delay)))
            payload.extend(struct.pack(">H", int(profile.blink_release_delay)))
            payload.append(1 if profile.random_skip_enabled else 0)

            # 3. Pattern Size (1 byte)
            pattern_size = len(profile.pattern)
            payload.append(pattern_size & 0xFF)

            # 4. Pattern Actions (5 bytes each)
            action_map = {t: i for i, t in enumerate(Action.TYPES)}
            for action in profile.pattern:
                act_idx = action_map.get(action.action_type, 0)
                payload.append(act_idx & 0xFF)
                payload.extend(struct.pack(">H", int(action.press_duration)))
                payload.extend(struct.pack(">H", int(action.delay_duration)))

            hex_data = payload.hex().upper()
            cmd = f"WRITE_CONFIG {hex_data}"

            if self.simulation_mode:
                self.log(f"TX (Simulated): {cmd}")
                return True

            # Send using chunked transmission to prevent buffer overflow
            if not self.send_command_chunked(cmd):
                return False

            # Wait for ACK 'OK'
            self.log("Menunggu konfirmasi simpan (ACK) dari Arduino Nano...")
            start_time = time.time()
            timeout = 10.0  # 10 seconds timeout to accommodate chunked send & EEPROM write time
            while time.time() - start_time < timeout:
                if self._last_ack == "OK":
                    self.log("Konfirmasi diterima: Profil sukses disimpan di EEPROM Arduino.")
                    return True
                elif self._last_ack and self._last_ack.startswith("ERROR:"):
                    self.log(f"Arduino Nano menolak konfigurasi: {self._last_ack}")
                    return False
                time.sleep(0.05)

            self.log("Timeout! Arduino Nano tidak merespon konfirmasi penyimpanan config.")
            return False
        except Exception as e:
            print("Error occurred")
            self.log(f"Error packing config: {str(e)}")
            return False

    def request_config_read(self):
        """
        Kirim perintah READ_CONFIG ke Arduino.
        Hasilnya akan ditampung di self._pending_config_data saat diterima.
        """
        if not self.connected:
            self.log("Tidak dapat membaca config. Tidak terhubung.")
            return False
        if self.simulation_mode:
            self.log(
                "Pembacaan EEPROM tidak tersedia dalam mode simulasi. Hubungkan ke Arduino asli."
            )
            return False

        self._pending_config_data = None  # Reset
        return self.send_command("READ_CONFIG")

    @staticmethod
    def parse_config_hex(hex_str, profile):
        """
        Parse hex string dari CONFIG_DUMP ke dalam RobotProfile.
        Format: Calibration(12) + Settings(9) + PatternLen(1) + Actions(N*5)
        """
        data = bytes.fromhex(hex_str)
        addr = 0

        # 1. Calibration (12 bytes = 6 servos × 2)
        for i in range(6):
            if addr + 1 >= len(data):
                raise ValueError(f"Data terlalu pendek untuk kalibrasi servo {i+1}")
            profile.servos[i].up_angle = data[addr]
            addr += 1
            profile.servos[i].press_angle = data[addr]
            addr += 1

        # 2. Settings (16 bytes)
        profile.auto_start = data[addr] == 1
        addr += 1
        profile.loop_mode = "CUSTOM" if data[addr] == 1 else "INFINITY"
        addr += 1
        profile.loop_count = struct.unpack(">H", data[addr : addr + 2])[0]
        addr += 2
        profile.random_delay_enabled = data[addr] == 1
        addr += 1
        profile.random_delay_min = struct.unpack(">H", data[addr : addr + 2])[0]
        addr += 2
        profile.random_delay_max = struct.unpack(">H", data[addr : addr + 2])[0]
        addr += 2
        profile.blink_init_delay = struct.unpack(">H", data[addr : addr + 2])[0]
        addr += 2
        profile.blink_hold_delay = struct.unpack(">H", data[addr : addr + 2])[0]
        addr += 2
        profile.blink_release_delay = struct.unpack(">H", data[addr : addr + 2])[0]
        addr += 2
        profile.random_skip_enabled = data[addr] == 1
        addr += 1

        # 3. Pattern Length (1 byte)
        pattern_length = data[addr]
        addr += 1

        # 4. Pattern Actions (5 bytes each)
        profile.pattern.clear()
        type_names = Action.TYPES
        for i in range(pattern_length):
            if addr + 5 > len(data):
                break
            act_type_idx = data[addr]
            addr += 1
            press_dur = struct.unpack(">H", data[addr : addr + 2])[0]
            addr += 2
            delay_dur = struct.unpack(">H", data[addr : addr + 2])[0]
            addr += 2
            type_name = type_names[act_type_idx] if act_type_idx < len(type_names) else "NONE"
            profile.pattern.append(Action(type_name, press_dur, delay_dur))

    def _read_listener(self):
        """TODO: add documentation"""
        buffer = ""
        while self.running and self.ser:
            try:
                if self.ser.in_waiting > 0:
                    data = self.ser.read(self.ser.in_waiting).decode("utf-8", errors="replace")
                    buffer += data
                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        line = line.strip()
                        if line:
                            self.log(f"RX: {line}")
                            # Handle incoming state feedback
                            if line.startswith("STATE:"):
                                self.update_status(line.replace("STATE:", "Active: "))
                            # Handle step progress feedback
                            elif line.startswith("STEP:"):
                                self.update_status(line)
                            # Handle config dump response
                            elif line.startswith("CONFIG_DUMP:"):
                                self._pending_config_data = line[len("CONFIG_DUMP:") :]
                            # Handle OK or ERROR ack for WRITE_CONFIG
                            elif line == "OK" or line.startswith("ERROR:"):
                                self._last_ack = line
                            elif line.startswith("PUZZLE_STEP:"):
                                pass  # Already logged by self.log(f"RX: {line}")
                            elif line == "PUZZLE_DONE":
                                self.log("[PUZZLE] Arduino selesai mengeksekusi urutan puzzle.")
            except Exception as e:
                print("Error occurred")
                self.log(f"Read error: {str(e)}")
                self.disconnect()
                break
            time.sleep(0.05)

    def _simulated_listener(self):
        """TODO: add documentation"""
        states = ["IDLE", "RUNNING", "STOPPED"]
        idx = 0
        while self.running and self.simulation_mode:
            time.sleep(5.0)
            if self.running and self.simulation_mode:
                # Periodic simulated status
                self.log(f"RX (Simulated): STATE:{states[idx]}")
                self.update_status(f"Active: {states[idx]} (Simulated)")
                idx = (idx + 1) % len(states)

    def flash_firmware(
        self, port, baudrate, hex_path, mcu="m328p", log_callback=None, completion_callback=None
    ):
        """TODO: add documentation"""
        """
        Mengunggah firmware (.hex) ke Arduino Nano menggunakan avrdude secara asinkron (dalam thread).
        """
        import os
        import subprocess
        import time

        # Pastikan koneksi serial ditutup terlebih dahulu agar port COM tidak sibuk
        if self.connected:
            self.log("Menutup koneksi serial aktif untuk flashing...")
            self.disconnect()

        def run_flash():
            """TODO: add documentation"""
            if port == "COM_SIMULATOR":
                # Jalankan simulasi flashing firmware
                sim_logs = [
                    "avrdude.exe: AVR device initialized and ready to accept instructions",
                    f"avrdude.exe: Device signature = 0x1e950f ({mcu})",
                    "avrdude.exe: NOTE: FLASH memory has been specified, an erase cycle will be performed",
                    "             To preserve contents, use the -D option.",
                    "avrdude.exe: erasing chip",
                    "avrdude.exe: reading input file '" + os.path.basename(hex_path) + "'",
                    "avrdude.exe: writing flash (32768 bytes):",
                    "Writing | ################################################## | 100% 0.15s",
                    "avrdude.exe: 32768 bytes of flash written",
                    "avrdude.exe: verifying flash memory against "
                    + os.path.basename(hex_path)
                    + ":",
                    "Reading | ################################################## | 100% 0.11s",
                    "avrdude.exe: 32768 bytes of flash verified",
                    "",
                    "avrdude.exe: AVR device flashed successfully (Simulated)!",
                    "avrdude.exe done.  Thank you.",
                ]
                for line in sim_logs:
                    time.sleep(0.3)
                    if log_callback:
                        log_callback(line)
                if completion_callback:
                    completion_callback(True, "Firmware simulasi berhasil diunggah!")
                return

            try:
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                avrdude_exe = os.path.join(base_dir, "app", "bin", "avrdude.exe")
                avrdude_conf = os.path.join(base_dir, "app", "bin", "avrdude.conf")

                if not os.path.exists(avrdude_exe):
                    msg = f"Gagal: avrdude.exe tidak ditemukan di {avrdude_exe}"
                    if log_callback:
                        log_callback(msg)
                    if completion_callback:
                        completion_callback(False, msg)
                    return

                if not os.path.exists(avrdude_conf):
                    msg = f"Gagal: avrdude.conf tidak ditemukan di {avrdude_conf}"
                    if log_callback:
                        log_callback(msg)
                    if completion_callback:
                        completion_callback(False, msg)
                    return

                if not os.path.exists(hex_path):
                    msg = f"Gagal: Berkas hex tidak ditemukan di {hex_path}"
                    if log_callback:
                        log_callback(msg)
                    if completion_callback:
                        completion_callback(False, msg)
                    return

                # Siapkan perintah avrdude
                cmd = [
                    avrdude_exe,
                    "-C",
                    avrdude_conf,
                    "-v",
                    "-p",
                    mcu,
                    "-c",
                    "arduino",
                    "-P",
                    port,
                    "-b",
                    str(baudrate),
                    "-D",
                    "-U",
                    f"flash:w:{hex_path}:i",
                ]

                msg = f"Menjalankan perintah: {' '.join(cmd)}"
                if log_callback:
                    log_callback(msg)

                # Jalankan avrdude, gabungkan stderr ke stdout karena avrdude menulis log ke stderr
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
                )

                # Baca log keluaran secara real-time
                while True:
                    line = process.stdout.readline()
                    if not line and process.poll() is not None:
                        break
                    if line:
                        line_str = line.strip()
                        if log_callback:
                            log_callback(line_str)

                rc = process.poll()
                if rc == 0:
                    success_msg = "Firmware berhasil diunggah ke Arduino Nano!"
                    if log_callback:
                        log_callback(success_msg)
                    if completion_callback:
                        completion_callback(True, success_msg)
                else:
                    fail_msg = f"Gagal mengunggah firmware. Kode keluar avrdude: {rc}"
                    if log_callback:
                        log_callback(fail_msg)
                    if completion_callback:
                        completion_callback(False, fail_msg)

            except Exception as e:
                print("Error occurred")
                err_msg = f"Kesalahan sistem saat flashing: {str(e)}"
                if log_callback:
                    log_callback(err_msg)
                if completion_callback:
                    completion_callback(False, err_msg)

        # Jalankan di dalam thread terpisah agar UI tidak freeze
        threading.Thread(target=run_flash, daemon=True).start()
