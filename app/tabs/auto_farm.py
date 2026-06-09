"""TODO: module documentation"""

import time
import tkinter as tk
from tkinter import messagebox, ttk

import cv2
from PIL import Image, ImageTk

from app.auto_farm.controller import AutoFarmController


class AutoFarmTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        # Instantiate controller lazily or fetch/store globally in parent ModernApp
        # ModernApp has connection as self.connection. We can initialize/link the controller
        app = self.winfo_toplevel()
        if not hasattr(app, "auto_farm_controller"):
            app.auto_farm_controller = AutoFarmController(connection, profile)
            app.auto_farm_controller.start()

        self.controller = app.auto_farm_controller
        self.capture = self.controller.capture

        # Setup variables from controller settings
        self.var_enabled_rune = tk.BooleanVar(
            value=self.controller.settings.get("enabled_rune", False)
        )
        self.var_enabled_boss = tk.BooleanVar(
            value=self.controller.settings.get("enabled_boss", False)
        )
        self.var_enabled_lie_detector = tk.BooleanVar(
            value=self.controller.settings.get("enabled_lie_detector", False)
        )
        self.var_interact_key = tk.StringVar(
            value=self.controller.settings.get("interact_key", "alt")
        )
        self.var_jump_key = tk.StringVar(value=self.controller.settings.get("jump_key", "space"))
        self.var_vertical_jump_mode = tk.StringVar(
            value=self.get_display_jump_mode(
                self.controller.settings.get("vertical_jump_mode", "double_jump")
            )
        )
        self.var_blink_key = tk.StringVar(value=self.controller.settings.get("blink_key", "shift"))
        self.var_rune_input_mode = tk.StringVar(
            value=self.get_display_input_mode(
                self.controller.settings.get("rune_input_mode", "software")
            )
        )

        # Setup grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Build GUI cards
        self.create_left_card()
        self.create_right_card()

        # Check initial state to disable/enable blink key dropdown
        self.update_blink_dropdown_state()

        # Start periodic GUI updates
        self.update_gui_loop()

    def create_left_card(self):
        """TODO: add documentation"""
        # LEFT CARD: Settings & Configuration
        card_settings = ttk.LabelFrame(
            self, text=" 🎛️ Pengaturan Fitur Otomatis (Auto) ", padding=25
        )
        card_settings.grid(row=0, column=0, padx=(40, 20), pady=20, sticky="nsew")
        card_settings.columnconfigure(0, weight=1)

        # 1. Feature Checkbuttons
        ttk.Label(card_settings, text="Aktifkan Modul Fitur:", font=("Helvetica", 11, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )

        chk_rune = tk.Checkbutton(
            card_settings,
            text="Auto Clear Rune (ViT Machine Learning Solver)",
            variable=self.var_enabled_rune,
            command=self.save_settings_from_gui,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 10),
        )
        chk_rune.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        chk_boss = tk.Checkbutton(
            card_settings,
            text="Field Boss / Elite Boss Warning & Auto Stop",
            variable=self.var_enabled_boss,
            command=self.save_settings_from_gui,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 10),
        )
        chk_boss.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        chk_lie = tk.Checkbutton(
            card_settings,
            text="Auto Stop & Alarm on Lie Detector (Local Image)",
            variable=self.var_enabled_lie_detector,
            command=self.save_settings_from_gui,
            bg="#1a1a24",
            fg="#ffffff",
            selectcolor="#13131c",
            activebackground="#1a1a24",
            activeforeground="#ffffff",
            font=("Helvetica", 10),
        )
        chk_lie.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        # Divider
        ttk.Separator(card_settings, orient="horizontal").grid(
            row=4, column=0, sticky="ew", pady=15
        )

        # 2. Key Bindings
        ttk.Label(
            card_settings,
            text="Konfigurasi Tombol Virtual (pynput):",
            font=("Helvetica", 11, "bold"),
        ).grid(row=5, column=0, sticky="w", pady=(0, 10))

        # Interact Key Row
        interact_frame = ttk.Frame(card_settings)
        interact_frame.grid(row=6, column=0, sticky="ew", pady=5)
        interact_frame.columnconfigure(1, weight=1)

        ttk.Label(interact_frame, text="Tombol Interact (Buka Rune):", font=("Helvetica", 10)).grid(
            row=0, column=0, sticky="w", padx=5
        )

        keys_list = [
            "alt",
            "space",
            "shift",
            "ctrl",
            "space",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        cb_interact = ttk.Combobox(
            interact_frame,
            textvariable=self.var_interact_key,
            values=keys_list,
            width=12,
            state="readonly",
        )
        cb_interact.grid(row=0, column=1, sticky="e", padx=5)
        cb_interact.bind("<<ComboboxSelected>>", lambda e: self.save_settings_from_gui())

        # Jump Key Row
        jump_frame = ttk.Frame(card_settings)
        jump_frame.grid(row=7, column=0, sticky="ew", pady=5)
        jump_frame.columnconfigure(1, weight=1)

        ttk.Label(jump_frame, text="Tombol Lompat (Jump):", font=("Helvetica", 10)).grid(
            row=0, column=0, sticky="w", padx=5
        )

        cb_jump = ttk.Combobox(
            jump_frame, textvariable=self.var_jump_key, values=keys_list, width=12, state="readonly"
        )
        cb_jump.grid(row=0, column=1, sticky="e", padx=5)
        cb_jump.bind("<<ComboboxSelected>>", lambda e: self.save_settings_from_gui())

        # Mode Lompat Vertikal Row
        vjump_frame = ttk.Frame(card_settings)
        vjump_frame.grid(row=8, column=0, sticky="ew", pady=5)
        vjump_frame.columnconfigure(1, weight=1)

        ttk.Label(vjump_frame, text="Mode Lompat Vertikal (Ke Atas):", font=("Helvetica", 10)).grid(
            row=0, column=0, sticky="w", padx=5
        )

        cb_vjump = ttk.Combobox(
            vjump_frame,
            textvariable=self.var_vertical_jump_mode,
            values=[
                "Double Jump (Atas + Jump 2x)",
                "Blink (Gunakan Tombol)",
                "Climb Only (Tangga/Tali)",
            ],
            width=25,
            state="readonly",
        )
        cb_vjump.grid(row=0, column=1, sticky="e", padx=5)
        cb_vjump.bind("<<ComboboxSelected>>", self.on_jump_mode_changed)

        # Blink Key Row
        self.blink_frame = ttk.Frame(card_settings)
        self.blink_frame.grid(row=9, column=0, sticky="ew", pady=5)
        self.blink_frame.columnconfigure(1, weight=1)

        self.lbl_blink = ttk.Label(
            self.blink_frame, text="Tombol Blink (Blink Key):", font=("Helvetica", 10)
        )
        self.lbl_blink.grid(row=0, column=0, sticky="w", padx=5)

        self.cb_blink = ttk.Combobox(
            self.blink_frame,
            textvariable=self.var_blink_key,
            values=keys_list,
            width=12,
            state="readonly",
        )
        self.cb_blink.grid(row=0, column=1, sticky="e", padx=5)
        self.cb_blink.bind("<<ComboboxSelected>>", lambda e: self.save_settings_from_gui())

        # Rune Input Mode Row
        self.input_mode_frame = ttk.Frame(card_settings)
        self.input_mode_frame.grid(row=10, column=0, sticky="ew", pady=5)
        self.input_mode_frame.columnconfigure(1, weight=1)

        ttk.Label(
            self.input_mode_frame, text="Mode Input Rune Solver:", font=("Helvetica", 10)
        ).grid(row=0, column=0, sticky="w", padx=5)

        self.cb_input_mode = ttk.Combobox(
            self.input_mode_frame,
            textvariable=self.var_rune_input_mode,
            values=["Virtual PC (Software)", "Servo Robot (Hardware)"],
            width=25,
            state="readonly",
        )
        self.cb_input_mode.grid(row=0, column=1, sticky="e", padx=5)
        self.cb_input_mode.bind("<<ComboboxSelected>>", lambda e: self.save_settings_from_gui())

        # Divider
        ttk.Separator(card_settings, orient="horizontal").grid(
            row=11, column=0, sticky="ew", pady=15
        )

        # 3. System Commands / Actions
        ttk.Label(
            card_settings, text="Aksi Perangkat Keras / Alarm:", font=("Helvetica", 11, "bold")
        ).grid(row=12, column=0, sticky="w", pady=(0, 10))

        # Alarm stop button
        self.btn_mute = tk.Button(
            card_settings,
            text="🔇 HENTIKAN ALARM SIRENE",
            font=("Segoe UI", 10, "bold"),
            bg="#dec0f1",
            fg="white",
            activebackground="#ffb142",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.mute_siren,
        )
        self.btn_mute.grid(row=13, column=0, sticky="ew", pady=5)
        self.btn_mute.bind("<Enter>", lambda e: self.btn_mute.config(bg="#ffb142"))
        self.btn_mute.bind("<Leave>", lambda e: self.btn_mute.config(bg="#dec0f1"))

        # 4. Status Description Alert Box
        desc_frame = tk.Frame(card_settings, bg="#13131c", bd=1, relief="solid")
        desc_frame.grid(row=14, column=0, sticky="ew", pady=20)

        lbl_hint = tk.Label(
            desc_frame,
            text="ℹ️ INFORMASI INTEGRASI AUTOMATION:",
            font=("Segoe UI", 8, "bold"),
            fg="#747d8c",
            bg="#13131c",
        )
        lbl_hint.pack(pady=(8, 2))

        hint_text = (
            "Ketika Rune terdeteksi di minimap:\n"
            "1. PC akan mengirim perintah 'STOP' untuk menonaktifkan gerakan servo Arduino.\n"
            "2. Keyboard virtual (pynput) akan memandu karakter ke arah rune secara otomatis.\n"
            "3. Setelah puzzle diselesaikan oleh AI ViT, gerakan makro Arduino akan di-START kembali."
        )
        tk.Label(
            desc_frame,
            text=hint_text,
            font=("Segoe UI", 8),
            fg="#dec0f1",
            bg="#13131c",
            justify="left",
        ).pack(pady=(2, 10), padx=15)

    def create_right_card(self):
        """TODO: add documentation"""
        # RIGHT CARD: Live Camera & Vision Calibration Preview (macOS styled)
        card_monitor = ttk.LabelFrame(
            self, text=" 🖥️ Pemantauan Kamera Minimap & Koordinat ", padding=25
        )
        card_monitor.grid(row=0, column=1, padx=(20, 40), pady=20, sticky="nsew")
        card_monitor.columnconfigure(0, weight=1)
        card_monitor.rowconfigure(3, weight=1)

        # 1. State Status Badge Frame
        status_subframe = ttk.Frame(card_monitor)
        status_subframe.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        status_subframe.columnconfigure(1, weight=1)

        self.lbl_vision_status = tk.Label(
            status_subframe,
            text="● MENCARI WINDOW MAPLESTORY",
            font=("Segoe UI", 9, "bold"),
            fg="#ff4757",
            bg="#2a1b20",
            padx=12,
            pady=6,
            bd=1,
            relief="solid",
        )
        self.lbl_vision_status.grid(row=0, column=0, sticky="w")

        self.lbl_fps = ttk.Label(
            status_subframe, text="-- FPS", font=("Consolas", 10, "bold"), foreground="#dec0f1"
        )
        self.lbl_fps.grid(row=0, column=1, sticky="e")

        # 2. Coordinates details & Manual Recalibrate Button
        coords_frame = ttk.Frame(card_monitor)
        coords_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        coords_frame.columnconfigure(1, weight=1)

        self.lbl_coords = ttk.Label(
            coords_frame,
            text="Posisi Pemain: (-, -) | Status Rune: Tidak Terdeteksi",
            font=("Consolas", 9, "bold"),
            foreground="#2ed573",
        )
        self.lbl_coords.grid(row=0, column=0, sticky="w")

        btn_recalibrate = tk.Button(
            coords_frame,
            text="🔄 KALIBRASI MANUAL",
            font=("Segoe UI", 8, "bold"),
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            relief="flat",
            bd=0,
            padx=8,
            pady=3,
            cursor="hand2",
            command=self.trigger_recalibration,
        )
        btn_recalibrate.grid(row=0, column=1, sticky="e")
        btn_recalibrate.bind("<Enter>", lambda e: btn_recalibrate.config(bg="#ff9ff3"))
        btn_recalibrate.bind("<Leave>", lambda e: btn_recalibrate.config(bg="#ff75a0"))

        # 3. Minimap Camera Canvas Frame (macOS styled container)
        self.cam_container = tk.Frame(
            card_monitor,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
        )
        self.cam_container.grid(row=3, column=0, sticky="nsew")
        self.cam_container.columnconfigure(0, weight=1)
        self.cam_container.rowconfigure(1, weight=1)

        # macOS Terminal-style Header Bar
        cam_header = tk.Frame(self.cam_container, bg="#1b1b26", height=28)
        cam_header.grid(row=0, column=0, sticky="ew")

        # Dots
        dots_frame = tk.Frame(cam_header, bg="#1b1b26")
        dots_frame.pack(side="left", padx=10)
        tk.Label(
            dots_frame, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 8, "bold")
        ).pack(side="left", padx=1)
        tk.Label(
            dots_frame, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 8, "bold")
        ).pack(side="left", padx=1)
        tk.Label(
            dots_frame, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 8, "bold")
        ).pack(side="left", padx=1)

        tk.Label(
            cam_header,
            text="minimap-live-feed",
            font=("Consolas", 8, "bold"),
            fg="#94a3b8",
            bg="#1b1b26",
        ).pack(side="left", padx=5)

        # Live Canvas Display
        self.lbl_preview_img = tk.Label(
            self.cam_container,
            bg="#13131c",
            text="Menunggu Kalibrasi Minimap...",
            font=("Helvetica", 10),
            fg="#747d8c",
        )
        self.lbl_preview_img.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    def get_display_jump_mode(self, value):
        """TODO: add documentation"""
        mapping = {
            "double_jump": "Double Jump (Atas + Jump 2x)",
            "blink": "Blink (Gunakan Tombol)",
            "climb": "Climb Only (Tangga/Tali)",
        }
        return mapping.get(value, "Double Jump (Atas + Jump 2x)")

    def get_raw_jump_mode(self, display_value):
        """TODO: add documentation"""
        mapping = {
            "Double Jump (Atas + Jump 2x)": "double_jump",
            "Blink (Gunakan Tombol)": "blink",
            "Climb Only (Tangga/Tali)": "climb",
        }
        return mapping.get(display_value, "double_jump")

    def get_display_input_mode(self, value):
        """TODO: add documentation"""
        mapping = {"software": "Virtual PC (Software)", "hardware": "Servo Robot (Hardware)"}
        return mapping.get(value, "Virtual PC (Software)")

    def get_raw_input_mode(self, display_value):
        """TODO: add documentation"""
        mapping = {"Virtual PC (Software)": "software", "Servo Robot (Hardware)": "hardware"}
        return mapping.get(display_value, "software")

    def save_settings_from_gui(self):
        """TODO: add documentation"""
        self.controller.settings["enabled_rune"] = self.var_enabled_rune.get()
        self.controller.settings["enabled_boss"] = self.var_enabled_boss.get()
        self.controller.settings["enabled_lie_detector"] = self.var_enabled_lie_detector.get()
        self.controller.settings["interact_key"] = self.var_interact_key.get()
        self.controller.settings["jump_key"] = self.var_jump_key.get()
        self.controller.settings["vertical_jump_mode"] = self.get_raw_jump_mode(
            self.var_vertical_jump_mode.get()
        )
        self.controller.settings["blink_key"] = self.var_blink_key.get()
        self.controller.settings["rune_input_mode"] = self.get_raw_input_mode(
            self.var_rune_input_mode.get()
        )
        self.controller.save_settings()

    def mute_siren(self):
        """TODO: add documentation"""
        self.controller.stop_alert()
        # Restoring boss check toggle and lie detector toggle just in case
        self.var_enabled_boss.set(True)
        self.var_enabled_lie_detector.set(True)
        self.save_settings_from_gui()
        self.connection.log("[Alarm] Sirene alarm dinonaktifkan secara manual oleh pengguna.")

    def trigger_recalibration(self):
        """TODO: add documentation"""
        self.capture.calibrated = False
        self.capture.ready = False
        self.connection.log("[Capture] Memicu kalibrasi ulang minimap manual...")

    def update_gui_loop(self):
        """Update live camera frames, FPS and player dot positions in UI loop."""
        try:
            # Sync checkbox variables from controller settings only when they change
            for attr, setting_key in [
                ("var_enabled_rune", "enabled_rune"),
                ("var_enabled_boss", "enabled_boss"),
                ("var_enabled_lie_detector", "enabled_lie_detector"),
            ]:
                var = getattr(self, attr)
                if var.get() != self.controller.settings.get(setting_key, False):
                    var.set(self.controller.settings.get(setting_key, False))

            # 1. Update State Badges
            if self.controller.alert_active:
                self.lbl_vision_status.config(
                    text="🚨 ALARM SIRENE AKTIF (ELITE / MATI)", fg="#ff4757", bg="#2a1b20"
                )
            elif self.controller.solving_rune:
                self.lbl_vision_status.config(
                    text="🧩 MENYELESAIKAN PUZZLE RUNE...", fg="#dec0f1", bg="#2b231b"
                )
            elif self.capture.calibrated:
                self.lbl_vision_status.config(
                    text="● AUTO MONITORING AKTIF", fg="#2ed573", bg="#1b2a20"
                )
            elif self.capture.ready:
                self.lbl_vision_status.config(
                    text="● KALIBRASI MINIMAP...", fg="#dec0f1", bg="#2b231b"
                )
            else:
                self.lbl_vision_status.config(
                    text="● MENCARI WINDOW GAME...", fg="#ff4757", bg="#2a1b20"
                )

            # 2. Update FPS
            self.lbl_fps.config(
                text=f"{self.capture.fps:.1f} FPS" if self.capture.ready else "-- FPS"
            )

            # 3. Update Coords and Rune state
            rune_detected = "Terdeteksi" if self.controller._scan_for_rune() else "Tidak Terdeteksi"
            px, py = self.capture.player_pos
            self.lbl_coords.config(
                text=f"Posisi Pemain: ({px:.3f}, {py:.3f}) | Status Rune: {rune_detected}"
            )

            # 4. Update live minimap camera feed image
            minimap_frame = self.capture.minimap
            if minimap_frame is not None and minimap_frame.size > 0:
                # Convert BGR (OpenCV) to RGB (PIL)
                rgb_frame = cv2.cvtColor(minimap_frame, cv2.COLOR_BGR2RGB)

                # Resize to fit the preview panel nicely
                h, w = rgb_frame.shape[:2]
                target_w = 320
                target_h = int(h * (target_w / w))
                pil_img = Image.fromarray(rgb_frame).resize((target_w, target_h), Image.LANCZOS)

                # Draw relative target overlays if in calibration
                tk_img = ImageTk.PhotoImage(pil_img)
                self.lbl_preview_img.config(image=tk_img, text="")
                self.lbl_preview_img.image = tk_img  # Keep a reference!
            else:
                self.lbl_preview_img.config(image="", text="Menunggu Kalibrasi Minimap...")

        except Exception as e:
            print("Error occurred")
            # Prevent print spam if window is closing
            pass

        self.after(100, self.update_gui_loop)

    def on_jump_mode_changed(self, event=None):
        """TODO: add documentation"""
        self.update_blink_dropdown_state()
        self.save_settings_from_gui()

    def update_blink_dropdown_state(self):
        """TODO: add documentation"""
        mode = self.get_raw_jump_mode(self.var_vertical_jump_mode.get())
        if mode == "blink":
            self.cb_blink.config(state="readonly")
            self.lbl_blink.config(foreground="#ffffff")
        else:
            self.cb_blink.config(state="disabled")
            self.lbl_blink.config(foreground="#57606f")

    def reload_from_profile(self):
        """TODO: add documentation"""
        # Refresh configuration variables from updated profile
        self.settings = self.controller.load_settings()
        self.var_enabled_rune.set(self.settings.get("enabled_rune", False))
        self.var_enabled_boss.set(self.settings.get("enabled_boss", False))
        self.var_enabled_lie_detector.set(self.settings.get("enabled_lie_detector", False))
        self.var_interact_key.set(self.settings.get("interact_key", "alt"))
        self.var_jump_key.set(self.settings.get("jump_key", "space"))
        self.var_vertical_jump_mode.set(
            self.get_display_jump_mode(self.settings.get("vertical_jump_mode", "double_jump"))
        )
        self.var_blink_key.set(self.settings.get("blink_key", "shift"))
        self.var_rune_input_mode.set(
            self.get_display_input_mode(self.settings.get("rune_input_mode", "software"))
        )
        self.update_blink_dropdown_state()
