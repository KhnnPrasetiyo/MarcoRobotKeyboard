"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    img_path = "c:/Users/Admin/Downloads/AutoFarmMaple/NanoKeyboardControllerLite/debug_rune_last/resized_band.png"
    img = cv2.imread(img_path)
    if img is None:
        print("Could not load image")
        return

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # The arrows have a gradient from green to red.
    # Let's search for green/yellow/orange/red colors of the arrows.
    # Green range: H in [35, 85], S in [100, 255], V in [100, 255]
    # Yellow/Orange/Red range: H in [0, 30] or [150, 180]
    # Let's combine them or just search for the green/yellow part of the arrow.
    lower_arrow = np.array([10, 50, 100])
    upper_arrow = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    # Save mask for debug
    cv2.imwrite(
        "c:/Users/Admin/.gemini/antigravity-ide/brain/3ad08d59-5724-48aa-92fb-e7542343e430/arrow_mask.png",
        mask,
    )

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    arrow_candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        # Arrow contour area in resized_band should be around 100 to 1000
        if 80 <= area <= 2000:
            x, y, w, h = cv2.boundingRect(c)
            # Aspect ratio of arrow is close to 1
            aspect = w / h
            if 0.5 <= aspect <= 2.0:
                cx = x + w // 2
                cy = y + h // 2
                arrow_candidates.append((cx, cy, area, (x, y, w, h)))

    # Sort by X coordinate
    arrow_candidates = sorted(arrow_candidates, key=lambda a: a[0])

    print(f"Found {len(arrow_candidates)} arrow candidates:")
    for idx, (cx, cy, area, bbox) in enumerate(arrow_candidates):
        print(f"Candidate {idx}: Center=({cx}, {cy}), Area={area}, BBox={bbox}")
        # Crop and save candidate
        crop = img[bbox[1] : bbox[1] + bbox[3], bbox[0] : bbox[0] + bbox[2]]
        cv2.imwrite(
            f"c:/Users/Admin/.gemini/antigravity-ide/brain/3ad08d59-5724-48aa-92fb-e7542343e430/color_arrow_{idx}.png",
            crop,
        )


if __name__ == "__main__":
    main()
