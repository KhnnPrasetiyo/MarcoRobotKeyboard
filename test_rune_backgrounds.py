"""Test Offline ViT Rune Solver against all rune images in assets folder.

Tests:
1. Panel detection (template matching + color segmentation)
2. Arrow box localization
3. ViT direction prediction
4. Debug visualization output
"""

import os
import sys
import cv2
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw

# Ensure we can import from app module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.auto_farm.rune_solver.panel_detect import arrow_boxes_for, _REF_IMAGE
from app.auto_farm.rune_solver.vit_solver import ViTSolver


def test_panel_template_exists():
    """Check that the panel template file actually exists."""
    print("=" * 60)
    print("[TEST 1] Cek keberadaan file rune_panel_template.png")
    print("=" * 60)
    exists = _REF_IMAGE.exists()
    print(f"  Path     : {_REF_IMAGE}")
    print(f"  Exists   : {exists}")
    if exists:
        ref_img = cv2.imread(str(_REF_IMAGE))
        if ref_img is not None:
            h, w = ref_img.shape[:2]
            print(f"  Size     : {w}x{h}")
            print(f"  Status   : ✅ OK")
        else:
            print(f"  Status   : ❌ GAGAL - File ada tapi tidak bisa dibaca!")
    else:
        print(f"  Status   : ❌ GAGAL - File tidak ditemukan!")
    print()
    return exists


def test_rune_image(image_path: str, solver: ViTSolver, idx: int):
    """Test a single rune image through the full pipeline."""
    print(f"{'=' * 60}")
    print(f"[TEST] Rune Image: {os.path.basename(image_path)}")
    print(f"{'=' * 60}")

    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"  ❌ GAGAL - Tidak bisa membaca: {image_path}")
        print()
        return False

    h, w = img.shape[:2]
    print(f"  Ukuran asli       : {w}x{h}")

    # Convert to PIL & resize to 528x304
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil = Image.fromarray(rgb).convert("RGB")

    # Apply same proportional resize as ViTSolver
    pil_resized = ViTSolver._proportional_resize_center_crop(pil, 528, 304)
    print(f"  Ukuran setelah resize : {pil_resized.size}")

    # --- Stage 1: Panel Detection ---
    print(f"\n  --- Stage 1: Panel & Arrow Detection ---")
    try:
        boxes, score = arrow_boxes_for(pil_resized)
        print(f"  Template match score : {score:.2f}")
        print(f"  Jumlah arrow boxes   : {len(boxes)}")
        for bi, b in enumerate(boxes):
            bw = b[2] - b[0]
            bh = b[3] - b[1]
            print(f"    Box #{bi}: ({b[0]}, {b[1]}) -> ({b[2]}, {b[3]}) [{bw}x{bh}]")

        if len(boxes) == 4:
            # Check spacing consistency
            centers = [(b[0] + b[2]) // 2 for b in boxes]
            spacings = [centers[i + 1] - centers[i] for i in range(3)]
            print(f"  Arrow centers X      : {centers}")
            print(f"  Spacings             : {spacings}")
            spacing_ok = all(40 <= s <= 120 for s in spacings)
            print(f"  Spacing consistency  : {'✅ OK' if spacing_ok else '⚠️ PERINGATAN - spacing tidak konsisten'}")
        elif len(boxes) == 0:
            print(f"  ⚠️ PERINGATAN: Tidak ada arrow terdeteksi!")
        else:
            print(f"  ⚠️ PERINGATAN: Jumlah arrow bukan 4 ({len(boxes)})")
    except Exception as e:
        print(f"  ❌ GAGAL - Error saat panel detection: {e}")
        import traceback
        traceback.print_exc()
        return False

    # --- Stage 2: ViT Prediction ---
    print(f"\n  --- Stage 2: ViT Direction Prediction ---")
    try:
        # Use solver directly on PIL image
        directions = solver.solve(pil_resized, save_debug=False)
        print(f"  Prediksi arah        : {directions}")
        print(f"  Solver last_score    : {solver.last_score:.2f}")

        if len(directions) == 4:
            valid_dirs = {"up", "down", "left", "right"}
            all_valid = all(d in valid_dirs for d in directions)
            print(f"  Validasi arah        : {'✅ OK - semua arah valid' if all_valid else '❌ GAGAL - ada arah tidak valid'}")
        elif len(directions) == 0:
            print(f"  ⚠️ PERINGATAN: Solver mengembalikan list kosong!")
        else:
            print(f"  ⚠️ PERINGATAN: Jumlah prediksi bukan 4 ({len(directions)})")
    except Exception as e:
        print(f"  ❌ GAGAL - Error saat ViT prediction: {e}")
        import traceback
        traceback.print_exc()
        return False

    # --- Save debug visualization ---
    debug_dir = Path("debug_rune_last") / f"test_{idx}"
    debug_dir.mkdir(parents=True, exist_ok=True)

    # Draw boxes on resized image
    vis = pil_resized.copy()
    draw = ImageDraw.Draw(vis)
    box_colors = ["#FF0000", "#FF8800", "#FFFF00", "#00FFFF"]
    for bi, b in enumerate(boxes):
        c = box_colors[bi % len(box_colors)]
        draw.rectangle(b, outline=c, width=3)
        label = directions[bi] if bi < len(directions) else "?"
        draw.text((b[0] + 5, b[1] + 5), f"#{bi}: {label}", fill=c)
    draw.text((4, 4), f"score={score:.2f} boxes={len(boxes)}", fill="lime")
    vis.save(debug_dir / "debug_vis.png")
    pil_resized.save(debug_dir / "resized_input.png")

    # Save individual arrow crops
    for bi, b in enumerate(boxes):
        arrow_crop = pil_resized.crop(b)
        arrow_crop.save(debug_dir / f"arrow_{bi}.png")
        arrow_big = arrow_crop.resize((180, 180), Image.NEAREST)
        arrow_big.save(debug_dir / f"arrow_{bi}_big.png")

    print(f"\n  Debug images saved to: {debug_dir}")
    print(f"  {'✅ LULUS' if len(directions) == 4 else '❌ GAGAL'}")
    print()
    return len(directions) == 4


def main():
    print("\n" + "=" * 60)
    print("  OFFLINE ViT RUNE SOLVER - BACKGROUND TEST")
    print("  Test terhadap semua gambar rune di folder assets")
    print("=" * 60 + "\n")

    # Test 1: Panel template
    template_ok = test_panel_template_exists()
    if not template_ok:
        print("FATAL: rune_panel_template.png tidak ditemukan. Solver tidak bisa berjalan.")
        sys.exit(1)

    # Initialize solver
    print("Memuat ViT Solver...")
    try:
        solver = ViTSolver()
        print(f"  Model loaded: ✅\n")
    except Exception as e:
        print(f"  ❌ GAGAL memuat model: {e}")
        sys.exit(1)

    # Find all rune test images
    test_images = []
    assets_dir = "assets"
    for fn in sorted(os.listdir(assets_dir)):
        if fn.lower().startswith("rune") and fn.lower().endswith((".png", ".jpg")):
            # Skip small templates
            fpath = os.path.join(assets_dir, fn)
            fsize = os.path.getsize(fpath)
            if fsize > 5000:  # Only test actual screenshots, not tiny templates
                test_images.append(fpath)

    # Also check for runefull.jpg
    runefull = os.path.join(assets_dir, "runefull.jpg")
    if os.path.exists(runefull) and runefull not in test_images:
        test_images.append(runefull)

    print(f"Ditemukan {len(test_images)} gambar rune untuk ditest:")
    for ti in test_images:
        sz = os.path.getsize(ti)
        print(f"  - {ti} ({sz:,} bytes)")
    print()

    # Run tests
    results = []
    for idx, img_path in enumerate(test_images):
        ok = test_rune_image(img_path, solver, idx)
        results.append((img_path, ok))

    # Summary
    print("\n" + "=" * 60)
    print("  RINGKASAN HASIL TEST")
    print("=" * 60)
    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    for img_path, ok in results:
        status = "✅ LULUS" if ok else "❌ GAGAL"
        print(f"  {status}  {os.path.basename(img_path)}")
    print(f"\nTotal: {passed}/{total} lulus")

    if passed == total:
        print("\n🎉 Semua test LULUS! Latar belakang terdeteksi dengan benar.")
    else:
        print(f"\n⚠️ {total - passed} test GAGAL. Cek debug images untuk detail.")


if __name__ == "__main__":
    main()
