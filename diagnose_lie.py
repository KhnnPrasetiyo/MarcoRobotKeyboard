import os
import cv2
import numpy as np

d = 'assets/lie'
files = os.listdir(d)

screenshots = [f for f in files if f.startswith('photo_') and f.endswith(('.jpg', '.png'))]
templates = [f for f in files if 'crop' in f.lower() and f.endswith(('.jpg', '.png'))]

print(f"Screenshots found: {screenshots}")
print(f"Templates found: {templates}")

for scr_name in screenshots:
    scr_path = os.path.join(d, scr_name)
    scr = cv2.imread(scr_path)
    if scr is None:
        continue
    # Emulate controller.py: resize frame to 1366 width
    h, w = scr.shape[:2]
    target_w = 1366
    target_h = int(round(h * (target_w / w)))
    resized_scr = cv2.resize(scr, (target_w, target_h), interpolation=cv2.INTER_AREA)
    
    gray_scr = cv2.cvtColor(resized_scr, cv2.COLOR_BGR2GRAY)
    
    print(f"\n--- Matching against Resized Screenshot (width=1366): {scr_name} (Resized: {resized_scr.shape}) ---")
    
    for tpl_name in templates:
        tpl_path = os.path.join(d, tpl_name)
        tpl = cv2.imread(tpl_path, cv2.IMREAD_GRAYSCALE)
        if tpl is None:
            continue
            
        # Test template matching at original template size
        if tpl.shape[0] > gray_scr.shape[0] or tpl.shape[1] > gray_scr.shape[1]:
            print(f"  {tpl_name} too large ({tpl.shape}), skipping")
            continue
            
        res = cv2.matchTemplate(gray_scr, tpl, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)
        
        # Test matching at multiple scales of the template (0.8 to 1.2)
        best_scale = 1.0
        best_score = max_val
        
        for scale in [0.8, 0.9, 1.0, 1.1, 1.2]:
            if scale == 1.0:
                continue
            new_w = max(1, int(round(tpl.shape[1] * scale)))
            new_h = max(1, int(round(tpl.shape[0] * scale)))
            if new_h > gray_scr.shape[0] or new_w > gray_scr.shape[1]:
                continue
            scaled_tpl = cv2.resize(tpl, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
            res_s = cv2.matchTemplate(gray_scr, scaled_tpl, cv2.TM_CCOEFF_NORMED)
            _, score, _, _ = cv2.minMaxLoc(res_s)
            if score > best_score:
                best_score = score
                best_scale = scale
                
        print(f"  {tpl_name} ({tpl.shape[1]}x{tpl.shape[0]}): Best Score = {best_score:.3f} (at scale {best_scale})")
