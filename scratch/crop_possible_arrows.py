"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    img = cv2.imread("debug_rune_last/debug_fullframe_after_interact.png")
    if img is None:
        print("Image not found")
        return

    # Let's save small crops of size 80x80 around the expected arrow locations:
    # 368, 455, 562, 652, 746 at y = 220
    # Let's also try different y centers if they are shifted.
    # We will save a composite image containing these crops.

    xs = [368, 455, 562, 652, 746]
    cy = 220

    crops = []
    for idx, cx in enumerate(xs):
        # crop 80x80
        x0 = cx - 40
        y0 = cy - 40
        x1 = cx + 40
        y1 = cy + 40

        # clamp
        x0 = max(0, min(img.shape[1], x0))
        y0 = max(0, min(img.shape[0], y0))
        x1 = max(0, min(img.shape[1], x1))
        y1 = max(0, min(img.shape[0], y1))

        crop = img[y0:y1, x0:x1]

        # draw center dot
        cv2.circle(crop, (cx - x0, cy - y0), 3, (0, 255, 0), -1)

        crops.append(crop)
        cv2.imwrite(f"scratch/crop_cx_{cx}.png", crop)

    print("Saved arrow crops to scratch/crop_cx_*.png")


if __name__ == "__main__":
    main()
