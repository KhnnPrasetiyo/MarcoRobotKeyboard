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
    cropped = cv2.imread("debug_rune_last/debug_interact_panel.png")
    if cropped is None:
        print("debug_interact_panel.png not found")
        return

    # Resize proportionally to target height 304
    h_orig, w_orig = cropped.shape[:2]
    scale = 304.0 / h_orig
    w_new = int(round(w_orig * scale))
    h_new = 304

    img = cv2.resize(cropped, (w_new, h_new), interpolation=cv2.INTER_LANCZOS4)
    print(f"Resized shape: {img.shape} (scale={scale:.4f})")

    # Load templates
    ref_img = cv2.imread("assets/rune_panel_template.png")
    _TPL_BOX = (25, 120, 55, 200)
    tpl_l = ref_img[_TPL_BOX[1] : _TPL_BOX[3], _TPL_BOX[0] : _TPL_BOX[2]]
    tpl_r = ref_img[120:200, 435:465]

    # Match left endcap
    (px, py), max_score = detect_panel_origin(img, tpl_l)
    print(f"Left match: px={px}, py={py}, score={max_score:.4f}")

    L = px + 15
    cy = py + 25
    print(f"L={L}, cy={cy}")

    # Match right endcap
    (rx, ry), r_score = detect_right_endcap(img, tpl_r, px, py)
    print(f"Right match: rx={rx}, ry={ry}, score={r_score:.4f}")

    R = rx + 45 if r_score >= 3.0 else L + 370
    print(f"R={R}")

    # Run color detection
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
                    color_candidates.append((cx, cy_col, area))

    color_candidates = sorted(color_candidates, key=lambda pt: pt[0])
    print(f"Color candidates: {len(color_candidates)}")
    for idx, cand in enumerate(color_candidates):
        print(f"  Cand {idx}: cx={cand[0]}, cy={cand[1]}, area={cand[2]}")

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

    use_color = False
    if len(filtered_centers) == 4:
        spacings_ok = all(
            filtered_centers[i + 1][0] - filtered_centers[i][0] >= 55 for i in range(3)
        )
        bounds_ok = all(x_min_allowed <= c[0] <= x_max_allowed for c in filtered_centers)
        use_color = spacings_ok and bounds_ok
        print(f"spacings_ok={spacings_ok}, bounds_ok={bounds_ok}")

    print(f"use_color={use_color}")

    # Final boxes
    ARROW_HALF_W = 47
    ARROW_HALF_H = 47
    boxes = []
    if use_color:
        for cx, cy_col, _ in filtered_centers:
            boxes.append(
                (cx - ARROW_HALF_W, cy - ARROW_HALF_H, cx + ARROW_HALF_W, cy + ARROW_HALF_H)
            )
    else:
        for idx in range(4):
            cx = L + 50 + idx * 90
            boxes.append(
                (cx - ARROW_HALF_W, cy - ARROW_HALF_H, cx + ARROW_HALF_W, cy + ARROW_HALF_H)
            )

    # Run ViT solver
    from app.auto_farm.rune_solver.crop import DIRECTIONS
    from app.auto_farm.rune_solver.vit_solver import ViTSolver

    solver = ViTSolver()
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    tiles = []
    offsets = [(0, 0), (-3, 0), (3, 0), (0, -3), (0, 3)]
    for b in boxes:
        for dx, dy in offsets:
            cropped_tile = solver._crop_with_offset(pil_img, b, dx, dy)
            tiles.append(solver._preprocess(cropped_tile))

    batch = np.stack(tiles).astype(np.float32)
    input_name = solver.session.get_inputs()[0].name
    logits = solver.session.run(None, {input_name: batch})[0]

    logits_stable = logits - np.max(logits, axis=-1, keepdims=True)
    exp_logits = np.exp(logits_stable)
    probs = exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)

    probs = probs.reshape(len(boxes), len(offsets), -1)
    mean_probs = probs.mean(axis=1)
    preds = mean_probs.argmax(axis=-1).tolist()

    directions = [DIRECTIONS[p] for p in preds]
    print(f"Final Solution: {directions}")


if __name__ == "__main__":
    main()
