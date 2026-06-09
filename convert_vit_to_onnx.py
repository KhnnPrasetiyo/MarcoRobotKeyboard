"""TODO: module documentation"""

import sys
from pathlib import Path

import numpy as np
import torch

from app.auto_farm.rune_solver.model_vit import ArrowViT

# Ensure Windows terminal handles UTF-8 output cleanly
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception as e:
        print("Error occurred")
        pass


def main():
    """TODO: add documentation"""
    ckpt_path = Path("assets/models/arrow_vit.pt")
    onnx_path = Path("assets/models/arrow_vit.onnx")

    print(f"Loading PyTorch checkpoint from {ckpt_path}...")
    state = torch.load(ckpt_path, map_location="cpu", weights_only=True)

    backbone = state.get("backbone") or "vit_small_patch16_224.augreg_in21k_ft_in1k"
    print(f"Detected backbone: {backbone}")

    model = ArrowViT(backbone_name=backbone, pretrained=False)
    model.load_state_dict(state["model"])
    model.eval()

    # Dummy input representing a batch of 4 arrow crops (224x224 RGB image tensors)
    dummy_input = torch.randn(4, 3, 224, 224)

    print(f"Exporting model to ONNX format at {onnx_path}...")
    torch.onnx.export(
        model,
        dummy_input,
        str(onnx_path),
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
        opset_version=14,
        do_constant_folding=True,
    )
    print("Export completed successfully!")


if __name__ == "__main__":
    main()
