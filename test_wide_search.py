"""TODO: module documentation"""

from pathlib import Path

import cv2
import numpy as np
from PIL import Image

from app.auto_farm.utils import resolve_path


def main():
    """TODO: add documentation"""
    img_path = "debug_rune_last/resized_band.png"
    img_bgr = cv2.imread(img_path)

    _REF_IMAGE = Path(resolve_path("assets/rune_panel_template.png"))
    ref_img = cv2.imread(str(_REF_IMAGE))
    _TPL_BOX = (25, 120, 75, 200)
    tpl = ref_img[_TPL_BOX[1] : _TPL_BOX[3], _TPL_BOX[0] : _TPL_BOX[2]]

    # Match template
    res = cv2.matchTemplate(img_bgr, tpl, cv2.TM_CCOEFF_NORMED)

    # Let's search in a wider region
    # y: 50 to 200, x: 0 to 400
    y0, y1 = 50, 200
    x0, x1 = 0, 400

    search_score = res[y0:y1, x0:x1]

    # Find top matches
    # We can use cv2.minMaxLoc repeatedly or just sort
    flat_indices = np.argsort(search_score.ravel())[::-1]

    print("Top template matches in wide search region:")
    count = 0
    seen_coords = []

    for idx in flat_indices:
        yy_rel, xx_rel = divmod(idx, search_score.shape[1])
        xx = xx_rel + x0
        yy = yy_rel + y0
        score = res[yy, xx] * 19.79484

        # Filter out coordinates that are extremely close to already printed ones
        too_close = False
        for sx, sy in seen_coords:
            if abs(sx - xx) < 15 and abs(sy - yy) < 15:
                too_close = True
                break
        if too_close:
            continue

        print(f"Match #{count+1}: Coordinate=({xx}, {yy}), Score={score:.4f}")
        seen_coords.append((xx, yy))
        count += 1
        if count >= 5:
            break


if __name__ == "__main__":
    main()
