"""TODO: module documentation"""

import cv2
import numpy as np
from PIL import Image

from app.auto_farm.rune_solver.crop import DIRECTIONS
from app.auto_farm.rune_solver.vit_solver import ViTSolver


def main():
    """TODO: add documentation"""
    img_path = "c:/Users/Admin/Downloads/AutoFarmMaple/NanoKeyboardControllerLite/debug_rune_last/resized_band.png"
    img = Image.open(img_path)
    img_cv = cv2.imread(img_path)

    # 1. Load templates
    ref_path = "c:/Users/Admin/Downloads/AutoFarmMaple/NanoKeyboardControllerLite/assets/rune_panel_template.png"
    ref_img = cv2.imread(ref_path)
    tpl_l = ref_img[120:200, 25:75]
    tpl_r = ref_img[120:200, 425:475]

    # 2. Match left endcap with center constraint
    res_l = cv2.matchTemplate(img_cv, tpl_l, cv2.TM_CCOEFF_NORMED) * 19.79484
    best_l_score = -999
    best_l_coord = None

    # Wide search region
    for y in range(70, min(180, res_l.shape[0])):
        for x in range(0, min(250, res_l.shape[1])):
            score = res_l[y, x]
            est_center = x + 190
            dist = abs(est_center - 264)
            constrained = score - 0.05 * dist
            if constrained > best_l_score:
                best_l_score = constrained
                best_l_coord = (x, y)

    px, py = best_l_coord
    L = px + 25
    print(f"Left Endcap: px={px}, py={py}, score={res_l[py, px]:.4f}, L={L}")

    # 3. Match right endcap
    res_r = cv2.matchTemplate(img_cv, tpl_r, cv2.TM_CCOEFF_NORMED) * 19.79484
    best_r_score = -999
    best_r_coord = None

    y_min = max(0, py - 30)
    y_max = min(res_r.shape[0], py + 30)
    x_min = min(res_r.shape[1], px + 150)
    x_max = min(res_r.shape[1] - 1, 478)

    for y in range(y_min, y_max):
        for x in range(x_min, x_max + 1):
            score = res_r[y, x]
            if score > best_r_score:
                best_r_score = score
                best_r_coord = (x, y)

    rx, ry = best_r_coord
    R = rx + 25
    print(f"Right Endcap: rx={rx}, ry={ry}, score={res_r[ry, rx]:.4f}, R={R}")

    # 4. Color segment arrows
    hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
    lower_arrow = np.array([10, 50, 100])
    upper_arrow = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cy = int(round((py + ry) / 2)) + 40

    color_centers = []
    for c in contours:
        area = cv2.contourArea(c)
        if 80 <= area <= 2000:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h
            if 0.5 <= aspect <= 2.0:
                cx = x + w // 2
                col_cy = y + h // 2
                # Filter by spatial constraints relative to detected panel
                if abs(col_cy - cy) < 25 and (L - 15) <= cx <= (R + 15):
                    color_centers.append((cx, col_cy))

    # Sort by X
    color_centers = sorted(color_centers, key=lambda pt: pt[0])

    # Filter close duplicates (e.g. split contours)
    filtered_centers = []
    for pt in color_centers:
        if not filtered_centers:
            filtered_centers.append(pt)
        else:
            last_pt = filtered_centers[-1]
            if abs(pt[0] - last_pt[0]) > 20:  # at least 20px apart
                filtered_centers.append(pt)

    print(f"Color-detected arrow centers: {filtered_centers}")

    # 5. Formulate final boxes
    boxes = []
    half_w = 45
    half_h = 45

    if len(filtered_centers) == 4:
        print("Using precise color-detected centers!")
        for cx, col_cy in filtered_centers:
            boxes.append((cx - half_w, cy - half_h, cx + half_w, cy + half_h))
    else:
        print(
            f"Color detection found {len(filtered_centers)} centers (expected 4). Falling back to interpolation!"
        )
        W_panel = R - L
        rel_positions = [0.1625, 0.3875, 0.6125, 0.8375]
        for p in rel_positions:
            cx = int(round(L + p * W_panel))
            boxes.append((cx - half_w, cy - half_h, cx + half_w, cy + half_h))

    # 6. Run ViT solver
    solver = ViTSolver()
    tiles = []
    offsets = [(0, 0), (-3, 0), (3, 0), (0, -3), (0, 3)]
    for b in boxes:
        for dx, dy in offsets:
            cropped = solver._crop_with_offset(img, b, dx, dy)
            tiles.append(solver._preprocess(cropped))

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
