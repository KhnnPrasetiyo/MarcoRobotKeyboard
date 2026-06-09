"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    img_path = "debug_rune_last/debug_fullframe_after_interact.png"
    img = cv2.imread(img_path)
    if img is None:
        print("Image not found")
        return

    print(f"Full image shape: {img.shape}")

    # Let's search for arrow colors in the full image using HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_arrow = np.array([10, 50, 100])
    upper_arrow = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        if 200 <= area <= 5000:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h if h > 0 else 0
            if 0.5 <= aspect <= 2.0:
                cx = x + w // 2
                cy = y + h // 2
                candidates.append((cx, cy, area, (x, y, w, h)))

    candidates = sorted(candidates, key=lambda pt: pt[0])
    print(f"Found {len(candidates)} candidates in full frame:")
    for idx, (cx, cy, area, bbox) in enumerate(candidates):
        print(f"Cand {idx}: Center=({cx}, {cy}), Area={area}, BBox={bbox}")


if __name__ == "__main__":
    main()
