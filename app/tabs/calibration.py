"""TODO: module documentation"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class CalibrationTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Main frame
        main_scroll = tk.Canvas(self, borderwidth=0, highlightthickness=0, bg="#1a1a24")
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=main_scroll.yview)

        scrollable_frame = ttk.Frame(main_scroll)

        scrollable_frame.bind(
            "<Configure>", lambda e: main_scroll.configure(scrollregion=main_scroll.bbox("all"))
        )

        canvas_window = main_scroll.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_scroll.configure(yscrollcommand=scrollbar.set)

        main_scroll.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        # Make scrollable frame stretch to canvas width on window resize
        main_scroll.bind(
            "<Configure>",
            lambda e: (
                main_scroll.itemconfigure(canvas_window, width=e.width),
                main_scroll.configure(scrollregion=main_scroll.bbox("all")),
            ),
        )

        # Add title and save controls in a header frame
        header_frame = ttk.Frame(scrollable_frame)
        header_frame.pack(fill="x", padx=5, pady=(10, 15))

        tk.Label(
            header_frame,
            text=" 🌸  Kalibrasi Sudut Servo ",
            font=("Segoe UI", 13, "bold"),
            fg="#ff75a0",
            bg="#1a1a24",
        ).pack(side="left", anchor="w")

        # Save profile button
        # Save profile button
        self.btn_save_profile = tk.Button(
            header_frame,
            text="💾 SAVE",
            font=("Segoe UI", 9, "bold"),
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.save_profile,
            padx=12,
            pady=6,
        )
        self.btn_save_profile.pack(side="right", padx=5)
        self.btn_save_profile.bind("<Enter>", lambda e: self.btn_save_profile.config(bg="#26af5f"))
        self.btn_save_profile.bind("<Leave>", lambda e: self.btn_save_profile.config(bg="#2ed573"))

        # Save profile as... button
        self.btn_save_profile_as = tk.Button(
            header_frame,
            text="💾 Simpan Sebagai...",
            font=("Segoe UI", 9, "bold"),
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.save_profile_as,
            padx=12,
            pady=6,
        )
        self.btn_save_profile_as.pack(side="right", padx=5)
        self.btn_save_profile_as.bind(
            "<Enter>", lambda e: self.btn_save_profile_as.config(bg="#ff9ff3")
        )
        self.btn_save_profile_as.bind(
            "<Leave>", lambda e: self.btn_save_profile_as.config(bg="#ff75a0")
        )

        # Profile path status label
        self.lbl_profile_path = tk.Label(
            header_frame,
            text="Berkas: Belum disimpan",
            font=("Segoe UI", 9, "italic"),
            fg="#94a3b8",
            bg="#1a1a24",
        )
        self.lbl_profile_path.pack(side="right", padx=15)

        # Grid container to hold 2 columns of servo cards
        grid_frame = ttk.Frame(scrollable_frame)
        grid_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Configure equal-width columns for grid
        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=1)

        # We have 6 servos
        self.servo_rows = []
        for i, servo in enumerate(self.profile.servos):
            row_idx = i // 2
            col_idx = i % 2

            card = ttk.LabelFrame(
                grid_frame, text=f" Servo {i+1}: {servo.name} (Pin D{servo.pin}) ", padding=15
            )
            card.grid(row=row_idx, column=col_idx, padx=8, pady=8, sticky="nsew")

            card.columnconfigure(1, weight=1)

            # --- ROW 0: Sudut UP ---
            tk.Label(
                card, text="Sudut UP (°):", font=("Segoe UI", 9, "bold"), fg="#94a3b8", bg="#1a1a24"
            ).grid(row=0, column=0, padx=5, pady=8, sticky="e")
            up_val = tk.IntVar(value=servo.up_angle)
            up_scale = ttk.Scale(card, from_=0, to=180, variable=up_val, orient="horizontal")
            up_scale.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

            # Decrement button
            btn_up_minus = tk.Button(
                card,
                text="−",
                font=("Segoe UI", 10, "bold"),
                bg="#272736",
                fg="#cbd5e1",
                activebackground="#47475c",
                activeforeground="white",
                relief="flat",
                bd=0,
                width=3,
                command=lambda v=up_val: v.set(max(0, v.get() - 1)),
            )
            btn_up_minus.grid(row=0, column=2, padx=2, pady=8)
            btn_up_minus.bind(
                "<Enter>", lambda e, b=btn_up_minus: b.config(bg="#47475c", fg="white")
            )
            btn_up_minus.bind(
                "<Leave>", lambda e, b=btn_up_minus: b.config(bg="#272736", fg="#cbd5e1")
            )

            up_lbl = tk.Label(
                card,
                text=str(servo.up_angle),
                width=5,
                font=("Consolas", 10, "bold"),
                fg="#4ade80",
                bg="#272736",
                anchor="center",
                relief="flat",
                padx=4,
            )
            up_lbl.grid(row=0, column=3, padx=5, pady=8)

            # Increment button
            btn_up_plus = tk.Button(
                card,
                text="+",
                font=("Segoe UI", 10, "bold"),
                bg="#272736",
                fg="#cbd5e1",
                activebackground="#47475c",
                activeforeground="white",
                relief="flat",
                bd=0,
                width=3,
                command=lambda v=up_val: v.set(min(180, v.get() + 1)),
            )
            btn_up_plus.grid(row=0, column=4, padx=2, pady=8)
            btn_up_plus.bind("<Enter>", lambda e, b=btn_up_plus: b.config(bg="#47475c", fg="white"))
            btn_up_plus.bind(
                "<Leave>", lambda e, b=btn_up_plus: b.config(bg="#272736", fg="#cbd5e1")
            )

            btn_test_up = tk.Button(
                card,
                text="Posisi UP",
                font=("Segoe UI", 9, "bold"),
                bg="#2ed573",
                fg="white",
                activebackground="#26af5f",
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda idx=i, v=up_val: self.test_angle(idx, v.get()),
                padx=10,
            )
            btn_test_up.grid(row=0, column=5, padx=10, pady=8)
            btn_test_up.bind("<Enter>", lambda e, b=btn_test_up: b.config(bg="#26af5f"))
            btn_test_up.bind("<Leave>", lambda e, b=btn_test_up: b.config(bg="#2ed573"))

            # Link scale motion to update label
            def make_up_callback(lbl, var, s_idx):
                """TODO: add documentation"""
                return lambda *args: (
                    lbl.config(text=str(var.get())),
                    self.update_profile_servo_angle(s_idx, "up", var.get()),
                )

            up_val.trace_add("write", make_up_callback(up_lbl, up_val, i))

            # --- ROW 1: Sudut PRESS ---
            tk.Label(
                card,
                text="Sudut PRESS (°):",
                font=("Segoe UI", 9, "bold"),
                fg="#94a3b8",
                bg="#1a1a24",
            ).grid(row=1, column=0, padx=5, pady=8, sticky="e")
            press_val = tk.IntVar(value=servo.press_angle)
            press_scale = ttk.Scale(card, from_=0, to=180, variable=press_val, orient="horizontal")
            press_scale.grid(row=1, column=1, padx=10, pady=8, sticky="ew")

            # Decrement button
            btn_press_minus = tk.Button(
                card,
                text="−",
                font=("Segoe UI", 10, "bold"),
                bg="#272736",
                fg="#cbd5e1",
                activebackground="#47475c",
                activeforeground="white",
                relief="flat",
                bd=0,
                width=3,
                command=lambda v=press_val: v.set(max(0, v.get() - 1)),
            )
            btn_press_minus.grid(row=1, column=2, padx=2, pady=8)
            btn_press_minus.bind(
                "<Enter>", lambda e, b=btn_press_minus: b.config(bg="#47475c", fg="white")
            )
            btn_press_minus.bind(
                "<Leave>", lambda e, b=btn_press_minus: b.config(bg="#272736", fg="#cbd5e1")
            )

            press_lbl = tk.Label(
                card,
                text=str(servo.press_angle),
                width=5,
                font=("Consolas", 10, "bold"),
                fg="#dec0f1",
                bg="#272736",
                anchor="center",
                relief="flat",
                padx=4,
            )
            press_lbl.grid(row=1, column=3, padx=5, pady=8)

            # Increment button
            btn_press_plus = tk.Button(
                card,
                text="+",
                font=("Segoe UI", 10, "bold"),
                bg="#272736",
                fg="#cbd5e1",
                activebackground="#47475c",
                activeforeground="white",
                relief="flat",
                bd=0,
                width=3,
                command=lambda v=press_val: v.set(min(180, v.get() + 1)),
            )
            btn_press_plus.grid(row=1, column=4, padx=2, pady=8)
            btn_press_plus.bind(
                "<Enter>", lambda e, b=btn_press_plus: b.config(bg="#47475c", fg="white")
            )
            btn_press_plus.bind(
                "<Leave>", lambda e, b=btn_press_plus: b.config(bg="#272736", fg="#cbd5e1")
            )

            btn_test_press = tk.Button(
                card,
                text="Posisi PRESS",
                font=("Segoe UI", 9, "bold"),
                bg="#dec0f1",
                fg="white",
                activebackground="#ffb142",
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda idx=i, v=press_val: self.test_angle(idx, v.get()),
                padx=10,
            )
            btn_test_press.grid(row=1, column=5, padx=10, pady=8)
            btn_test_press.bind("<Enter>", lambda e, b=btn_test_press: b.config(bg="#ffb142"))
            btn_test_press.bind("<Leave>", lambda e, b=btn_test_press: b.config(bg="#dec0f1"))

            def make_press_callback(lbl, var, s_idx):
                """TODO: add documentation"""
                return lambda *args: (
                    lbl.config(text=str(var.get())),
                    self.update_profile_servo_angle(s_idx, "press", var.get()),
                )

            press_val.trace_add("write", make_press_callback(press_lbl, press_val, i))

            # --- ROW 2: Wide Test sequence button ---
            btn_test = tk.Button(
                card,
                text="⚡ JALANKAN UJI TEKAN (PRESS & RELEASE SEQUENCE)",
                font=("Segoe UI", 9, "bold"),
                bg="#ff75a0",
                fg="white",
                activebackground="#ff9ff3",
                activeforeground="white",
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda idx=i, u=up_val, p=press_val: self.run_test_sequence(
                    idx, u.get(), p.get()
                ),
                pady=8,
            )
            btn_test.grid(row=2, column=1, columnspan=5, padx=10, pady=10, sticky="ew")
            btn_test.bind("<Enter>", lambda e, b=btn_test: b.config(bg="#ff9ff3"))
            btn_test.bind("<Leave>", lambda e, b=btn_test: b.config(bg="#ff75a0"))

            self.servo_rows.append({"up_val": up_val, "press_val": press_val})

    def update_profile_servo_angle(self, index, angle_type, val):
        """TODO: add documentation"""
        if angle_type == "up":
            self.profile.servos[index].up_angle = val
        else:
            self.profile.servos[index].press_angle = val

    def test_angle(self, index, angle):
        """TODO: add documentation"""
        # Arduino pins are defined. We send TEST_SERVO <index> <angle> command
        self.connection.send_command(f"TEST_SERVO {index} {angle}")

    def run_test_sequence(self, index, up_angle, press_angle):
        """TODO: add documentation"""
        self.connection.log(
            f"Mensimulasikan uji tekan untuk servo {index+1} ({self.profile.servos[index].name})..."
        )
        # Direct rapid tests
        self.test_angle(index, press_angle)
        self.after(250, lambda: self.test_angle(index, up_angle))

    def save_profile(self):
        """TODO: add documentation"""
        # Validasi hanya servos
        issues = []
        for i, s in enumerate(self.profile.servos):
            if s.up_angle < 0 or s.up_angle > 180 or s.press_angle < 0 or s.press_angle > 180:
                issues.append(f"Servo {i+1} ({s.name}) memiliki kalibrasi di luar batas 0-180°.")
            elif s.up_angle == s.press_angle:
                issues.append(
                    f"Sudut UP & PRESS Servo {i+1} ({s.name}) bernilai sama ({s.up_angle}°)."
                )

        if issues:
            error_msg = (
                "Konfigurasi kalibrasi memiliki kesalahan kritis dan tidak dapat disimpan:\n\n"
            )
            for iss in issues:
                error_msg += f"• {iss}\n"
            messagebox.showerror("Validasi Kalibrasi Gagal", error_msg)
            return

        import json
        import os

        # 1. Dapatkan JSON dasar yang akan diperbarui
        base_dict = None

        # Coba ambil dari Manajer Profil (editor text)
        try:
            top = self.winfo_toplevel()
            if hasattr(top, "pages") and "Manajer Profil" in top.pages:
                pm_tab = top.pages["Manajer Profil"]
                editor_text = pm_tab.json_text.get("1.0", "end-1c").strip()
                if editor_text:
                    base_dict = json.loads(editor_text)
        except Exception as e:
            print("Error occurred")
            base_dict = None

        file_path = getattr(self.profile, "file_path", None)

        # Jika gagal mengambil dari editor, coba ambil dari berkas di disk
        if not base_dict and file_path and os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    base_dict = json.loads(f.read())
            except Exception as e:
                print("Error occurred")
                base_dict = None

        # Jika masih tidak ada, buat dari self.profile saat ini
        if not base_dict:
            base_dict = self.profile.to_dict()

        # 2. Hanya perbarui bagian kalibrasi (servos) di base_dict
        base_dict["servos"] = [s.to_dict() for s in self.profile.servos]

        # 3. Konversi kembali ke format JSON string berinden
        updated_json_str = json.dumps(base_dict, indent=4)

        # 4. Terapkan JSON yang diperbarui ke self.profile di memori aktif
        try:
            self.profile.load_from_json(updated_json_str)
        except Exception as e:
            print("Error occurred")
            messagebox.showerror("Error", f"Gagal memuat profil setelah update kalibrasi: {str(e)}")
            return

        # 5. Simpan ke berkas fisik jika ada
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_json_str)
                fname = os.path.basename(file_path)
                self.connection.log(
                    f"[Kalibrasi] Kalibrasi servo berhasil disimpan ke berkas: {fname}"
                )
                self.lbl_profile_path.config(text=f"Berkas: {fname}")
            except Exception as e:
                print("Error occurred")
                messagebox.showerror("Error", f"Gagal menyimpan profil ke berkas: {str(e)}")
                return
        else:
            self.connection.log("[Kalibrasi] Kalibrasi servo berhasil diperbarui di memori aktif.")
            self.lbl_profile_path.config(text="Berkas: Memori Aktif")

        # 6. Pemicu sinkronisasi untuk memperbarui editor Manajer Profil dan tab lainnya
        if hasattr(self, "on_profile_updated") and self.on_profile_updated:
            self.on_profile_updated()

        messagebox.showinfo(
            "Berhasil",
            "Kalibrasi servo berhasil disimpan ke Manajer Profil (Editor) tanpa menimpa pola makro!",
        )

    def save_profile_as(self):
        """TODO: add documentation"""
        # Validasi hanya servos
        issues = []
        for i, s in enumerate(self.profile.servos):
            if s.up_angle < 0 or s.up_angle > 180 or s.press_angle < 0 or s.press_angle > 180:
                issues.append(f"Servo {i+1} ({s.name}) memiliki kalibrasi di luar batas 0-180°.")
            elif s.up_angle == s.press_angle:
                issues.append(
                    f"Sudut UP & PRESS Servo {i+1} ({s.name}) bernilai sama ({s.up_angle}°)."
                )

        if issues:
            error_msg = (
                "Konfigurasi kalibrasi memiliki kesalahan kritis dan tidak dapat disimpan:\n\n"
            )
            for iss in issues:
                error_msg += f"• {iss}\n"
            messagebox.showerror("Validasi Kalibrasi Gagal", error_msg)
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("File JSON", "*.json"), ("Semua File", "*.*")],
            title="Simpan Profil Sebagai",
        )
        if not file_path:
            return

        import json
        import os

        # Dapatkan JSON dasar yang akan diperbarui
        base_dict = None
        try:
            top = self.winfo_toplevel()
            if hasattr(top, "pages") and "Manajer Profil" in top.pages:
                pm_tab = top.pages["Manajer Profil"]
                editor_text = pm_tab.json_text.get("1.0", "end-1c").strip()
                if editor_text:
                    base_dict = json.loads(editor_text)
        except Exception as e:
            print("Error occurred")
            base_dict = None

        if not base_dict:
            # Coba dari file_path lama
            old_path = getattr(self.profile, "file_path", None)
            if old_path and os.path.exists(old_path):
                try:
                    with open(old_path, "r", encoding="utf-8") as f:
                        base_dict = json.loads(f.read())
                except Exception as e:
                    print("Error occurred")
                    base_dict = None

        if not base_dict:
            base_dict = self.profile.to_dict()

        # Hanya perbarui servos
        base_dict["servos"] = [s.to_dict() for s in self.profile.servos]
        updated_json_str = json.dumps(base_dict, indent=4)

        try:
            self.profile.load_from_json(updated_json_str)
        except Exception as e:
            print("Error occurred")
            messagebox.showerror("Error", f"Gagal memuat profil setelah update kalibrasi: {str(e)}")
            return

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_json_str)

            self.profile.file_path = file_path
            fname = os.path.basename(file_path)
            self.connection.log(f"[Kalibrasi] Profil disimpan sebagai: {fname}")

            # Update path label
            self.lbl_profile_path.config(text=f"Berkas: {fname}")

            # Sync other tabs
            if hasattr(self, "on_profile_updated") and self.on_profile_updated:
                self.on_profile_updated()

            messagebox.showinfo("Berhasil", f"Profil berhasil disimpan ke:\n{fname}")
        except Exception as e:
            print("Error occurred")
            messagebox.showerror("Error", f"Gagal menyimpan profil: {str(e)}")

    def reload_from_profile(self):
        """TODO: add documentation"""
        for i, servo in enumerate(self.profile.servos):
            self.servo_rows[i]["up_val"].set(servo.up_angle)
            self.servo_rows[i]["press_val"].set(servo.press_angle)

        # Update path label
        file_path = getattr(self.profile, "file_path", None)
        if file_path:
            fname = os.path.basename(file_path)
            self.lbl_profile_path.config(text=f"Berkas: {fname}")
        else:
            self.lbl_profile_path.config(text="Berkas: Belum disimpan")
