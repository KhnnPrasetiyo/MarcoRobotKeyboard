"""Hybrid solver: Roboflow detects, local ViT classifies.

The Roboflow Direct path (primary) requires NO PyTorch — it uses class
labels returned directly by the Roboflow API.  Only the local-ViT
fallback path imports torch/torchvision, and those imports are done
lazily so that the module can be loaded in a PyTorch-free EXE build.
"""

from __future__ import annotations

import itertools

from PIL import Image

from .crop import DIRECTIONS
from .roboflow_client import RoboflowClient


class HybridSolver:
    """TODO: add documentation"""

    def __init__(
        self,
        vit_module=None,
        device=None,
        roboflow_kwargs: dict | None = None,
        margin: int = 4,
    ) -> None:
        """TODO: add documentation"""
        self.vit = vit_module
        self.device = device
        self._tf = None  # lazy-loaded torchvision transforms
        self.margin = margin

        # Set a lower confidence threshold by default to ensure we detect all 4 arrows
        roboflow_kwargs = roboflow_kwargs or {}
        if "confidence" not in roboflow_kwargs:
            roboflow_kwargs["confidence"] = 0.2
        self.client = RoboflowClient(**roboflow_kwargs)

    # ------------------------------------------------------------------
    # Lazy helpers – only called when the local-ViT fallback is needed
    # ------------------------------------------------------------------
    def _get_transforms(self):
        """TODO: add documentation"""
        if self._tf is None:
            from .data_vit import build_transforms

            self._tf = build_transforms(train=False)
        return self._tf

    def _crop_box(self, img: Image.Image, p: dict):
        """TODO: add documentation"""
        import torch  # lazy

        cx, cy = p["x"], p["y"]
        # Use native crop size of 90x90 pixels for ViT model to preserve context and scale
        side = 90
        l = max(0, int(round(cx - side / 2)))
        t = max(0, int(round(cy - side / 2)))
        r = min(img.width, int(round(cx + side / 2)))
        b = min(img.height, int(round(cy + side / 2)))

        tf = self._get_transforms()
        return tf(img.crop((l, t, r, b)))

    # ------------------------------------------------------------------
    # Main solve
    # ------------------------------------------------------------------
    def solve(self, image: Image.Image, save_debug: bool = True) -> list[str]:
        """TODO: add documentation"""
        if image.size != (528, 304):
            from .vit_solver import ViTSolver

            image = ViTSolver._proportional_resize_center_crop(image, 528, 304)
        preds = self.client.infer(image)

        # Select the 4 arrow predictions that form the best horizontal line
        valid_subset = None
        if len(preds) >= 4:
            best_y_range = 999.0
            # Search for a subset of 4 predictions that are horizontally aligned and properly spaced
            for subset in itertools.combinations(preds, 4):
                ys = [p["y"] for p in subset]
                y_range = max(ys) - min(ys)

                # y-coordinates should be within 35 pixels
                if y_range < 35:
                    sorted_sub = sorted(subset, key=lambda p: p["x"])
                    xs = [p["x"] for p in sorted_sub]

                    # Spacing between consecutive arrows in 528px width should be between 40px and 120px
                    spacings = [xs[i + 1] - xs[i] for i in range(3)]
                    if all(40 <= sp <= 120 for sp in spacings):
                        if y_range < best_y_range:
                            best_y_range = y_range
                            valid_subset = sorted_sub

            if valid_subset is not None:
                preds = valid_subset
            else:
                # Fallback to sorting by confidence if no horizontally aligned subset of 4 is found
                preds = sorted(preds, key=lambda p: -p["confidence"])[:4]
                preds = sorted(preds, key=lambda p: p["x"])

        if len(preds) < 4:
            raise RuntimeError(f"Roboflow returned {len(preds)} detections (<4): {preds}")

        # 1. Best Solution: return Roboflow classes directly if present and valid
        classes = [p.get("class", "").lower() for p in preds]
        if len(classes) == 4 and all(c in DIRECTIONS for c in classes):
            print(f"[HybridSolver] Using Direct Roboflow Predictions: {classes}")
            return classes

        # 2. Fallback: run local ViT classifier if Roboflow class labels are invalid
        if self.vit is None:
            raise RuntimeError(
                "Roboflow returned invalid classes and local ViT fallback is not available (PyTorch missing)."
            )

        import torch  # lazy

        print(
            "[HybridSolver] Direct classes invalid or incomplete. Falling back to local ViT classification."
        )
        with torch.no_grad():
            crops = torch.stack([self._crop_box(image, p) for p in preds]).to(self.device)
            logits = self.vit(crops)
            idxs = logits.argmax(-1).tolist()
            res = [DIRECTIONS[i] for i in idxs]
            print(f"[HybridSolver] ViT Fallback Result: {res}")
            return res
