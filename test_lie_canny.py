import cv2
import numpy as np
import os

d = 'assets/lie'
# Load screenshot with Lie Detector (underwater blue background)
screen_path = os.path.join(d, 'photo_2026-06-08_20-26-30.jpg')
# Load template (blue background crop)
tpl_path = os.path.join(d, 'photolie2_Crop.jpg')

screen = cv2.imread(screen_path)
tpl = cv2.imread(tpl_path)

if screen is None or tpl is None:
    print("Test images not found!")
    sys.exit(1)

gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
gray_tpl = cv2.cvtColor(tpl, cv2.COLOR_BGR2GRAY)

# Method 1: Standard template matching
res_std = cv2.matchTemplate(gray_screen, gray_tpl, cv2.TM_CCOEFF_NORMED)
_, max_val_std, _, max_loc_std = cv2.minMaxLoc(res_std)
print(f"Standard Match Score: {max_val_std:.3f}")

# Method 2: Canny Edge template matching
edge_screen = cv2.Canny(gray_screen, 100, 200)
edge_tpl = cv2.Canny(gray_tpl, 100, 200)

res_edge = cv2.matchTemplate(edge_screen, edge_tpl, cv2.TM_CCORR_NORMED)
_, max_val_edge, _, max_loc_edge = cv2.minMaxLoc(res_edge)
print(f"Canny Edge Match Score: {max_val_edge:.3f}")

# Save edge images for visual confirmation
cv2.imwrite('debug_edge_screen.png', edge_screen)
cv2.imwrite('debug_edge_tpl.png', edge_tpl)
print("Saved debug edge images.")
