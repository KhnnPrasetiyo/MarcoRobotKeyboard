"""TODO: module documentation"""

import os
import shutil

from PIL import Image, ImageEnhance


def setup_wallpaper():
    """TODO: add documentation"""
    src_path = r"C:\Users\Admin\Pictures\download (1).jpg"
    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    dst_original = os.path.join(assets_dir, "wibu_wallpaper_original.jpg")
    dst_optimized = os.path.join(assets_dir, "wibu_wallpaper.jpg")

    print("Mengecek gambar sumber...")
    if not os.path.exists(src_path):
        print(f"ERROR: Gambar sumber tidak ditemukan di {src_path}")
        return False

    try:
        # 1. Salin file original
        shutil.copy(src_path, dst_original)
        print(f"Pola asli disalin ke: {dst_original}")

        # 2. Proses dan optimalkan untuk performa & kontras
        img = Image.open(src_path)
        print(f"Resolusi asli: {img.size}")

        # Downscale jika lebih besar dari 1920px lebar
        max_width = 1920
        if img.size[0] > max_width:
            w_percent = max_width / float(img.size[0])
            h_size = int((float(img.size[1]) * float(w_percent)))
            img = img.resize((max_width, h_size), Image.Resampling.LANCZOS)
            print(f"Diturunkan resolusinya ke: {img.size}")

        # Redupkan kecerahan (0.20) agar teks putih/pink kontras
        enhancer = ImageEnhance.Brightness(img)
        img_darkened = enhancer.enhance(0.20)

        # Simpan versi teroptimasi
        img_darkened.save(dst_optimized, "JPEG", quality=85)
        print(f"Wallpaper teroptimasi disimpan ke: {dst_optimized}")
        return True

    except Exception as e:
        print(f"ERROR saat memproses wallpaper: {e}")
        return False


if __name__ == "__main__":
    setup_wallpaper()
