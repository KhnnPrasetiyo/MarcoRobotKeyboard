import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.tabs.validator import validate_profile

class SerialManagerTab(ttk.Frame):
    def __init__(self, parent, profile, connection, on_connection_state_change):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection
        self.on_state_change = on_connection_state_change
        self._reload_callback = None  # Akan di-set oleh main.py

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # CARD 1: Pengaturan Koneksi Serial
        main_card = ttk.LabelFrame(self, text=" Pengaturan Koneksi Serial ", padding=20)
        main_card.grid(row=0, column=0, padx=(40, 20), pady=40, sticky="nsew")

        # Port selection
        ttk.Label(main_card, text="Port Serial COM:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
        self.port_var = tk.StringVar()
        self.port_combo = ttk.Combobox(main_card, textvariable=self.port_var, width=25, state="readonly")
        self.port_combo.grid(row=0, column=1, padx=10, pady=10)

        # Refresh button
        self.btn_refresh = tk.Button(main_card, text="🔄 Segarkan Port", font=("Helvetica", 9, "bold"),
                                     bg="#57606f", fg="white", activebackground="#747d8c", activeforeground="white",
                                     relief="flat", bd=0, cursor="hand2", command=self.refresh_ports, padx=10, pady=4)
        self.btn_refresh.grid(row=0, column=2, padx=5, pady=10)
        self.btn_refresh.bind("<Enter>", lambda e: self.btn_refresh.config(bg="#747d8c"))
        self.btn_refresh.bind("<Leave>", lambda e: self.btn_refresh.config(bg="#57606f"))

        # Baudrate selection
        ttk.Label(main_card, text="Baud Rate:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
        self.baud_var = tk.StringVar(value="115200")
        self.baud_combo = ttk.Combobox(main_card, textvariable=self.baud_var, values=["9600", "19200", "38400", "57600", "115200"], width=25, state="readonly")
        self.baud_combo.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        # Connect / Disconnect Buttons
        self.btn_connect = tk.Button(main_card, text="🔌 HUBUNGKAN PERANGKAT", bg="#2ed573", fg="white", 
                                     activebackground="#26af5f", font=("Helvetica", 11, "bold"), relief="flat", bd=0, 
                                     height=2, cursor="hand2", command=self.toggle_connect)
        self.btn_connect.grid(row=2, column=0, columnspan=3, pady=25, sticky="ew")
        self.btn_connect.bind("<Enter>", lambda e: self.btn_connect.config(bg="#26af5f") if not self.connection.connected else self.btn_connect.config(bg="#ff6b81"))
        self.btn_connect.bind("<Leave>", lambda e: self.btn_connect.config(bg="#2ed573") if not self.connection.connected else self.btn_connect.config(bg="#ff4757"))

        # Device upload/download card
        self.info_card = ttk.LabelFrame(main_card, text=" Perintah Cepat ", padding=10)
        self.info_card.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(10, 0))

        self.btn_upload = tk.Button(self.info_card, text="📤 Unggah Profil ke EEPROM", font=("Helvetica", 10, "bold"),
                                    bg="#3867d6", fg="white", activebackground="#4b7bec", activeforeground="white",
                                    relief="flat", bd=0, cursor="hand2", command=self.upload_config, pady=8)
        self.btn_upload.pack(fill="x", pady=5)
        self.btn_upload.bind("<Enter>", lambda e: self.btn_upload.config(bg="#4b7bec"))
        self.btn_upload.bind("<Leave>", lambda e: self.btn_upload.config(bg="#3867d6"))

        self.btn_read = tk.Button(self.info_card, text="📥 Baca Profil dari Arduino", font=("Helvetica", 10, "bold"),
                                  bg="#2ed573", fg="white", activebackground="#26af5f", activeforeground="white",
                                  relief="flat", bd=0, cursor="hand2", command=self.read_config, pady=8)
        self.btn_read.pack(fill="x", pady=5)
        self.btn_read.bind("<Enter>", lambda e: self.btn_read.config(bg="#26af5f"))
        self.btn_read.bind("<Leave>", lambda e: self.btn_read.config(bg="#2ed573"))

        # Status label untuk feedback operasi
        self.lbl_operation_status = ttk.Label(main_card, text="", font=("Helvetica", 9), foreground="#747d8c")
        self.lbl_operation_status.grid(row=4, column=0, columnspan=3, pady=(10, 0))

        # CARD 2: Unggah Firmware Arduino Nano (Tanpa IDE)
        fw_card = ttk.LabelFrame(self, text=" ⚡ Unggah Firmware Arduino Nano ", padding=20)
        fw_card.grid(row=0, column=1, padx=(20, 40), pady=40, sticky="nsew")
        fw_card.columnconfigure(1, weight=1)
        fw_card.rowconfigure(4, weight=1)

        # Tipe Bootloader
        ttk.Label(fw_card, text="Tipe Bootloader:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.bootloader_var = tk.StringVar(value="New Bootloader (115200)")
        self.bootloader_combo = ttk.Combobox(fw_card, textvariable=self.bootloader_var, values=["New Bootloader (115200)", "Old Bootloader (57600)"], state="readonly", width=25)
        self.bootloader_combo.grid(row=0, column=1, padx=(10, 0), pady=(0, 5), sticky="ew")

        # Berkas Firmware (.hex)
        ttk.Label(fw_card, text="Berkas Firmware (.hex):", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
        
        fw_select_frame = ttk.Frame(fw_card)
        fw_select_frame.grid(row=1, column=1, padx=(10, 0), pady=10, sticky="ew")
        fw_select_frame.columnconfigure(0, weight=1)
        
        self.hex_var = tk.StringVar()
        self.hex_combo = ttk.Combobox(fw_select_frame, textvariable=self.hex_var, state="readonly")
        self.hex_combo.grid(row=0, column=0, sticky="ew")
        
        self.btn_refresh_hex = tk.Button(fw_select_frame, text="🔄", font=("Helvetica", 9, "bold"),
                                         bg="#57606f", fg="white", activebackground="#747d8c", activeforeground="white",
                                         relief="flat", bd=0, cursor="hand2", command=self.refresh_hex_files, width=3)
        self.btn_refresh_hex.grid(row=0, column=1, padx=(5, 0))
        self.btn_refresh_hex.bind("<Enter>", lambda e: self.btn_refresh_hex.config(bg="#747d8c"))
        self.btn_refresh_hex.bind("<Leave>", lambda e: self.btn_refresh_hex.config(bg="#57606f"))

        # Tombol Flash
        self.btn_flash = tk.Button(fw_card, text="⚡ UNGGAH FIRMWARE (FLASH)", bg="#ffa502", fg="white", 
                                   activebackground="#ffb142", font=("Helvetica", 11, "bold"), relief="flat", bd=0, 
                                   height=2, cursor="hand2", command=self.start_firmware_flash)
        self.btn_flash.grid(row=2, column=0, columnspan=2, pady=15, sticky="ew")
        self.btn_flash.bind("<Enter>", lambda e: self.btn_flash.config(bg="#ffb142") if self.btn_flash["state"] == "normal" else None)
        self.btn_flash.bind("<Leave>", lambda e: self.btn_flash.config(bg="#ffa502") if self.btn_flash["state"] == "normal" else None)

        # Output Log / Konsol avrdude
        ttk.Label(fw_card, text="Log Aktivitas Pengunggahan:", font=("Helvetica", 9, "bold")).grid(row=3, column=0, columnspan=2, sticky="w", pady=(5, 2))
        
        self.fw_console = tk.Text(fw_card, bg="#1e272e", fg="#ffa502", font=("Consolas", 9), wrap="word", bd=0, height=8)
        self.fw_console.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.fw_console.config(state="disabled")

        self.refresh_ports()
        self.refresh_hex_files()

    def set_reload_callback(self, callback):
        """Set callback untuk reload semua tab setelah profil dibaca dari Arduino."""
        self._reload_callback = callback

    def refresh_ports(self):
        ports = self.connection.get_available_ports()
        self.port_combo['values'] = ports
        if ports:
            self.port_combo.current(0)

    def toggle_connect(self):
        if not self.connection.connected:
            port = self.port_var.get()
            baud = int(self.baud_var.get())
            if not port:
                return
            if self.connection.connect(port, baud):
                self.btn_connect.config(text="🔌 PUTUSKAN PERANGKAT", bg="#ff4757", activebackground="#ff6b81")
                self.on_state_change(True)
                
                # Sinkronisasi otomatis status & konfigurasi saat koneksi berhasil
                if port != "COM_SIMULATOR":
                    self.connection.send_command("STATUS")
                    self.auto_sync_config()
        else:
            self.connection.disconnect()
            self.btn_connect.config(text="🔌 HUBUNGKAN PERANGKAT", bg="#2ed573", activebackground="#26af5f")
            self.on_state_change(False)

    def upload_config(self):
        if not self.connection.connected:
            self.connection.log("Error: Harus terhubung ke port COM untuk mengunggah profil.")
            return
        
        # Jalankan validasi sebelum upload
        issues, warnings, _ = validate_profile(self.profile)
        
        # Jika ada kesalahan kritis, blokir upload
        if issues:
            error_msg = "Profil tidak dapat diunggah karena ditemukan kesalahan kritis:\n\n"
            for iss in issues:
                error_msg += f"• {iss}\n"
            error_msg += "\nPerbaiki kesalahan di atas terlebih dahulu, lalu coba lagi."
            messagebox.showerror("Validasi Gagal", error_msg)
            self.connection.log(f"Upload dibatalkan: {len(issues)} kesalahan kritis ditemukan.")
            return
        
        # Jika ada peringatan, tampilkan konfirmasi
        if warnings:
            warn_msg = "Ditemukan peringatan berikut:\n\n"
            for w in warnings:
                warn_msg += f"• {w}\n"
            warn_msg += "\nApakah Anda tetap ingin melanjutkan pengunggahan?"
            if not messagebox.askyesno("Peringatan Validasi", warn_msg, icon="warning"):
                self.connection.log("Upload dibatalkan oleh pengguna.")
                return
        
        # Konfirmasi akhir
        if not messagebox.askyesno("Konfirmasi Upload", 
                                    "Data yang tersimpan di EEPROM Arduino akan ditimpa.\n"
                                    "Apakah Anda yakin ingin mengunggah profil aktif?"):
            return
        
        self.connection.log("Memulai proses pengunggahan profil aktif...")
        if self.connection.upload_profile(self.profile):
            self.connection.log("Profil berhasil ditulis ke EEPROM!")
        else:
            self.connection.log("Gagal mengunggah profil.")

    def read_config(self):
        """Baca konfigurasi yang tersimpan di EEPROM Arduino."""
        if not self.connection.connected:
            self.connection.log("Error: Harus terhubung ke port COM untuk membaca konfigurasi.")
            return
        
        if self.connection.simulation_mode:
            messagebox.showinfo("Tidak Tersedia", 
                                "Pembacaan EEPROM tidak tersedia dalam mode simulasi.\n"
                                "Hubungkan ke Arduino asli untuk menggunakan fitur ini.")
            return

        # Konfirmasi — profil aktif akan ditimpa
        if not messagebox.askyesno("Konfirmasi Baca Konfigurasi",
                                    "Profil aktif di aplikasi akan ditimpa dengan data dari Arduino.\n"
                                    "Apakah Anda yakin ingin melanjutkan?"):
            return

        self.connection.log("Mengirim perintah READ_CONFIG ke Arduino...")
        self.lbl_operation_status.config(text="⏳ Menunggu respons dari Arduino...", foreground="#ffa502")
        
        if self.connection.request_config_read():
            # Poll untuk menunggu response CONFIG_DUMP (max 5 detik)
            self._poll_config_response(attempts=0)
        else:
            self.lbl_operation_status.config(text="❌ Gagal mengirim perintah.", foreground="#ff4757")

    def _poll_config_response(self, attempts):
        """Poll response CONFIG_DUMP dari Arduino, max 10 kali (5 detik)."""
        if self.connection._pending_config_data is not None:
            # Data diterima, parse ke profil
            hex_data = self.connection._pending_config_data
            self.connection._pending_config_data = None
            
            try:
                from app.connection import SerialConnectionManager
                SerialConnectionManager.parse_config_hex(hex_data, self.profile)
                self.connection.log(f"Konfigurasi berhasil dibaca dari Arduino! "
                                    f"({len(self.profile.pattern)} aksi ditemukan)")
                self.lbl_operation_status.config(
                    text=f"✅ Konfigurasi dibaca: {len(self.profile.servos)} servo, "
                         f"{len(self.profile.pattern)} aksi",
                    foreground="#2ed573"
                )
                # Reload semua tab UI
                if self._reload_callback:
                    self._reload_callback()
                messagebox.showinfo("Berhasil", 
                                    f"Konfigurasi berhasil dibaca dari EEPROM Arduino!\n\n"
                                    f"• {len(self.profile.pattern)} aksi ditemukan\n"
                                    f"• Mode loop: {self.profile.loop_mode}\n"
                                    f"• Random delay: {'Aktif' if self.profile.random_delay_enabled else 'Nonaktif'}")
            except Exception as e:
                self.connection.log(f"Error parsing konfigurasi: {str(e)}")
                self.lbl_operation_status.config(text=f"❌ Error parsing: {str(e)}", foreground="#ff4757")
                messagebox.showerror("Error", f"Gagal mem-parsing data EEPROM:\n{str(e)}")
        elif attempts < 10:
            # Coba lagi setelah 500ms (total max 5 detik)
            self.after(500, lambda: self._poll_config_response(attempts + 1))
        else:
            # Timeout
            self.connection.log("Timeout: Tidak ada respons CONFIG_DUMP dari Arduino dalam 5 detik.")
            self.lbl_operation_status.config(text="❌ Timeout: Arduino tidak merespons.", foreground="#ff4757")
            messagebox.showwarning("Timeout", 
                                    "Arduino tidak mengirimkan data konfigurasi dalam 5 detik.\n\n"
                                    "Pastikan firmware yang benar sudah ter-upload ke Arduino.")

    def refresh_hex_files(self):
        """Mencari berkas .hex di folder firmware/"""
        import os
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        firmware_dir = os.path.join(base_dir, "firmware")
        
        hex_files = []
        if os.path.exists(firmware_dir):
            for f in os.listdir(firmware_dir):
                if f.endswith(".hex"):
                    hex_files.append(f)
        
        if hex_files:
            self.hex_combo['values'] = hex_files
            self.hex_combo.current(0)
            self.btn_flash.config(state="normal", bg="#ffa502")
        else:
            self.hex_combo['values'] = ["[Tidak ada berkas .hex di folder firmware/]"]
            self.hex_combo.current(0)
            self.btn_flash.config(state="disabled", bg="#747d8c")

    def start_firmware_flash(self):
        """Memulai pengunggahan firmware menggunakan avrdude."""
        import os
        
        # 1. Ambil port
        port = self.port_var.get()
        if not port:
            messagebox.showerror("Error", "Harap pilih Port Serial COM terlebih dahulu.")
            return

        is_simulation = (port == "COM_SIMULATOR")

        # 2. Ambil baudrate
        bootloader_type = self.bootloader_var.get()
        if "Old" in bootloader_type:
            baudrate = 57600
        else:
            baudrate = 115200

        # 3. Ambil berkas hex
        selected_hex = self.hex_var.get()
        if not selected_hex or "Tidak ada" in selected_hex:
            messagebox.showerror("Error", "Harap pilih berkas .hex yang valid.")
            return

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        hex_path = os.path.join(base_dir, "firmware", selected_hex)

        # 4. Konfirmasi
        if is_simulation:
            confirm_msg = (
                f"Anda memilih port COM_SIMULATOR.\n\n"
                f"Aplikasi akan mensimulasikan proses flashing firmware '{selected_hex}' "
                f"dengan tipe bootloader {bootloader_type}.\n\n"
                "Apakah Anda yakin ingin memulai simulasi?"
            )
        else:
            confirm_msg = (
                f"Anda akan mengunggah firmware '{selected_hex}' ke Arduino Nano pada port {port}.\n\n"
                f"Tipe Bootloader: {bootloader_type}\n"
                f"Pastikan papan Arduino Nano Anda sudah terhubung via USB.\n\n"
                "Apakah Anda yakin ingin melanjutkan?"
            )
            
        if not messagebox.askyesno("Konfirmasi Flash Firmware", confirm_msg, icon="warning"):
            return

        # 5. Nonaktifkan kontrol selama flash
        self.btn_flash.config(state="disabled", text="⏳ FLASHING SEDANG BERJALAN...", bg="#747d8c")
        self.btn_connect.config(state="disabled")
        
        # Bersihkan log console
        self.fw_console.config(state="normal")
        self.fw_console.delete("1.0", tk.END)
        self.fw_console.insert(tk.END, "=== MEMULAI FLASHING FIRMWARE ===\n")
        self.fw_console.see(tk.END)
        self.fw_console.config(state="disabled")

        # 6. Jalankan flashing asinkron
        def log_cb(msg):
            self.fw_console.config(state="normal")
            self.fw_console.insert(tk.END, msg + "\n")
            self.fw_console.see(tk.END)
            self.fw_console.config(state="disabled")

        def completion_cb(success, msg):
            self.btn_flash.config(state="normal", text="⚡ UNGGAH FIRMWARE (FLASH)", bg="#ffa502")
            self.btn_connect.config(state="normal")
            
            # Jika saat ini koneksi serial dinonaktifkan dalam UI, pastikan tombol connect disesuaikan
            if not self.connection.connected:
                self.btn_connect.config(text="🔌 HUBUNGKAN PERANGKAT", bg="#2ed573", activebackground="#26af5f")
                self.on_state_change(False)
            
            if success:
                messagebox.showinfo("Sukses", "Firmware berhasil diunggah!\n\nSekarang Anda dapat menghubungkan kembali koneksi serial.")
            else:
                messagebox.showerror("Gagal", f"Proses flashing gagal:\n\n{msg}")

        # Jalankan
        self.connection.flash_firmware(
            port=port,
            baudrate=baudrate,
            hex_path=hex_path,
            log_callback=log_cb,
            completion_callback=completion_cb
        )

    def auto_sync_config(self):
        """Meminta konfigurasi secara otomatis di latar belakang."""
        self.connection.log("Memulai sinkronisasi konfigurasi otomatis...")
        self.lbl_operation_status.config(text="⏳ Sinkronisasi otomatis...", foreground="#ffa502")
        
        # Reset data tunda
        self.connection._pending_config_data = None
        
        if self.connection.request_config_read():
            # Mulai polling asinkron senyap
            self._poll_config_response_auto(attempts=0)
        else:
            self.lbl_operation_status.config(text="❌ Gagal kirim perintah sinkronisasi.", foreground="#ff4757")

    def _poll_config_response_auto(self, attempts):
        """Poll respon CONFIG_DUMP secara senyap di latar belakang, tanpa memicu popup."""
        if self.connection._pending_config_data is not None:
            hex_data = self.connection._pending_config_data
            self.connection._pending_config_data = None
            
            try:
                from app.connection import SerialConnectionManager
                SerialConnectionManager.parse_config_hex(hex_data, self.profile)
                self.connection.log("Pengaturan berhasil disinkronkan dari Arduino secara otomatis!")
                self.lbl_operation_status.config(
                    text=f"✅ Sinkronisasi Berhasil: {len(self.profile.servos)} servo, "
                         f"{len(self.profile.pattern)} aksi",
                    foreground="#2ed573"
                )
                # Sinkronkan UI ke semua tab
                if self._reload_callback:
                    self._reload_callback()
            except Exception as e:
                self.connection.log(f"Gagal mem-parse konfigurasi otomatis: {str(e)}")
                self.lbl_operation_status.config(text=f"❌ Error parsing: {str(e)}", foreground="#ff4757")
        elif attempts < 10:
            # Coba lagi setelah 500ms
            self.after(500, lambda: self._poll_config_response_auto(attempts + 1))
        else:
            # Timeout senyap
            self.connection.log("Sinkronisasi Otomatis: Timeout (Tidak ada respons CONFIG_DUMP dari Arduino).")
            self.lbl_operation_status.config(text="⚠️ Timeout Sinkronisasi Otomatis.", foreground="#ffa502")
