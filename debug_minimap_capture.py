"""
Debug script: Capture minimap dan player position secara live
Jalankan saat MapleStory aktif untuk melihat apakah minimap terkalibrasi dengan benar
"""

import os
import sys

sys.path.insert(0, os.getcwd())

from lazy_imports import lazy_import

# Langsung test capture dengan mss dan window detection
ctypes = lazy_import("ctypes")
import time
from pathlib import Path

import cv2
import mss
import numpy as np
import pygetwindow as gw

win32gui = lazy_import("win32gui")

# Set DPI awareness
try:
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    try:
        ctypes.windll.user32.SetThreadDpiAwarenessContext(ctypes.c_void_p(-4))
        print("[OK] DPI awareness: Per-Monitor V2")
    except:
        print("[OK] DPI awareness: Per-Process")
except:
    print("[WARN] Gagal set DPI awareness")


def find_game_window():
    """TODO: add documentation"""
    for title in gw.getAllTitles():
        title_lower = title.lower()
        if any(
            term in title_lower
            for term in ["remote desktop connection", "maplestory", "moonlight", "远程桌面协议"]
        ):
            windows = gw.getWindowsWithTitle(title)
            if windows:
                return windows[0]
    return None


def get_client_rect(window_obj):
    """TODO: add documentation"""
    hwnd = window_obj._hWnd
    rect = win32gui.GetClientRect(hwnd)
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    x, y = win32gui.ClientToScreen(hwnd, (0, 0))
    return {"left": x, "top": y, "width": w, "height": h}


print("\n[SCAN] Mencari window game...")
win = find_game_window()
if win is None:
    print("[ERROR] Window game tidak ditemukan! Pastikan MapleStory/Moonlight berjalan.")
    print("Window yang tersedia:")
    for t in gw.getAllTitles():
        if t.strip():
            print(f"  - '{t}'")
    sys.exit(1)

print(f"[OK] Window ditemukan: '{win.title}'")

# Get client rect
client = get_client_rect(win)
print(
    f"[INFO] Client area: left={client['left']}, top={client['top']}, width={client['width']}, height={client['height']}"
)

# Capture screenshot
with mss.mss() as sct:
    shot = sct.grab(client)
    frame = np.array(shot)
    if frame.shape[2] == 4:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    print(f"[INFO] Frame captured: {frame.shape}")

    # Save full frame
    out_dir = Path("debug_rune_last")
    out_dir.mkdir(exist_ok=True)
    cv2.imwrite(str(out_dir / "debug_fullframe.png"), frame)
    print(f"[SAVED] Full frame -> debug_rune_last/debug_fullframe.png")

    # Crop area pencarian TL minimap (100x150 px kiri atas)
    h, w = frame.shape[:2]
    tl_region = frame[0 : min(h, 150), 0 : min(w, 100)]
    cv2.imwrite(str(out_dir / "debug_tl_search_region.png"), tl_region)
    print(f"[SAVED] TL search region -> debug_rune_last/debug_tl_search_region.png")

    # Load template dan coba match
    from app.auto_farm.utils import load_image, multi_match

    MM_TL_TEMPLATE = load_image("assets/minimap_tl_template.png", cv2.IMREAD_GRAYSCALE)
    MM_BR_TEMPLATE = load_image("assets/minimap_br_template.png", cv2.IMREAD_GRAYSCALE)
    PLAYER_TEMPLATE = load_image("assets/player_template.png", cv2.IMREAD_GRAYSCALE)

    print(f"[INFO] TL template shape: {MM_TL_TEMPLATE.shape}")
    print(f"[INFO] BR template shape: {MM_BR_TEMPLATE.shape}")
    print(f"[INFO] Player template shape: {PLAYER_TEMPLATE.shape}")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    tl_search_h = min(h, 150)
    tl_search_w = min(w, 100)
    tl_region_gray = gray[0:tl_search_h, 0:tl_search_w]

    result_tl = cv2.matchTemplate(tl_region_gray, MM_TL_TEMPLATE, cv2.TM_CCOEFF_NORMED)
    _, max_val_tl, _, tl = cv2.minMaxLoc(result_tl)
    print(f"\n[MATCH TL] Score: {max_val_tl:.3f}, pos: {tl}")

    if max_val_tl >= 0.80:
        y_min = tl[1] + 15
        y_max = min(h, tl[1] + 100)
        x_min = tl[0] + 50
        x_max = min(w, tl[0] + 250)

        search_region = gray[y_min:y_max, x_min:x_max]
        result_br = cv2.matchTemplate(search_region, MM_BR_TEMPLATE, cv2.TM_CCOEFF_NORMED)
        _, max_val_br, _, br_rel = cv2.minMaxLoc(result_br)

        br_tl = (x_min + br_rel[0], y_min + br_rel[1])
        br = (br_tl[0] + MM_BR_TEMPLATE.shape[1], br_tl[1] + MM_BR_TEMPLATE.shape[0])

        print(f"[MATCH BR] Score: {max_val_br:.3f}, br_abs: {br}")

        PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape
        mm_tl = (tl[0] + 2, tl[1] + 2)
        mm_br = (max(mm_tl[0] + PT_WIDTH, br[0] - 8), max(mm_tl[1] + PT_HEIGHT, br[1] - 9))

        width = abs(mm_tl[0] - mm_br[0])
        height = abs(mm_tl[1] - mm_br[1])
        print(f"[MINIMAP] TL: {mm_tl}, BR: {mm_br}, size: {width}x{height}")

        if 100 <= width <= 250 and 30 <= height <= 100:
            print(f"[OK] Minimap kalibrasi SUKSES!")

            # Crop minimap
            minimap = frame[mm_tl[1] : mm_br[1], mm_tl[0] : mm_br[0]]
            cv2.imwrite(str(out_dir / "debug_minimap.png"), minimap)
            print(f"[SAVED] Minimap -> debug_rune_last/debug_minimap.png")

            # Match player
            gray_mm = (
                cv2.cvtColor(minimap, cv2.COLOR_BGR2GRAY) if len(minimap.shape) == 3 else minimap
            )
            result_player = cv2.matchTemplate(gray_mm, PLAYER_TEMPLATE, cv2.TM_CCOEFF_NORMED)
            _, max_val_p, _, max_loc_p = cv2.minMaxLoc(result_player)
            print(f"[PLAYER] Match score: {max_val_p:.3f}, loc: {max_loc_p}")

            if max_val_p >= 0.75:
                raw_px = int(round(max_loc_p[0] + PLAYER_TEMPLATE.shape[1] / 2))
                raw_py = int(round(max_loc_p[1] + PLAYER_TEMPLATE.shape[0] / 2))
                minimap_ratio = width / height
                rel_x = raw_px / minimap.shape[1]
                rel_y = raw_py / minimap_ratio / minimap.shape[0]
                print(f"[PLAYER] Posisi relatif: ({rel_x:.3f}, {rel_y:.3f})")
            else:
                print(f"[WARN] Player tidak terdeteksi (score {max_val_p:.3f} < 0.75)")
        else:
            print(f"[ERROR] Ukuran minimap tidak valid: {width}x{height}")
            print(f"  Expected: 100-250 wide, 30-100 high")
    else:
        print(f"[ERROR] TL minimap tidak terdeteksi! Score {max_val_tl:.3f} < 0.80")
        print(f"  Kemungkinan minimap tidak terlihat atau UI berubah")

print("\n[DONE] Cek file di folder debug_rune_last/")
