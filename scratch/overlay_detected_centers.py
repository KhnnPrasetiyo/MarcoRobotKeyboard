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

    # Candidates from detect_arrow_centers_by_color.py
    # Candidate 2: Center=(144, 172)
    # Candidate 4: Center=(194, 166)
    # Candidate 5: Center=(281, 164)
    # Candidate 6: Center=(365, 158)

    vis_img = img.copy()
    centers = [(144, 172), (194, 166), (281, 164), (365, 158)]
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

    for idx, (cx, cy) in enumerate(centers):
        cv2.circle(vis_img, (cx, cy), 5, colors[idx], -1)
        cv2.putText(
            vis_img,
            f"C{idx}:{cx}",
            (cx - 15, cy - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            colors[idx],
            1,
        )

    vis_path = "c:/Users/Admin/.gemini/antigravity-ide/brain/3ad08d59-5724-48aa-92fb-e7542343e430/centers_overlay_vis.png"
    cv2.imwrite(vis_path, vis_img)
    print(f"Saved visualization to {vis_path}")


if __name__ == "__main__":
    main()
