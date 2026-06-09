"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    # Load template
    ref = cv2.imread("assets/rune_panel_template.png")
    # Load user's resized crop
    img = cv2.imread("debug_rune_last/resized_band.png")

    # Let's check their shapes
    print(f"ref shape: {ref.shape}, img shape: {img.shape}")

    # Save a patch of the template left endcap
    tpl_l = ref[120:200, 25:55]
    cv2.imwrite("scratch/tpl_l_ref.png", tpl_l)

    # Save the region in the user's resized image where we expect the left endcap to be.
    # In resized_band.png, the first arrow center was at 200.
    # The left endcap should be around x = 200 - 40 = 160, y = 146 - 40 = 106.
    # Let's save a crop around x=160, y=106
    user_l = img[106:186, 145:175]
    cv2.imwrite("scratch/user_l_expected.png", user_l)

    # Let's print the average color of both patches to see if they match at all
    print(f"Template patch mean color (BGR): {tpl_l.mean(axis=(0,1))}")
    print(f"User patch mean color (BGR): {user_l.mean(axis=(0,1))}")

    # Let's calculate the normalized cross-correlation between the two patches directly
    res = cv2.matchTemplate(user_l, tpl_l, cv2.TM_CCOEFF_NORMED)
    print(f"Direct correlation score: {res[0,0]:.4f}")


if __name__ == "__main__":
    main()
