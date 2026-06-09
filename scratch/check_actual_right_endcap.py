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

    ref_path = "c:/Users/Admin/Downloads/AutoFarmMaple/NanoKeyboardControllerLite/assets/rune_panel_template.png"
    ref_img = cv2.imread(ref_path)
    if ref_img is None:
        print("Could not load reference")
        return

    # Extract right endcap template
    tpl_r = ref_img[120:200, 425:475]

    # Find matches
    res = cv2.matchTemplate(img, tpl_r, cv2.TM_CCOEFF_NORMED)
    scaled_res = res * 19.79484

    # Search in a region close to the left endcap y-coordinate (108)
    # x around 350 to 440, y around 80 to 130
    y0, y1 = 80, 130
    x0, x1 = 350, 428

    sub_score = scaled_res[y0:y1, x0:x1]
    _, max_val, _, max_loc = cv2.minMaxLoc(sub_score)

    best_x = max_loc[0] + x0
    best_y = max_loc[1] + y0

    print(f"Best match in correct right endcap region ({x0}-{x1}, {y0}-{y1}):")
    print(f"Coordinate=({best_x}, {best_y}), Score={max_val:.4f}")

    # Save a crop of this region to see what it looks like
    crop = img[best_y : best_y + 80, best_x : best_x + 50]
    cv2.imwrite(
        "c:/Users/Admin/.gemini/antigravity-ide/brain/3ad08d59-5724-48aa-92fb-e7542343e430/actual_right_endcap_match.png",
        crop,
    )
    print("Saved crop to actual_right_right_endcap_match.png")


if __name__ == "__main__":
    main()
