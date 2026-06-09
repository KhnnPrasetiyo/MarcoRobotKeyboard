"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    img = cv2.imread("debug_rune_last/debug_fullframe_after_interact.png")
    if img is None:
        print("Image not found")
        return

    print(f"Image shape: {img.shape}")

    # The rune panel is purple/blue. Let's convert to HSV and find purple/blue areas.
    # Purple/blue H range is usually around [100, 140]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_purple = np.array([100, 30, 30])
    upper_purple = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_purple, upper_purple)

    # Let's find contours of purple regions
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # We look for a large horizontal banner in the middle third of the screen
    # middle third y: [240, 480] for a 720h screen
    h, w = img.shape[:2]
    y_min, y_max = h // 4, 3 * h // 4

    print("Large purple regions in the middle of the screen:")
    for idx, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area > 1000:
            x, y, w_box, h_box = cv2.boundingRect(c)
            # Check if it overlaps with middle y
            if y_min <= y + h_box // 2 <= y_max:
                print(f"Region {idx}: x={x}, y={y}, w={w_box}, h={h_box}, area={area}")
                # Save a crop of this region
                crop = img[y : y + h_box, x : x + w_box]
                cv2.imwrite(f"scratch/purple_region_{idx}.png", crop)


if __name__ == "__main__":
    main()
