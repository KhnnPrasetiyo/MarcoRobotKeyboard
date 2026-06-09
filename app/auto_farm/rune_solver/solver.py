"""Rune solver facade.

Preserves the BGR-ndarray contract used by ``detection.merge_detection``:
``RuneSolver().solve(image)`` returns either a 4-element list of direction
strings or an empty list on failure.

Backend selection:
- If ``ROBOFLOW_API_KEY`` is set in the environment, both ``HybridSolver``
  and ``ViTSolver`` are loaded and the hybrid path is tried first. On any
  hybrid runtime error we silently fall through to ViT.
- Otherwise, only ``ViTSolver`` is loaded and used directly.

The ViT module is built once and shared between both backends to avoid
double-loading the ~87 MB checkpoint.
"""

from __future__ import annotations

import os
from pathlib import Path

from app.auto_farm.utils import resolve_path

DEFAULT_WEIGHTS = Path(resolve_path("assets/models/arrow_vit.onnx"))


class RuneSolver:
    """TODO: add documentation"""

    def __init__(self, weights_path: Path = DEFAULT_WEIGHTS, api_key: str | None = None):
        """TODO: add documentation"""
        self._vit = None
        self.device = "cpu"
        self.model = None
        self.last_score = 0.0

        # Try to load offline ViTSolver (which requires PyTorch)
        try:
            from .vit_solver import ViTSolver

            self._vit = ViTSolver(ckpt_path=weights_path)
            self.device = self._vit.device
            self.model = self._vit.model
        except (ImportError, ModuleNotFoundError) as e:
            print(f"[RUNE] Peringatan: Model lokal offline (PyTorch/ViT) tidak dapat dimuat: {e}")
            print("[RUNE] Deteksi akan berjalan murni menggunakan server cloud Roboflow.")

        key = api_key or os.environ.get("ROBOFLOW_API_KEY")
        if key:
            try:
                from .hybrid_solver import HybridSolver

                self._hybrid = HybridSolver(
                    vit_module=self.model,
                    device=self.device,
                    roboflow_kwargs={"api_key": key},
                )
                self._mode = (
                    "hybrid+vit (Roboflow Direct)"
                    if self._vit is not None
                    else "Roboflow Direct (Online Only)"
                )
            except Exception as e:
                print(f"[RUNE] Gagal menginisialisasi HybridSolver: {e}")
                self._hybrid = None
                self._mode = "None"
        else:
            self._hybrid = None
            self._mode = "vit" if self._vit is not None else "None"
            if self._vit is None:
                print(
                    "[RUNE] ERROR: Tidak ada model solver yang aktif! Silakan masukkan Roboflow API Key di pengaturan."
                )
        print(f"[~] Rune solver mode: {self._mode}")

    def solve(self, image: any, log_func=None, save_debug: bool = True) -> list[str]:
        """BGR ndarray -> 4 direction strings, or [] on failure."""
        self.last_score = 0.0
        if image is None or image.size == 0:
            return []

        import cv2
        from PIL import Image

        if image.ndim == 3 and image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil = Image.fromarray(rgb)

        if self._hybrid is not None:
            try:
                # Hybrid solver does not output score, set default
                self.last_score = 15.0
                return self._hybrid.solve(pil, save_debug=save_debug)
            except Exception as e:
                msg = f"[!] Hybrid solver error: {e}"
                print(msg)
                if log_func:
                    log_func(msg)
                if self._vit is None:
                    fallback_msg = "[!] Model offline (ViT) tidak tersedia sebagai fallback."
                    print(fallback_msg)
                    if log_func:
                        log_func(fallback_msg)
                    return []

        if self._vit is not None:
            try:
                res = self._vit.solve(pil, log_func=log_func, save_debug=save_debug)
                self.last_score = self._vit.last_score
                return res
            except Exception as e:
                print(f"[!] ViT solver error: {e}")
                return []
        return []
