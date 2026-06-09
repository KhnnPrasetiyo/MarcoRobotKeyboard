"""Virtual key emulation module for Auto Farm using low-level Win32 SendInput (with pynput fallback)."""

import sys
import time

from lazy_imports import lazy_import

# Win32 virtual key codes (VK_CODES)
VK_CODES = {
    "left": 0x25,
    "up": 0x26,
    "right": 0x27,
    "down": 0x28,
    "space": 0x20,
    "shift": 0x10,
    "ctrl": 0x11,
    "alt": 0x12,
    "enter": 0x0D,
    "esc": 0x1B,
}

# Add letter and number virtual key codes
for c in "abcdefghijklmnopqrstuvwxyz":
    VK_CODES[c] = ord(c.upper())
for c in "0123456789":
    VK_CODES[c] = ord(c)

# Set of keys that are extended (like arrow keys) which require KEYEVENTF_EXTENDEDKEY
EXTENDED_KEYS = {"left", "right", "up", "down"}

# Pynput fallback lazy initialization variables
_pynput_initialized = False
keyboard = None
PYNPUT_MAP = {}

def _ensure_pynput():
    global _pynput_initialized, keyboard, PYNPUT_MAP
    if _pynput_initialized:
        return
    try:
        from pynput.keyboard import Controller, Key

        keyboard = Controller()
        PYNPUT_MAP = {
            "left": Key.left,
            "right": Key.right,
            "up": Key.up,
            "down": Key.down,
            "space": Key.space,
            "shift": Key.shift,
            "ctrl": Key.ctrl,
            "alt": Key.alt,
            "enter": Key.enter,
            "esc": Key.esc,
        }
        for c in "abcdefghijklmnopqrstuvwxyz0123456789":
            PYNPUT_MAP[c] = c
    except Exception as e:
        print("Error occurred")
        keyboard = None
        PYNPUT_MAP = {}
        print(f"[vkeys] Peringatan: Gagal memuat pynput: {e}")
    _pynput_initialized = True

# Win32 SendInput structures and imports
if sys.platform == "win32":
    ctypes = lazy_import("ctypes")
    from ctypes import wintypes

    # SendInput constants
    INPUT_KEYBOARD = 1
    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP = 0x0002
    KEYEVENTF_SCANCODE = 0x0008
    MAPVK_VK_TO_VSC = 0

    class KeyboardInput(ctypes.Structure):
        """TODO: add documentation"""

        _fields_ = [
            ("wVk", wintypes.WORD),
            ("wScan", wintypes.WORD),
            ("dwFlags", wintypes.DWORD),
            ("time", wintypes.DWORD),
            ("dwExtraInfo", ctypes.c_void_p),
        ]

    class MouseInput(ctypes.Structure):
        """TODO: add documentation"""

        _fields_ = [
            ("dx", wintypes.LONG),
            ("dy", wintypes.LONG),
            ("mouseData", wintypes.DWORD),
            ("dwFlags", wintypes.DWORD),
            ("time", wintypes.DWORD),
            ("dwExtraInfo", ctypes.c_void_p),
        ]

    class HardwareInput(ctypes.Structure):
        """TODO: add documentation"""

        _fields_ = [
            ("uMsg", wintypes.DWORD),
            ("wParamL", wintypes.WORD),
            ("wParamH", wintypes.WORD),
        ]

    class InputUnion(ctypes.Union):
        """TODO: add documentation"""

        _fields_ = [("ki", KeyboardInput), ("mi", MouseInput), ("hi", HardwareInput)]

    class Input(ctypes.Structure):
        """TODO: add documentation"""

        _fields_ = [("type", wintypes.DWORD), ("u", InputUnion)]

    def _win32_send_input(vk_code, is_up=False, is_extended=False):
        """Kirim penekanan tombol menggunakan Windows SendInput API (DirectInput scan code)."""
        try:
            user32 = ctypes.windll.user32

            # Konversi Virtual Key ke Hardware Scan Code
            scan_code = user32.MapVirtualKeyW(vk_code, MAPVK_VK_TO_VSC)
            if not scan_code:
                # Fallback standard scan codes jika MapVirtualKey gagal
                fallback_sc = {0x25: 0x4B, 0x26: 0x48, 0x27: 0x4D, 0x28: 0x50, 0x20: 0x39}
                scan_code = fallback_sc.get(vk_code, 0)

            flags = KEYEVENTF_SCANCODE
            if is_up:
                flags |= KEYEVENTF_KEYUP
            if is_extended:
                flags |= KEYEVENTF_EXTENDEDKEY

            ki = KeyboardInput(
                wVk=vk_code, wScan=scan_code, dwFlags=flags, time=0, dwExtraInfo=None
            )
            inp = Input(type=INPUT_KEYBOARD, u=InputUnion(ki=ki))

            # Panggil SendInput
            result = user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(inp))
            return result > 0
        except Exception as e:
            print(f"[vkeys] Gagal memanggil SendInput: {e}")
            return False

else:

    def _win32_send_input(vk_code, is_up=False, is_extended=False):
        """TODO: add documentation"""
        return False


def key_down(key):
    """Tahan tombol secara virtual menggunakan low-level SendInput (fallback ke pynput)."""
    if not key:
        return
    key = key.lower()

    # 1. Coba Win32 SendInput (terbaik untuk game DirectX/DirectInput)
    if sys.platform == "win32" and key in VK_CODES:
        vk = VK_CODES[key]
        is_ext = key in EXTENDED_KEYS
        if _win32_send_input(vk, is_up=False, is_extended=is_ext):
            return

    # 2. Fallback ke pynput
    _ensure_pynput()
    if keyboard and key in PYNPUT_MAP:
        try:
            keyboard.press(PYNPUT_MAP[key])
        except Exception as e:
            print(f"[vkeys] Gagal menekan tombol {key} via pynput: {e}")
    else:
        print(f"[vkeys] Tombol tidak valid atau pynput tidak terinisialisasi: {key}")


def key_up(key):
    """Lepas tombol secara virtual menggunakan low-level SendInput dan pynput."""
    if not key:
        return
    key = key.lower()

    # 1. Coba Win32 SendInput (terbaik untuk game DirectX/DirectInput)
    if sys.platform == "win32" and key in VK_CODES:
        vk = VK_CODES[key]
        is_ext = key in EXTENDED_KEYS
        _win32_send_input(vk, is_up=True, is_extended=is_ext)

    # 2. Juga panggil pynput release untuk memastikan tidak ada kunci stuck
    _ensure_pynput()
    if keyboard and key in PYNPUT_MAP:
        try:
            keyboard.release(PYNPUT_MAP[key])
        except Exception as e:
            print(f"[vkeys] Gagal melepas tombol {key} via pynput: {e}")
    else:
        print(f"[vkeys] Tombol tidak valid atau pynput tidak terinisialisasi: {key}")


def press(key, n=1, down_time=0.05, up_time=0.1):
    """Tekan tombol virtual N kali, dengan waktu tekan (down_time) dan jeda lepas (up_time) yang diacak sedikit (humanized)."""
    if not key:
        return
    import random

    for _ in range(n):
        # Tambahkan variasi acak kecil (-15ms s/d +20ms) agar durasi tekan terkesan manusiawi
        actual_down = down_time + random.uniform(-0.015, 0.020)
        if actual_down < 0.01:
            actual_down = 0.01

        key_down(key)
        time.sleep(actual_down)
        key_up(key)

        # Tambahkan variasi acak kecil (-20ms s/d +30ms) pada jeda rilis
        actual_up = up_time + random.uniform(-0.020, 0.030)
        if actual_up < 0.01:
            actual_up = 0.01
        time.sleep(actual_up)
