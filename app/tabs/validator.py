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
            issues.append(f"KRITIS: Servo {i+1} ({s.name}) memiliki kalibrasi di luar batas (sudut harus 0-180°).")
            cal_pass = False
        elif abs(s.up_angle - s.press_angle) < 10:
            warnings.append(f"PERINGATAN: Sudut UP & PRESS Servo {i+1} ({s.name}) sangat dekat ({s.up_angle}° vs {s.press_angle}°). Pastikan penekanan tombol terjadi secara fisik.")
    
    if cal_pass:
        passes.append("✓ Pemeriksaan batas kalibrasi berhasil (Semua servo dipetakan antara 0-180°).")

    # 2. Verify Pattern not empty
    if not profile.pattern:
        issues.append("KRITIS: Pembuat Pola berisi 0 aksi. Arduino tidak memiliki apa pun untuk dijalankan!")
    else:
        # 2b. Verify pattern count within firmware limit
        if len(profile.pattern) > MAX_PATTERNS:
            issues.append(f"KRITIS: Jumlah aksi ({len(profile.pattern)}) melebihi batas firmware ({MAX_PATTERNS}). Kurangi jumlah aksi!")
        else:
            passes.append(f"✓ Pemeriksaan jumlah pola berhasil ({len(profile.pattern)}/{MAX_PATTERNS} aksi terprogram).")

        # 3. Verify action values
        invalid_actions = 0
        for idx, act in enumerate(profile.pattern):
            if act.action_type != "NONE" and act.press_duration < 50:
                issues.append(f"KRITIS: Aksi #{idx+1} ({act.action_type}) memiliki durasi tekan terlalu rendah ({act.press_duration}ms). Minimum adalah 50ms.")
                invalid_actions += 1
            if act.delay_duration < 0:
                issues.append(f"KRITIS: Jeda aksi #{idx+1} tidak boleh negatif.")
                invalid_actions += 1
        
        if invalid_actions == 0:
            passes.append("✓ Pemeriksaan durasi aksi berhasil (Semua jeda dan durasi tekan valid).")

    # 4. Loop validation
    if profile.loop_mode == "CUSTOM" and profile.loop_count <= 0:
        issues.append("KRITIS: Mode Loop adalah KUSTOM tetapi jumlah pengulangan kurang dari atau sama dengan 0.")
    else:
        passes.append(f"✓ Pemeriksaan perulangan berhasil (Mode {profile.loop_mode}).")

    # 5. Random Delay sanity check
    if profile.random_delay_enabled:
        if profile.random_delay_min > profile.random_delay_max:
            issues.append("KRITIS: Jeda Acak Minimum lebih besar dari Maksimum.")
        elif profile.random_delay_min == profile.random_delay_max:
            warnings.append("PERINGATAN: Jeda Acak Minimum sama dengan Maksimum. Pengacakan tidak akan berpengaruh.")
        else:
            passes.append(f"✓ Pemeriksaan batas jeda acak berhasil ({profile.random_delay_min}ms - {profile.random_delay_max}ms).")

    return issues, warnings, passes


class ValidatorTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        card = ttk.LabelFrame(self, text=" Validator Konfigurasi & Keselamatan ", padding=20)
        card.grid(row=0, column=0, padx=40, pady=40, sticky="n")

        self.btn_validate = tk.Button(card, text="🔍 JALANKAN DIAGNOSTIK & VALIDASI", bg="#3867d6", fg="white", 
                                     activebackground="#4b7bec", font=("Helvetica", 11, "bold"), relief="flat", bd=0, 
                                     height=2, command=self.run_validation)
        self.btn_validate.grid(row=0, column=0, columnspan=2, pady=15, sticky="ew")

        # Results area
        self.results_txt = tk.Text(card, bg="#1e272e", fg="#2ed573", font=("Consolas", 10), width=60, height=15, bd=0, wrap="word")
        self.results_txt.grid(row=1, column=0, columnspan=2, pady=10)

        self.run_validation()

    def run_validation(self):
        self.results_txt.config(state="normal")
        self.results_txt.delete("1.0", tk.END)

        issues, warnings, passes = validate_profile(self.profile)

        self.results_txt.insert(tk.END, "=== Memulai Diagnostik Verifikasi Profil ===\n\n")

        # Render output
        for p in passes:
            self.results_txt.insert(tk.END, f"[BERHASIL] {p}\n")
        
        if warnings:
            self.results_txt.insert(tk.END, "\n")
            for w in warnings:
                self.results_txt.insert(tk.END, f"[PERINGATAN] {w}\n", "warn")
                
        if issues:
            self.results_txt.insert(tk.END, "\n")
            for iss in issues:
                self.results_txt.insert(tk.END, f"[GAGAL] {iss}\n", "fail")

        # Status summary
        self.results_txt.insert(tk.END, "\n=== Ringkasan Diagnostik ===\n")
        if issues:
            self.results_txt.insert(tk.END, f"STATUS: GAGAL ({len(issues)} kesalahan kritis ditemukan. Pengunggahan dinonaktifkan sampai diperbaiki!)\n", "fail")
        else:
            self.results_txt.insert(tk.END, "STATUS: BERHASIL (Semua uji validasi lolos. Siap untuk diunggah!)\n", "success")

        # Tag formatting
        self.results_txt.tag_config("warn", foreground="#ffa502")
        self.results_txt.tag_config("fail", foreground="#ff4757")
        self.results_txt.tag_config("success", foreground="#2ed573")
        self.results_txt.config(state="disabled")
