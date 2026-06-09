"""TODO: module documentation"""

import sys

import cv2
import numpy as np
from PIL import Image

# Add workspace directory to python search path
sys.path.insert(0, r"C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite")

from app.auto_farm.rune_solver.crop import DIRECTIONS
from app.auto_farm.rune_solver.vit_solver import ViTSolver


def main():
    """TODO: add documentation"""
    # Load user's cropped panel (640x247)
    cropped = cv2.imread("debug_rune_last/debug_interact_panel.png")
    if cropped is None:
        print("debug_interact_panel.png not found")
        return

    print(f"Cropped shape: {cropped.shape}")

    # 1. Convert to HSV
    hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
    lower_arrow = np.array([10, 50, 80])  # Slightly relaxed HSV to capture all arrows
    upper_arrow = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        if 50 <= area <= 4000:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h if h > 0 else 0
            if 0.4 <= aspect <= 2.5:
                cx = x + w // 2
                cy = y + h // 2
                candidates.append((cx, cy, area, (x, y, w, h)))

    # Sort candidates by X
    candidates = sorted(candidates, key=lambda pt: pt[0])
    print(f"Initial color candidates: {len(candidates)}")

    # Initialize ViTSolver
    solver = ViTSolver()
    pil_cropped = Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))

    valid_arrows = []

    # Size of crops for ViT input (in cropped image space)
    # The arrow is about 40-50 pixels in 640x247 space
    half_size = 35

    for idx, (cx, cy, area, bbox) in enumerate(candidates):
        # Crop region around (cx, cy)
        l = max(0, cx - half_size)
        t = max(0, cy - half_size)
        r = min(cropped.shape[1], cx + half_size)
        b = min(cropped.shape[0], cy + half_size)

        crop_pil = pil_cropped.crop((l, t, r, b))

        # Run ViT model prediction
        arr = solver._preprocess(crop_pil)
        batch = np.expand_dims(arr, axis=0)

        input_name = solver.session.get_inputs()[0].name
        logits = solver.session.run(None, {input_name: batch})[0][0]

        # Softmax
        logits_stable = logits - np.max(logits)
        probs = np.exp(logits_stable) / np.sum(np.exp(logits_stable))

        max_prob = np.max(probs)
        pred_dir = DIRECTIONS[np.argmax(probs)]

        print(f"Cand {idx} at ({cx}, {cy}): ViT Pred={pred_dir} ({max_prob:.1%})")

        # Filter by confidence threshold
        if max_prob >= 0.85:
            valid_arrows.append((cx, cy, pred_dir, max_prob))

    # Sort valid arrows by X coordinate
    valid_arrows = sorted(valid_arrows, key=lambda a: a[0])

    # Filter close duplicates (within 25px)
    filtered_arrows = []
    for a in valid_arrows:
        if not filtered_arrows:
            filtered_arrows.append(a)
        else:
            last_a = filtered_arrows[-1]
            if abs(a[0] - last_a[0]) <= 25:
                # Keep the one with higher confidence
                if a[3] > last_a[3]:
                    filtered_arrows[-1] = a
            else:
                filtered_arrows.append(a)

    print(f"\nFiltered valid arrows: {len(filtered_arrows)}")
    for idx, a in enumerate(filtered_arrows):
        print(f"  Arrow {idx+1}: Center=({a[0]}, {a[1]}), Pred={a[2]} ({a[3]:.1%})")


if __name__ == "__main__":
    main()
