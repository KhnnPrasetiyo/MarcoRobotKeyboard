"""TODO: module documentation"""

import cv2
import numpy as np


def main():
    """TODO: add documentation"""
    cropped = cv2.imread("debug_rune_last/debug_interact_panel.png")
    if cropped is None:
        print("debug_interact_panel.png not found")
        return

    print(f"Cropped shape: {cropped.shape}")

    hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
    lower_arrow = np.array([10, 50, 100])
    upper_arrow = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        if 80 <= area <= 3000:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h if h > 0 else 0
            if 0.45 <= aspect <= 2.5:  # Relaxed aspect ratio for merged contours
                cx = x + w // 2
                cy = y + h // 2
                candidates.append((cx, cy, area, (x, y, w, h)))

    candidates = sorted(candidates, key=lambda pt: pt[0])
    print(f"Initial candidates count: {len(candidates)}")
    for idx, (cx, cy, area, bbox) in enumerate(candidates):
        print(f"  Cand {idx}: cx={cx}, cy={cy}, area={area}, bbox={bbox}")

    best_group = []
    best_y_diff = 9999

    n = len(candidates)
    if n >= 4:
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        group = [candidates[i], candidates[j], candidates[k], candidates[l]]
                        ys = [pt[1] for pt in group]
                        y_diff = max(ys) - min(ys)

                        xs = [pt[0] for pt in group]
                        spacings = [xs[1] - xs[0], xs[2] - xs[1], xs[3] - xs[2]]

                        # Spacing between consecutive arrows in 640px width
                        # should be roughly equal (approx 80-120 pixels)
                        spacings_ok = all(40 <= sp <= 180 for sp in spacings)

                        min_sp = min(spacings)
                        if min_sp > 0:
                            ratio_ok = (max(spacings) / min_sp) <= 2.2
                        else:
                            ratio_ok = False

                        if y_diff < 30 and spacings_ok and ratio_ok:
                            if y_diff < best_y_diff:
                                best_y_diff = y_diff
                                best_group = group

    if best_group:
        print("FOUND BEST GROUP OF 4 ARROWS:")
        for idx, pt in enumerate(best_group):
            print(f"  Arrow {idx}: cx={pt[0]}, cy={pt[1]}, area={pt[2]}, bbox={pt[3]}")
    else:
        print("Could not find a group of 4 aligned arrows.")


if __name__ == "__main__":
    main()
