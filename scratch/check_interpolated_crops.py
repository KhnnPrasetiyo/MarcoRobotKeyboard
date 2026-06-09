"""TODO: module documentation"""

import cv2


def main():
    """TODO: add documentation"""
    img_path = "c:/Users/Admin/Downloads/AutoFarmMaple/NanoKeyboardControllerLite/debug_rune_last/resized_band.png"
    img = cv2.imread(img_path)
    if img is None:
        print("Could not load image")
        return

    # L = 116, R = 406
    # Centers: 163, 228, 294, 359
    # Y-coordinate center of template: y = 160 (since template was y=120 to 200, curve was at y=160, template center is 120 + 40 = 160.
    # User y-coordinate match was y = 108.
    # In template, y_curve = 160. Template top-left is 120. Curve offset is 40.
    # User top-left is 108. So user curve is at 108 + 40 = 148.
    # Let's verify: user y_center is 148.
    cy = 148

    centers_x = [163, 228, 294, 359]
    half_w = 45
    half_h = 45

    for idx, cx in enumerate(centers_x):
        l = max(0, cx - half_w)
        t = max(0, cy - half_h)
        r = min(img.shape[1], cx + half_w)
        b = min(img.shape[0], cy + half_h)
        crop = img[t:b, l:r]
        crop_path = f"c:/Users/Admin/.gemini/antigravity-ide/brain/3ad08d59-5724-48aa-92fb-e7542343e430/interpolated_arrow_{idx}.png"
        cv2.imwrite(crop_path, crop)
        print(f"Saved interpolated arrow {idx} from center {cx}, {cy} to {crop_path}")


if __name__ == "__main__":
    main()
