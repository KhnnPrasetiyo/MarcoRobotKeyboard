"""TODO: module documentation"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from app.tabs.validator import validate_profile


class ProfileManagerTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection, on_profile_loaded_callback):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection
        self.on_profile_loaded = on_profile_loaded_callback

        self.columnconfigure(0, weight=3)  # JSON editor - wider
        self.columnconfigure(1, weight=2)  # Control panel
        self.rowconfigure(0, weight=1)

        # ─────────────────────────────────────────────
        # LEFT: JSON Editor Terminal
        # ─────────────────────────────────────────────
        left_card = ttk.LabelFrame(self, text=" 📄 Editor Profil (JSON) ", padding=15)
        left_card.grid(row=0, column=0, padx=(40, 10), pady=40, sticky="nsew")
        left_card.columnconfigure(0, weight=1)
        left_card.rowconfigure(0, weight=1)

        # Terminal Container (macOS styled)
        term_editor = tk.Frame(
            left_card,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
            highlightcolor="#47475c",
        )
        term_editor.grid(row=0, column=0, sticky="nsew")
        term_editor.columnconfigure(0, weight=1)
        term_editor.rowconfigure(1, weight=1)

        # Terminal Header Bar
        hdr_editor = tk.Frame(term_editor, bg="#1b1b26", height=32)
        hdr_editor.grid(row=0, column=0, sticky="ew")
        hdr_editor.columnconfigure(2, weight=1)

        dots_e = tk.Frame(hdr_editor, bg="#1b1b26")
        dots_e.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(dots_e, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 10, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots_e, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 10, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots_e, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 10, "bold")).pack(
            side="left", padx=2
        )

        tk.Label(
            hdr_editor,
            text="profile.json — editor@kbd-robot",
            font=("Consolas", 8, "bold"),
            fg="#94a3b8",
            bg="#1b1b26",
        ).grid(row=0, column=1, padx=(5, 10), pady=5, sticky="w")

        # Editor action buttons (top-right of header)
        hdr_btn_frame = tk.Frame(hdr_editor, bg="#1b1b26")
        hdr_btn_frame.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        btn_refresh_json = tk.Button(
            hdr_btn_frame,
            text="🔃 Segarkan",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.reload_from_profile,
            padx=8,
        )
        btn_refresh_json.pack(side="left", padx=3)
        btn_refresh_json.bind(
            "<Enter>", lambda e: btn_refresh_json.config(bg="#47475c", fg="white")
        )
        btn_refresh_json.bind(
            "<Leave>", lambda e: btn_refresh_json.config(bg="#272736", fg="#cbd5e1")
        )

        btn_copy_json = tk.Button(
            hdr_btn_frame,
            text="📋 Salin",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.copy_json,
            padx=8,
        )
        btn_copy_json.pack(side="left", padx=3)
        btn_copy_json.bind("<Enter>", lambda e: btn_copy_json.config(bg="#47475c", fg="white"))
        btn_copy_json.bind("<Leave>", lambda e: btn_copy_json.config(bg="#272736", fg="#cbd5e1"))

        # Text area with scrollbars
        text_container = tk.Frame(term_editor, bg="#13131c")
        text_container.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        text_container.columnconfigure(0, weight=1)
        text_container.rowconfigure(0, weight=1)

        self.json_text = tk.Text(
            text_container,
            bg="#13131c",
            fg="#e2e8f0",
            font=("Consolas", 10),
            wrap="none",
            bd=0,
            padx=12,
            pady=12,
            spacing1=2,
            spacing2=1,
            spacing3=2,
            selectbackground="#47475c",
            selectforeground="#ffffff",
            insertbackground="#4ade80",
        )
        self.json_text.grid(row=0, column=0, sticky="nsew")

        sb_y = ttk.Scrollbar(text_container, orient="vertical", command=self.json_text.yview)
        sb_y.grid(row=0, column=1, sticky="ns")
        sb_x = ttk.Scrollbar(text_container, orient="horizontal", command=self.json_text.xview)
        sb_x.grid(row=1, column=0, sticky="ew")
        self.json_text.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)

        # ─────────────────────────────────────────────
        # RIGHT: Control Panel
        # ─────────────────────────────────────────────
        right_card = ttk.LabelFrame(self, text=" 🎛️ Panel Kontrol Profil ", padding=20)
        right_card.grid(row=0, column=1, padx=(10, 40), pady=40, sticky="nsew")
        right_card.columnconfigure(0, weight=1)
        right_card.rowconfigure(5, weight=1)

        # Description
        desc = tk.Label(
            right_card,
            text="Kelola, simpan, dan sinkronisasi konfigurasi\nrobot antar komputer & perangkat keras.",
            font=("Segoe UI", 9),
            fg="#94a3b8",
            bg="#1a1a24",
            justify="left",
            anchor="w",
        )
        desc.grid(row=0, column=0, sticky="w", pady=(0, 15))

        # ── Section: PC File Operations ──
        tk.Label(
            right_card,
            text="💻  BERKAS KOMPUTER",
            font=("Segoe UI", 8, "bold"),
            fg="#64748b",
            bg="#1a1a24",
            anchor="w",
        ).grid(row=1, column=0, sticky="w", pady=(5, 4))

        pc_frame = ttk.Frame(right_card)
        pc_frame.grid(row=2, column=0, sticky="ew", pady=(0, 12))
        pc_frame.columnconfigure(0, weight=1)
        pc_frame.columnconfigure(1, weight=1)

        self.btn_import = tk.Button(
            pc_frame,
            text="📂 IMPORT\nDARI PC (.JSON)",
            font=("Segoe UI", 9, "bold"),
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            relief="flat",
            bd=0,
            height=3,
            cursor="hand2",
            command=self.import_json,
        )
        self.btn_import.grid(row=0, column=0, padx=(0, 4), sticky="ew")
        self.btn_import.bind("<Enter>", lambda e: self.btn_import.config(bg="#ff9ff3"))
        self.btn_import.bind("<Leave>", lambda e: self.btn_import.config(bg="#ff75a0"))

        self.btn_export = tk.Button(
            pc_frame,
            text="💾 EXPORT\nKE PC (.JSON)",
            font=("Segoe UI", 9, "bold"),
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            relief="flat",
            bd=0,
            height=3,
            cursor="hand2",
            command=self.export_json,
        )
        self.btn_export.grid(row=0, column=1, padx=(4, 0), sticky="ew")
        self.btn_export.bind("<Enter>", lambda e: self.btn_export.config(bg="#26af5f"))
        self.btn_export.bind("<Leave>", lambda e: self.btn_export.config(bg="#2ed573"))

        # ── Section: Arduino EEPROM Operations ──
        tk.Label(
            right_card,
            text="🔌  ARDUINO EEPROM",
            font=("Segoe UI", 8, "bold"),
            fg="#64748b",
            bg="#1a1a24",
            anchor="w",
        ).grid(row=3, column=0, sticky="w", pady=(5, 4))

        hw_frame = ttk.Frame(right_card)
        hw_frame.grid(row=4, column=0, sticky="ew", pady=(0, 12))
        hw_frame.columnconfigure(0, weight=1)
        hw_frame.columnconfigure(1, weight=1)

        self.btn_read_arduino = tk.Button(
            hw_frame,
            text="📥 LOAD\nDARI ARDUINO",
            font=("Segoe UI", 9, "bold"),
            bg="#0abde3",
            fg="white",
            activebackground="#48dbfb",
            relief="flat",
            bd=0,
            height=3,
            cursor="hand2",
            command=self.read_config,
        )
        self.btn_read_arduino.grid(row=0, column=0, padx=(0, 4), sticky="ew")
        self.btn_read_arduino.bind("<Enter>", lambda e: self.btn_read_arduino.config(bg="#48dbfb"))
        self.btn_read_arduino.bind("<Leave>", lambda e: self.btn_read_arduino.config(bg="#0abde3"))

        self.btn_upload_arduino = tk.Button(
            hw_frame,
            text="📤 UPLOAD\nKE ARDUINO",
            font=("Segoe UI", 9, "bold"),
            bg="#dec0f1",
            fg="white",
            activebackground="#ffb142",
            relief="flat",
            bd=0,
            height=3,
            cursor="hand2",
            command=self.upload_config,
        )
        self.btn_upload_arduino.grid(row=0, column=1, padx=(4, 0), sticky="ew")
        self.btn_upload_arduino.bind(
            "<Enter>", lambda e: self.btn_upload_arduino.config(bg="#ffb142")
        )
        self.btn_upload_arduino.bind(
            "<Leave>", lambda e: self.btn_upload_arduino.config(bg="#dec0f1")
        )

        # ── Apply JSON button ──
        self.btn_load = tk.Button(
            right_card,
            text="🚀  TERAPKAN EDIT JSON KE PROFIL AKTIF",
            font=("Segoe UI", 9, "bold"),
            bg="#5f27cd",
            fg="white",
            activebackground="#6c5ce7",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.apply_json_preview,
        )
        self.btn_load.grid(row=5, column=0, sticky="sew", pady=(0, 12))
        self.btn_load.bind("<Enter>", lambda e: self.btn_load.config(bg="#6c5ce7"))
        self.btn_load.bind("<Leave>", lambda e: self.btn_load.config(bg="#5f27cd"))

        # ── Activity Log Terminal ──
        tk.Label(
            right_card,
            text="📋  LOG AKTIVITAS",
            font=("Segoe UI", 8, "bold"),
            fg="#64748b",
            bg="#1a1a24",
            anchor="w",
        ).grid(row=6, column=0, sticky="w", pady=(8, 4))

        log_term = tk.Frame(
            right_card,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
            highlightcolor="#47475c",
        )
        log_term.grid(row=7, column=0, sticky="nsew")
        right_card.rowconfigure(7, weight=1)
        log_term.columnconfigure(0, weight=1)
        log_term.rowconfigure(1, weight=1)

        # Log terminal header
        hdr_log = tk.Frame(log_term, bg="#1b1b26", height=28)
        hdr_log.grid(row=0, column=0, sticky="ew")
        hdr_log.columnconfigure(2, weight=1)

        dots_l = tk.Frame(hdr_log, bg="#1b1b26")
        dots_l.grid(row=0, column=0, padx=8, pady=4, sticky="w")
        tk.Label(dots_l, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 9, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots_l, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 9, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots_l, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 9, "bold")).pack(
            side="left", padx=2
        )

        tk.Label(
            hdr_log,
            text="bash - profiles@kbd-robot",
            font=("Consolas", 8, "bold"),
            fg="#94a3b8",
            bg="#1b1b26",
        ).grid(row=0, column=1, padx=(5, 8), pady=4, sticky="w")

        # Clear log button
        hdr_log_btns = tk.Frame(hdr_log, bg="#1b1b26")
        hdr_log_btns.grid(row=0, column=3, padx=8, pady=4, sticky="e")

        btn_clear_log = tk.Button(
            hdr_log_btns,
            text="🗑️ Hapus",
            font=("Segoe UI", 7, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#ef4444",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.clear_log,
            padx=6,
        )
        btn_clear_log.pack(side="left", padx=2)
        btn_clear_log.bind("<Enter>", lambda e: btn_clear_log.config(bg="#ef4444", fg="white"))
        btn_clear_log.bind("<Leave>", lambda e: btn_clear_log.config(bg="#272736", fg="#cbd5e1"))

        # Log text area
        log_text_wrap = tk.Frame(log_term, bg="#13131c")
        log_text_wrap.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        log_text_wrap.columnconfigure(0, weight=1)
        log_text_wrap.rowconfigure(0, weight=1)

        self.activity_log = tk.Text(
            log_text_wrap,
            bg="#13131c",
            fg="#e2e8f0",
            font=("Consolas", 9),
            wrap="word",
            bd=0,
            height=6,
            padx=10,
            pady=8,
            spacing1=2,
            spacing2=1,
            spacing3=2,
            selectbackground="#47475c",
            selectforeground="#ffffff",
            insertbackground="#ffffff",
        )
        self.activity_log.grid(row=0, column=0, sticky="nsew")

        sb_log = ttk.Scrollbar(log_text_wrap, orient="vertical", command=self.activity_log.yview)
        sb_log.grid(row=0, column=1, sticky="ns")
        self.activity_log.configure(yscrollcommand=sb_log.set)

        self.activity_log.tag_config("timestamp", foreground="#64748b")
        self.activity_log.tag_config("info", foreground="#38bdf8")
        self.activity_log.tag_config("success", foreground="#4ade80")
        self.activity_log.tag_config("error", foreground="#f87171")
        self.activity_log.tag_config("warning", foreground="#dec0f1")
        self.activity_log.config(state="disabled")

        # Operation status label (below log)
        self.lbl_operation_status = ttk.Label(
            right_card, text="", font=("Segoe UI", 9, "bold"), foreground="#747d8c"
        )
        self.lbl_operation_status.grid(row=8, column=0, sticky="w", pady=(6, 0))

        # Load initial JSON
        self.reload_from_profile()
        self.log_activity("Manajer Profil siap.", "info")

    # ─────────────────────────────────────────────
    # Activity Log Helpers
    # ─────────────────────────────────────────────
    def log_activity(self, message, tag="info"):
        """TODO: add documentation"""
        import time

        t_str = time.strftime("%H:%M:%S")
        self.activity_log.config(state="normal")
        self.activity_log.insert(tk.END, f"[{t_str}] ", "timestamp")
        self.activity_log.insert(tk.END, f"{message}\n", tag)
        self.activity_log.see(tk.END)
        self.activity_log.config(state="disabled")

    def clear_log(self):
        """TODO: add documentation"""
        self.activity_log.config(state="normal")
        self.activity_log.delete("1.0", tk.END)
        self.activity_log.insert(tk.END, "=== LOG AKTIVITAS BERSIH ===\n", "timestamp")
        self.activity_log.config(state="disabled")

    # ─────────────────────────────────────────────
    # JSON Editor Helpers
    # ─────────────────────────────────────────────
    def reload_from_profile(self):
        """Penyelarasan teks JSON di editor dengan data profil aktif saat ini."""
        self.json_text.delete("1.0", tk.END)
        self.json_text.insert("1.0", self.profile.to_json())

    def copy_json(self):
        """TODO: add documentation"""
        self.clipboard_clear()
        self.clipboard_append(self.json_text.get("1.0", tk.END).strip())
        messagebox.showinfo("Sukses", "Isi editor JSON berhasil disalin ke clipboard!")

    # ─────────────────────────────────────────────
    # PC File Operations
    # ─────────────────────────────────────────────
    def export_json(self):
        """TODO: add documentation"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("File JSON", "*.json"), ("Semua File", "*.*")],
            title="Export Profil JSON",
        )
        if not file_path:
            return
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.profile.to_json())
            self.profile.file_path = file_path
            fname = os.path.basename(file_path)
            self.log_activity(f"Profil diexport ke: {fname}", "success")
            self.connection.log(f"Profil JSON diexport ke: {fname}")
            messagebox.showinfo("Berhasil", "Profil JSON berhasil diexport!")
        except Exception as e:
            print("Error occurred")
            self.log_activity(f"Gagal export: {str(e)}", "error")
            messagebox.showerror("Error", f"Gagal export profil JSON: {str(e)}")

    def import_json(self):
        """TODO: add documentation"""
        file_path = filedialog.askopenfilename(
            filetypes=[("File JSON", "*.json"), ("Semua File", "*.*")], title="Import Profil JSON"
        )
        if not file_path:
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json_str = f.read()
            self.profile.file_path = file_path
            self.json_text.delete("1.0", tk.END)
            self.json_text.insert("1.0", json_str)
            fname = os.path.basename(file_path)
            self.log_activity(f"Profil diimport dari: {fname}", "success")
            self.connection.log(f"Profil JSON diimport dari: {fname}")
            messagebox.showinfo(
                "Berhasil",
                "JSON berhasil diimport ke editor.\nKlik '🚀 TERAPKAN' untuk menerapkan.",
            )
        except Exception as e:
            print("Error occurred")
            self.log_activity(f"Gagal import: {str(e)}", "error")
            messagebox.showerror("Error", f"Gagal import JSON: {str(e)}")

    def apply_json_preview(self):
        """TODO: add documentation"""
        raw = self.json_text.get("1.0", "end-1c").strip()
        try:
            self.profile.load_from_json(raw)
            self.on_profile_loaded()
            self.log_activity("Profil JSON berhasil diterapkan ke memori aktif.", "success")
            messagebox.showinfo("Berhasil", "Profil JSON berhasil diterapkan!")
        except Exception as e:
            print("Error occurred")
            self.log_activity(f"Error parsing JSON: {str(e)}", "error")
            messagebox.showerror("Kesalahan JSON", f"Tidak dapat mengurai JSON: {str(e)}")

    # ─────────────────────────────────────────────
    # Arduino EEPROM Operations
    # ─────────────────────────────────────────────
    def upload_config(self):
        """TODO: add documentation"""
        if not self.connection.connected:
            self.log_activity("Harus terhubung ke port COM untuk upload profil.", "error")
            messagebox.showerror(
                "Error Koneksi", "Harus terhubung ke port COM untuk mengunggah profil."
            )
            return

        issues, warnings, _ = validate_profile(self.profile)

        if issues:
            error_msg = "Profil tidak dapat diunggah karena ditemukan kesalahan kritis:\n\n"
            for iss in issues:
                error_msg += f"• {iss}\n"
            error_msg += "\nPerbaiki kesalahan di atas terlebih dahulu, lalu coba lagi."
            self.log_activity(f"Upload dibatalkan: {len(issues)} kesalahan kritis.", "error")
            messagebox.showerror("Validasi Gagal", error_msg)
            return

        if warnings:
            warn_msg = "Ditemukan peringatan berikut:\n\n"
            for w in warnings:
                warn_msg += f"• {w}\n"
            warn_msg += "\nApakah Anda tetap ingin melanjutkan pengunggahan?"
            if not messagebox.askyesno("Peringatan Validasi", warn_msg, icon="warning"):
                self.log_activity("Upload dibatalkan oleh pengguna.", "warning")
                return

        if not messagebox.askyesno(
            "Konfirmasi Upload",
            "Data yang tersimpan di EEPROM Arduino akan ditimpa.\n"
            "Apakah Anda yakin ingin mengunggah profil aktif?",
        ):
            return

        self.log_activity("Memulai proses pengunggahan ke Arduino EEPROM...", "info")
        self.lbl_operation_status.config(
            text="⏳ Mengunggah profil ke Arduino...", foreground="#dec0f1"
        )

        if self.connection.upload_profile(self.profile):
            self.log_activity("Profil berhasil ditulis ke EEPROM Arduino!", "success")
            self.lbl_operation_status.config(
                text="✅ Profil berhasil ditulis ke EEPROM!", foreground="#2ed573"
            )
            messagebox.showinfo("Sukses", "Profil berhasil diunggah ke Arduino Nano!")
        else:
            self.log_activity("Gagal mengunggah profil ke EEPROM.", "error")
            self.lbl_operation_status.config(
                text="❌ Gagal mengunggah profil.", foreground="#ff4757"
            )
            messagebox.showerror("Gagal", "Gagal mengunggah profil ke Arduino Nano.")

    def read_config(self):
        """TODO: add documentation"""
        if not self.connection.connected:
            self.log_activity("Harus terhubung ke port COM untuk membaca EEPROM.", "error")
            messagebox.showerror(
                "Error Koneksi", "Harus terhubung ke port COM untuk membaca konfigurasi."
            )
            return

        if self.connection.simulation_mode:
            messagebox.showinfo(
                "Tidak Tersedia",
                "Pembacaan EEPROM tidak tersedia dalam mode simulasi.\n"
                "Hubungkan ke Arduino asli untuk menggunakan fitur ini.",
            )
            return

        if not messagebox.askyesno(
            "Konfirmasi Baca Konfigurasi",
            "Profil aktif di aplikasi akan ditimpa dengan data dari Arduino.\n"
            "Apakah Anda yakin ingin melanjutkan?",
        ):
            return

        self.log_activity("Mengirim perintah READ_CONFIG ke Arduino...", "info")
        self.lbl_operation_status.config(
            text="⏳ Menunggu respons dari Arduino...", foreground="#dec0f1"
        )

        if self.connection.request_config_read():
            self._poll_config_response(attempts=0)
        else:
            self.log_activity("Gagal mengirim perintah READ_CONFIG.", "error")
            self.lbl_operation_status.config(
                text="❌ Gagal mengirim perintah.", foreground="#ff4757"
            )

    def _poll_config_response(self, attempts):
        """TODO: add documentation"""
        if self.connection._pending_config_data is not None:
            hex_data = self.connection._pending_config_data
            self.connection._pending_config_data = None

            try:
                from app.connection import SerialConnectionManager

                SerialConnectionManager.parse_config_hex(hex_data, self.profile)
                self.log_activity(
                    f"Sinkronisasi berhasil: {len(self.profile.servos)} servo, "
                    f"{len(self.profile.pattern)} aksi dimuat.",
                    "success",
                )
                self.lbl_operation_status.config(
                    text=f"✅ Sinkronisasi Berhasil: {len(self.profile.servos)} servo, "
                    f"{len(self.profile.pattern)} aksi",
                    foreground="#2ed573",
                )
                self.on_profile_loaded()
                self.reload_from_profile()
                messagebox.showinfo("Sukses", "Profil berhasil diambil dan dimuat dari Arduino!")
            except Exception as e:
                print("Error occurred")
                self.log_activity(f"Gagal parse EEPROM: {str(e)}", "error")
                self.lbl_operation_status.config(
                    text=f"❌ Error parsing: {str(e)}", foreground="#ff4757"
                )
                messagebox.showerror("Error", f"Gagal mem-parsing data EEPROM:\n{str(e)}")

        elif attempts < 10:
            self.after(500, lambda: self._poll_config_response(attempts + 1))
        else:
            self.log_activity(
                "Timeout: Tidak ada respons CONFIG_DUMP dari Arduino (5 detik).", "error"
            )
            self.lbl_operation_status.config(
                text="❌ Timeout: Arduino tidak merespons.", foreground="#ff4757"
            )
            messagebox.showwarning(
                "Timeout",
                "Arduino tidak mengirimkan data konfigurasi dalam 5 detik.\n\n"
                "Pastikan firmware yang benar sudah ter-upload ke Arduino.",
            )

    # ─────────────────────────────────────────────
    # Legacy compatibility shims
    # ─────────────────────────────────────────────
    def save_profile(self):
        """TODO: add documentation"""
        self.export_json()

    def load_profile(self):
        """TODO: add documentation"""
        self.import_json()

    def toggle_json_preview(self):
        """TODO: add documentation"""
        pass

    def hide_json_preview(self):
        """TODO: add documentation"""
        pass
