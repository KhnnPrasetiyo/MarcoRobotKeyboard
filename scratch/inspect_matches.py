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
    tpl_l = ref_img[120:200, 25:55]
    tpl_r = ref_img[120:200, 435:465]

    # Left match: px=79, py=121
    # Right match: rx=481, ry=91

    px, py = 79, 121
    rx, ry = 481, 91

    # Crop the matched areas in the image
    match_l = img[py : py + 80, px : px + 30]
    match_r = img[ry : ry + 80, rx : rx + 30]

    cv2.imwrite("scratch/match_left.png", match_l)
    cv2.imwrite("scratch/match_right.png", match_r)
    cv2.imwrite("scratch/tpl_left.png", tpl_l)
    cv2.imwrite("scratch/tpl_right.png", tpl_r)
    print("Saved match crops and template crops to scratch/")


if __name__ == "__main__":
    main()
