"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    img = cv2.imread("debug_rune_last/resized_band.png")
    if img is None:
        print("resized_band.png not found")
        return

    ref_img = cv2.imread("assets/rune_panel_template.png")
    tpl_r = ref_img[120:200, 435:465]  # width 30, height 80

    res = cv2.matchTemplate(img, tpl_r, cv2.TM_CCOEFF_NORMED)
    scaled_res = res * 19.79484

    flat_indices = np.argsort(scaled_res.ravel())[::-1]

    print("Top right endcap matches in resized_band.png:")
    count = 0
    seen_coords = []
    for idx in flat_indices:
        yy, xx = divmod(idx, scaled_res.shape[1])
        score = scaled_res[yy, xx]

        too_close = False
        for sx, sy in seen_coords:
            if abs(sx - xx) < 15 and abs(sy - yy) < 15:
                too_close = True
                break
        if too_close:
            continue

        print(f"Match #{count}: ({xx}, {yy}), score={score:.4f}")
        seen_coords.append((xx, yy))
        count += 1
        if count >= 10:
            break


if __name__ == "__main__":
    main()
