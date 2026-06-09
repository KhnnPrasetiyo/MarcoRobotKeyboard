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
    solver = ViTSolver()

    xs = [368, 455, 562, 652, 746]

    for cx in xs:
        crop_path = f"scratch/crop_cx_{cx}.png"
        img = Image.open(crop_path)

        # We preprocess and run prediction
        # Since the crop size is 80x80 (from 1280x720 frame), let's see how the solver performs
        # The solver normally expects the crop to be from the 528x304 resized band.
        # Wait, if the crop is from the 1280x720 frame directly:
        # Let's run it anyway to see the confidence scores.

        # We also want to try matching it using the standard solve path by resizing it
        # to the size of a crop from the resized band:
        # A crop in resized_band has size 94x94 (since ARROW_HALF_W = 47).
        # An 80x80 crop in 1280x720 frame, if scaled to 1366x768 first, would be:
        # 80 * (1366/1280) = 85.3 pixels.
        # In 1366x768, the crop is resized to 528x304, so the crop is scaled by:
        # 528 / 1366 = 0.386.
        # So 85.3 * 0.386 = 33 pixels!
        # Ah! The arrow crop size in the resized band is actually much smaller!
        # Wait, ARROW_HALF_W = 47 means the crop width is 94 pixels.
        # So a 94x94 crop in a 528x304 image!
        # Let's test the prediction:

        # Preprocess using the solver's internal preprocess
        # We'll try passing the image directly to solver._preprocess
        arr = solver._preprocess(img)
        batch = np.expand_dims(arr, axis=0)

        input_name = solver.session.get_inputs()[0].name
        logits = solver.session.run(None, {input_name: batch})[0][0]

        logits_stable = logits - np.max(logits)
        probs = np.exp(logits_stable) / np.sum(np.exp(logits_stable))

        pred_idx = np.argmax(probs)
        print(
            f"Crop cx={cx}: Pred={DIRECTIONS[pred_idx]} ({probs[pred_idx]:.1%}), all: "
            f"up={probs[0]:.1%}, down={probs[1]:.1%}, left={probs[2]:.1%}, right={probs[3]:.1%}"
        )


if __name__ == "__main__":
    main()
