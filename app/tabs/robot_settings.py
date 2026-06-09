"""TODO: module documentation"""

import random
import time
import tkinter as tk
from tkinter import messagebox, ttk

from app.tabs.calibration import CalibrationTab
from app.tabs.validator import ValidatorTab


class TimingSettingsFrame(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        # Initialize shared variables first
        self.loop_mode_var = tk.StringVar(value=self.profile.loop_mode)
        self.loop_count_var = tk.IntVar(value=self.profile.loop_count)
        self.autostart_var = tk.BooleanVar(value=self.profile.auto_start)
        self.random_enabled_var = tk.BooleanVar(value=self.profile.random_delay_enabled)
        self.random_min_var = tk.IntVar(value=self.profile.random_delay_min)
        self.random_max_var = tk.IntVar(value=self.profile.random_delay_max)
        self.random_skip_var = tk.BooleanVar(value=self.profile.random_skip_enabled)
        self.blink_init_var = tk.IntVar(value=self.profile.blink_init_delay)
        self.blink_hold_var = tk.IntVar(value=self.profile.blink_hold_delay)
        self.blink_release_var = tk.IntVar(value=self.profile.blink_release_delay)

        # Setup write traces for real-time model sync and constraints
        self.loop_count_var.trace_add("write", self.on_loop_count_write)
        self.random_min_var.trace_add("write", self.on_random_min_write)
        self.random_max_var.trace_add("write", self.on_random_max_write)
        self.blink_init_var.trace_add("write", self.on_blink_init_write)
        self.blink_hold_var.trace_add("write", self.on_blink_hold_write)
        self.blink_release_var.trace_add("write", self.on_blink_release_write)

        # Layout Column: Left (Configuration Controls), Right (Simulation & Live Test)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Left scroll container
        left_container = ttk.Frame(self)
        left_container.grid(row=0, column=0, sticky="nsew", padx=(15, 10), pady=10)
        left_container.columnconfigure(0, weight=1)
        left_container.rowconfigure(0, weight=1)

        left_scroll = tk.Canvas(left_container, borderwidth=0, highlightthickness=0, bg="#1a1a24")
        scrollbar = ttk.Scrollbar(left_container, orient="vertical", command=left_scroll.yview)

        self.scrollable_left = ttk.Frame(left_scroll)
        self.scrollable_left.bind(
            "<Configure>", lambda e: left_scroll.configure(scrollregion=left_scroll.bbox("all"))
        )
        canvas_window = left_scroll.create_window((0, 0), window=self.scrollable_left, anchor="nw")
        left_scroll.configure(yscrollcommand=scrollbar.set)
        left_scroll.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.scrollable_left.columnconfigure(0, weight=1)

        # Make scrollable frame stretch to canvas width on window resize
        left_scroll.bind(
            "<Configure>",
            lambda e: (
                left_scroll.itemconfigure(canvas_window, width=e.width),
                left_scroll.configure(scrollregion=left_scroll.bbox("all")),
            ),
        )

        # --- Left Configuration Cards ---
        self.create_loop_card(self.scrollable_left)
        self.create_random_delay_card(self.scrollable_left)
        self.create_blink_timing_card(self.scrollable_left)

        # --- Right Card: Simulation & Testing console ---
        self.create_testing_card(self)

        # Sync visual states
        self.on_mode_change()
        self.on_toggle_random_enabled()
        self.update_blink_flow_label()

        # Initial synchronization of scales (since variables were set before traces were added)
        try:
            self.on_loop_count_write()
            self.on_random_min_write()
            self.on_random_max_write()
            self.on_blink_init_write()
            self.on_blink_hold_write()
            self.on_blink_release_write()
        except Exception as e:
            print("Error occurred")
            pass

    def on_scale_scroll(self, var, val):
        """TODO: add documentation"""
        try:
            var.set(int(float(val)))
        except (ValueError, tk.TclError):
            pass

    # --- Write Trace Callbacks for variables ---
    def on_loop_count_write(self, *args):
        """TODO: add documentation"""
        try:
            val = self.loop_count_var.get()
            default_min = 1
            default_max = 1000
            new_from = min(default_min, val)
            new_to = max(default_max, val)

            if (
                int(self.scale_loop.cget("from")) != new_from
                or int(self.scale_loop.cget("to")) != new_to
            ):
                self.scale_loop.config(from_=new_from, to=new_to)

            self.scale_loop.set(val)
            self.profile.loop_count = val
            if self.loop_mode_var.get() == "CUSTOM":
                self.status_badge.config(text=f"🔁 LOOP: {val} KALI", fg="#4ade80", bg="#1b3628")
        except tk.TclError:
            pass

    def on_random_min_write(self, *args):
        """TODO: add documentation"""
        try:
            val = self.random_min_var.get()
            default_min = 0
            default_max = 10000
            new_from = min(default_min, val)
            new_to = max(default_max, val)

            if (
                int(self.scale_random_min.cget("from")) != new_from
                or int(self.scale_random_min.cget("to")) != new_to
            ):
                self.scale_random_min.config(from_=new_from, to=new_to)

            self.scale_random_min.set(val)
            self.profile.random_delay_min = val

            # Ensure max is at least min
            if self.random_max_var.get() < val:
                self.random_max_var.set(val)
        except tk.TclError:
            pass

    def on_random_max_write(self, *args):
        """TODO: add documentation"""
        try:
            val = self.random_max_var.get()
            default_min = 0
            default_max = 10000
            new_from = min(default_min, val)
            new_to = max(default_max, val)

            if (
                int(self.scale_random_max.cget("from")) != new_from
                or int(self.scale_random_max.cget("to")) != new_to
            ):
                self.scale_random_max.config(from_=new_from, to=new_to)

            self.scale_random_max.set(val)

            min_val = self.random_min_var.get()
            if val < min_val:
                val = min_val
                self.random_max_var.set(min_val)
            self.profile.random_delay_max = val
        except tk.TclError:
            pass

    def on_blink_init_write(self, *args):
        """TODO: add documentation"""
        try:
            val = self.blink_init_var.get()
            default_min = 50
            default_max = 1000
            new_from = min(default_min, val)
            new_to = max(default_max, val)

            if (
                int(self.scale_blink_init.cget("from")) != new_from
                or int(self.scale_blink_init.cget("to")) != new_to
            ):
                self.scale_blink_init.config(from_=new_from, to=new_to)

            self.scale_blink_init.set(val)
            self.profile.blink_init_delay = val
            self.update_blink_flow_label()
        except tk.TclError:
            pass

    def on_blink_hold_write(self, *args):
        """TODO: add documentation"""
        try:
            val = self.blink_hold_var.get()
            default_min = 50
            default_max = 1000
            new_from = min(default_min, val)
            new_to = max(default_max, val)

            if (
                int(self.scale_blink_hold.cget("from")) != new_from
                or int(self.scale_blink_hold.cget("to")) != new_to
            ):
                self.scale_blink_hold.config(from_=new_from, to=new_to)

            self.scale_blink_hold.set(val)
            self.profile.blink_hold_delay = val
            self.update_blink_flow_label()
        except tk.TclError:
            pass

    def on_blink_release_write(self, *args):
        """TODO: add documentation"""
        try:
            val = self.blink_release_var.get()
            default_min = 50
            default_max = 1000
            new_from = min(default_min, val)
            new_to = max(default_max, val)

            if (
                int(self.scale_blink_release.cget("from")) != new_from
                or int(self.scale_blink_release.cget("to")) != new_to
            ):
                self.scale_blink_release.config(from_=new_from, to=new_to)

            self.scale_blink_release.set(val)
            self.profile.blink_release_delay = val
            self.update_blink_flow_label()
        except tk.TclError:
            pass

    # --- Card 1: Loop Config ---
    def create_loop_card(self, parent):
        """TODO: add documentation"""
        card = ttk.LabelFrame(parent, text=" 🔄 Konfigurasi Perulangan (Loop) ", padding=12)
        card.pack(fill="x", pady=6, padx=10)
        card.columnconfigure(0, weight=1)

        ttk.Label(card, text="Mode Perulangan:", font=("Helvetica", 9, "bold")).pack(
            anchor="w", pady=(2, 5)
        )

        rb_inf = tk.Radiobutton(
            card,
            text="Mode Tak Terbatas (Mengulang selamanya)",
            variable=self.loop_mode_var,
            value="INFINITY",
            command=self.on_mode_change,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 9),
        )
        rb_inf.pack(anchor="w", padx=5, pady=2)

        rb_cust = tk.Radiobutton(
            card,
            text="Mode Kustom Jumlah Perulangan",
            variable=self.loop_mode_var,
            value="CUSTOM",
            command=self.on_mode_change,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 9),
        )
        rb_cust.pack(anchor="w", padx=5, pady=2)

        self.lbl_loop_count = ttk.Label(
            card, text="Jumlah Perulangan Kustom:", font=("Helvetica", 8, "bold")
        )
        self.lbl_loop_count.pack(anchor="w", padx=5, pady=(8, 2))

        count_frame = ttk.Frame(card)
        count_frame.pack(fill="x", padx=5, pady=(2, 6))
        count_frame.columnconfigure(0, weight=1)

        self.scale_loop = tk.Scale(
            count_frame,
            from_=1,
            to=1000,
            orient="horizontal",
            showvalue=False,
            bd=0,
            bg="#1a1a24",
            highlightthickness=0,
            troughcolor="#13131c",
            activebackground="#ff75a0",
            cursor="hand2",
            command=lambda val: self.on_scale_scroll(self.loop_count_var, val),
        )
        self.scale_loop.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.count_spin = ttk.Spinbox(
            count_frame, from_=1, to=65535, increment=1, textvariable=self.loop_count_var, width=8
        )
        self.count_spin.grid(row=0, column=1, sticky="w")

        self.chk_autostart = tk.Checkbutton(
            card,
            text="Mulai otomatis (Auto Start) saat Arduino menyalakan",
            variable=self.autostart_var,
            command=self.on_autostart_change,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 9),
        )
        self.chk_autostart.pack(anchor="w", padx=5, pady=5)

    def on_mode_change(self):
        """TODO: add documentation"""
        mode = self.loop_mode_var.get()
        self.profile.loop_mode = mode
        if mode == "INFINITY":
            self.count_spin.config(state="disabled")
            self.scale_loop.config(state="disabled")
            self.lbl_loop_count.config(state="disabled")
            self.status_badge.config(text="🔁 LOOP: SELAMANYA", fg="#38bdf8", bg="#102e3b")
        else:
            self.count_spin.config(state="normal")
            self.scale_loop.config(state="active")
            self.lbl_loop_count.config(state="normal")
            self.status_badge.config(
                text=f"🔁 LOOP: {self.loop_count_var.get()} KALI", fg="#4ade80", bg="#1b3628"
            )

    def on_autostart_change(self):
        """TODO: add documentation"""
        self.profile.auto_start = self.autostart_var.get()

    # --- Card 2: Random Delays ---
    def create_random_delay_card(self, parent):
        """TODO: add documentation"""
        card = ttk.LabelFrame(parent, text=" 🛡️ Pengaturan Jeda Acak (Humanis) ", padding=12)
        card.pack(fill="x", pady=6, padx=10)
        card.columnconfigure(0, weight=1)

        self.chk_random = tk.Checkbutton(
            card,
            text="Aktifkan jeda acak di antara aksi",
            variable=self.random_enabled_var,
            command=self.on_toggle_random_enabled,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 9, "bold"),
        )
        self.chk_random.pack(anchor="w", pady=(2, 4))

        self.chk_random_skip = tk.Checkbutton(
            card,
            text="Aktifkan skip blink acak per loop (50% per loop, hanya BLINK)",
            variable=self.random_skip_var,
            command=self.on_toggle_random_skip,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 9, "bold"),
        )
        self.chk_random_skip.pack(anchor="w", pady=(0, 6))

        # Min delay
        self.lbl_rand_min = ttk.Label(
            card, text="Jeda Minimum (ms):", font=("Helvetica", 8, "bold")
        )
        self.lbl_rand_min.pack(anchor="w", padx=5, pady=(5, 1))

        min_frame = ttk.Frame(card)
        min_frame.pack(fill="x", padx=5, pady=2)
        min_frame.columnconfigure(0, weight=1)

        self.scale_random_min = tk.Scale(
            min_frame,
            from_=0,
            to=10000,
            orient="horizontal",
            showvalue=False,
            bd=0,
            bg="#1a1a24",
            highlightthickness=0,
            troughcolor="#13131c",
            activebackground="#ff75a0",
            cursor="hand2",
            command=lambda val: self.on_scale_scroll(self.random_min_var, val),
        )
        self.scale_random_min.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.spin_random_min = ttk.Spinbox(
            min_frame, from_=0, to=60000, increment=100, textvariable=self.random_min_var, width=8
        )
        self.spin_random_min.grid(row=0, column=1, sticky="w")

        # Max delay
        self.lbl_rand_max = ttk.Label(
            card, text="Jeda Maksimum (ms):", font=("Helvetica", 8, "bold")
        )
        self.lbl_rand_max.pack(anchor="w", padx=5, pady=(5, 1))

        max_frame = ttk.Frame(card)
        max_frame.pack(fill="x", padx=5, pady=2)
        max_frame.columnconfigure(0, weight=1)

        self.scale_random_max = tk.Scale(
            max_frame,
            from_=0,
            to=10000,
            orient="horizontal",
            showvalue=False,
            bd=0,
            bg="#1a1a24",
            highlightthickness=0,
            troughcolor="#13131c",
            activebackground="#ff75a0",
            cursor="hand2",
            command=lambda val: self.on_scale_scroll(self.random_max_var, val),
        )
        self.scale_random_max.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.spin_random_max = ttk.Spinbox(
            max_frame, from_=0, to=60000, increment=100, textvariable=self.random_max_var, width=8
        )
        self.spin_random_max.grid(row=0, column=1, sticky="w")

    def on_toggle_random_enabled(self):
        """TODO: add documentation"""
        enabled = self.random_enabled_var.get()
        self.profile.random_delay_enabled = enabled
        state = "normal" if enabled else "disabled"
        self.spin_random_min.config(state=state)
        self.spin_random_max.config(state=state)
        self.scale_random_min.config(state="active" if enabled else "disabled")
        self.scale_random_max.config(state="active" if enabled else "disabled")
        self.lbl_rand_min.config(state=state)
        self.lbl_rand_max.config(state=state)
        if enabled:
            self.random_badge.config(text="🛡️ JEDA ACAK: AKTIF", fg="#4ade80", bg="#1b3628")
        else:
            self.random_badge.config(text="🛡️ JEDA ACAK: NON-AKTIF", fg="#94a3b8", bg="#272736")

    def on_toggle_random_skip(self):
        """TODO: add documentation"""
        self.profile.random_skip_enabled = self.random_skip_var.get()

    # --- Card 3: Blink Timings ---
    def create_blink_timing_card(self, parent):
        """TODO: add documentation"""
        card = ttk.LabelFrame(parent, text=" ⚡ Konfigurasi Timing Blink Fisik ", padding=12)
        card.pack(fill="x", pady=6, padx=10)
        card.columnconfigure(0, weight=1)

        # 1. Blink Init
        ttk.Label(card, text="Jeda Arah -> Shift (ms):", font=("Helvetica", 8, "bold")).pack(
            anchor="w", padx=5, pady=(4, 1)
        )
        init_frame = ttk.Frame(card)
        init_frame.pack(fill="x", padx=5, pady=2)
        init_frame.columnconfigure(0, weight=1)

        self.scale_blink_init = tk.Scale(
            init_frame,
            from_=50,
            to=1000,
            orient="horizontal",
            showvalue=False,
            bd=0,
            bg="#1a1a24",
            highlightthickness=0,
            troughcolor="#13131c",
            activebackground="#ff75a0",
            cursor="hand2",
            command=lambda val: self.on_scale_scroll(self.blink_init_var, val),
        )
        self.scale_blink_init.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.spin_blink_init = ttk.Spinbox(
            init_frame, from_=0, to=5000, increment=10, textvariable=self.blink_init_var, width=8
        )
        self.spin_blink_init.grid(row=0, column=1, sticky="w")

        # 2. Blink Hold
        ttk.Label(card, text="Durasi Tekan Shift (ms):", font=("Helvetica", 8, "bold")).pack(
            anchor="w", padx=5, pady=(4, 1)
        )
        hold_frame = ttk.Frame(card)
        hold_frame.pack(fill="x", padx=5, pady=2)
        hold_frame.columnconfigure(0, weight=1)

        self.scale_blink_hold = tk.Scale(
            hold_frame,
            from_=50,
            to=1000,
            orient="horizontal",
            showvalue=False,
            bd=0,
            bg="#1a1a24",
            highlightthickness=0,
            troughcolor="#13131c",
            activebackground="#ff75a0",
            cursor="hand2",
            command=lambda val: self.on_scale_scroll(self.blink_hold_var, val),
        )
        self.scale_blink_hold.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.spin_blink_hold = ttk.Spinbox(
            hold_frame, from_=0, to=5000, increment=10, textvariable=self.blink_hold_var, width=8
        )
        self.spin_blink_hold.grid(row=0, column=1, sticky="w")

        # 3. Blink Release
        ttk.Label(card, text="Jeda Lepas Shift -> Arah (ms):", font=("Helvetica", 8, "bold")).pack(
            anchor="w", padx=5, pady=(4, 1)
        )
        release_frame = ttk.Frame(card)
        release_frame.pack(fill="x", padx=5, pady=2)
        release_frame.columnconfigure(0, weight=1)

        self.scale_blink_release = tk.Scale(
            release_frame,
            from_=50,
            to=1000,
            orient="horizontal",
            showvalue=False,
            bd=0,
            bg="#1a1a24",
            highlightthickness=0,
            troughcolor="#13131c",
            activebackground="#ff75a0",
            cursor="hand2",
            command=lambda val: self.on_scale_scroll(self.blink_release_var, val),
        )
        self.scale_blink_release.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.spin_blink_release = ttk.Spinbox(
            release_frame,
            from_=0,
            to=5000,
            increment=10,
            textvariable=self.blink_release_var,
            width=8,
        )
        self.spin_blink_release.grid(row=0, column=1, sticky="w")

        # Flow visual
        self.lbl_blink_flow = tk.Label(
            card,
            text="",
            font=("Consolas", 8, "bold"),
            fg="#dec0f1",
            bg="#13131c",
            padx=4,
            pady=4,
            bd=1,
            relief="solid",
        )
        self.lbl_blink_flow.pack(fill="x", pady=8)

        # Save timing profiles
        self.btn_save_timing = tk.Button(
            card,
            text="💾 SAVE",
            font=("Segoe UI", 9, "bold"),
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.save_blink_config,
        )
        self.btn_save_timing.pack(fill="x", pady=5)

    def update_blink_flow_label(self):
        """TODO: add documentation"""
        txt = (
            f"[Arah] -> ({self.profile.blink_init_delay}ms) -> [Shift] -> "
            f"({self.profile.blink_hold_delay}ms) -> [Lepas Shift] -> "
            f"({self.profile.blink_release_delay}ms) -> [Lepas Arah]"
        )
        self.lbl_blink_flow.config(text=txt)

    def save_blink_config(self):
        """TODO: add documentation"""
        # Validasi hanya timing / loop / random
        issues = []
        if self.profile.loop_mode == "CUSTOM" and self.profile.loop_count <= 0:
            issues.append(
                "KRITIS: Mode Loop adalah KUSTOM tetapi jumlah pengulangan kurang dari atau sama dengan 0."
            )
        if self.profile.random_delay_enabled:
            if self.profile.random_delay_min > self.profile.random_delay_max:
                issues.append("KRITIS: Jeda Acak Minimum lebih besar dari Maksimum.")
        if issues:
            error_msg = "Konfigurasi timing memiliki kesalahan kritis dan tidak dapat disimpan:\n\n"
            for iss in issues:
                error_msg += f"• {iss}\n"
            messagebox.showerror("Validasi Timing Gagal", error_msg)
            return

        import json
        import os

        file_path = getattr(self.profile, "file_path", None)

        # 1. Dapatkan JSON dasar yang akan diperbarui
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

        if not base_dict and file_path and os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    base_dict = json.loads(f.read())
            except Exception as e:
                print("Error occurred")
                base_dict = None

        if not base_dict:
            base_dict = self.profile.to_dict()

        # 2. Ambil data profil saat ini, tapi pertahankan kalibrasi servos DAN pola makro dari base_dict
        current_dict = self.profile.to_dict()
        current_dict["servos"] = base_dict.get("servos", current_dict["servos"])
        current_dict["pattern"] = base_dict.get("pattern", current_dict["pattern"])

        updated_json_str = json.dumps(current_dict, indent=4)

        try:
            self.profile.load_from_json(updated_json_str)
        except Exception as e:
            print("Error occurred")
            messagebox.showerror("Error", f"Gagal memuat profil setelah update timing: {str(e)}")
            return

        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_json_str)
                fname = os.path.basename(file_path)
                self.connection.log(f"[Timing] Profil berhasil disimpan ke berkas: {fname}")
            except Exception as e:
                print("Error occurred")
                messagebox.showerror("Error", f"Gagal menyimpan profil ke berkas: {str(e)}")
                return
        else:
            self.connection.log("[Timing] Profil berhasil diperbarui di memori aktif.")

        if hasattr(self, "on_profile_updated") and self.on_profile_updated:
            self.on_profile_updated()

        messagebox.showinfo(
            "Berhasil",
            "Parameter timing & jeda berhasil disimpan ke Manajer Profil (Editor) tanpa menimpa kalibrasi & pola makro!",
        )

    # --- Right Card: Simulation and Hardware testing ---
    def create_testing_card(self, parent):
        """TODO: add documentation"""
        card = ttk.LabelFrame(parent, text=" ⚡ Uji Coba Timing & Simulasi ", padding=15)
        card.grid(row=0, column=1, padx=(10, 15), pady=10, sticky="nsew")
        card.columnconfigure(0, weight=1)
        card.rowconfigure(3, weight=1)

        # Status Badges
        badge_frame = ttk.Frame(card)
        badge_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        self.status_badge = tk.Label(
            badge_frame,
            text="🔁 LOOP: -",
            font=("Segoe UI", 8, "bold"),
            fg="#38bdf8",
            bg="#102e3b",
            padx=6,
            pady=4,
            bd=1,
            relief="solid",
        )
        self.status_badge.pack(side="left", padx=2)

        self.random_badge = tk.Label(
            badge_frame,
            text="🛡️ JEDA ACAK: -",
            font=("Segoe UI", 8, "bold"),
            fg="#4ade80",
            bg="#1b3628",
            padx=6,
            pady=4,
            bd=1,
            relief="solid",
        )
        self.random_badge.pack(side="left", padx=2)

        # Simulation Buttons Frame
        sim_btn_frame = ttk.Frame(card)
        sim_btn_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        sim_btn_frame.columnconfigure(0, weight=1)
        sim_btn_frame.columnconfigure(1, weight=1)

        btn_sim_loop = tk.Button(
            sim_btn_frame,
            text="🔄 Simulasi Loop",
            font=("Segoe UI", 9, "bold"),
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.run_loop_simulation,
        )
        btn_sim_loop.grid(row=0, column=0, padx=2, sticky="ew")

        btn_sim_rand = tk.Button(
            sim_btn_frame,
            text="🛡️ Simulasi Jeda Acak",
            font=("Segoe UI", 9, "bold"),
            bg="#dec0f1",
            fg="white",
            activebackground="#ffb142",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.run_random_simulation,
        )
        btn_sim_rand.grid(row=0, column=1, padx=2, sticky="ew")

        # Hardware directional test grid
        hw_btn_grid = ttk.LabelFrame(
            card, text=" 🎮 Uji Gerakan Blink Fisik (Hubungkan USB) ", padding=10
        )
        hw_btn_grid.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        hw_btn_grid.columnconfigure(0, weight=1)
        hw_btn_grid.columnconfigure(1, weight=1)
        hw_btn_grid.columnconfigure(2, weight=1)

        btn_up = tk.Button(
            hw_btn_grid,
            text="⬆️ Blink Atas",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="white",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.run_test_blink("UP"),
        )
        btn_up.grid(row=0, column=1, padx=2, pady=2, sticky="ew")

        btn_left = tk.Button(
            hw_btn_grid,
            text="⬅️ Blink Kiri",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="white",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.run_test_blink("LEFT"),
        )
        btn_left.grid(row=1, column=0, padx=2, pady=2, sticky="ew")

        btn_right = tk.Button(
            hw_btn_grid,
            text="➡️ Blink Kanan",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="white",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.run_test_blink("RIGHT"),
        )
        btn_right.grid(row=1, column=2, padx=2, pady=2, sticky="ew")

        btn_down = tk.Button(
            hw_btn_grid,
            text="⬇️ Blink Bawah",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="white",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda: self.run_test_blink("DOWN"),
        )
        btn_down.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

        # Terminal log area (macOS styled)
        term_container = tk.Frame(
            card,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
        )
        term_container.grid(row=3, column=0, sticky="nsew")
        term_container.columnconfigure(0, weight=1)
        term_container.rowconfigure(1, weight=1)

        term_header = tk.Frame(term_container, bg="#1b1b26", height=28)
        term_header.grid(row=0, column=0, sticky="ew")

        dots = tk.Frame(term_header, bg="#1b1b26")
        dots.pack(side="left", padx=8)
        tk.Label(dots, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 8, "bold")).pack(
            side="left", padx=1
        )
        tk.Label(dots, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 8, "bold")).pack(
            side="left", padx=1
        )
        tk.Label(dots, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 8, "bold")).pack(
            side="left", padx=1
        )

        tk.Label(
            term_header,
            text="bash - timing-simulator@kbd-robot",
            font=("Consolas", 8, "bold"),
            fg="#94a3b8",
            bg="#1b1b26",
        ).pack(side="left", padx=4)

        text_container = tk.Frame(term_container, bg="#13131c")
        text_container.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        text_container.columnconfigure(0, weight=1)
        text_container.rowconfigure(0, weight=1)

        self.sim_console = tk.Text(
            text_container,
            bg="#13131c",
            fg="#e2e8f0",
            font=("Consolas", 9),
            wrap="word",
            bd=0,
            padx=8,
            pady=8,
        )
        self.sim_console.grid(row=0, column=0, sticky="nsew")

        sb = ttk.Scrollbar(text_container, orient="vertical", command=self.sim_console.yview)
        sb.grid(row=0, column=1, sticky="ns")
        self.sim_console.configure(yscrollcommand=sb.set)

        self.sim_console.tag_config("timestamp", foreground="#64748b")
        self.sim_console.tag_config("info", foreground="#38bdf8")
        self.sim_console.tag_config("success", foreground="#4ade80")
        self.sim_console.tag_config("warning", foreground="#dec0f1")
        self.sim_console.tag_config("error", foreground="#f87171")
        self.sim_console.config(state="disabled")

        self.log_sim("Konsol Simulasi siap.")

    def log_sim(self, msg, tag="info"):
        """TODO: add documentation"""
        self.sim_console.config(state="normal")
        t_str = time.strftime("%H:%M:%S")
        self.sim_console.insert(tk.END, f"[{t_str}] ", "timestamp")
        self.sim_console.insert(tk.END, f"{msg}\n", tag)
        self.sim_console.see(tk.END)
        self.sim_console.config(state="disabled")

    def run_loop_simulation(self):
        """TODO: add documentation"""
        self.sim_console.config(state="normal")
        self.sim_console.delete("1.0", tk.END)
        self.sim_console.insert(tk.END, "=== MEMULAI SIMULASI LOOP ===\n\n", "timestamp")
        self.sim_console.config(state="disabled")

        mode = self.loop_mode_var.get()
        self.log_sim(f"Inisialisasi loop. Auto-Start: {self.autostart_var.get()}", "info")
        if mode == "INFINITY":
            for i in range(1, 4):
                self.log_sim(f"Siklus #{i} berjalan...", "success")
                self.log_sim(
                    f"       Langkah pola 1 s.d {max(1, len(self.profile.pattern))} selesai.",
                    "info",
                )
            self.log_sim("♻️ Loop terus berjalan selamanya (INFINITY)...", "warning")
        else:
            total_loops = self.loop_count_var.get()
            cycles = min(4, total_loops)
            for i in range(1, cycles + 1):
                self.log_sim(f"Siklus #{i}/{total_loops} berjalan...", "success")
                self.log_sim(
                    f"       Langkah pola 1 s.d {max(1, len(self.profile.pattern))} selesai.",
                    "info",
                )
            if total_loops > cycles:
                self.sim_console.config(state="normal")
                self.sim_console.insert(
                    tk.END,
                    f"...\n[+ {total_loops - cycles} siklus lainnya disembunyikan]\n",
                    "timestamp",
                )
                self.sim_console.config(state="disabled")
            self.log_sim(f"✅ Selesai. Total eksekusi terencana: {total_loops} siklus.", "success")

    def run_random_simulation(self):
        """TODO: add documentation"""
        if not self.random_enabled_var.get():
            messagebox.showwarning("Simulasi Jeda", "Harap aktifkan Jeda Acak terlebih dahulu.")
            return
        self.sim_console.config(state="normal")
        self.sim_console.delete("1.0", tk.END)
        self.sim_console.insert(tk.END, "=== MEMULAI SIMULASI JEDA HUMANIS ===\n\n", "timestamp")
        self.sim_console.config(state="disabled")

        min_d = self.random_min_var.get()
        max_d = self.random_max_var.get()
        if min_d > max_d:
            self.log_sim("GAGAL: Batas jeda tidak valid!", "error")
            return
        for i in range(1, 6):
            r_delay = random.randint(min_d, max_d)
            self.log_sim(
                f"Aksi #{i} -> Jeda acak terpilih: {r_delay} ms",
                "success" if r_delay < 1500 else "warning",
            )
        self.log_sim(f"✅ Selesai. Deviasi acak maks: {max_d - min_d} ms.", "success")

    def run_test_blink(self, direction):
        """TODO: add documentation"""
        if not self.connection.connected:
            self.log_sim("Uji coba GAGAL: Koneksi serial tidak aktif!", "error")
            messagebox.showwarning(
                "Koneksi Mati", "Harap hubungkan Arduino Nano Anda terlebih dahulu."
            )
            return
        self.log_sim(f"Mengunggah profil timing sementara...", "info")
        if self.connection.upload_profile(self.profile):
            self.log_sim(f"Mengirim komando TEST_BLINK {direction} ke Arduino...", "success")
            if self.connection.send_command(f"TEST_BLINK {direction}"):
                self.log_sim(f"Blink {direction} berhasil dipicu!", "success")
            else:
                self.log_sim("Gagal mengirim komando TEST_BLINK.", "error")
        else:
            self.log_sim("Gagal mengunggah konfigurasi timing.", "error")

    def reload_from_profile(self):
        """TODO: add documentation"""
        self.loop_mode_var.set(self.profile.loop_mode)
        self.loop_count_var.set(self.profile.loop_count)
        self.autostart_var.set(self.profile.auto_start)
        self.on_mode_change()

        self.random_enabled_var.set(self.profile.random_delay_enabled)
        self.random_min_var.set(self.profile.random_delay_min)
        self.random_max_var.set(self.profile.random_delay_max)
        self.random_skip_var.set(self.profile.random_skip_enabled)
        self.on_toggle_random_enabled()

        self.blink_init_var.set(self.profile.blink_init_delay)
        self.blink_hold_var.set(self.profile.blink_hold_delay)
        self.blink_release_var.set(self.profile.blink_release_delay)
        self.update_blink_flow_label()


class RobotSettingsTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.calibration = CalibrationTab(self.notebook, profile, connection)
        self.timing = TimingSettingsFrame(self.notebook, profile, connection)
        self.validator = ValidatorTab(self.notebook, profile, connection)

        self.notebook.add(self.calibration, text=" 🔧 Kalibrasi Servo ")
        self.notebook.add(self.timing, text=" ⏳ Jeda & Timing ")
        self.notebook.add(self.validator, text=" 🔒 Diagnostik Keamanan ")

    @property
    def on_profile_updated(self):
        """TODO: add documentation"""
        return getattr(self, "_on_profile_updated", None)

    @on_profile_updated.setter
    def on_profile_updated(self, value):
        """TODO: add documentation"""
        self._on_profile_updated = value
        self.calibration.on_profile_updated = value
        self.timing.on_profile_updated = value
        self.validator.on_profile_updated = value

    def reload_table(self):
        """TODO: add documentation"""
        if hasattr(self.calibration, "reload_table"):
            self.calibration.reload_table()
        if hasattr(self.timing, "reload_table"):
            self.timing.reload_table()
        if hasattr(self.validator, "reload_table"):
            self.validator.reload_table()

    def reload_from_profile(self):
        """TODO: add documentation"""
        if hasattr(self.calibration, "reload_from_profile"):
            self.calibration.reload_from_profile()
        elif hasattr(self.calibration, "reload_table"):
            self.calibration.reload_table()

        if hasattr(self.timing, "reload_from_profile"):
            self.timing.reload_from_profile()
        elif hasattr(self.timing, "reload_table"):
            self.timing.reload_table()

        if hasattr(self.validator, "reload_from_profile"):
            self.validator.reload_from_profile()
        elif hasattr(self.validator, "reload_table"):
            self.validator.reload_table()
