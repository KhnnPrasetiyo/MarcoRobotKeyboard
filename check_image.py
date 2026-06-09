"""TODO: module documentation"""

import cv2
from PIL import Image


def main():
    """TODO: add documentation"""
    path = "C:/Users/Admin/.gemini/antigravity-ide/brain/30cf0336-1c0a-4833-929d-b4cf41392a80/scratch/debug_rune_last/debug_interact_panel.png"
    img = cv2.imread(path)
    if img is None:
        print("Image not found")
        return
    print(f"Shape: {img.shape}")


if __name__ == "__main__":
    main()
