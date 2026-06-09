"""Locate the rune panel in a 528x304 screenshot via OpenCV template matching.

Idea: extract a single "left endcap" template (a distinctive curved gold corner
that always appears at the panel's left edge), slide it across a bounded search
band, and place the four arrow boxes at fixed offsets within the panel frame.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

from app.auto_farm.utils import resolve_path

_REF_IMAGE = Path(resolve_path("assets/rune_panel_template.png"))
_PANEL_LEFT_REF = 25
_PANEL_TOP_REF = 120
_TPL_BOX = (_PANEL_LEFT_REF, _PANEL_TOP_REF, _PANEL_LEFT_REF + 30, _PANEL_TOP_REF + 80)
ARROW_CENTERS_REL: tuple[tuple[int, int], ...] = (
    (65, 45),
    (155, 45),
    (245, 45),
    (335, 45),
)
ARROW_HALF_W = 47
ARROW_HALF_H = 47

# Minimum spacing between consecutive arrow centers (px) to filter out false positives
_MIN_ARROW_SPACING = 55

_SEARCH_X = (0, 250)
_SEARCH_Y = (70, 180)


def detect_panel_origin(img_bgr: np.ndarray, tpl_l: np.ndarray) -> tuple[tuple[int, int], float]:
    """Matches the left endcap in a wide search region using a center-constrained scoring system."""
    res = cv2.matchTemplate(img_bgr, tpl_l, cv2.TM_CCOEFF_NORMED)
    scaled_res = res * 19.79484

    best_score = -999.0
    best_coord = (30, 104)  # safe fallback

    y0, y1 = _SEARCH_Y
    x0, x1 = _SEARCH_X

    y_max = min(y1, scaled_res.shape[0])
    x_max = min(x1, scaled_res.shape[1])

    for y in range(y0, y_max):
        for x in range(x0, x_max):
            score = scaled_res[y, x]
            # Center constraint: penalize distance from the expected panel center (264)
            est_center = x + 190
            dist = abs(est_center - 264)
            constrained = score - 0.05 * dist

            if constrained > best_score:
                best_score = constrained
                best_coord = (x, y)

    xx, yy = best_coord
    raw_score = float(scaled_res[yy, xx])
    return (xx, yy), raw_score


def detect_right_endcap(
    img_bgr: np.ndarray, tpl_r: np.ndarray, px: int, py: int
) -> tuple[tuple[int, int], float]:
    """Matches the right endcap in a constrained vertical range relative to the detected left endcap."""
    res = cv2.matchTemplate(img_bgr, tpl_r, cv2.TM_CCOEFF_NORMED)
    scaled_res = res * 19.79484

    best_score = -999.0
    best_coord = (px + 300, py)  # fallback width

    y0 = max(0, py - 30)
    y1 = min(scaled_res.shape[0], py + 30)
    x0 = min(scaled_res.shape[1] - 1, px + 370)
    x1 = min(scaled_res.shape[1] - 1, px + 450)

    if x0 >= x1 or y0 >= y1:
        return best_coord, 0.0

    for y in range(y0, y1):
        for x in range(x0, x1 + 1):
            score = scaled_res[y, x]
            if score > best_score:
                best_score = score
                best_coord = (x, y)

    xx, yy = best_coord
    return (xx, yy), float(scaled_res[yy, xx])


def arrow_boxes_for(img: Image.Image) -> tuple[list[tuple[int, int, int, int]], float]:
    """TODO: add documentation"""
    # Convert PIL Image to OpenCV BGR
    img_bgr = cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)

    # Load template image
    ref_img = cv2.imread(str(_REF_IMAGE))
    if ref_img is None:
        raise FileNotFoundError(f"Template panel tidak ditemukan di: {_REF_IMAGE}")

    tpl_l = ref_img[_TPL_BOX[1] : _TPL_BOX[3], _TPL_BOX[0] : _TPL_BOX[2]]
    tpl_r = ref_img[120:200, 435:465]  # right endcap template (width 30)

    # 1. Detect left endcap
    (px, py), max_score = detect_panel_origin(img_bgr, tpl_l)

    # If left endcap match is extremely poor, fallback to default centered values
    if max_score < 3.0:
        L = 79
        cy = 150
    else:
        L = px + 15
        cy = py + 25

    # Sanity check on L and cy to protect against false positive template matches
    if not (30 <= L <= 150):
        L = 79
    if not (100 <= cy <= 200):
        cy = 150

    # 2. Detect right endcap
    if max_score < 3.0:
        R = L + 370
    else:
        (rx, ry), r_score = detect_right_endcap(img_bgr, tpl_r, px, py)
        R = rx + 45 if r_score >= 3.0 else L + 370

    # Sanity check on R
    if not (350 <= R <= 520) or R <= L:
        R = L + 370

    # 3. Detect arrow centers via HSV color segmentation
    # Use tighter HSV range for rune arrows (green/yellow/orange gradient)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    lower_arrow = np.array([15, 80, 120])  # Tighter lower bound (avoid dark yellows)
    upper_arrow = np.array([85, 255, 255])  # Tighter upper bound
    mask = cv2.inRange(hsv, lower_arrow, upper_arrow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Collect ALL color candidates without strict spatial constraints.
    # The old approach filtered by L/R panel bounds from template matching,
    # but those bounds are often inaccurate after proportional resize/center-crop.
    color_candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        if 100 <= area <= 1800:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h if h > 0 else 0
            if 0.45 <= aspect <= 2.2:
                cx = x + w // 2
                cy_col = y + h // 2
                color_candidates.append((cx, cy_col, area))

    # Sort candidates by X coordinate
    color_candidates = sorted(color_candidates, key=lambda pt: pt[0])

    # Filter close duplicates/split contours (merge within 25px)
    filtered_centers = []
    for pt in color_candidates:
        if not filtered_centers:
            filtered_centers.append(pt)
        else:
            last_pt = filtered_centers[-1]
            if abs(pt[0] - last_pt[0]) <= 25:
                # Keep candidate with larger contour area
                if pt[2] > last_pt[2]:
                    filtered_centers[-1] = pt
            else:
                filtered_centers.append(pt)

    # Find the best subset of 4 candidates forming a horizontal line
    # with consistent spacing (robust against noise/false positives).
    use_color = False
    best_group = None

    if len(filtered_centers) >= 4:
        best_y_diff = 9999
        for subset in itertools.combinations(filtered_centers, 4):
            ys = [pt[1] for pt in subset]
            y_diff = max(ys) - min(ys)

            xs = [pt[0] for pt in subset]
            spacings = [xs[i + 1] - xs[i] for i in range(3)]

            spacings_ok = all(sp >= _MIN_ARROW_SPACING for sp in spacings)
            min_sp = min(spacings) if spacings else 0
            ratio_ok = (max(spacings) / min_sp <= 2.0) if min_sp > 0 else False

            # Total X span should cover a reasonable panel width
            x_span = max(xs) - min(xs)
            x_span_ok = 150 <= x_span <= 400

            if y_diff < 25 and spacings_ok and ratio_ok and x_span_ok:
                if y_diff < best_y_diff:
                    best_y_diff = y_diff
                    best_group = list(subset)

        if best_group is not None:
            use_color = True

    boxes: list[tuple[int, int, int, int]] = []

    if use_color and best_group is not None:
        # Color detection found 4 well-spaced, horizontally aligned arrows
        cy_avg = int(round(sum(pt[1] for pt in best_group) / 4))
        for cx, cy_col, _ in best_group:
            boxes.append(
                (cx - ARROW_HALF_W, cy_avg - ARROW_HALF_H, cx + ARROW_HALF_W, cy_avg + ARROW_HALF_H)
            )
    else:
        # Geometric interpolation using detected/default panel boundaries (reliable fallback)
        for idx in range(4):
            cx = L + 50 + idx * 90
            boxes.append(
                (cx - ARROW_HALF_W, cy - ARROW_HALF_H, cx + ARROW_HALF_W, cy + ARROW_HALF_H)
            )

    # Clamp all box coordinates to image bounds
    H_img, W_img = img_bgr.shape[:2]
    boxes = [(max(0, l), max(0, t), min(W_img, r), min(H_img, b)) for l, t, r, b in boxes]

    return boxes, max_score
