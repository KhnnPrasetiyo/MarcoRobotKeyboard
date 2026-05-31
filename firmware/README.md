# Petunjuk Ekspor Firmware (.hex)

Agar aplikasi desktop dapat mengunggah *firmware* langsung ke Arduino Nano Anda tanpa perlu membuka Arduino IDE di kemudian hari, Anda perlu mengekspor hasil kompilasi *firmware* ini sekali saja ke folder `firmware/` ini.

### Cara Mengekspor dari Arduino IDE:

1. Buka berkas [firmware.ino](file:///c:/Users/Admin/Documents/App/NanoKeyboardConroller/firmware/firmware.ino) menggunakan **Arduino IDE**.
2. Pastikan papan (**Board**) telah diset ke **Arduino Nano** dan prosesor yang tepat (**ATmega328P** atau **ATmega328P (Old Bootloader)**) telah dipilih.
3. Di menu bagian atas Arduino IDE, pilih:
   * **Sketsa** -> **Ekspor Biner Terkompilasi** (Bahasa Indonesia)
   * *atau* **Sketch** -> **Export Compiled Binary** (Bahasa Inggris)
4. Arduino IDE akan melakukan kompilasi. Setelah selesai, direktori `firmware/` ini akan berisi berkas baru dengan ekstensi `.hex`, contohnya:
   * `firmware.ino.hex`
   * `firmware.ino.with_bootloader.hex`
5. Buka kembali aplikasi desktop Anda, masuk ke tab **Koneksi Serial**, klik tombol **🔄** (Segarkan) di bagian berkas firmware, pilih berkas `.hex` tersebut, dan tekan **⚡ FLASH FIRMWARE**.

---
*Catatan: Aplikasi desktop akan mendeteksi secara otomatis semua file berkas `.hex` yang berada di dalam folder `firmware/` ini.*
