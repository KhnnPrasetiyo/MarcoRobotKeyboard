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

    h, w = img.shape[:2]

    # Let's crop as in controller.py
    target_ratio = 2.587
    width = w // 2
    height = int(round(width / target_ratio))
    y_center = int(round(0.328 * h))
    y0 = max(0, y_center - height // 2)
    y1 = min(h, y0 + height)
    x0 = w // 4
    x1 = x0 + width

    # We will draw a green rectangle on the full frame showing the crop region
    vis_img = img.copy()
    cv2.rectangle(vis_img, (x0, y0), (x1, y1), (0, 255, 0), 2)

    # Now let's find the actual arrow colors using the HSV filter in the crop region
    cropped = img[y0:y1, x0:x1]
    hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
    lower_arrow = np.array([10, 50, 100])
    upper_arrow = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        if 80 <= area <= 2000:
            x, y, w_box, h_box = cv2.boundingRect(c)
            aspect = w_box / h_box
            if 0.5 <= aspect <= 2.0:
                cx = x + w_box // 2
                cy = y + h_box // 2
                candidates.append((cx, cy, area, (x, y, w_box, h_box)))

    candidates = sorted(candidates, key=lambda pt: pt[0])
    print(f"Candidates inside the cropped region (relative coords):")
    for idx, (cx, cy, area, bbox) in enumerate(candidates):
        print(f"Cand {idx}: Center=({cx}, {cy}), Area={area}, BBox={bbox}")
        # Draw on the cropped image
        cv2.circle(cropped, (cx, cy), 5, (0, 0, 255), -1)
        cv2.putText(
            cropped, f"{idx}", (cx - 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1
        )

    cv2.imwrite("scratch/vis_crop_region.png", vis_img)
    cv2.imwrite("scratch/vis_arrows_cropped.png", cropped)
    print("Saved vis_crop_region.png and vis_arrows_cropped.png to scratch/")


if __name__ == "__main__":
    main()
