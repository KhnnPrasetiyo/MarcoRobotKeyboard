"""TODO: module documentation"""

import time

from PIL import Image

from app.auto_farm.rune_solver.vit_solver import ViTSolver


def main():
    """TODO: add documentation"""
    image_path = "debug_rune_last/resized_band.png"
    print(f"Running ONNX ViTSolver test on: {image_path}")

    try:
        # Initialize solver
        solver = ViTSolver()

        # Load test image
        img = Image.open(image_path)

        # Run inference
        t0 = time.time()
        result = solver.solve(img)
        t1 = time.time()

        print("\n=== TEST RESULTS ===")
        print(f"Inference Time: {(t1 - t0)*1000:.2f} ms")
        print(f"Detected Arrows: {result}")
        print(f"Max Score: {solver.last_score:.4f}")
        print("====================")

    except Exception as e:
        print(f"Error during test: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
