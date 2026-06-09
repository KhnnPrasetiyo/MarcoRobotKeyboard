"""TODO: module documentation"""

import tkinter as tk
from tkinter import ttk

MAX_PATTERNS = 150  # Must match firmware MAX_PATTERNS


def validate_profile(profile):
    """
    Validates a RobotProfile and returns (issues, warnings, passes).
    Can be called without any UI context.
    """
    issues = []
    warnings = []
    passes = []

    # 1. Verify Calibration Complete
    cal_pass = True
    for i, s in enumerate(profile.servos):
        if s.up_angle < 0 or s.up_angle > 180 or s.press_angle < 0 or s.press_angle > 180:
            issues.append(
                f"KRITIS: Servo {i+1} ({s.name}) memiliki kalibrasi di luar batas (sudut harus 0-180°)."
            )
            cal_pass = False
        elif s.up_angle == s.press_angle:
            issues.append(
                f"KRITIS: Sudut UP & PRESS Servo {i+1} ({s.name}) bernilai sama ({s.up_angle}°). Servo tidak akan bergerak secara fisik!"
            )
            cal_pass = False
        elif abs(s.up_angle - s.press_angle) < 10:
            warnings.append(
                f"PERINGATAN: Sudut UP & PRESS Servo {i+1} ({s.name}) sangat dekat ({s.up_angle}° vs {s.press_angle}°). Pastikan gerakan penekanan tombol dapat terjadi secara fisik."
            )

    if cal_pass:
        passes.append(
            "✓ Pemeriksaan batas kalibrasi berhasil (Semua servo terkalibrasi antara 0-180° dengan sudut gerak valid)."
        )

    # 2. Verify Pattern not empty
    if not profile.pattern:
        issues.append(
            "KRITIS: Pembuat Pola berisi 0 aksi. Arduino tidak memiliki apa pun untuk dijalankan!"
        )
    else:
        # Cek apakah pola HANYA berisi aksi "NONE" (tidak ada penekanan tombol fisik sama sekali)
        has_physical_action = any(act.action_type != "NONE" for act in profile.pattern)
        if not has_physical_action:
            issues.append(
                "KRITIS: Pola tidak berisi aksi tombol fisik sama sekali (semua aksi adalah 'NONE'). Robot tidak akan menekan tombol apa pun secara fisik! Tambahkan setidaknya satu aksi penekanan tombol aktif."
            )
        else:
            passes.append(
                f"✓ Pemeriksaan konten pola berhasil (Terdapat aksi tombol aktif terprogram)."
            )

        # 2b. Verify pattern count within firmware limit
        if len(profile.pattern) > MAX_PATTERNS:
            issues.append(
                f"KRITIS: Jumlah aksi ({len(profile.pattern)}) melebihi batas firmware ({MAX_PATTERNS}). Kurangi jumlah aksi!"
            )
        else:
            passes.append(
                f"✓ Pemeriksaan jumlah pola berhasil ({len(profile.pattern)}/{MAX_PATTERNS} aksi terprogram)."
            )

        # 3. Verify action values
        invalid_actions = 0
        for idx, act in enumerate(profile.pattern):
            if act.action_type != "NONE" and act.press_duration < 50:
                issues.append(
                    f"KRITIS: Aksi #{idx+1} ({act.action_type}) memiliki durasi tekan terlalu rendah ({act.press_duration}ms). Minimum adalah 50ms."
                )
                invalid_actions += 1
            if act.delay_duration < 0:
                issues.append(f"KRITIS: Jeda aksi #{idx+1} tidak boleh negatif.")
                invalid_actions += 1
            if act.press_duration > 15000:
                warnings.append(
                    f"PERINGATAN: Aksi #{idx+1} ({act.action_type}) memiliki durasi tekan sangat lama ({act.press_duration}ms). Pastikan ini disengaja."
                )
            if act.delay_duration > 60000:
                warnings.append(
                    f"PERINGATAN: Aksi #{idx+1} ({act.action_type}) memiliki durasi jeda sangat lama ({act.delay_duration}ms). Pastikan ini disengaja."
                )

        # Cek aksi NONE berurutan (redundansi)
        for idx in range(len(profile.pattern) - 1):
            if (
                profile.pattern[idx].action_type == "NONE"
                and profile.pattern[idx + 1].action_type == "NONE"
            ):
                warnings.append(
                    f"PERINGATAN: Ditemukan aksi 'NONE' berurutan pada langkah #{idx+1} dan #{idx+2}. Sebaiknya gabungkan durasinya menjadi satu aksi untuk menghemat EEPROM."
                )

        if invalid_actions == 0:
            passes.append(
                "✓ Pemeriksaan parameter durasi aksi berhasil (Semua nilai durasi valid)."
            )

    # 4. Loop validation
    if profile.loop_mode == "CUSTOM" and profile.loop_count <= 0:
        issues.append(
            "KRITIS: Mode Loop adalah KUSTOM tetapi jumlah pengulangan kurang dari atau sama dengan 0."
        )
    else:
        passes.append(f"✓ Pemeriksaan perulangan berhasil (Mode {profile.loop_mode}).")

    # 5. Random Delay sanity check
    if profile.random_delay_enabled:
        if profile.random_delay_min > profile.random_delay_max:
            issues.append("KRITIS: Jeda Acak Minimum lebih besar dari Maksimum.")
        elif profile.random_delay_min == profile.random_delay_max:
            warnings.append(
                "PERINGATAN: Jeda Acak Minimum sama dengan Maksimum. Pengacakan tidak akan berpengaruh."
            )
        else:
            passes.append(
                f"✓ Pemeriksaan batas jeda acak berhasil ({profile.random_delay_min}ms - {profile.random_delay_max}ms)."
            )

    return issues, warnings, passes


class ValidatorTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        card = ttk.LabelFrame(self, text=" Validator Konfigurasi & Keselamatan ", padding=20)
        card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        card.columnconfigure(0, weight=1)
        card.rowconfigure(1, weight=1)  # Area hasil diagnostik membesar dinamis

        self.btn_validate = tk.Button(
            card,
            text="🔍 JALANKAN DIAGNOSTIK & VALIDASI",
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.run_validation,
        )
        self.btn_validate.grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="ew")
        self.btn_validate.bind("<Enter>", lambda e: self.btn_validate.config(bg="#ff9ff3"))
        self.btn_validate.bind("<Leave>", lambda e: self.btn_validate.config(bg="#ff75a0"))

        # Results area (Premium macOS-styled Terminal)
        results_frame = ttk.Frame(card)
        results_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)

        # Terminal Container (slate border and dark bg)
        term_container = tk.Frame(
            results_frame,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
            highlightcolor="#47475c",
        )
        term_container.grid(row=0, column=0, sticky="nsew")
        term_container.columnconfigure(0, weight=1)
        term_container.rowconfigure(1, weight=1)

        # Terminal Header Bar (macOS style dots + title + actions)
        term_header = tk.Frame(term_container, bg="#1b1b26", height=32)
        term_header.grid(row=0, column=0, sticky="ew")
        term_header.columnconfigure(2, weight=1)  # spacer

        # macOS Dots
        dots_frame = tk.Frame(term_header, bg="#1b1b26")
        dots_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(
            dots_frame, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 10, "bold")
        ).pack(side="left", padx=2)
        tk.Label(
            dots_frame, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 10, "bold")
        ).pack(side="left", padx=2)
        tk.Label(
            dots_frame, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 10, "bold")
        ).pack(side="left", padx=2)

        # Title
        tk.Label(
            term_header,
            text="bash - validator@kbd-robot",
            font=("Consolas", 9, "bold"),
            fg="#94a3b8",
            bg="#1b1b26",
        ).grid(row=0, column=1, padx=(5, 10), pady=5, sticky="w")

        # Action Buttons frame on the right
        btn_frame = tk.Frame(term_header, bg="#1b1b26")
        btn_frame.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        btn_copy_log = tk.Button(
            btn_frame,
            text="📋 Salin",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.copy_log,
            padx=8,
        )
        btn_copy_log.pack(side="left", padx=3)
        btn_copy_log.bind("<Enter>", lambda e: btn_copy_log.config(bg="#47475c", fg="white"))
        btn_copy_log.bind("<Leave>", lambda e: btn_copy_log.config(bg="#272736", fg="#cbd5e1"))

        btn_clear_log = tk.Button(
            btn_frame,
            text="🗑️ Hapus",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#ef4444",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.clear_log,
            padx=8,
        )
        btn_clear_log.pack(side="left", padx=3)
        btn_clear_log.bind("<Enter>", lambda e: btn_clear_log.config(bg="#ef4444", fg="white"))
        btn_clear_log.bind("<Leave>", lambda e: btn_clear_log.config(bg="#272736", fg="#cbd5e1"))

        # Scrollable Text Area
        text_container = tk.Frame(term_container, bg="#13131c")
        text_container.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        text_container.columnconfigure(0, weight=1)
        text_container.rowconfigure(0, weight=1)

        self.results_txt = tk.Text(
            text_container,
            bg="#13131c",
            fg="#e2e8f0",
            font=("Consolas", 10),
            wrap="word",
            bd=0,
            padx=12,
            pady=12,
            spacing1=3,
            spacing2=1,
            spacing3=3,
            selectbackground="#47475c",
            selectforeground="#ffffff",
            insertbackground="#ffffff",
        )
        self.results_txt.grid(row=0, column=0, sticky="nsew")

        sb_log = ttk.Scrollbar(text_container, orient="vertical", command=self.results_txt.yview)
        sb_log.grid(row=0, column=1, sticky="ns")
        self.results_txt.configure(yscrollcommand=sb_log.set)

        self.run_validation()

    def clear_log(self):
        """Clears the diagnostics console logs."""
        self.results_txt.config(state="normal")
        self.results_txt.delete("1.0", tk.END)
        self.results_txt.insert(tk.END, "=== KONSOL DIAGNOSTIK KOSONG ===\n", "timestamp")
        self.results_txt.config(state="disabled")

    def copy_log(self):
        """Copies the diagnostics log content to the system clipboard."""
        self.clipboard_clear()
        log_content = self.results_txt.get("1.0", tk.END).strip()
        self.clipboard_append(log_content)
        from tkinter import messagebox

        messagebox.showinfo("Sukses", "Laporan diagnostik berhasil disalin ke clipboard!")

    def run_validation(self):
        """TODO: add documentation"""
        self.results_txt.config(state="normal")
        self.results_txt.delete("1.0", tk.END)

        issues, warnings, passes = validate_profile(self.profile)

        self.results_txt.insert(
            tk.END, "=== Memulai Diagnostik Verifikasi Profil ===\n\n", "timestamp"
        )

        # Render output
        for p in passes:
            self.results_txt.insert(tk.END, f"[BERHASIL] {p}\n", "success")

        if warnings:
            self.results_txt.insert(tk.END, "\n")
            for w in warnings:
                self.results_txt.insert(tk.END, f"[PERINGATAN] {w}\n", "warn")

        if issues:
            self.results_txt.insert(tk.END, "\n")
            for iss in issues:
                self.results_txt.insert(tk.END, f"[GAGAL] {iss}\n", "fail")

        # Status summary
        self.results_txt.insert(tk.END, "\n=== Ringkasan Diagnostik ===\n", "timestamp")
        if issues:
            self.results_txt.insert(
                tk.END,
                f"STATUS: GAGAL ({len(issues)} kesalahan kritis ditemukan. Pengunggahan dinonaktifkan sampai diperbaiki!)\n",
                "fail",
            )
        else:
            self.results_txt.insert(
                tk.END,
                "STATUS: BERHASIL (Semua uji validasi lolos. Siap untuk diunggah!)\n",
                "success",
            )

        # Tag formatting
        self.results_txt.tag_config("timestamp", foreground="#64748b")
        self.results_txt.tag_config("warn", foreground="#dec0f1")
        self.results_txt.tag_config("fail", foreground="#f87171")
        self.results_txt.tag_config("success", foreground="#4ade80")
        self.results_txt.config(state="disabled")
