"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    frame = cv2.imread("debug_rune_last/debug_fullframe_after_interact.png")
    ref_img = cv2.imread("assets/rune_panel_template.png")

    # Let's extract the left endcap template from the template image (which is 528x304)
    # The left endcap is in the region [120:200, 25:75] in the template
    tpl = ref_img[120:200, 25:75]

    # Let's match the template at various scales of the frame
    # Since the template is from a 528x304 image, let's see if we resize the full frame
    # such that the panel matches the template size.
    # What if the panel in the game is always the same physical size (e.g. 528x304)?
    # Let's search the template in the frame at different scales:
    best_score = -1
    best_scale = 1.0
    best_loc = (0, 0)

    for scale in np.linspace(0.5, 1.5, 21):
        w_new = int(frame.shape[1] * scale)
        h_new = int(frame.shape[0] * scale)
        if w_new < tpl.shape[1] or h_new < tpl.shape[0]:
            continue
        resized_frame = cv2.resize(frame, (w_new, h_new), interpolation=cv2.INTER_LANCZOS4)
        res = cv2.matchTemplate(resized_frame, tpl, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        print(
            f"Scale {scale:.2f}: shape={resized_frame.shape}, max_score={max_val:.4f} at {max_loc}"
        )
        if max_val > best_score:
            best_score = max_val
            best_scale = scale
            best_loc = max_loc

    print(f"Best scale: {best_scale} with score {best_score} at {best_loc}")


if __name__ == "__main__":
    main()
