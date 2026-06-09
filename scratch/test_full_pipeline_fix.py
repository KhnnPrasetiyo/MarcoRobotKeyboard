"""Test: proportional resize + color-based arrow detection + ViT."""

import sys

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, r"C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite")

from app.auto_farm.rune_solver.crop import DIRECTIONS
from app.auto_farm.rune_solver.vit_solver import ViTSolver

_MIN_ARROW_SPACING = 55
ARROW_HALF_W = 47
ARROW_HALF_H = 47


def proportional_resize_center_crop(image: Image.Image, target_w=528, target_h=304):
    """Resize proportionally to target height, then center-crop to target width."""
    w, h = image.size
    new_h = target_h
    new_w = int(round(w * new_h / h))
    image = image.resize((new_w, new_h), Image.LANCZOS)
    if new_w > target_w:
        left = (new_w - target_w) // 2
        image = image.crop((left, 0, left + target_w, new_h))
    elif new_w < target_w:
        padded = Image.new("RGB", (target_w, target_h), (0, 0, 0))
        left = (target_w - new_w) // 2
        padded.paste(image, (left, 0))
        image = padded
    return image


def detect_arrows_by_color(img_bgr):
    """Detect arrow centers using HSV color segmentation."""
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    lower = np.array([15, 80, 120])
    upper = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        if 100 <= area <= 1800:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h if h > 0 else 0
            if 0.45 <= aspect <= 2.2:
                cx = x + w // 2
                cy = y + h // 2
                candidates.append((cx, cy, area))

    candidates = sorted(candidates, key=lambda pt: pt[0])

    # Merge close duplicates
    filtered = []
    for pt in candidates:
        if not filtered:
            filtered.append(pt)
        else:
            last = filtered[-1]
            if abs(pt[0] - last[0]) <= 25:
                if pt[2] > last[2]:
                    filtered[-1] = pt
            else:
                filtered.append(pt)

    return filtered


def find_best_4_arrows(candidates, img_h, img_w):
    """Find the best subset of 4 arrow candidates that form a horizontal line."""
    import itertools

    best_group = None
    best_y_diff = 9999

    for subset in itertools.combinations(candidates, 4):
        ys = [pt[1] for pt in subset]
        y_diff = max(ys) - min(ys)

        xs = [pt[0] for pt in subset]
        spacings = [xs[i + 1] - xs[i] for i in range(3)]

        spacings_ok = all(sp >= _MIN_ARROW_SPACING for sp in spacings)
        min_sp = min(spacings) if spacings else 0
        ratio_ok = (max(spacings) / min_sp <= 2.0) if min_sp > 0 else False

        # All x within a reasonable panel range
        x_span = max(xs) - min(xs)
        x_span_ok = 150 <= x_span <= 400

        if y_diff < 25 and spacings_ok and ratio_ok and x_span_ok:
            if y_diff < best_y_diff:
                best_y_diff = y_diff
                best_group = list(subset)

    return best_group


def main():
    """TODO: add documentation"""
    cropped_bgr = cv2.imread("debug_rune_last/debug_interact_panel.png")
    if cropped_bgr is None:
        print("Image not found")
        return

    print(f"Crop shape: {cropped_bgr.shape}")

    cropped_rgb = cv2.cvtColor(cropped_bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(cropped_rgb)

    # Step 1: Proportional resize + center-crop
    resized = proportional_resize_center_crop(pil_img, 528, 304)
    resized.save("scratch/method3_resized.png")
    resized_bgr = cv2.cvtColor(np.array(resized), cv2.COLOR_RGB2BGR)

    # Step 2: Detect arrows by color
    candidates = detect_arrows_by_color(resized_bgr)
    print(f"Color candidates: {len(candidates)}")
    for idx, (cx, cy, area) in enumerate(candidates):
        print(f"  Cand {idx}: cx={cx}, cy={cy}, area={area}")

    # Step 3: Find best group of 4 arrows
    h_img, w_img = resized_bgr.shape[:2]
    best_group = find_best_4_arrows(candidates, h_img, w_img)

    if best_group:
        print(f"\nBest group of 4 arrows:")
        cy_avg = int(round(np.mean([pt[1] for pt in best_group])))
        boxes = []
        for idx, (cx, cy, area) in enumerate(best_group):
            print(f"  Arrow {idx}: cx={cx}, cy={cy}")
            boxes.append(
                (cx - ARROW_HALF_W, cy_avg - ARROW_HALF_H, cx + ARROW_HALF_W, cy_avg + ARROW_HALF_H)
            )
    else:
        print("\nNo 4-arrow group found. Falling back to geometric...")
        # Geometric fallback using template matching
        from app.auto_farm.rune_solver.panel_detect import arrow_boxes_for

        boxes, score = arrow_boxes_for(resized)
        print(f"Fallback boxes: {boxes}, score: {score:.4f}")

    # Clamp boxes
    boxes = [(max(0, l), max(0, t), min(528, r), min(304, b)) for l, t, r, b in boxes]

    print(f"\nFinal boxes: {boxes}")

    # Step 4: Run ViT
    solver = ViTSolver()
    offsets = [(0, 0), (-3, 0), (3, 0), (0, -3), (0, 3)]
    tiles = []
    for b in boxes:
        for dx, dy in offsets:
            c = solver._crop_with_offset(resized, b, dx, dy)
            tiles.append(solver._preprocess(c))
    batch = np.stack(tiles).astype(np.float32)
    input_name = solver.session.get_inputs()[0].name
    logits = solver.session.run(None, {input_name: batch})[0]
    logits = logits - np.max(logits, axis=-1, keepdims=True)
    probs = np.exp(logits) / np.sum(np.exp(logits), axis=-1, keepdims=True)
    probs = probs.reshape(len(boxes), len(offsets), -1).mean(axis=1)
    preds = probs.argmax(axis=-1).tolist()

    for idx in range(len(preds)):
        prob_str = ", ".join([f"{DIRECTIONS[i]}: {probs[idx][i]:.1%}" for i in range(4)])
        print(f"  Slot {idx+1}: {DIRECTIONS[preds[idx]]} ({prob_str})")
    print(f"\n  FINAL RESULT: {[DIRECTIONS[p] for p in preds]}")


if __name__ == "__main__":
    main()
