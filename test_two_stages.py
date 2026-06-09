import os
import cv2
import numpy as np

def run_test():
    new_tpl_path = r"assets/lie/LieNew_click_Crop.png"
    if not os.path.exists(new_tpl_path):
        print(f"Error: {new_tpl_path} not found.")
        return

    img_bgr = cv2.imread(new_tpl_path)
    h, w = img_bgr.shape[:2]
    print(f"Loaded LieNew_click_Crop.png (Resolution: {w}x{h})")

    # Convert to grayscale for Stage 1
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # --- Test Case 1: Self-Match (Perfect Match) ---
    res_gray = cv2.matchTemplate(img_gray, img_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val_gray, _, max_loc = cv2.minMaxLoc(res_gray)

    x, y = max_loc
    crop_bgr = img_bgr[y:y+h, x:x+w]
    res_bgr = cv2.matchTemplate(crop_bgr[:, :, :3], img_bgr, cv2.TM_CCOEFF_NORMED)
    _, max_val_bgr, _, _ = cv2.minMaxLoc(res_bgr)

    # --- Test Case 2: Wrong Color Match (Inverted Colors) ---
    wrong_color_img = cv2.bitwise_not(img_bgr)
    gray_wrong = cv2.cvtColor(wrong_color_img, cv2.COLOR_BGR2GRAY)
    res_gray_wrong = cv2.matchTemplate(gray_wrong, img_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val_gray_wrong, _, max_loc_wrong = cv2.minMaxLoc(res_gray_wrong)

    x_w, y_w = max_loc_wrong
    crop_wrong_bgr = wrong_color_img[y_w:y_w+h, x_w:x_w+w]
    res_bgr_wrong = cv2.matchTemplate(crop_wrong_bgr[:, :, :3], img_bgr, cv2.TM_CCOEFF_NORMED)
    _, max_val_bgr_wrong, _, _ = cv2.minMaxLoc(res_bgr_wrong)

    print("\n--- Diagnostic Test Results ---")
    print("Test Case 1 (Real Warning - Correct Colors):")
    print(f"  Stage 1 Grayscale Score : {max_val_gray:.3f}")
    print(f"  Stage 2 BGR Color Score  : {max_val_bgr:.3f}")
    print(f"  Status                  : {'VERIFIED' if max_val_bgr >= 0.70 else 'REJECTED'}")

    print("\nTest Case 2 (False Positive - Wrong Colors / Monsters):")
    print(f"  Stage 1 Grayscale Score : {max_val_gray_wrong:.3f}")
    print(f"  Stage 2 BGR Color Score  : {max_val_bgr_wrong:.3f}")
    print(f"  Status                  : {'VERIFIED' if max_val_bgr_wrong >= 0.70 else 'REJECTED (FALSE POSITIVE PREVENTED)'}")

if __name__ == "__main__":
    run_test()
