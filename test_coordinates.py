"""TODO: module documentation"""

from pathlib import Path

import cv2
import numpy as np
import torch
from PIL import Image

from app.auto_farm.rune_solver.panel_detect import \
    detect_panel_origin as detect_onnx
from app.auto_farm.utils import resolve_path


def main():
    """TODO: add documentation"""
    img_path = "debug_rune_last/resized_band.png"
    img = Image.open(img_path)

    # 1. OpenCV / ONNX version origin
    img_bgr = cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)
    _REF_IMAGE = Path(resolve_path("assets/rune_panel_template.png"))
    ref_img = cv2.imread(str(_REF_IMAGE))
    _TPL_BOX = (
        120,
        200,
        25,
        75,
    )  # Note: _TPL_BOX in panel_detect.py is (25, 120, 75, 200) -> [120:200, 25:75]
    tpl_l = ref_img[120:200, 25:75]
    onnx_origin, onnx_score = detect_onnx(img_bgr, tpl_l)
    print("ONNX/OpenCV origin:", onnx_origin, "Score:", onnx_score)

    # 2. PyTorch version origin
    _REF_IMAGE = Path(resolve_path("assets/rune_panel_template.png"))
    _TPL_BOX = (25, 120, 25 + 50, 120 + 80)

    def _to_chw_tensor(image_pil):
        """TODO: add documentation"""
        arr = np.asarray(image_pil.convert("RGB"), dtype=np.float32) / 255.0
        return torch.from_numpy(arr).permute(2, 0, 1)

    tpl_img = Image.open(_REF_IMAGE).crop(_TPL_BOX)
    tpl_tensor = _to_chw_tensor(tpl_img)
    tpl_tensor = tpl_tensor - tpl_tensor.mean(dim=(1, 2), keepdim=True)

    image_tensor = _to_chw_tensor(img)
    x = image_tensor.unsqueeze(0)
    k = tpl_tensor.unsqueeze(0)

    import torch.nn.functional as F

    numer = F.conv2d(x, k.sum(dim=0, keepdim=True))

    C, H, W = image_tensor.shape
    h, w = tpl_tensor.shape[1:]
    ones = torch.ones(1, C, h, w, dtype=x.dtype)
    sum_x = F.conv2d(x, ones)
    sum_x2 = F.conv2d(x * x, ones)
    n = float(C * h * w)
    var = sum_x2 - sum_x * sum_x / n
    denom = torch.sqrt(torch.clamp(var, min=1e-6))
    score = (numer / denom).squeeze(0).squeeze(0)

    mask = torch.full_like(score, float("-inf"))
    y0, y1 = 95, 165
    x0, x1 = 5, 80
    mask[y0:y1, x0:x1] = 0.0
    score_masked = score + mask

    flat = int(score_masked.argmax().item())
    yy, xx = divmod(flat, score.shape[1])
    pytorch_score = float(score[yy, xx].item())

    print("PyTorch origin:    ", (xx, yy), "Score:", pytorch_score)
    print("Coordinates match:", onnx_origin == (xx, yy))


if __name__ == "__main__":
    main()
