"""TODO: module documentation"""

import json
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, r"c:\Users\Admin\Downloads\AutoFarmMaple\NanoKeyboardControllerLite_Lie")

from app.auto_farm.rune_solver.roboflow_client import RoboflowClient


def main():
    api_key = "4useHPDmgrlnnEc9uIR1, dxcHG3bmFP7FQtJTyKyf"
    client = RoboflowClient(api_key=api_key, timeout=25.0)

    img_path = Path(
        "C:/Users/Admin/.gemini/antigravity-ide/brain/30cf0336-1c0a-4833-929d-b4cf41392a80/scratch/debug_rune_last/resized_band.png"
    )
    if not img_path.exists():
        img_path = Path(
            "C:/Users/Admin/.gemini/antigravity-ide/brain/30cf0336-1c0a-4833-929d-b4cf41392a80/scratch/debug_rune_last/debug_interact_panel.png"
        )

    if not img_path.exists():
        print("Debug image not found.")
        return

    print(f"Testing image: {img_path}")
    img = Image.open(img_path)

    print("Inference on original size:")
    try:
        preds = client.infer(img)
        print(json.dumps(preds, indent=2))
    except Exception as e:
        print(f"Error: {e}")

    print("\nInference on resized (528, 304):")
    try:
        img_resized = img.resize((528, 304), Image.LANCZOS)
        preds_resized = client.infer(img_resized)
        print(json.dumps(preds_resized, indent=2))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
