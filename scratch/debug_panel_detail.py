"""TODO: module documentation"""

import sys

import cv2
import numpy as np
from PIL import Image

# Add workspace directory to python search path
sys.path.insert(0, r"C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite")

from app.auto_farm.rune_solver.panel_detect import (detect_panel_origin,
                                                    detect_right_endcap)


def main():
    """TODO: add documentation"""
    img = cv2.imread("debug_rune_last/resized_band.png")
    ref_img = cv2.imread("assets/rune_panel_template.png")

    _TPL_BOX = (25, 120, 55, 200)
    tpl_l = ref_img[_TPL_BOX[1] : _TPL_BOX[3], _TPL_BOX[0] : _TPL_BOX[2]]
    tpl_r = ref_img[120:200, 435:465]

    (px, py), max_score = detect_panel_origin(img, tpl_l)
    print(f"Left match: px={px}, py={py}, score={max_score:.4f}")

    if max_score < 3.0:
        L = 79
        cy = 150
    else:
        L = px + 15
        cy = py + 25

    print(f"Calculated L={L}, cy={cy}")

    (rx, ry), r_score = detect_right_endcap(img, tpl_r, px, py)
    print(f"Right match: rx={rx}, ry={ry}, score={r_score:.4f}")

    if max_score < 3.0:
        R = L + 370
    else:
        R = rx + 45 if r_score >= 3.0 else L + 370

    print(f"Calculated R={R}")

    # Let's run the color detection code
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_arrow = np.array([15, 80, 120])
    upper_arrow = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    color_candidates = []
    x_min_allowed = L + 30
    x_max_allowed = R - 10

    for c in contours:
        area = cv2.contourArea(c)
        if 100 <= area <= 1800:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h if h > 0 else 0
            if 0.45 <= aspect <= 2.2:
                cx = x + w // 2
                cy_col = y + h // 2
                if abs(cy_col - cy) < 30 and x_min_allowed <= cx <= x_max_allowed:
                    color_candidates.append((cx, cy_col, area, (x, y, w, h)))

    color_candidates = sorted(color_candidates, key=lambda pt: pt[0])
    print(f"Color candidates: {len(color_candidates)}")
    for idx, cand in enumerate(color_candidates):
        print(f"  Cand {idx}: cx={cand[0]}, cy={cand[1]}, area={cand[2]}, bbox={cand[3]}")

    filtered_centers = []
    for pt in color_candidates:
        if not filtered_centers:
            filtered_centers.append(pt)
        else:
            last_pt = filtered_centers[-1]
            if abs(pt[0] - last_pt[0]) <= 25:
                if pt[2] > last_pt[2]:
                    filtered_centers[-1] = pt
            else:
                filtered_centers.append(pt)

    print(f"Filtered centers: {len(filtered_centers)}")
    for idx, cand in enumerate(filtered_centers):
        print(f"  Center {idx}: cx={cand[0]}, cy={cand[1]}")

    use_color = False
    if len(filtered_centers) == 4:
        spacings_ok = all(
            filtered_centers[i + 1][0] - filtered_centers[i][0] >= 55 for i in range(3)
        )
        bounds_ok = all(x_min_allowed <= c[0] <= x_max_allowed for c in filtered_centers)
        use_color = spacings_ok and bounds_ok
        print(f"spacings_ok={spacings_ok}, bounds_ok={bounds_ok}")

    print(f"use_color={use_color}")


if __name__ == "__main__":
    main()
