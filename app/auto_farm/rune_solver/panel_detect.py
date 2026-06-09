"""Locate the rune panel in a 528x304 screenshot via multi-strategy detection.

Strategy priority:
1. Targeted HSV ranges (yellow/green/orange) — most reliable for arrow detection
2. Expanded HSV ranges (full spectrum) — catches cyan/blue/pink arrows
3. Template matching + content-aware geometric fallback

The color detection uses morphological cleanup and strict spatial/geometric
validation to work reliably on busy backgrounds with monsters, effects, etc.
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

# Maximum number of candidates before spatial pre-filtering
_MAX_CANDIDATES_FOR_COMBO = 25


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
    best_coord = (px + 300, py)

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


# ---------------------------------------------------------------------------
# Color-based arrow detection helpers
# ---------------------------------------------------------------------------

def _build_color_mask(
    img_bgr: np.ndarray,
    hsv_ranges: list[tuple[np.ndarray, np.ndarray]],
) -> np.ndarray:
    """Build a binary mask from multiple HSV ranges.

    Args:
        img_bgr: BGR input image
        hsv_ranges: List of (lower_bound, upper_bound) HSV arrays
    """
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    for lower, upper in hsv_ranges:
        mask = cv2.bitwise_or(mask, cv2.inRange(hsv, lower, upper))

    # Morphological cleanup:
    # - CLOSE to merge fragmented arrow pixels (arrows have multi-color gradients)
    # - OPEN to remove small noise specks from busy backgrounds
    kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_open, iterations=1)

    return mask


def _extract_candidates(
    mask: np.ndarray,
    y_top: int,
    y_bot: int,
    x_left: int = 0,
    x_right: int = 528,
) -> list[tuple[int, int, int]]:
    """Extract arrow center candidates from a binary mask.

    Filters contours by area, aspect ratio, dimensions, and compactness.
    Returns list of (cx, cy, area) tuples.
    """
    restricted = mask.copy()
    restricted[:y_top, :] = 0
    restricted[y_bot:, :] = 0
    restricted[:, :x_left] = 0
    restricted[:, x_right:] = 0

    contours, _ = cv2.findContours(restricted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    for c in contours:
        area = cv2.contourArea(c)
        if 80 <= area <= 3500:
            x, y, w, h = cv2.boundingRect(c)
            aspect = w / h if h > 0 else 0
            # Arrows are roughly square/diamond — NOT elongated like text
            # Strict aspect ratio to reject text characters and UI elements
            if 0.4 <= aspect <= 2.5 and 8 <= w <= 70 and 8 <= h <= 70:
                # Compactness check: real arrows are solid, not hollow
                hull = cv2.convexHull(c)
                hull_area = cv2.contourArea(hull)
                solidity = area / hull_area if hull_area > 0 else 0
                if solidity > 0.25:
                    cx = x + w // 2
                    cy = y + h // 2
                    candidates.append((cx, cy, area))

    return candidates


def _merge_nearby(
    candidates: list[tuple[int, int, int]], dist_thresh: int = 25
) -> list[tuple[int, int, int]]:
    """Merge candidates that are close together, keeping the one with larger area."""
    if not candidates:
        return []

    candidates = sorted(candidates, key=lambda pt: pt[0])
    merged: list[tuple[int, int, int]] = [candidates[0]]

    for pt in candidates[1:]:
        found_merge = False
        for i, existing in enumerate(merged):
            dx = abs(pt[0] - existing[0])
            dy = abs(pt[1] - existing[1])
            if dx <= dist_thresh and dy <= dist_thresh:
                if pt[2] > existing[2]:
                    merged[i] = pt
                found_merge = True
                break
        if not found_merge:
            merged.append(pt)

    return merged


def _find_best_arrow_group(
    candidates: list[tuple[int, int, int]],
    img_w: int = 528,
    img_h: int = 304,
) -> list[tuple[int, int, int]] | None:
    """Find the best group of 4 candidates forming a horizontal line with consistent spacing.

    Scores groups by alignment quality, spacing consistency, area, centrality,
    and preferring groups closer to the vertical center of the image.
    """
    if len(candidates) < 4:
        return None

    candidates = sorted(candidates, key=lambda pt: pt[0])

    # Pre-filter if too many candidates
    if len(candidates) > _MAX_CANDIDATES_FOR_COMBO:
        center_x = img_w // 2
        center_y = img_h // 2
        scored = []
        for pt in candidates:
            cx_dist = 1.0 - abs(pt[0] - center_x) / max(center_x, 1)
            cy_dist = 1.0 - abs(pt[1] - center_y) / max(center_y, 1)
            score = pt[2] * (0.3 + cx_dist * 0.4 + cy_dist * 0.3)
            scored.append((score, pt))
        scored.sort(key=lambda x: x[0], reverse=True)
        candidates = sorted(
            [s[1] for s in scored[:_MAX_CANDIDATES_FOR_COMBO]], key=lambda pt: pt[0]
        )

    best_group = None
    best_score = -1.0

    for subset in itertools.combinations(candidates, 4):
        xs = [pt[0] for pt in subset]
        ys = [pt[1] for pt in subset]

        # Y alignment: all arrows must be on the same horizontal line
        y_diff = max(ys) - min(ys)
        if y_diff > 30:
            continue

        # X spacing: must be consistent and >= minimum
        spacings = [xs[i + 1] - xs[i] for i in range(3)]
        if not all(sp >= _MIN_ARROW_SPACING for sp in spacings):
            continue

        min_sp = min(spacings)
        max_sp = max(spacings)
        if min_sp <= 0 or max_sp / min_sp > 2.0:
            continue

        # Total span check
        x_span = xs[-1] - xs[0]
        if not (150 <= x_span <= 420):
            continue

        # --- Score this group ---
        # Horizontal alignment quality
        alignment_score = max(0, 30 - y_diff) * 5

        # Spacing consistency
        spacing_range = max_sp - min_sp
        spacing_score = max(0, 100 - spacing_range * 2)

        # Horizontal centrality (arrows are typically centered)
        group_cx = sum(xs) / 4
        centrality_x = max(0, 50 - abs(group_cx - img_w / 2) / 2)

        # Vertical position: prefer groups in the middle 40-80% of image height
        # (arrows are below the text but not at the very bottom)
        group_cy = sum(ys) / 4
        vert_ideal = img_h * 0.55  # ideal vertical position
        vert_dist = abs(group_cy - vert_ideal) / img_h
        vert_score = max(0, 40 - vert_dist * 100)

        # Area: prefer larger contours (real arrows vs small noise)
        area_score = sum(pt[2] for pt in subset) / 500

        # Area consistency: prefer similar-sized contours
        areas = [pt[2] for pt in subset]
        area_ratio = max(areas) / max(min(areas), 1)
        consistency_score = max(0, 40 - area_ratio * 4)

        total_score = (
            alignment_score + spacing_score + centrality_x
            + vert_score + area_score + consistency_score
        )

        if total_score > best_score:
            best_score = total_score
            best_group = list(subset)

    return best_group


def _estimate_content_cy(img_bgr: np.ndarray) -> int:
    """Estimate the vertical center of the rune arrows using image brightness analysis.

    Analyzes the vertical brightness profile to find content area,
    then estimates arrow position (lower portion, below instruction text).
    """
    H, W = img_bgr.shape[:2]
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    row_means = gray.mean(axis=1)
    content_rows = np.where(row_means > 15)[0]

    if len(content_rows) > 0:
        content_top = int(content_rows[0])
        content_bot = int(content_rows[-1])
        content_height = content_bot - content_top
        # Arrows are in the lower portion (below the text)
        cy = int(content_top + content_height * 0.60)
    else:
        cy = H // 2

    return max(80, min(H - 60, cy))


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def arrow_boxes_for(img: Image.Image) -> tuple[list[tuple[int, int, int, int]], float]:
    """Detect the 4 rune arrow positions in a 528x304 rune panel image.

    Uses a multi-pass approach with progressively broader color detection:
    
    Pass 1: Yellow/green/orange HSV (H=15-85) — most arrow-specific, fewest false positives
    Pass 2: Extended warm colors (H=0-100) — adds red/cyan coverage
    Pass 3: Full spectrum with high S/V — catches all colored arrows
    Pass 4: Permissive full spectrum — for dark/washed backgrounds
    Pass 5: Geometric fallback with content-aware positioning

    Returns:
        (boxes, template_score) where boxes is a list of 4 (l, t, r, b) tuples.
    """
    img_bgr = cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)
    H_img, W_img = img_bgr.shape[:2]

    # Load template image
    ref_img = cv2.imread(str(_REF_IMAGE))
    if ref_img is None:
        raise FileNotFoundError(f"Template panel tidak ditemukan di: {_REF_IMAGE}")

    tpl_l = ref_img[_TPL_BOX[1] : _TPL_BOX[3], _TPL_BOX[0] : _TPL_BOX[2]]
    tpl_r = ref_img[120:200, 435:465]

    # Template matching for scoring
    (px, py), max_score = detect_panel_origin(img_bgr, tpl_l)

    # Search band: middle portion of image
    y_search_top = int(H_img * 0.15)
    y_search_bot = int(H_img * 0.92)
    x_search_left = int(W_img * 0.01)
    x_search_right = int(W_img * 0.99)

    best_group = None

    # Pass 1: Original targeted range — yellow/green/orange (H=15-85, S>=80, V>=120)
    # This is the most specific and reliable for rune arrows
    if best_group is None:
        hsv_ranges_targeted = [
            (np.array([15, 80, 120]), np.array([85, 255, 255])),
        ]
        mask = _build_color_mask(img_bgr, hsv_ranges_targeted)
        candidates = _extract_candidates(mask, y_search_top, y_search_bot, x_search_left, x_search_right)
        candidates = _merge_nearby(candidates)
        best_group = _find_best_arrow_group(candidates, W_img, H_img)

    # Pass 2: Extended warm + cyan (H=0-100, S>=90, V>=130)
    # Adds red/orange and cyan coverage while staying relatively specific
    if best_group is None:
        hsv_ranges_extended = [
            (np.array([0, 90, 130]), np.array([100, 255, 255])),
        ]
        mask = _build_color_mask(img_bgr, hsv_ranges_extended)
        candidates = _extract_candidates(mask, y_search_top, y_search_bot, x_search_left, x_search_right)
        candidates = _merge_nearby(candidates)
        best_group = _find_best_arrow_group(candidates, W_img, H_img)

    # Pass 3: Full spectrum with high thresholds (S>=120, V>=160)
    # Catches ALL bright colored arrows but with strict brightness requirements
    # to reject background elements
    if best_group is None:
        hsv_ranges_full_strict = [
            (np.array([0, 120, 160]), np.array([180, 255, 255])),
        ]
        mask = _build_color_mask(img_bgr, hsv_ranges_full_strict)
        candidates = _extract_candidates(mask, y_search_top, y_search_bot, x_search_left, x_search_right)
        candidates = _merge_nearby(candidates)
        best_group = _find_best_arrow_group(candidates, W_img, H_img)

    # Pass 4: Full spectrum permissive (S>=70, V>=100) — last resort for dark images
    if best_group is None:
        hsv_ranges_permissive = [
            (np.array([0, 70, 100]), np.array([180, 255, 255])),
        ]
        mask = _build_color_mask(img_bgr, hsv_ranges_permissive)
        candidates = _extract_candidates(mask, y_search_top, y_search_bot, x_search_left, x_search_right)
        candidates = _merge_nearby(candidates)
        best_group = _find_best_arrow_group(candidates, W_img, H_img)

    boxes: list[tuple[int, int, int, int]] = []

    if best_group is not None:
        # Color detection succeeded — boxes centered on actual arrow positions
        cy_avg = int(round(sum(pt[1] for pt in best_group) / 4))
        for cx, cy_col, _ in best_group:
            boxes.append(
                (cx - ARROW_HALF_W, cy_avg - ARROW_HALF_H, cx + ARROW_HALF_W, cy_avg + ARROW_HALF_H)
            )
    else:
        # Geometric fallback with content-aware positioning
        if max_score >= 6.0:
            L = px + 15
            cy = py + 25
        else:
            L = 79
            cy = _estimate_content_cy(img_bgr)

        if not (30 <= L <= 150):
            L = 79
        if not (80 <= cy <= 250):
            cy = _estimate_content_cy(img_bgr)

        if max_score >= 6.0:
            (rx, ry), r_score = detect_right_endcap(img_bgr, tpl_r, px, py)
            R = rx + 45 if r_score >= 6.0 else L + 370
        else:
            R = L + 370

        if not (350 <= R <= 520) or R <= L:
            R = L + 370

        for idx in range(4):
            cx = L + 50 + idx * 90
            boxes.append(
                (cx - ARROW_HALF_W, cy - ARROW_HALF_H, cx + ARROW_HALF_W, cy + ARROW_HALF_H)
            )

    # Clamp all box coordinates to image bounds
    boxes = [(max(0, l), max(0, t), min(W_img, r), min(H_img, b)) for l, t, r, b in boxes]

    return boxes, max_score
