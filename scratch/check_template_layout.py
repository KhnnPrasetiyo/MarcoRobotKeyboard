"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    ref_img = cv2.imread("assets/rune_panel_template.png")
    if ref_img is None:
        print("Template not found")
        return

    print(f"Template shape: {ref_img.shape}")

    # Let's find the left endcap (gold curved part) in the template image
    # Let's save a visualization of the template itself with _TPL_BOX drawn
    vis = ref_img.copy()
    _TPL_BOX = (25, 120, 55, 200)
    cv2.rectangle(vis, (_TPL_BOX[0], _TPL_BOX[1]), (_TPL_BOX[2], _TPL_BOX[3]), (0, 255, 0), 2)

    # Also draw the right endcap template box
    cv2.rectangle(vis, (435, 120), (465, 200), (0, 0, 255), 2)

    cv2.imwrite("scratch/vis_template_layout.png", vis)
    print("Saved scratch/vis_template_layout.png")


if __name__ == "__main__":
    main()
