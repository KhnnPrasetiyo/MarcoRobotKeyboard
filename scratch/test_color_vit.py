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

    # Precise centers from color detection
    centers = [(144, 165), (194, 165), (281, 165), (365, 165)]

    half_w = 45
    half_h = 45
    boxes = []
    for cx, cy in centers:
        boxes.append((cx - half_w, cy - half_h, cx + half_w, cy + half_h))

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
    print("=== FINAL PREDICTIONS ===")
    for idx, d in enumerate(directions):
        print(
            f"Slot {idx+1}: {d} (probs: up={mean_probs[idx][0]:.1%}, down={mean_probs[idx][1]:.1%}, left={mean_probs[idx][2]:.1%}, right={mean_probs[idx][3]:.1%})"
        )
    print(f"Result: {directions}")


if __name__ == "__main__":
    main()
