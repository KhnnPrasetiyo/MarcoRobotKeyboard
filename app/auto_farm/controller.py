"""Auto Farm Controller module for NanoKeyboardController."""

import json
import os
import random
# Define settings file path
import sys
import threading
import time
from pathlib import Path

import cv2
import numpy as np
import pygame

import app.auto_farm.vkeys as vkeys
from app.auto_farm.capture import Capture
from app.auto_farm.rune_solver.solver import RuneSolver
from app.auto_farm.utils import (distance, filter_color, load_image,
                                 match_score, multi_match, resolve_path)

if getattr(sys, "frozen", False):
    _settings_dir = os.path.dirname(sys.executable)
else:
    _settings_dir = os.path.abspath(".")
SETTINGS_FILE = os.path.join(_settings_dir, "auto_farm_settings.json")

# Color range for Rune magenta pixel on minimap (HSV)
RUNE_RANGES = (((130, 40, 200), (180, 255, 255)),)

# Load templates
try:
    RAW_RUNE_TPL = load_image("assets/rune_template.png")
    RUNE_FILTERED_TPL = filter_color(RAW_RUNE_TPL, RUNE_RANGES)
    RUNE_TEMPLATE = cv2.cvtColor(RUNE_FILTERED_TPL, cv2.COLOR_BGR2GRAY)

    ELITE_TEMPLATE = load_image("assets/elite_template.jpg", cv2.IMREAD_GRAYSCALE)
    DEATH_TEMPLATE = load_image("assets/death_template.png", cv2.IMREAD_GRAYSCALE)

    RUNE_BUFF_TEMPLATES = [
        load_image("assets/rune_buff_template.jpg", cv2.IMREAD_GRAYSCALE),
        load_image("assets/rune_buff_template_2.jpg", cv2.IMREAD_GRAYSCALE),
    ]

    LIE_TEMPLATES = []
    try:
        # Memuat secara dinamis semua template di folder assets/lie yang mengandung nama 'Crop' dan berakhiran .png / .jpg
        import glob
        import re

        lie_dir = resolve_path("assets/lie")
        if os.path.exists(lie_dir):
            for filename in os.listdir(lie_dir):
                if "crop" in filename.lower() and (
                    filename.endswith(".png") or filename.endswith(".jpg")
                ):
                    full_path = os.path.join(lie_dir, filename)
                    img_bgr = cv2.imread(full_path)
                    if img_bgr is not None:
                        # Default thresholds based on template type
                        if "lienew" in filename.lower():
                            threshold_gray = 0.90
                            threshold_bgr = 0.85
                        else:
                            threshold_gray = 0.83
                            threshold_bgr = 0.80
                        
                        # Override if custom threshold is present in filename, e.g. "LieNew_click_Crop_0.85.png" -> 0.85
                        match = re.search(r"_0\.(\d+)", filename)
                        if match:
                            threshold_gray = float(f"0.{match.group(1)}")
                            threshold_bgr = max(0.70, threshold_gray - 0.05)
                        
                        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                        LIE_TEMPLATES.append((filename, img_gray, img_bgr, threshold_gray, threshold_bgr))
            print(
                f"[Controller] Berhasil memuat {len(LIE_TEMPLATES)} template Lie Detector secara dinamis."
            )
        else:
            print(f"[Controller] Folder '{lie_dir}' tidak ditemukan!")
    except Exception as e:
        print(
            f"[Controller] Peringatan: Gagal memuat beberapa template Lie Detector secara dinamis: {e}"
        )
except Exception as e:
    print(f"[Controller] Gagal memuat template gambar: {e}")


class AutoFarmController:
    """Orchestrates Auto Rune solving and Field Boss safety warnings."""

    def __init__(self, connection, profile):
        """TODO: add documentation"""
        self.connection = connection
        self.profile = profile
        self.capture = Capture()
        self.solver = None

        # Load local settings
        self.settings = self.load_settings()

        self.running = False
        self.thread = None
        self.solving_rune = False
        self.alert_active = False
        self.last_lie_check_time = 0
        self.scaled_lie_templates = []
        self.pre_scaled_lie_templates = []

        # Caching for resolution-scaled templates to prevent scale mismatches
        self.last_scale = None
        self.scaled_elite = None
        self.scaled_death = None

        # Initialize pygame mixer for sound alerts
        try:
            pygame.mixer.init()
        except Exception as e:
            print(f"[Controller] Gagal menginisialisasi pygame mixer: {e}")

    def load_settings(self):
        """TODO: add documentation"""
        default_settings = {
            "enabled_rune": False,
            "enabled_boss": False,
            "enabled_lie_detector": False,
            "interact_key": "alt",
            "jump_key": "space",
            "vertical_jump_mode": "double_jump",
            "blink_key": "shift",
            "random_skip_enabled": False,
        }
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r") as f:
                    data = json.load(f)
                    default_settings.update(data)
            except Exception as e:
                print("Error occurred")
                pass
        return default_settings

    def save_settings(self):
        """TODO: add documentation"""
        try:
            with open(SETTINGS_FILE, "w") as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"[Controller] Gagal menyimpan pengaturan: {e}")

    def _focus_game_window(self):
        """Aktifkan dan fokuskan jendela game ke foreground sebelum melakukan input."""
        try:
            if self.capture and hasattr(self.capture, "window_obj") and self.capture.window_obj:
                hwnd = self.capture.window_obj._hWnd
                import win32api
                import win32con
                import win32gui
                import win32process

                # Cek apakah jendela game sudah berada di foreground
                foreground_hwnd = win32gui.GetForegroundWindow()
                if foreground_hwnd != hwnd:
                    self.connection.log(
                        f"[DEBUG-WINDOW] Memfokuskan jendela game (HWND: {hwnd})..."
                    )
                    # Jika diminimalkan, restore
                    if win32gui.IsIconic(hwnd):
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        time.sleep(0.1)

                    # Coba paksa fokus menggunakan metode Thread Input Attachment
                    try:
                        fore_thread = win32process.GetWindowThreadProcessId(foreground_hwnd)[0]
                        app_thread = win32api.GetCurrentThreadId()
                        if fore_thread != app_thread:
                            win32process.AttachThreadInput(app_thread, fore_thread, True)
                            win32gui.BringWindowToTop(hwnd)
                            win32gui.SetForegroundWindow(hwnd)
                            win32process.AttachThreadInput(app_thread, fore_thread, False)
                        else:
                            win32gui.SetForegroundWindow(hwnd)
                    except Exception as e:
                        print("Error occurred")
                        # Fallback ke SetForegroundWindow biasa
                        win32gui.SetForegroundWindow(hwnd)

                    time.sleep(0.3)  # Tunggu jeda agar fokus terdaftar
        except Exception as e:
            print("Error occurred")
            self.connection.log(f"[DEBUG-WINDOW] Gagal memfokuskan jendela game: {e}")

    def _get_servo_index_for_key(self, logical_key):
        """Maps logical key name to physical Arduino servo index (0-5)."""
        key_lower = logical_key.lower()
        if key_lower.startswith("puzzle_"):
            key_lower = key_lower[7:]  # "puzzle_left" -> "left"

        if key_lower == "left":
            return 0
        elif key_lower == "right":
            return 1
        elif key_lower == "up":
            return 2
        elif key_lower == "down":
            return 3
        elif key_lower in ["shift", "blink"]:
            return 4
        elif key_lower in ["interact", "space", "alt", "a"]:
            return 5
        return None

    def _hardware_key_down(self, key):
        """TODO: add documentation"""
        idx = self._get_servo_index_for_key(key)
        if idx is not None and idx < len(self.profile.servos):
            angle = self.profile.servos[idx].press_angle
            self.connection.log(
                f"[DEBUG-HARDWARE] Tahan tombol fisik via Servo {idx+1} ({self.profile.servos[idx].name}) -> Sudut: {angle}"
            )
            self.connection.send_command(f"TEST_SERVO {idx} {angle}")
            return True
        return False

    def _hardware_key_up(self, key):
        """TODO: add documentation"""
        idx = self._get_servo_index_for_key(key)
        if idx is not None and idx < len(self.profile.servos):
            angle = self.profile.servos[idx].up_angle
            self.connection.log(
                f"[DEBUG-HARDWARE] Lepas tombol fisik via Servo {idx+1} ({self.profile.servos[idx].name}) -> Sudut: {angle}"
            )
            self.connection.send_command(f"TEST_SERVO {idx} {angle}")
            return True
        return False

    def _hardware_press_key(self, key, down_time=0.35, up_time=0.65):
        """TODO: add documentation"""
        if self._hardware_key_down(key):
            time.sleep(down_time)
            self._hardware_key_up(key)
            time.sleep(up_time)
            return True
        return False

    def _press_key(self, logical_key, down_time=0.35, up_time=0.65, n=1):
        """Picu penekanan tombol secara fisik (servo) jika terhubung ke Arduino asli dan diaktifkan, atau virtual."""
        logical_lower = logical_key.lower()

        actual_key = logical_key
        if logical_lower.startswith("puzzle_"):
            actual_key = logical_lower[7:]  # "puzzle_left" -> "left"
        elif logical_lower == "interact":
            actual_key = self.settings.get("interact_key", "space")
        elif logical_lower == "blink":
            actual_key = self.settings.get("blink_key", "shift")
        elif logical_lower == "jump":
            actual_key = self.settings.get("jump_key", "alt")

        # Force software/virtual mode for movement and interact keys.
        # Hardware servos are ONLY allowed for arrow keys (which starts with 'puzzle_').
        is_puzzle_action = logical_lower.startswith("puzzle_") or logical_lower in ["left", "right", "up", "down"]
        
        if (
            is_puzzle_action
            and self.settings.get("rune_input_mode", "software") == "hardware"
            and self.connection.connected
            and not self.connection.simulation_mode
        ):
            for _ in range(n):
                self._hardware_press_key(logical_key, down_time, up_time)
        else:
            self.connection.log(
                f"[DEBUG-VIRTUAL] Menekan tombol virtual '{actual_key}' ({logical_key.upper()})"
            )
            vkeys.press(actual_key, n, down_time, up_time)

    def _send_puzzle_sequence(self, solution):
        """Kirim urutan puzzle ke Arduino. Arduino handle kalibrasi sendiri."""
        seq = ",".join([s.upper() for s in solution])
        self.connection.log(f"[RUNE] Mengirim PUZZLE_SEQ ke Arduino: {seq}")

        if not self.connection.connected:
            self.connection.log("[ERROR] Tidak terhubung! Tidak bisa kirim PUZZLE_SEQ.")
            return False

        if self.connection.simulation_mode:
            self.connection.log(f"[DEBUG-SERVO] (Simulasi) PUZZLE_SEQ: {seq}")
            return True

        self.connection.send_command(f"PUZZLE_SEQ {seq}")

        # Tunggu Arduino selesai eksekusi (4.5 detik + buffer)
        # Arduino akan kirim PUZZLE_DONE saat selesai
        time.sleep(5.5)
        return True

    def _release_all_keys(self):
        """Force-release semua tombol virtual/fisik untuk mencegah input 'ghost'."""
        # 1. Always release all virtual keys to prevent stuck keys
        keys_to_release = ["left", "right", "up", "down"]
        interact = self.settings.get("interact_key", "space")
        jump = self.settings.get("jump_key", "alt")
        blink = self.settings.get("blink_key", "shift")

        for k in [interact, jump, blink]:
            if k and k not in keys_to_release:
                keys_to_release.append(k)

        for k in ["space", "shift", "ctrl", "alt"]:
            if k not in keys_to_release:
                keys_to_release.append(k)

        for key in keys_to_release:
            try:
                vkeys.key_up(key)
            except Exception:
                pass
        self.connection.log(
            f"[DEBUG-VIRTUAL] Force-release semua tombol virtual: {', '.join(keys_to_release)}"
        )

        # 2. Release physical servos if hardware mode is active
        if (
            self.settings.get("rune_input_mode", "software") == "hardware"
            and self.connection.connected
            and not self.connection.simulation_mode
        ):
            self.connection.log("[DEBUG-HARDWARE] Force-release semua servo fisik...")
            for i in range(len(self.profile.servos)):
                angle = self.profile.servos[i].up_angle
                self.connection.send_command(f"TEST_SERVO {i} {angle}")
            time.sleep(0.3)

    def _key_down(self, logical_key):
        """Menahan tombol secara fisik (servo) jika terhubung ke Arduino asli dan diaktifkan, atau virtual."""
        logical_lower = logical_key.lower()
        actual_key = logical_key
        if logical_lower == "blink":
            actual_key = self.settings.get("blink_key", "shift")
        elif logical_lower == "jump":
            actual_key = self.settings.get("jump_key", "alt")

        is_puzzle_action = logical_lower.startswith("puzzle_") or logical_lower in ["left", "right", "up", "down"]
        if (
            is_puzzle_action
            and self.settings.get("rune_input_mode", "software") == "hardware"
            and self.connection.connected
            and not self.connection.simulation_mode
        ):
            self._hardware_key_down(logical_key)
        else:
            self.connection.log(
                f"[DEBUG-VIRTUAL] Tahan tombol virtual '{actual_key}' ({logical_key.upper()})"
            )
            vkeys.key_down(actual_key)

    def _key_up(self, logical_key):
        """Melepas tombol secara fisik (servo) jika terhubung ke Arduino asli dan diaktifkan, atau virtual."""
        logical_lower = logical_key.lower()
        actual_key = logical_key
        if logical_lower == "blink":
            actual_key = self.settings.get("blink_key", "shift")
        elif logical_lower == "jump":
            actual_key = self.settings.get("jump_key", "alt")

        is_puzzle_action = logical_lower.startswith("puzzle_") or logical_lower in ["left", "right", "up", "down"]
        if (
            is_puzzle_action
            and self.settings.get("rune_input_mode", "software") == "hardware"
            and self.connection.connected
            and not self.connection.simulation_mode
        ):
            self._hardware_key_up(logical_key)
        else:
            self.connection.log(
                f"[DEBUG-VIRTUAL] Lepas tombol virtual '{actual_key}' ({logical_key.upper()})"
            )
            vkeys.key_up(actual_key)

    def start(self):
        """Starts background monitoring loop."""
        if self.running:
            return
        self.running = True
        self.capture.start()
        self.thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.thread.start()
        print("[Controller] Thread pemantau Auto Farm dimulai.")

    def stop(self):
        """Stops background loop."""
        self.running = False
        self.capture.stop()
        if self.thread:
            self.thread.join(timeout=1.0)
            self.thread = None
        print("[Controller] Thread pemantau Auto Farm dihentikan.")

    def play_alert(self, name):
        """Plays a warning sound in a loop."""
        try:
            self.alert_active = True

            # Maksimalkan volume Windows master
            try:
                import win32api

                for _ in range(50):
                    win32api.keybd_event(0xAF, 0)  # VK_VOLUME_UP
            except Exception as e:
                print(f"[Controller] Gagal memaksimalkan volume Windows: {e}")

            # Gunakan file .wav yang sudah diboost jika tersedia, fallback ke .mp3
            sound_path = resolve_path(f"assets/alerts/{name}.wav")
            if not os.path.exists(sound_path):
                sound_path = resolve_path(f"assets/alerts/{name}.mp3")

            if os.path.exists(sound_path):
                pygame.mixer.music.load(sound_path)
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(-1)
                print(f"[Controller] Sirene dibunyikan: {name} ({os.path.basename(sound_path)})")
            else:
                # Fallback to beep if file not found
                import winsound

                winsound.Beep(1000, 2000)
        except Exception as e:
            print(f"[Controller] Gagal memutar suara: {e}")

    def stop_alert(self):
        """TODO: add documentation"""
        try:
            pygame.mixer.music.stop()
            self.alert_active = False
        except Exception as e:
            print("Error occurred")
            pass

    def _check_buff_active(self):
        """Matches top-right quadrant of screen to see if Rune Buff is active."""
        frame = self.capture.frame
        if frame is None or frame.size == 0:
            return False

        h, w = frame.shape[:2]
        top_right = frame[: h // 3, w // 2 :]
        gray = (
            cv2.cvtColor(top_right, cv2.COLOR_BGR2GRAY) if len(top_right.shape) == 3 else top_right
        )

        scores = []
        for template in RUNE_BUFF_TEMPLATES:
            score = match_score(gray, template)
            scores.append(score)

        best_score = max(scores) if scores else 0.0
        self.connection.log(
            f"[RUNE] Verifikasi Buff - Skor Terbaik: {best_score:.3f} (Threshold: 0.90)"
        )
        return best_score >= 0.90

    def _scan_for_rune(self):
        """Checks if a rune is active on the minimap using color clustering."""
        minimap = self.capture.minimap
        if minimap is None or minimap.size == 0:
            return None

        filtered = filter_color(minimap, RUNE_RANGES)
        gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)

        # Cari piksel berwarna magenta/ungu
        pts = np.argwhere(gray > 0)

        # Jika jumlah piksel ungu cukup banyak (misal minimal 4 piksel), maka rune terdeteksi
        if len(pts) >= 4:
            # Hitung titik tengah (centroid) dari kluster piksel ungu
            mean_y, mean_x = np.mean(pts, axis=0)
            abs_x = int(round(mean_x))
            abs_y = int(round(mean_y))

            # Konversi ke koordinat relatif
            rel_x = abs_x / minimap.shape[1]
            rel_y = abs_y / self.capture.minimap_ratio / minimap.shape[0]

            # Log deteksi (dikomentari agar tidak spam)
            # print(f"[Controller] RUNE TERDETEKSI via deteksi warna! Piksel: {len(pts)}, Posisi: ({abs_x}, {abs_y})")
            return (rel_x, rel_y)

        return None

    def _monitor_loop(self):
        """Continually checks screen for runes, field bosses, and death."""
        while self.running:
            time.sleep(0.5)  # Poll checking twice per second

            if self.alert_active:
                continue

            if not self.capture.ready:
                continue

            frame = self.capture.frame
            if frame is None or frame.size == 0:
                continue

            # Load model lazily when needed and enabled
            if self.settings["enabled_rune"] and self.solver is None:
                try:
                    print("[Controller] Menginisialisasi model deteksi ViT Rune...")
                    api_key = self.settings.get("roboflow_api_key")
                    self.solver = RuneSolver(api_key=api_key)
                    print("[Controller] Model ViT siap.")
                except Exception as e:
                    print(f"[Controller] Gagal memuat solver Rune ViT: {e}")
                    self.settings["enabled_rune"] = False  # Disable feature automatically

            # Compute current screen scale relative to reference resolution 1366x768
            h, w = frame.shape[:2]
            scale = w / 1366.0

            # Dynamically resize templates if game resolution changed, or first run
            if self.last_scale != scale:
                self.last_scale = scale
                try:
                    # Resize elite warning template (reference is 433x75)
                    if abs(scale - 1.0) > 0.01:
                        new_w_elite = max(1, int(round(ELITE_TEMPLATE.shape[1] * scale)))
                        new_h_elite = max(1, int(round(ELITE_TEMPLATE.shape[0] * scale)))
                        self.scaled_elite = cv2.resize(
                            ELITE_TEMPLATE,
                            (new_w_elite, new_h_elite),
                            interpolation=cv2.INTER_LANCZOS4,
                        )

                        # Resize death window template (reference is 422x191)
                        new_w_death = max(1, int(round(DEATH_TEMPLATE.shape[1] * scale)))
                        new_h_death = max(1, int(round(DEATH_TEMPLATE.shape[0] * scale)))
                        self.scaled_death = cv2.resize(
                            DEATH_TEMPLATE,
                            (new_w_death, new_h_death),
                            interpolation=cv2.INTER_LANCZOS4,
                        )

                    else:
                        self.scaled_elite = ELITE_TEMPLATE
                        self.scaled_death = DEATH_TEMPLATE

                    # Resize and pre-scale Lie templates using both resolution scale and detection scales
                    self.pre_scaled_lie_templates = []
                    scale_factors = [0.80, 0.85, 0.90, 0.95, 1.0, 1.05, 1.10, 1.15, 1.20]
                    for filename, img_gray, img_bgr, threshold_gray, threshold_bgr in LIE_TEMPLATES:
                        scaled_list_gray = []
                        scaled_list_bgr = []
                        for s in scale_factors:
                            combined_scale = scale * s
                            new_w = max(1, int(round(img_gray.shape[1] * combined_scale)))
                            new_h = max(1, int(round(img_gray.shape[0] * combined_scale)))
                            
                            scaled_gray = cv2.resize(img_gray, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
                            scaled_bgr = cv2.resize(img_bgr, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
                            
                            scaled_list_gray.append((s, scaled_gray))
                            scaled_list_bgr.append((s, scaled_bgr))
                        self.pre_scaled_lie_templates.append((filename, scaled_list_gray, scaled_list_bgr, threshold_gray, threshold_bgr))

                    print(
                        f"[Controller] Templates scaled to resolution scale {scale:.3f}: Elite={self.scaled_elite.shape}, Death={self.scaled_death.shape}, LieTemplates={len(self.pre_scaled_lie_templates)}"
                    )
                except Exception as e:
                    print(f"[Controller] Gagal me-resize template: {e}")
                    self.scaled_elite = ELITE_TEMPLATE
                    self.scaled_death = DEATH_TEMPLATE

            # 0.5. Lie Detector Warning Detection (if enabled)
            if self.settings.get("enabled_lie_detector", False):
                now = time.time()
                # Run the CPU-heavy template matching only once every 3.0 seconds
                if now - self.last_lie_check_time >= 3.0:
                    self.last_lie_check_time = now
                    # Pastikan frame adalah 3-channel BGR (membuang channel alpha jika frame berupa BGRA dari mss)
                    if len(frame.shape) == 3 and frame.shape[2] == 4:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    lie_detected = False
                    best_scores = []

                    for idx, (filename, scaled_list_gray, scaled_list_bgr, threshold_gray, threshold_bgr) in enumerate(self.pre_scaled_lie_templates):
                        max_score_gray = 0.0
                        best_scale_idx = -1
                        best_loc = (0, 0)
                        
                        for s_idx, (s, scaled_tpl_gray) in enumerate(scaled_list_gray):
                            # Skip if template is larger than the search frame
                            if scaled_tpl_gray.shape[0] > gray_frame.shape[0] or scaled_tpl_gray.shape[1] > gray_frame.shape[1]:
                                continue

                            try:
                                res = cv2.matchTemplate(gray_frame, scaled_tpl_gray, cv2.TM_CCOEFF_NORMED)
                                _, max_val, _, max_loc = cv2.minMaxLoc(res)
                            except Exception:
                                continue
                                
                            if max_val > max_score_gray:
                                max_score_gray = max_val
                                best_scale_idx = s_idx
                                best_loc = max_loc

                        best_scores.append(f"Tpl{idx}: {max_score_gray:.3f}")
                        if max_score_gray >= threshold_gray:
                            # Stage 2: BGR Color Verification
                            x, y = best_loc
                            s, scaled_tpl_bgr = scaled_list_bgr[best_scale_idx]
                            h_tpl, w_tpl = scaled_tpl_bgr.shape[:2]
                            
                            crop_y_end = min(frame.shape[0], y + h_tpl)
                            crop_x_end = min(frame.shape[1], x + w_tpl)
                            crop_bgr = frame[y:crop_y_end, x:crop_x_end]
                            
                            score_bgr = 0.0
                            if crop_bgr.shape[0] == h_tpl and crop_bgr.shape[1] == w_tpl:
                                try:
                                    # Slicing ekstra untuk menjamin 3 channel BGR
                                    crop_bgr_3ch = crop_bgr[:, :, :3]
                                    res_bgr = cv2.matchTemplate(crop_bgr_3ch, scaled_tpl_bgr, cv2.TM_CCOEFF_NORMED)
                                    _, score_bgr, _, _ = cv2.minMaxLoc(res_bgr)
                                except Exception as e:
                                    print(f"[DEBUG-LIE] Gagal melakukan pencocokan Stage 2: {e}")
                                    
                            if score_bgr >= threshold_bgr:
                                print(
                                    f"[WARNING] Lie Detector terdeteksi! Template '{filename}' cocok. "
                                    f"Stage 1 Grayscale: {max_score_gray:.3f}, Stage 2 BGR: {score_bgr:.3f}."
                                )
                                lie_detected = True
                                break
                            else:
                                print(
                                    f"[DEBUG-LIE] False positive dicegah untuk template '{filename}'. "
                                    f"Stage 1 Grayscale ({max_score_gray:.3f}) >= Threshold ({threshold_gray}), "
                                    f"tetapi Stage 2 BGR Color ({score_bgr:.3f}) < {threshold_bgr}."
                                )

                    # Cetak skor kecocokan ke konsol setiap 6.0 detik untuk kalibrasi tanpa log spam
                    if not lie_detected and (now - getattr(self, "last_lie_log_time", 0) > 6.0):
                        self.last_lie_log_time = now
                        print(
                            f"[DEBUG-LIE] Skor kecocokan saat ini (Pre-Scaled): {', '.join(best_scores)}"
                        )

                    if lie_detected:
                        self.connection.send_command("STOP")
                        self.connection.log("[WARNING] Lie Detector terdeteksi! Menghentikan bot.")
                        self.play_alert("siren")
                        # Disable loop tracking to prevent endless alerts
                        self.settings["enabled_lie_detector"] = False
                        self.save_settings()
                        continue

            # 1. Field Boss Warning Detection (if enabled)
            if self.settings["enabled_boss"]:
                # The warning banner is always in the center region of the screen
                elite_frame = frame[h // 4 : 3 * h // 4, w // 4 : 3 * w // 4]
                elite_gray = cv2.cvtColor(elite_frame, cv2.COLOR_BGR2GRAY)

                # Check for Elite Boss warning sign with robust scaled template
                # Lower threshold to 0.75 for blending and translucency tolerance
                elite_matches = multi_match(elite_gray, self.scaled_elite, threshold=0.75)
                if elite_matches:
                    print("[WARNING] Elite/Field Boss terdeteksi di layar!")
                    self.connection.send_command("STOP")
                    self.connection.log("[WARNING] Elite Boss terdeteksi! Menghentikan bot.")
                    self.play_alert("siren")
                    # Disable loop tracking to prevent endless alerts until user interacts
                    self.settings["enabled_boss"] = False
                    self.save_settings()
                    continue

            # 2. Death Detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            death_matches = multi_match(gray_frame, self.scaled_death, threshold=0.65)
            if death_matches:
                print("[WARNING] Karakter mati terdeteksi!")
                self.connection.send_command("STOP")
                self.connection.log("[WARNING] Karakter Mati! Menghentikan bot.")
                self.play_alert("siren")
                time.sleep(5)
                continue

            # 3. Auto Clear Rune (if enabled and robot is actively running)
            # We fetch parent app state or verify via connection status if robot is running
            app = self.connection.status_callback
            # If robot is active, try to detect rune
            if self.settings["enabled_rune"] and not self.solving_rune and self.capture.calibrated:
                # Check if system status indicates robot is running (or step progress is active)
                # In mainApp connection status tracker, "Terhubung" or "Active: RUNNING" or similar is checked
                # Let's inspect serial connected status
                if self.connection.connected:
                    rune_pos = self._scan_for_rune()
                    if rune_pos:
                        print(f"[RUNE] Rune terdeteksi di koordinat minimap {rune_pos}!")
                        self.solving_rune = True

                        # Stop Arduino macro loop and neutralise servos
                        self.connection.send_command("STOP")
                        self.connection.log(
                            "[RUNE] Rune terdeteksi! Menghentikan sementara makro servo."
                        )

                        # Run solver thread to keep GUI responsive
                        threading.Thread(
                            target=self._solve_rune_process, args=(rune_pos,), daemon=True
                        ).start()

    def _solve_rune_process(self, target_pos):
        """Drives character to rune, triggers puzzle, and inputs arrow keystrokes using pynput."""
        try:
            # Pastikan semua tombol virtual dilepas sebelum memulai
            self._release_all_keys()
            time.sleep(1.0)  # Stand still

            # Solve loop (repeat until successful)
            solve_success = False
            attempt_count = 0

            while self.running and self.settings["enabled_rune"] and not solve_success:
                attempt_count += 1
                self.connection.log(
                    f"[RUNE] Memulai navigasi pendekatan rune (Percobaan #{attempt_count})"
                )

                # Step A: Force-release sebelum navigasi
                self._release_all_keys()

                # Coba deteksi ulang koordinat rune di minimap jika terlihat
                new_pos = self._scan_for_rune()
                if new_pos:
                    target_pos = new_pos
                    self.connection.log(
                        f"[RUNE] Koordinat rune terdeteksi ulang di minimap: {target_pos}"
                    )
                else:
                    # Rune tidak ditemukan di awal percobaan. Cek ulang setelah 0.5 detik untuk menghindari noise
                    time.sleep(0.5)
                    new_pos = self._scan_for_rune()
                    if new_pos:
                        target_pos = new_pos
                        self.connection.log(
                            f"[RUNE] Koordinat rune terdeteksi ulang di minimap (uji ulang): {target_pos}"
                        )
                    else:
                        self.connection.log(
                            "[RUNE] Rune tidak terdeteksi lagi di minimap. Membatalkan penyelesaian rune..."
                        )
                        break

                # Navigate to Rune coordinate
                self._focus_game_window()
                navigate_success = self._navigate_to(target_pos)
                if not navigate_success:
                    self._release_all_keys()
                    self.connection.log("[RUNE] Gagal mendekati rune. Mencoba lagi...")
                    time.sleep(2.0)
                    continue

                # Step B: Force-release sebelum interact
                self._release_all_keys()
                time.sleep(1.2)  # Jeda setelah karakter mencapai titik rune sebelum interact

                # Save full frame sebelum interact
                frame_before = self.capture.frame
                if frame_before is not None:
                    try:
                        debug_dir = Path.cwd() / "debug_rune_last"
                        debug_dir.mkdir(parents=True, exist_ok=True)
                        cv2.imwrite(
                            str(debug_dir / "debug_fullframe_before_interact.png"), frame_before
                        )
                        self.connection.log(
                            f"[DEBUG-RUNE] Full frame sebelum interact disimpan ke: {debug_dir}/debug_fullframe_before_interact.png"
                        )
                    except Exception as e:
                        print("Error occurred")
                        self.connection.log(
                            f"[DEBUG-RUNE] Gagal menyimpan full frame sebelum interact: {e}"
                        )

                # Open Rune UI Puzzle (Press Interact)
                self._focus_game_window()
                self.connection.log("[RUNE] Mengirim perintah Interact...")
                self._press_key("interact", down_time=0.2, up_time=0.35)

                # Jeda 0.8 detik agar panel terbuka sempurna sebelum ambil pola puzzle
                time.sleep(0.8)

                # Save full frame setelah interact
                frame_after = self.capture.frame
                if frame_after is not None:
                    try:
                        debug_dir = Path.cwd() / "debug_rune_last"
                        debug_dir.mkdir(parents=True, exist_ok=True)
                        cv2.imwrite(
                            str(debug_dir / "debug_fullframe_after_interact.png"), frame_after
                        )
                        self.connection.log(
                            f"[DEBUG-RUNE] Full frame setelah interact disimpan ke: {debug_dir}/debug_fullframe_after_interact.png"
                        )
                    except Exception as e:
                        print("Error occurred")
                        self.connection.log(
                            f"[DEBUG-RUNE] Gagal menyimpan full frame setelah interact: {e}"
                        )

                # Ambil frame saat ini dan potong area panel puzzle untuk debug
                frame = self.capture.frame
                if frame is not None:
                    try:
                        h, w = frame.shape[:2]
                        target_ratio = 2.587
                        width = w // 2
                        height = int(round(width / target_ratio))
                        y_center = int(round(0.328 * h))
                        y0 = max(0, y_center - height // 2)
                        y1 = min(h, y0 + height)
                        x0 = w // 4
                        x1 = x0 + width
                        cropped = frame[y0:y1, x0:x1]
                        if len(cropped.shape) >= 3 and cropped.shape[2] == 4:
                            cropped = cv2.cvtColor(cropped, cv2.COLOR_BGRA2BGR)

                        # Simpan gambar band/panel utuh ke folder debug agar bisa dilihat
                        debug_dir = Path.cwd() / "debug_rune_last"
                        debug_dir.mkdir(parents=True, exist_ok=True)
                        cv2.imwrite(str(debug_dir / "debug_interact_panel.png"), cropped)
                        self.connection.log(
                            f"[DEBUG-RUNE] Gambar panel disimpan ke: {debug_dir}/debug_interact_panel.png"
                        )
                    except Exception as e:
                        print("Error occurred")
                        self.connection.log(f"[DEBUG-RUNE] Gagal menyimpan panel debug: {e}")

                # Voting Konsensus - poll 1 gambar sebanyak 7 kali (atau 1 kali untuk HybridSolver) untuk keandalan
                polled_solutions = []
                best_score = 0.0
                solution = None

                # Brief sleep to stabilize frame capture
                time.sleep(0.3)

                is_hybrid = (
                    self.solver is not None and getattr(self.solver, "_hybrid", None) is not None
                )
                poll_count = 1 if is_hybrid else 7
                self.connection.log(
                    f"[RUNE] Memulai deteksi panel (1 gambar dianalisa {poll_count}x)..."
                )
                static_frame = self.capture.frame
                if static_frame is None or static_frame.size == 0:
                    self.connection.log("[RUNE] Gagal menangkap gambar layar! Mencoba lagi...")
                    time.sleep(1.0)
                    continue

                for poll_idx in range(poll_count):
                    frame = static_frame

                    h, w = frame.shape[:2]
                    target_ratio = 2.587
                    width = w // 2
                    height = int(round(width / target_ratio))
                    y_center = int(round(0.328 * h))
                    y0 = max(0, y_center - height // 2)
                    y1 = min(h, y0 + height)
                    x0 = w // 4
                    x1 = x0 + width
                    cropped = frame[y0:y1, x0:x1]
                    if len(cropped.shape) >= 3 and cropped.shape[2] == 4:
                        cropped = cv2.cvtColor(cropped, cv2.COLOR_BGRA2BGR)

                    if cropped is None or cropped.size == 0:
                        continue

                    sol = self.solver.solve(
                        cropped, log_func=self.connection.log, save_debug=(poll_idx == 0)
                    )
                    score = self.solver.last_score
                    self.connection.log(
                        f"[RUNE] Analisa #{poll_idx+1}: skor={score:.2f}, solusi={sol}"
                    )

                    if sol and len(sol) == 4:
                        # Threshold 0.5 agar ONNX solver (yang skornya berbeda) tetap lolos
                        # HybridSolver mengembalikan score=15.0 secara default
                        if score >= 0.5:
                            polled_solutions.append(tuple(sol))
                            if score > best_score:
                                best_score = score

                self.connection.log(
                    f"[RUNE] Polling selesai: {len(polled_solutions)} frame valid dari {poll_count}"
                )

                if polled_solutions:
                    from collections import Counter

                    counter = Counter(polled_solutions)
                    most_common_sol, count = counter.most_common(1)[0]
                    total_valid = len(polled_solutions)
                    self.connection.log(
                        f"[RUNE] Voting - Pola: {most_common_sol} ({count}/{total_valid} cocok)"
                    )

                    # Konsensus adaptif:
                    # - Jika >=5 valid: butuh count>=3
                    # - Jika 3-4 valid: butuh count>=2
                    # - Jika 1-2 valid: terima jika count>=1 (panel mungkin baru muncul)
                    min_count = 3 if total_valid >= 5 else (2 if total_valid >= 3 else 1)
                    if count >= min_count:
                        solution = list(most_common_sol)
                        self.connection.log(
                            f"[RUNE] Solusi diterima (konsensus {count}/{total_valid}, min={min_count})"
                        )
                    else:
                        self.connection.log(
                            f"[RUNE] Konsensus tidak tercapai ({count}/{total_valid} < {min_count})"
                        )

                if not solution or len(solution) != 4:
                    self.connection.log(
                        f"[RUNE] Gagal dapat solusi valid (polled={len(polled_solutions)}). Geser karakter..."
                    )
                    self._release_all_keys()

                    # Smart Shift: Geser horisontal selama 1.5 detik
                    px, py = self.capture.player_pos
                    shift_direction = "right" if px < 0.15 else "left"
                    self.connection.log(
                        f"[RUNE] Karakter berada di px={px:.3f}. Menggeser karakter ke arah {shift_direction.upper()}..."
                    )
                    self._key_down(shift_direction)
                    time.sleep(1.5)
                    self._key_up(shift_direction)
                    self._release_all_keys()

                    self.connection.log(
                        "[RUNE] Jeda cooldown 2.0 detik sebelum mendeteksi dan mencoba navigasi ulang..."
                    )
                    time.sleep(2.0)
                    continue

                # Step D: Enter arrow keystrokes using virtual keys or hardware servos
                self._focus_game_window()
                self.connection.log(
                    f"[RUNE] Kode Panah Terdeteksi: {', '.join(solution)} (Skor Konsensus: {best_score:.2f})"
                )
                time.sleep(0.2)  # Jeda sebelum eksekusi

                if (
                    self.settings.get("rune_input_mode", "software") == "hardware"
                    and self.connection.connected
                    and not self.connection.simulation_mode
                ):
                    self.connection.log(
                        "[RUNE] Menggunakan physical servos Arduino untuk memasukkan kode..."
                    )
                    self._send_puzzle_sequence(solution)
                else:
                    self.connection.log(
                        "[RUNE] Menggunakan input virtual PC untuk memasukkan kode..."
                    )
                    for step_num, arrow in enumerate(solution, 1):
                        self.connection.log(
                            f"[RUNE] Input puzzle langkah {step_num}/4: {arrow.upper()}"
                        )
                        self._press_key(f"puzzle_{arrow}", down_time=0.1, up_time=0.15)

                self.connection.log("[RUNE] Kode selesai dimasukkan. Menunggu validasi buff...")
                time.sleep(2.0)  # Wait for server confirmation and buff icon rendering

                # Check if Rune Buff is active
                if self._check_buff_active():
                    self.connection.log(
                        "[SUCCESS] Rune berhasil diselesaikan! Mereset posisi karakter ke pojok kiri..."
                    )
                    # Hold LEFT key/servo for 6 seconds to walk to the far left wall
                    self._key_down("left")
                    time.sleep(6.0)
                    self._key_up("left")
                    self._release_all_keys()  # Pastikan semua virtual key benar-benar bersih

                    time.sleep(0.5)  # Wait to settle
                    self.connection.log(
                        "[RUNE] Posisi ter-reset. Mengaktifkan kembali makro servo."
                    )
                    self.connection.send_command("START")
                    solve_success = True
                else:
                    self.connection.log(
                        "[RUNE] Buff tidak terdeteksi setelah kode dimasukkan. Melakukan pergeseran karakter (smart shift)..."
                    )
                    self._release_all_keys()

                    # Smart Shift: Geser horisontal selama 1.5 detik
                    px, py = self.capture.player_pos
                    shift_direction = "right" if px < 0.15 else "left"
                    self.connection.log(
                        f"[RUNE] Karakter berada di px={px:.3f}. Menggeser karakter ke arah {shift_direction.upper()}..."
                    )
                    self._key_down(shift_direction)
                    time.sleep(1.5)
                    self._key_up(shift_direction)
                    self._release_all_keys()

                    self.connection.log(
                        "[RUNE] Jeda cooldown 2.0 detik sebelum mendeteksi dan mencoba navigasi ulang..."
                    )
                    time.sleep(2.0)
                    continue

        except Exception as e:
            print(f"[Controller] Kesalahan proses penyelesaian rune: {e}")
        finally:
            self._release_all_keys()
            self.solving_rune = False
            if not solve_success:
                self.connection.log("[RUNE] Mengaktifkan kembali makro servo (Penyelesaian Rune dibatalkan/selesai).")
                self.connection.send_command("START")
            import gc

            gc.collect()
            try:
                import torch

                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
            except Exception as e:
                print("Error occurred")
                pass

    def _navigate_to(self, target):
        """Simple feedback control loop to navigate character horizontally and vertially."""
        rx, ry = target
        stuck_counter = 0
        last_pos = (0, 0)
        start_time = time.time()

        # Lacak keberadaan Rune di minimap selama berjalan
        rune_not_found_time = 0.0
        last_rune_check = time.time()

        while self.running and self.settings["enabled_rune"]:
            px, py = self.capture.player_pos
            dx = rx - px
            dy = ry - py

            # Cek keberadaan Rune di minimap secara berkala (setiap 0.5 detik)
            now = time.time()
            if now - last_rune_check >= 0.5:
                last_rune_check = now
                new_rune_pos = self._scan_for_rune()
                if new_rune_pos:
                    rx, ry = new_rune_pos  # Update target koordinat secara dinamis
                    rune_not_found_time = 0.0
                else:
                    dist_to_target = distance((px, py), (rx, ry))
                    # Hanya batalkan jika jarak masih jauh (agar tidak membatalkan saat koordinat bertumpukan)
                    if dist_to_target > 0.06:
                        if rune_not_found_time == 0.0:
                            rune_not_found_time = now
                        elif now - rune_not_found_time >= 3.0:
                            self.connection.log(
                                "[NAVIGATION] Rune hilang dari minimap saat didekati (kemungkinan salah deteksi). Membatalkan navigasi..."
                            )
                            self._key_up("left")
                            self._key_up("right")
                            self._key_up("up")
                            self._key_up("down")
                            return False
                    else:
                        rune_not_found_time = 0.0

            # Check if we have arrived (tight tolerance)
            if abs(dx) <= 0.02 and abs(dy) <= 0.025:
                self.connection.log(
                    f"[NAVIGATION] Tiba di tujuan! Player: ({px:.3f}, {py:.3f}), Target: ({rx:.3f}, {ry:.3f}), Selisih: (dx={dx:.3f}, dy={dy:.3f})"
                )
                # Release keys and stand still
                self._key_up("left")
                self._key_up("right")
                self._key_up("up")
                self._key_up("down")
                time.sleep(0.5)
                return True

            # If navigation times out (e.g. stuck for > 45 seconds), fail and retry
            if time.time() - start_time > 45:
                self._key_up("left")
                self._key_up("right")
                self._key_up("up")
                self._key_up("down")
                return False

            # Check if player is stuck (coordinates not changing)
            if distance((px, py), last_pos) < 0.001:
                stuck_counter += 1
            else:
                stuck_counter = 0
            last_pos = (px, py)

            # If stuck, try jump to get unstuck
            if stuck_counter > 15:
                self._press_key("jump", down_time=0.1)
                stuck_counter = 0
                time.sleep(0.3)
                continue

            # Horizontal movement
            if dx < -0.018:
                self._key_up("right")
                self._key_down("left")
            elif dx > 0.018:
                self._key_up("left")
                self._key_down("right")
            else:
                self._key_up("left")
                self._key_up("right")

            # Vertical movement (climbing/descending) - ONLY when horizontally close to the target!
            if abs(dx) <= 0.03:
                if dy < -0.025:
                    # Player is below rune - choose jump mode
                    jump_mode = self.settings.get("vertical_jump_mode", "double_jump")

                    if jump_mode == "double_jump":
                        # Release horizontal movement temporarily to jump straight up
                        self._key_up("left")
                        self._key_up("right")
                        time.sleep(0.05)

                        # Perform upward double jump (press UP and jump 2x)
                        self._key_down("up")
                        time.sleep(0.05)

                        # First jump
                        self._key_down("jump")
                        time.sleep(0.08)
                        self._key_up("jump")
                        time.sleep(0.15)  # Wait brief moment in air

                        # Second jump
                        self._key_down("jump")
                        time.sleep(0.08)
                        self._key_up("jump")
                        time.sleep(0.5)  # Wait to land

                        self._key_up("up")

                    elif jump_mode == "blink":
                        # Release horizontal keys
                        self._key_up("left")
                        self._key_up("right")
                        time.sleep(0.05)

                        if (
                            self.profile.random_skip_enabled
                            and random.random() < 0.5
                        ):
                            self.connection.log(
                                "[DEBUG-SKIP] Random skip blink di-lewatkan pada loop ini."
                            )
                            # Ensure we release the up key after a short pause
                            self._key_up("up")
                            time.sleep(0.4)
                            # Skip the rest of the blink actions
                            continue

                        # Hold UP and press blink key
                        self._key_down("up")
                        time.sleep(0.05)
                        self._press_key("blink", down_time=0.1, up_time=0.1)
                        time.sleep(0.4)  # Wait to land/teleport

                        self._key_up("up")

                    else:  # "climb" mode
                        # Old behavior: climb up ladder or rope
                        self._key_down("up")
                        # Occasionally press jump if stuck below
                        if stuck_counter > 5:
                            self._press_key("jump", down_time=0.1)
                        time.sleep(0.3)
                        self._key_up("up")
                elif dy > 0.025:
                    # Player is above rune - down-jump
                    # Release horizontal movement first to prevent normal horizontal jump
                    self._key_up("left")
                    self._key_up("right")
                    time.sleep(0.05)

                    self._key_down("down")
                    time.sleep(0.05)
                    self._press_key("jump", down_time=0.1)
                    time.sleep(0.2)
                    self._key_up("down")
                    time.sleep(0.1)  # Wait to land
                else:
                    self._key_up("up")
                    self._key_up("down")
            else:
                # Horizontally far - ensure UP and DOWN keys are released to prevent unintended climbing/descending
                self._key_up("up")
                self._key_up("down")

            time.sleep(0.05)
