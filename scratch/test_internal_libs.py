"""TODO: module documentation"""

import os
import sys

# Clean sys.path to force loading only from the internal folder
sys.path = [p for p in sys.path if "site-packages" not in p.lower()]
internal_path = os.path.abspath("dist/NanoKeyboardControllerLiteApp/_internal")
sys.path.insert(0, internal_path)

import cv2
# Verify paths
import numpy as np
import onnxruntime as ort
from PIL import Image

print("numpy path:", np.__file__)
print("cv2 path:", cv2.__file__)
print("onnxruntime path:", ort.__file__)
print("PIL path:", Image.__file__)

# Now load the ViTSolver from the workspace
sys.path.insert(1, os.path.abspath("."))
from app.auto_farm.rune_solver.vit_solver import ViTSolver

solver = ViTSolver()
img_path = "debug_rune_last/resized_band.png"
if os.path.exists(img_path):
    img = Image.open(img_path)
    res = solver.solve(img, save_debug=False)
    print("Prediction using _internal libraries:", res)
else:
    print(f"Error: {img_path} not found")
