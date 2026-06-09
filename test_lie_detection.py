"""TODO: module documentation"""

import os

import cv2
import numpy as np

from app.auto_farm.utils import multi_match


def test_lie_detection():
    """TODO: add documentation"""
    assets_dir = os.path.join("assets", "lie")

    # Define templates and target images
    templates_info = [
        ("lie_capcha_Crop", os.path.join(assets_dir, "lie_capcha_Crop.png")),
        ("lie_click_Crop", os.path.join(assets_dir, "lie_click_Crop.png")),
        ("lie_stars_Crop", os.path.join(assets_dir, "lie_stars_Crop.png")),
        ("lie_violet_Crop", os.path.join(assets_dir, "lie_violet_Crop.png")),
    ]

    targets_info = [
        ("lie_capcha_Full", os.path.join(assets_dir, "lie_capcha.png")),
        ("lie_click_Full", os.path.join(assets_dir, "lie_click.png")),
        ("lie_stars_Full", os.path.join(assets_dir, "lie_stars.png")),
        ("lie_violet_Full", os.path.join(assets_dir, "lie_violet.png")),
    ]

    # Load templates in grayscale
    templates = []
    for name, path in templates_info:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Error: Could not load template {name} from {path}")
            continue
        templates.append((name, img))
        print(f"Loaded template: {name} (shape: {img.shape})")

    print("\n--- Running detection tests ---")
    threshold = 0.75

    for target_name, target_path in targets_info:
        target_img = cv2.imread(target_path, cv2.IMREAD_GRAYSCALE)
        if target_img is None:
            print(f"Error: Could not load target {target_name} from {target_path}")
            continue

        print(f"\nTarget: {target_name} (shape: {target_img.shape})")

        # Test against all templates
        matched_any = False
        for tpl_name, tpl_img in templates:
            # First try matching at original size
            matches = multi_match(target_img, tpl_img, threshold=threshold)
            if matches:
                print(
                    f"  [MATCH] Found {len(matches)} match(es) for template {tpl_name} at standard scale. Center coordinates: {matches}"
                )
                matched_any = True
            else:
                # If no match, check if resizing template with screen scaling makes a difference.
                # Let's check target image width vs reference width (1366)
                h, w = target_img.shape[:2]
                scale = w / 1366.0
                if abs(scale - 1.0) > 0.01:
                    new_w = max(1, int(round(tpl_img.shape[1] * scale)))
                    new_h = max(1, int(round(tpl_img.shape[0] * scale)))
                    scaled_tpl = cv2.resize(
                        tpl_img, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4
                    )
                    matches = multi_match(target_img, scaled_tpl, threshold=threshold)
                    if matches:
                        print(
                            f"  [MATCH] Found {len(matches)} match(es) for template {tpl_name} at SCALE {scale:.3f}. Center coordinates: {matches}"
                        )
                        matched_any = True

        if not matched_any:
            print(
                f"  [NO MATCH] No templates matched target {target_name} above threshold {threshold}"
            )


if __name__ == "__main__":
    test_lie_detection()
