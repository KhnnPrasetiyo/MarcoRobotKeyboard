"""TODO: module documentation"""

import cv2
import numpy as np
from PIL import Image

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

    # 2. Match left endcap in wide search region (center-constrained)
    res_l = cv2.matchTemplate(img_cv, tpl_l, cv2.TM_CCOEFF_NORMED) * 19.79484

    best_l_score = -999
    best_l_coord = None

    # Search x in [0, 250], y in [70, 180]
    for y in range(70, min(180, res_l.shape[0])):
        for x in range(0, min(250, res_l.shape[1])):
            score = res_l[y, x]
            # Center constraint
            est_center = x + 190
            dist = abs(est_center - 264)
            constrained = score - 0.05 * dist
            if constrained > best_l_score:
                best_l_score = constrained
                best_l_coord = (x, y)

    px, py = best_l_coord
    print(f"Detected Left Endcap: px={px}, py={py}, score={res_l[py, px]:.4f}")

    # 3. Match right endcap in wide search region
    res_r = cv2.matchTemplate(img_cv, tpl_r, cv2.TM_CCOEFF_NORMED) * 19.79484
    best_r_score = -999
    best_r_coord = None

    # Search x in [px + 150, 478], y in [py - 20, py + 20]
    y_min = max(0, py - 20)
    y_max = min(res_r.shape[0], py + 20)
    x_min = min(res_r.shape[1], px + 150)
    x_max = min(res_r.shape[1] - 1, 478)

    for y in range(y_min, y_max):
        for x in range(x_min, x_max + 1):
            score = res_r[y, x]
            if score > best_r_score:
                best_r_score = score
                best_r_coord = (x, y)

    rx, ry = best_r_coord
    print(
        f"Detected Right Endcap: rx={rx}, ry={ry}, score={rx_score if (rx_score:=res_r[ry, rx]) else 0.0:.4f}"
    )

    # 4. Interpolate centers
    L = px + 25
    R = rx + 25
    W_panel = R - L
    cy = int(round((py + ry) / 2)) + 40  # curve vertical center is top-left + 40

    rel_positions = [0.1625, 0.3875, 0.6125, 0.8375]
    arrow_centers_x = [int(round(L + p * W_panel)) for p in rel_positions]
    print(f"Interpolated Arrow Centers X: {arrow_centers_x}, Y: {cy}")

    # 5. Crop and solve
    half_w = 45
    half_h = 45
    boxes = []
    for cx in arrow_centers_x:
        boxes.append((cx - half_w, cy - half_h, cx + half_w, cy + half_h))

    # We will temporarily mock the arrow_boxes_for behavior or modify vit_solver to run solve
    solver = ViTSolver()

    # Let's override arrow_boxes_for in solver or run the crop ourselves
    # We can just run the solve on these custom boxes using the solver's internal session
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

    from app.auto_farm.rune_solver.crop import DIRECTIONS

    directions = [DIRECTIONS[p] for p in preds]
    print(f"Predicted Directions: {directions}")


if __name__ == "__main__":
    main()
