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
        self.rowconfigure(0, weight=1)

        main_card = ttk.LabelFrame(self, text=" Pengaturan Koneksi Serial ", padding=20)
        main_card.grid(row=0, column=0, padx=40, pady=40, sticky="n")

        # Port selection
        ttk.Label(main_card, text="Port Serial COM:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
        self.port_var = tk.StringVar()
        self.port_combo = ttk.Combobox(main_card, textvariable=self.port_var, width=25, state="readonly")
        self.port_combo.grid(row=0, column=1, padx=10, pady=10)

        # Refresh button
        self.btn_refresh = ttk.Button(main_card, text="🔄 Segarkan Port", command=self.refresh_ports)
        self.btn_refresh.grid(row=0, column=2, padx=5, pady=10)

        # Baudrate selection
        ttk.Label(main_card, text="Baud Rate:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
        self.baud_var = tk.StringVar(value="115200")
        self.baud_combo = ttk.Combobox(main_card, textvariable=self.baud_var, values=["9600", "19200", "38400", "57600", "115200"], width=25, state="readonly")
        self.baud_combo.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")

        # Connect / Disconnect Buttons
        self.btn_connect = tk.Button(main_card, text="🔌 HUBUNGKAN PERANGKAT", bg="#2ed573", fg="white", 
                                     activebackground="#26af5f", font=("Helvetica", 11, "bold"), relief="flat", bd=0, 
                                     height=2, command=self.toggle_connect)
        self.btn_connect.grid(row=2, column=0, columnspan=3, pady=25, sticky="ew")

        # Device upload/download card
        self.info_card = ttk.LabelFrame(main_card, text=" Perintah Cepat ", padding=10)
        self.info_card.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(10, 0))

        self.btn_upload = ttk.Button(self.info_card, text="📤 Unggah Profil Aktif ke EEPROM", command=self.upload_config)
        self.btn_upload.pack(fill="x", pady=5)

        self.btn_read = ttk.Button(self.info_card, text="📥 Baca Konfigurasi dari Arduino", command=self.read_config)
        self.btn_read.pack(fill="x", pady=5)

        # Status label untuk feedback operasi
        self.lbl_operation_status = ttk.Label(main_card, text="", font=("Helvetica", 9), foreground="#747d8c")
        self.lbl_operation_status.grid(row=4, column=0, columnspan=3, pady=(10, 0))

        self.refresh_ports()

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
