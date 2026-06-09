"""Utility functions for Auto Farm."""

import math
import os
import sys

import cv2
import numpy as np


def resolve_path(relative_path):
    """Resolve paths to support PyInstaller bundled assets."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def load_image(path, flags=cv2.IMREAD_COLOR):
    """Loads an image with path resolution, raising FileNotFoundError on error."""
    full_path = resolve_path(path)
    img = cv2.imread(full_path, flags)
    if img is None:
        raise FileNotFoundError(f"Aset tidak ditemukan: '{full_path}'")
    return img


def distance(a, b):
    """Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def multi_match(frame, template, threshold=0.95):
    """Finds template match center locations exceeding the correlation threshold."""
    if len(frame.shape) != 2:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        gray = frame

    try:
        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    except cv2.error:
        return []

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    results = []
    for p in locations:
        x = int(round(p[0] + template.shape[1] / 2))
        y = int(round(p[1] + template.shape[0] / 2))
        results.append((x, y))
    return results


def match_score(frame, template):
    """Returns the maximum normalized template match score."""
    try:
        if frame is None or template is None:
            return 0.0
        if len(frame.shape) == 2:
            gray = frame
        elif len(frame.shape) == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            return 0.0
        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        return float(result.max())
    except Exception as e:
        print("Error occurred")
        return 0.0


def filter_color(img, ranges):
    """Returns BGR image filtered to pixels matching the HSV ranges."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, ranges[0][0], ranges[0][1])
    for i in range(1, len(ranges)):
        mask = cv2.bitwise_or(mask, cv2.inRange(hsv, ranges[i][0], ranges[i][1]))

    color_mask = mask > 0
    result = np.zeros_like(img, np.uint8)
    result[color_mask] = img[color_mask]
    return result
