"""Offline ONNX ViT-based rune solver: panel template + per-arrow ViT + 5-offset TTA."""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import onnxruntime as ort
from PIL import Image

from app.auto_farm.utils import resolve_path

from .crop import DIRECTIONS
from .panel_detect import arrow_boxes_for

_CKPT_DEFAULT = Path(resolve_path("assets/models/arrow_vit.onnx"))

_TTA_OFFSETS: tuple[tuple[int, int], ...] = (
    (0, 0),
    (-3, 0),
    (3, 0),
    (0, -3),
    (0, 3),
)

_IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype=np.float32).reshape(3, 1, 1)
_IMAGENET_STD = np.array([0.229, 0.224, 0.225], dtype=np.float32).reshape(3, 1, 1)


class ViTSolver:
    """TODO: add documentation"""

    def __init__(
        self,
        ckpt_path: Path | str = _CKPT_DEFAULT,
        device: str | None = None,
        tta: bool = True,
    ):
        """TODO: add documentation"""
        # We enforce CPU execution provider for the Lite version
        onnx_path = Path(ckpt_path)
        if onnx_path.suffix == ".pt":
            onnx_path = onnx_path.with_suffix(".onnx")

        print(f"[ViTSolver] Memuat model ONNX dari {onnx_path}...")
        self.session = ort.InferenceSession(str(onnx_path), providers=["CPUExecutionProvider"])

        # Backwards-compat surface
        self.device = "cpu"
        self.model = self
        self.tta = tta
        self.last_score = 0.0

    def _crop_with_offset(
        self, image: Image.Image, box: tuple[int, int, int, int], dx: int, dy: int
    ) -> Image.Image:
        """TODO: add documentation"""
        l, t, r, b = box
        W, H = image.size
        l2 = max(0, min(W - (r - l), l + dx))
        t2 = max(0, min(H - (b - t), t + dy))
        return image.crop((l2, t2, l2 + (r - l), t2 + (b - t)))

    def _preprocess(self, pil_img: Image.Image) -> np.ndarray:
        """TODO: add documentation"""
        # 1. Resize to 224x224 (INPUT_SIZE)
        resized = pil_img.resize((224, 224), Image.BILINEAR)
        # 2. ToTensor (convert to float32 and divide by 255)
        arr = np.asarray(resized, dtype=np.float32) / 255.0  # shape: (224, 224, 3)
        # transpose to (3, 224, 224)
        arr = arr.transpose(2, 0, 1)
        # 3. Normalize with ImageNet mean and std
        normalized = (arr - _IMAGENET_MEAN) / _IMAGENET_STD
        return normalized

    @staticmethod
    def _proportional_resize_center_crop(
        image: Image.Image, target_w: int = 528, target_h: int = 304
    ) -> Image.Image:
        """Resize proportionally to target height, then center-crop to target width.

        This avoids aspect-ratio distortion that occurs when the controller's
        crop region has a different aspect ratio than the 528×304 template.
        """
        w, h = image.size
        new_h = target_h
        new_w = int(round(w * new_h / h))
        image = image.resize((new_w, new_h), Image.LANCZOS)

        if new_w > target_w:
            left = (new_w - target_w) // 2
            image = image.crop((left, 0, left + target_w, new_h))
        elif new_w < target_w:
            padded = Image.new("RGB", (target_w, target_h), (0, 0, 0))
            left = (target_w - new_w) // 2
            padded.paste(image, (left, 0))
            image = padded
        return image

    def solve(
        self, image: Image.Image | str | Path, log_func=None, save_debug: bool = True
    ) -> list[str]:
        """TODO: add documentation"""
        if not isinstance(image, Image.Image):
            image = Image.open(image)
        image = image.convert("RGB")
        if image.size != (528, 304):
            image = self._proportional_resize_center_crop(image, 528, 304)

        boxes, max_score = arrow_boxes_for(image)
        self.last_score = max_score

        # Save debug images for analysis
        if save_debug:
            try:
                import cv2 as _cv2
                import numpy as _np
                from PIL import ImageDraw, ImageFont

                debug_dir = Path.cwd() / "debug_rune_last"
                debug_dir.mkdir(parents=True, exist_ok=True)

                # 1. Save the resized band (full panel area)
                image.save(debug_dir / "resized_band.png")

                # 2. Save visualization: panel with colored boxes drawn
                vis = image.copy()
                draw = ImageDraw.Draw(vis)
                box_colors = ["#FF0000", "#FF8800", "#FFFF00", "#00FFFF"]
                for idx, b in enumerate(boxes):
                    c = box_colors[idx % len(box_colors)]
                    draw.rectangle(b, outline=c, width=3)
                    draw.text((b[0] + 2, b[1] + 2), f"#{idx}", fill=c)
                # Draw score info
                draw.text((4, 4), f"score={max_score:.2f} boxes={len(boxes)}", fill="lime")
                vis.save(debug_dir / "debug_boxes_vis.png")

                # 3. Save each individual arrow crop
                for idx, b in enumerate(boxes):
                    arrow_crop = image.crop(b)
                    arrow_crop.save(debug_dir / f"arrow_{idx}.png")
                    # Also save upscaled version for easier inspection
                    arrow_big = arrow_crop.resize((180, 180), Image.NEAREST)
                    arrow_big.save(debug_dir / f"arrow_{idx}_big.png")

            except Exception as e:
                print(f"[ViTSolver] Gagal menyimpan debug crop: {e}")

        # Guard: jika tidak ada boxes terdeteksi, jangan crash
        if not boxes:
            msg = f"[ViTSolver] Tidak ada panel/arrow terdeteksi (score={max_score:.2f} < 2.0). Cek debug_rune_last/resized_band.png"
            if log_func:
                log_func(msg)
            else:
                print(msg)
            return []

        offsets = _TTA_OFFSETS if self.tta else ((0, 0),)
        tiles: list[np.ndarray] = []
        for b in boxes:
            for dx, dy in offsets:
                cropped = self._crop_with_offset(image, b, dx, dy)
                tiles.append(self._preprocess(cropped))

        # Stack into batch (shape: [num_boxes * num_offsets, 3, 224, 224])
        batch = np.stack(tiles).astype(np.float32)

        # Run ONNX Session
        input_name = self.session.get_inputs()[0].name
        logits = self.session.run(None, {input_name: batch})[0]  # shape: [20, 4]

        # Compute Softmax in numpy
        # Subtract max for numerical stability
        logits_stable = logits - np.max(logits, axis=-1, keepdims=True)
        exp_logits = np.exp(logits_stable)
        probs = exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)

        # Reshape to (num_boxes, num_offsets, num_classes)
        probs = probs.reshape(len(boxes), len(offsets), -1)
        # Average probabilities across offsets (axis 1)
        mean_probs = probs.mean(axis=1)  # shape: [num_boxes, 4]
        preds = mean_probs.argmax(axis=-1).tolist()

        # Log detailed probabilities for debugging
        for idx in range(len(preds)):
            prob_details = ", ".join(
                [f"{DIRECTIONS[i]}: {mean_probs[idx][i]:.1%}" for i in range(len(DIRECTIONS))]
            )
            msg = f"[ViTSolver DEBUG] Slot {idx+1}: Prediksi={DIRECTIONS[preds[idx]]} ({prob_details})"
            if log_func:
                log_func(msg)
            else:
                print(msg)

        return [DIRECTIONS[p] for p in preds]
