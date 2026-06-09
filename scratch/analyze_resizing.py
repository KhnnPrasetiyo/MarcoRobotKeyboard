"""TODO: module documentation"""

import os
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

# Add workspace directory to python search path
sys.path.insert(0, r"C:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite")

from app.auto_farm.rune_solver.panel_detect import arrow_boxes_for
from app.auto_farm.rune_solver.vit_solver import ViTSolver


def main():
    """TODO: add documentation"""
    img_path = Path("debug_rune_last/debug_fullframe_after_interact.png")
    if not img_path.exists():
        print("debug_fullframe_after_interact.png not found")
        return

    frame = cv2.imread(str(img_path))
    h, w = frame.shape[:2]
    print(f"Frame shape: {frame.shape}")

    # Crop exactly as in controller.py
    target_ratio = 2.587
    width = w // 2
    height = int(round(width / target_ratio))
    y_center = int(round(0.328 * h))
    y0 = max(0, y_center - height // 2)
    y1 = min(h, y0 + height)
    x0 = w // 4
    x1 = x0 + width
    cropped_bgr = frame[y0:y1, x0:x1]
    print(f"Cropped shape: {cropped_bgr.shape}")

    # Convert to PIL RGB
    cropped_rgb = cv2.cvtColor(cropped_bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(cropped_rgb)

    # Run ViTSolver solve without writing to original directories
    solver = ViTSolver()

    # We want to see what arrow_boxes_for does when it resizes the image
    # In vit_solver.py:
    # if image.size != (528, 304):
    #     image = image.resize((528, 304), Image.LANCZOS)

    resized_pil = pil_img.resize((528, 304), Image.LANCZOS)

    # Let's save the resized image to scratch/temp_resized.png to check it
    resized_pil.save("scratch/temp_resized.png")

    boxes, max_score = arrow_boxes_for(resized_pil)
    print(f"Resized image (528x304) template match score: {max_score}")
    print(f"Boxes detected: {boxes}")

    # What if we didn't crop or crop with a different ratio?
    # Let's check how the original template matches the fullframe if we scale it.


if __name__ == "__main__":
    main()
