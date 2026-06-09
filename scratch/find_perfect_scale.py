"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    # Load user's cropped panel
    cropped = cv2.imread("debug_rune_last/debug_interact_panel.png")
    if cropped is None:
        print("debug_interact_panel.png not found")
        return

    print(f"User cropped shape: {cropped.shape}")

    # Load template left endcap
    ref_img = cv2.imread("assets/rune_panel_template.png")
    _TPL_BOX = (25, 120, 55, 200)
    tpl_l = ref_img[_TPL_BOX[1] : _TPL_BOX[3], _TPL_BOX[0] : _TPL_BOX[2]]

    # Let's search over a grid of scale factors for width and height separately
    # to see if the panel is stretched/resized.
    best_raw_score = -1.0
    best_w_scale = 1.0
    best_h_scale = 1.0
    best_loc = (0, 0)

    # We test scales from 0.5 to 1.5 for both width and height
    for w_scale in np.linspace(0.5, 1.5, 21):
        for h_scale in np.linspace(0.5, 1.5, 21):
            w_new = int(cropped.shape[1] * w_scale)
            h_new = int(cropped.shape[0] * h_scale)

            if w_new < tpl_l.shape[1] or h_new < tpl_l.shape[0]:
                continue

            resized = cv2.resize(cropped, (w_new, h_new), interpolation=cv2.INTER_LANCZOS4)
            res = cv2.matchTemplate(resized, tpl_l, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)

            if max_val > best_raw_score:
                best_raw_score = max_val
                best_w_scale = w_scale
                best_h_scale = h_scale
                best_loc = max_loc

    print(f"Best raw match score: {best_raw_score:.4f}")
    print(f"Best width scale: {best_w_scale:.2f}, height scale: {best_h_scale:.2f}")
    print(f"Best location: {best_loc}")

    # Let's see: what if we scale the image proportionally?
    best_prop_score = -1.0
    best_prop_scale = 1.0
    for scale in np.linspace(0.5, 2.0, 31):
        w_new = int(cropped.shape[1] * scale)
        h_new = int(cropped.shape[0] * scale)
        if w_new < tpl_l.shape[1] or h_new < tpl_l.shape[0]:
            continue
        resized = cv2.resize(cropped, (w_new, h_new), interpolation=cv2.INTER_LANCZOS4)
        res = cv2.matchTemplate(resized, tpl_l, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        if max_val > best_prop_score:
            best_prop_score = max_val
            best_prop_scale = scale

    print(f"Best proportional scale: {best_prop_scale:.2f} with score {best_prop_score:.4f}")


if __name__ == "__main__":
    main()
