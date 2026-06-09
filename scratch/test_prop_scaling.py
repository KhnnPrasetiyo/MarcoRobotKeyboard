"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    cropped = cv2.imread("debug_rune_last/debug_interact_panel.png")
    if cropped is None:
        print("debug_interact_panel.png not found")
        return

    ref_img = cv2.imread("assets/rune_panel_template.png")
    # Left endcap template from 528x304 ref image:
    # 120:200, 25:55 (height 80, width 30)
    tpl_l = ref_img[120:200, 25:55]
    tpl_r = ref_img[120:200, 435:465]

    # We want to find the best scaling factor for matching
    # Let's try scaling cropped image to a target height of 304, but what should the width be?
    # If we resize cropped to (528, 304):
    # - Left template matches at px=79, py=121 (score 6.96)
    # - Right template matches at rx=362, ry=157 (score 7.77)
    # Let's see: the distance in the resized image is rx - px = 362 - 79 = 283.
    # But in the template image, the distance is 435 - 25 = 410.
    # Why is the distance 283 instead of 410?
    # This means the panel in the resized image is only 283/410 = 69% of its expected width!
    # Why is it so narrow?
    # Let's think: is the user's cropped image showing the actual rune panel, but the panel
    # has a different aspect ratio? Or was the crop from the screen too wide, so when we resized
    # it to 528 width, the panel got squished?
    # Yes! If the crop width was 640 (which is very wide) and the panel itself was only a small
    # part of it, then when we resized the 640x247 crop to 528x304, the width was scaled by 528/640 = 0.825,
    # and the height was scaled by 304/247 = 1.231.
    # Since width was scaled down (0.825) and height was scaled up (1.231), the panel became
    # much narrower relative to its height!
    # Let's calculate: if the panel in the game has a fixed aspect ratio, and we want to resize it
    # without distortion:
    # If the original panel is at scale S:
    # Let's find the left and right endcap directly in the cropped image by scaling the templates!
    # Or by scaling the cropped image proportionally!

    # Let's test proportional scaling of the cropped image:
    for scale in [0.8, 0.9, 1.0, 1.1, 1.2]:
        w_new = int(cropped.shape[1] * scale)
        h_new = int(cropped.shape[0] * scale)
        resized = cv2.resize(cropped, (w_new, h_new), interpolation=cv2.INTER_LANCZOS4)

        # Match left template
        res_l = cv2.matchTemplate(resized, tpl_l, cv2.TM_CCOEFF_NORMED)
        _, max_val_l, _, max_loc_l = cv2.minMaxLoc(res_l)

        # Match right template
        res_r = cv2.matchTemplate(resized, tpl_r, cv2.TM_CCOEFF_NORMED)
        _, max_val_r, _, max_loc_r = cv2.minMaxLoc(res_r)

        dist = max_loc_r[0] - max_loc_l[0]
        print(
            f"Scale {scale:.1f}: L_score={max_val_l:.3f} at {max_loc_l}, R_score={max_val_r:.3f} at {max_loc_r}, dist={dist} (expected ~410)"
        )


if __name__ == "__main__":
    main()
