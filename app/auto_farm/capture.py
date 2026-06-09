"""Screen Capture module for Auto Farm."""

from lazy_imports import lazy_import

ctypes = lazy_import("ctypes")
import threading
import time
from collections import deque

import cv2
import mss
import numpy as np
import pygetwindow as gw

win32gui = lazy_import("win32gui")

from app.auto_farm.utils import load_image, multi_match

# Win32 DPI awareness configuration
try:
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
except Exception as e:
    print("Error occurred")
    pass

# Load templates
try:
    MM_TL_TEMPLATE = load_image("assets/minimap_tl_template.png", cv2.IMREAD_GRAYSCALE)
    MM_BR_TEMPLATE = load_image("assets/minimap_br_template.png", cv2.IMREAD_GRAYSCALE)
    PLAYER_TEMPLATE = load_image("assets/player_template.png", cv2.IMREAD_GRAYSCALE)
    PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape
except Exception as e:
    print(f"[Capture] Gagal memuat template gambar: {e}")


class Capture:
    """Class to capture the game screen and track player coordinates."""

    def __init__(self):
        """TODO: add documentation"""
        self.frame = None
        self.minimap = None
        self.player_pos = (0.0, 0.0)
        self.minimap_ratio = 1.0
        self.window = {"left": 0, "top": 0, "width": 1366, "height": 768}
        self.window_obj = None
        self.ready = False
        self.calibrated = False
        self.running = False
        self.thread = None
        self._lock = threading.Lock()
        self._frame_times = deque(maxlen=30)

    @property
    def fps(self):
        """TODO: add documentation"""
        if len(self._frame_times) < 2:
            return 0.0
        span = self._frame_times[-1] - self._frame_times[0]
        if span <= 0:
            return 0.0
        return (len(self._frame_times) - 1) / span

    def start(self):
        """Starts the capture background thread."""
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._main, daemon=True)
        self.thread.start()
        print("[Capture] Thread penangkap video dimulai.")

    def stop(self):
        """Stops the capture thread."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1.0)
            self.thread = None
        print("[Capture] Thread penangkap video dihentikan.")

    def _find_game_window(self):
        """Finds PyGetWindow object for Maplestory."""
        for title in gw.getAllTitles():
            title_lower = title.lower()
            if any(
                term in title_lower
                for term in [
                    "remote desktop connection",
                    "远程桌面协议",
                    "maplestory",
                    "moonlight",
                    "photo viewer",
                    "photos",
                    "lie_capcha",
                ]
            ):
                # Pastikan bukan jendela browser, discord, text editor, dll.
                excludes = [
                    "chrome",
                    "firefox",
                    "edge",
                    "brave",
                    "opera",
                    "safari",
                    "explorer",
                    "discord",
                    "vscode",
                    "visual studio",
                    "notepad",
                    "sublime",
                ]
                if any(e in title_lower for e in excludes):
                    continue
                windows = gw.getWindowsWithTitle(title)
                if windows:
                    return windows[0]
        return None

    def _update_window_rect(self, window_obj):
        """Updates self.window to cover only the client area of the window, excluding borders/title bar."""
        hwnd = window_obj._hWnd
        rect = win32gui.GetClientRect(hwnd)
        w = rect[2] - rect[0]
        h = rect[3] - rect[1]
        x, y = win32gui.ClientToScreen(hwnd, (0, 0))

        # Detect if coordinates changed significantly and log for debugging
        prev = (
            self.window["left"],
            self.window["top"],
            self.window["width"],
            self.window["height"],
        )
        new = (x, y, w, h)
        if prev != new:
            print(f"[Capture] Window rect updated: left={x}, top={y}, width={w}, height={h}")

        self.window["left"] = x
        self.window["top"] = y
        self.window["width"] = w
        self.window["height"] = h

    def _main(self):
        """TODO: add documentation"""
        # Configure thread DPI awareness context to Per-Monitor Aware V2 or fallback to Per-Monitor Aware
        try:
            # -4 is DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
            ctypes.windll.user32.SetThreadDpiAwarenessContext(ctypes.c_void_p(-4))
            print("[Capture] Thread DPI awareness set to Per-Monitor V2.")
        except Exception as e:
            print("Error occurred")
            try:
                # -3 is DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE
                ctypes.windll.user32.SetThreadDpiAwarenessContext(ctypes.c_void_p(-3))
                print("[Capture] Thread DPI awareness set to Per-Monitor (Fallback).")
            except Exception as e:
                print("[Capture] Gagal mengatur thread DPI awareness.")

        window_obj = None
        with mss.mss() as sct:
            while self.running:
                if window_obj is None:
                    window_obj = self._find_game_window()
                    if window_obj is None:
                        self.ready = False
                        self.frame = None
                        time.sleep(1.0)
                        continue
                    self.window_obj = window_obj
                    print(f"[Capture] Menemukan jendela game: '{window_obj.title}'")

                try:
                    if window_obj.isMinimized:
                        self.calibrated = False
                        self.ready = False
                        self.frame = None
                        time.sleep(1.0)
                        continue
                    self._update_window_rect(window_obj)
                except Exception as e:
                    print("Error occurred")
                    # Window closed or handle invalid
                    window_obj = None
                    self.window_obj = None
                    self.calibrated = False
                    self.ready = False
                    self.frame = None
                    time.sleep(1.0)
                    continue

                # First screenshot to calibrate minimap size
                try:
                    raw_shot = sct.grab(self.window)
                    self.frame = np.array(raw_shot)
                    self.ready = True
                except Exception as e:
                    print("Error occurred")
                    time.sleep(1.0)
                    continue

                if self.frame is None or self.frame.size == 0:
                    time.sleep(0.5)
                    continue

                # Calibrate minimap bounding box
                try:
                    gray_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                    h, w = gray_frame.shape[:2]

                    # Batasi wilayah pencarian TL hanya di area kiri atas layar game (maksimal 100px lebar, 150px tinggi)
                    # Ini mencegah pencocokan salah (false match) pada chat window/UI di bagian bawah/tengah layar
                    tl_search_h = min(h, 150)
                    tl_search_w = min(w, 100)
                    tl_search_region = gray_frame[0:tl_search_h, 0:tl_search_w]

                    result_tl = cv2.matchTemplate(
                        tl_search_region, MM_TL_TEMPLATE, cv2.TM_CCOEFF_NORMED
                    )
                    _, max_val_tl, _, tl = cv2.minMaxLoc(result_tl)
                    # Batasi wilayah pencarian BR di sebelah kanan bawah titik TL
                    # Membatasi rentang pencarian BR lebih ketat (lebar 50-250, tinggi 15-100)
                    # Ini mencegah pencocokan salah pada UI lain di luar area minimap yang sebenarnya
                    y_min = tl[1] + 15
                    y_max = min(h, tl[1] + 100)
                    x_min = tl[0] + 50
                    x_max = min(w, tl[0] + 250)

                    if y_min >= y_max or x_min >= x_max:
                        self.calibrated = False
                        time.sleep(1.0)
                        continue

                    search_region = gray_frame[y_min:y_max, x_min:x_max]
                    if (
                        search_region.shape[0] < MM_BR_TEMPLATE.shape[0]
                        or search_region.shape[1] < MM_BR_TEMPLATE.shape[1]
                    ):
                        self.calibrated = False
                        time.sleep(1.0)
                        continue

                    result_br = cv2.matchTemplate(
                        search_region, MM_BR_TEMPLATE, cv2.TM_CCOEFF_NORMED
                    )
                    _, max_val_br, _, br_rel = cv2.minMaxLoc(result_br)

                    br_tl = (x_min + br_rel[0], y_min + br_rel[1])
                    br = (br_tl[0] + MM_BR_TEMPLATE.shape[1], br_tl[1] + MM_BR_TEMPLATE.shape[0])

                    # Hanya kalibrasi jika kecocokan tinggi (TL minimal 80% mirip, BR minimal 50% mirip)
                    if max_val_tl < 0.80 or max_val_br < 0.50:
                        self.calibrated = False
                        time.sleep(1.0)
                        continue

                    mm_tl = (tl[0] + 2, tl[1] + 2)
                    mm_br = (
                        max(mm_tl[0] + PT_WIDTH, br[0] - 8),
                        max(mm_tl[1] + PT_HEIGHT, br[1] - 9),
                    )

                    # Sanity check on size
                    width = abs(mm_tl[0] - mm_br[0])
                    height = abs(mm_tl[1] - mm_br[1])
                    print(f"[Capture] Validasi ukuran: width = {width}, height = {height}")

                    # Perketat rentang ukuran minimap agar tidak mencocokkan area luar game secara tidak sengaja
                    if 100 <= width <= 250 and 30 <= height <= 100:
                        self.minimap_ratio = width / height
                        self.calibrated = True
                        self.ready = True
                        print(f"[Capture] Kalibrasi minimap sukses. Batas: {mm_tl} hingga {mm_br}")
                    else:
                        self.calibrated = False
                        time.sleep(1.0)
                        continue
                except Exception as e:
                    print(f"[Capture] Gagal mengkalibrasi minimap: {e}")
                    self.calibrated = False
                    time.sleep(1.0)
                    continue

                # Main loop once calibrated
                while self.running and self.calibrated:
                    try:
                        # Update window coordinates in case the user moves the window
                        if window_obj.isMinimized:
                            self.calibrated = False
                            self.ready = False
                            self.frame = None
                            time.sleep(1.0)
                            continue
                        self._update_window_rect(window_obj)

                        # Sanity check on window size to prevent huge memory allocations
                        if (
                            self.window["width"] < 100
                            or self.window["height"] < 100
                            or self.window["width"] > 4096
                            or self.window["height"] > 2160
                        ):
                            self.calibrated = False
                            self.ready = False
                            self.frame = None
                            time.sleep(1.0)
                            continue

                        raw_shot = sct.grab(self.window)
                        current_frame = np.array(raw_shot)
                        if current_frame is None or current_frame.size == 0:
                            continue

                        # Remove alpha channel if present
                        if current_frame.shape[2] == 4:
                            current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGRA2BGR)

                        with self._lock:
                            self.frame = current_frame
                            self._frame_times.append(time.time())

                            # Crop minimap. Use copy() to avoid keeping the full screen frame reference in memory
                            minimap = self.frame[mm_tl[1] : mm_br[1], mm_tl[0] : mm_br[0]].copy()
                            self.minimap = minimap

                            # Match player position using robust minMaxLoc (always selects absolute best match)
                            gray_minimap = (
                                cv2.cvtColor(minimap, cv2.COLOR_BGR2GRAY)
                                if len(minimap.shape) == 3
                                else minimap
                            )
                            result_player = cv2.matchTemplate(
                                gray_minimap, PLAYER_TEMPLATE, cv2.TM_CCOEFF_NORMED
                            )
                            _, max_val, _, max_loc = cv2.minMaxLoc(result_player)

                            if max_val >= 0.75:
                                raw_px = int(round(max_loc[0] + PLAYER_TEMPLATE.shape[1] / 2))
                                raw_py = int(round(max_loc[1] + PLAYER_TEMPLATE.shape[0] / 2))
                                rel_x = raw_px / minimap.shape[1]
                                rel_y = raw_py / self.minimap_ratio / minimap.shape[0]
                                self.player_pos = (rel_x, rel_y)
                    except Exception as e:
                        print(f"[Capture] Kesalahan di loop utama capture: {e}")
                        self.calibrated = False  # Force re-calibration
                        self.ready = False
                        self.frame = None
                        import gc

                        gc.collect()
                    time.sleep(0.1)
