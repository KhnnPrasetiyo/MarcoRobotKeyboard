"""Test: proportional resize + center-crop to 528x304 (the fix)."""

import sys

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, r"C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite")

from app.auto_farm.rune_solver.crop import DIRECTIONS
from app.auto_farm.rune_solver.panel_detect import arrow_boxes_for
from app.auto_farm.rune_solver.vit_solver import ViTSolver


def proportional_resize_center_crop(image: Image.Image, target_w=528, target_h=304) -> Image.Image:
    """Resize proportionally to target height, then center-crop to target width."""
    w, h = image.size
    # Resize proportionally to target height
    new_h = target_h
    new_w = int(round(w * new_h / h))
    image = image.resize((new_w, new_h), Image.LANCZOS)

    # Center-crop to target width
    if new_w > target_w:
        left = (new_w - target_w) // 2
        image = image.crop((left, 0, left + target_w, new_h))
    elif new_w < target_w:
        # Pad with black on both sides
        padded = Image.new("RGB", (target_w, target_h), (0, 0, 0))
        left = (target_w - new_w) // 2
        padded.paste(image, (left, 0))
        image = padded
    return image


def main():
    """TODO: add documentation"""
    # Load the cropped panel (640x247) from the controller
    cropped_bgr = cv2.imread("debug_rune_last/debug_interact_panel.png")
    if cropped_bgr is None:
        print("debug_interact_panel.png not found")
        return

    print(f"Original crop shape: {cropped_bgr.shape}")

    cropped_rgb = cv2.cvtColor(cropped_bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(cropped_rgb)

    # === METHOD 1: Old distorted resize (current code) ===
    print("\n=== METHOD 1: Old distorted resize (528x304) ===")
    old_resized = pil_img.resize((528, 304), Image.LANCZOS)
    old_resized.save("scratch/old_distorted_resize.png")

    boxes_old, score_old = arrow_boxes_for(old_resized)
    print(f"Score: {score_old:.4f}")
    print(f"Boxes: {boxes_old}")

    solver = ViTSolver()

    offsets = [(0, 0), (-3, 0), (3, 0), (0, -3), (0, 3)]
    tiles_old = []
    for b in boxes_old:
        for dx, dy in offsets:
            c = solver._crop_with_offset(old_resized, b, dx, dy)
            tiles_old.append(solver._preprocess(c))
    batch_old = np.stack(tiles_old).astype(np.float32)
    input_name = solver.session.get_inputs()[0].name
    logits_old = solver.session.run(None, {input_name: batch_old})[0]
    logits_old = logits_old - np.max(logits_old, axis=-1, keepdims=True)
    probs_old = np.exp(logits_old) / np.sum(np.exp(logits_old), axis=-1, keepdims=True)
    probs_old = probs_old.reshape(len(boxes_old), len(offsets), -1).mean(axis=1)
    preds_old = probs_old.argmax(axis=-1).tolist()

    for idx in range(len(preds_old)):
        prob_str = ", ".join([f"{DIRECTIONS[i]}: {probs_old[idx][i]:.1%}" for i in range(4)])
        print(f"  Slot {idx+1}: {DIRECTIONS[preds_old[idx]]} ({prob_str})")
    print(f"  Result: {[DIRECTIONS[p] for p in preds_old]}")

    # === METHOD 2: New proportional resize + center-crop ===
    print("\n=== METHOD 2: Proportional resize + center-crop (528x304) ===")
    new_resized = proportional_resize_center_crop(pil_img, 528, 304)
    new_resized.save("scratch/new_proportional_resize.png")

    boxes_new, score_new = arrow_boxes_for(new_resized)
    print(f"Score: {score_new:.4f}")
    print(f"Boxes: {boxes_new}")

    tiles_new = []
    for b in boxes_new:
        for dx, dy in offsets:
            c = solver._crop_with_offset(new_resized, b, dx, dy)
            tiles_new.append(solver._preprocess(c))
    batch_new = np.stack(tiles_new).astype(np.float32)
    logits_new = solver.session.run(None, {input_name: batch_new})[0]
    logits_new = logits_new - np.max(logits_new, axis=-1, keepdims=True)
    probs_new = np.exp(logits_new) / np.sum(np.exp(logits_new), axis=-1, keepdims=True)
    probs_new = probs_new.reshape(len(boxes_new), len(offsets), -1).mean(axis=1)
    preds_new = probs_new.argmax(axis=-1).tolist()

    for idx in range(len(preds_new)):
        prob_str = ", ".join([f"{DIRECTIONS[i]}: {probs_new[idx][i]:.1%}" for i in range(4)])
        print(f"  Slot {idx+1}: {DIRECTIONS[preds_new[idx]]} ({prob_str})")
    print(f"  Result: {[DIRECTIONS[p] for p in preds_new]}")


if __name__ == "__main__":
    main()
