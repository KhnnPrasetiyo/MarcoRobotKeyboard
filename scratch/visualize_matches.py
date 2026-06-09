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
    tpl_l = ref_img[
        120:200, 25:55
    ]  # width 30, height 80 (since _TPL_BOX in panel_detect.py is (25, 120, 55, 200))

    # Let's run template matching
    res = cv2.matchTemplate(img, tpl_l, cv2.TM_CCOEFF_NORMED)
    scaled_res = res * 19.79484

    # Draw top 5 match locations on the image
    flat_indices = np.argsort(scaled_res.ravel())[::-1]

    vis_img = img.copy()
    count = 0
    seen_coords = []

    print("Match coordinates in resized_band.png:")
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

        # Draw on image
        cv2.rectangle(vis_img, (xx, yy), (xx + 30, yy + 80), (0, 0, 255), 1)
        cv2.putText(
            vis_img,
            f"#{count}:{score:.1f}",
            (xx, yy - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.35,
            (0, 0, 255),
            1,
        )

        count += 1
        if count >= 10:
            break

    cv2.imwrite("scratch/vis_template_matches.png", vis_img)
    print("Saved scratch/vis_template_matches.png")


if __name__ == "__main__":
    main()
