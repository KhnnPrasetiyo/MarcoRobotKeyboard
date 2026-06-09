"""TODO: module documentation"""

import json
import subprocess
import sys
import threading
import time
import tkinter as tk
from tkinter import messagebox, ttk

from app.models import Action

import importlib.util

HAS_KEYBOARD = importlib.util.find_spec("keyboard") is not None


class RecorderTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        # Recording state
        self.recording_active = False
        self.global_active = False
        self.recorded_pattern = []
        self.keys_down = {}
        self.key_press_times = {}
        self.key_modifier_state = (
            {}
        )  # Tracks modifier states at press time to avoid release race conditions
        self.last_release_time = None
        self.shift_pressed = False

        # Configure layout grids
        self.columnconfigure(0, weight=1)  # Left controls & Canvas
        self.columnconfigure(1, weight=1)  # Right Table & Editor
        self.rowconfigure(0, weight=1)

        # 1. Left Side: Controls & Visual HUD
        left_frame = ttk.Frame(self, padding=10)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)

        # Controls Card
        ctrl_card = ttk.LabelFrame(left_frame, text=" Kontrol Perekam ", padding=15)
        ctrl_card.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        ctrl_card.columnconfigure(0, weight=1)
        ctrl_card.columnconfigure(1, weight=1)

        # Perekaman State Button
        self.btn_toggle_rec = tk.Button(
            ctrl_card,
            text="🔴 MULAI PEREKAMAN",
            font=("Segoe UI", 10, "bold"),
            bg="#ff4757",
            fg="white",
            activebackground="#ff6b81",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.toggle_recording,
        )
        self.btn_toggle_rec.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Focus button to capture inputs reliably in Focused Mode
        self.focus_btn = tk.Button(
            ctrl_card,
            text="🔌 Klik & Ketik di Sini untuk Merekam",
            font=("Segoe UI", 10, "bold"),
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
        )
        self.focus_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.focus_btn.bind("<Button-1>", self.on_focus_click)
        self.focus_btn.bind("<FocusOut>", self.on_focus_lost)
        self.focus_btn.bind("<KeyPress>", self.on_key_press)
        self.focus_btn.bind("<KeyRelease>", self.on_key_release)

        # Key Mappings for focused mode
        self.key_mapping = {
            "Up": "UP",
            "Left": "LEFT",
            "Down": "DOWN",
            "Right": "RIGHT",
            "a": "A",
            "A": "A",
            "Shift_L": "SHIFT",
            "Shift_R": "SHIFT",
            "shift": "SHIFT",
            "Shift": "SHIFT",
            "Alt_L": "ALT",
            "Alt_R": "ALT",
            "alt": "ALT",
            "Alt": "ALT",
            "space": "SPACE",
            "Space": "SPACE",
        }

        # Global Recording UI elements
        global_ui_frame = ttk.Frame(ctrl_card)
        global_ui_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
        global_ui_frame.columnconfigure(0, weight=1)

        # Checkbox Mode Latar Belakang (Game)
        self.chk_global_var = tk.BooleanVar(value=HAS_KEYBOARD)
        self.chk_global = ttk.Checkbutton(
            global_ui_frame,
            text="Rekam di Latar Belakang (Aktif Saat Main Game)",
            variable=self.chk_global_var,
            command=self.on_toggle_global_checkbox,
        )
        self.chk_global.grid(row=0, column=0, padx=5, pady=2, sticky="w")

        # Status mode latar belakang
        self.lbl_global_status = ttk.Label(global_ui_frame, font=("Helvetica", 9, "bold"))
        self.lbl_global_status.grid(row=1, column=0, padx=5, pady=2, sticky="w")

        # Auto-installer button for 'keyboard' package
        self.btn_install_kb = tk.Button(
            global_ui_frame,
            text="🔌 Instal Library Latar Belakang (keyboard)",
            font=("Segoe UI", 8, "bold"),
            bg="#dec0f1",
            fg="white",
            activebackground="#ffb142",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.start_keyboard_installation,
            padx=10,
            pady=4,
        )
        self.btn_install_kb.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Configure dynamic visibility based on installation state
        self.update_global_mode_ui_state()

        # Clear and Save Buttons
        btn_action_frame = ttk.Frame(ctrl_card)
        btn_action_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky="ew")
        btn_action_frame.columnconfigure(0, weight=1)
        btn_action_frame.columnconfigure(1, weight=1)

        self.btn_clear = tk.Button(
            btn_action_frame,
            text="🗑️ BERSIHKAN REKAMAN",
            font=("Segoe UI", 9, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#ef4444",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.clear_recording,
        )
        self.btn_clear.grid(row=0, column=0, padx=5, sticky="ew")
        self.btn_clear.bind("<Enter>", lambda e: self.btn_clear.config(bg="#ef4444", fg="white"))
        self.btn_clear.bind("<Leave>", lambda e: self.btn_clear.config(bg="#272736", fg="#cbd5e1"))

        self.btn_save_to_active = tk.Button(
            btn_action_frame,
            text="💾  SAVE",
            font=("Segoe UI", 9, "bold"),
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            activeforeground="white",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.save_to_profile,
        )
        self.btn_save_to_active.grid(row=0, column=1, padx=5, sticky="ew")

        # HUD Screen (Canvas)
        hud_card = ttk.LabelFrame(left_frame, text=" Monitor HUD Perekaman ", padding=10)
        hud_card.grid(row=1, column=0, sticky="nsew")
        hud_card.columnconfigure(0, weight=1)
        hud_card.rowconfigure(0, weight=1)

        self.hud_canvas = tk.Canvas(hud_card, bg="#13131c", highlightthickness=0)
        self.hud_canvas.grid(row=0, column=0, sticky="nsew")
        self.hud_canvas.bind("<Configure>", lambda e: self.draw_hud())

        # 2. Right Side: Treeview Table & Editor Fields
        right_frame = ttk.Frame(self, padding=10)
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)

        table_card = ttk.LabelFrame(
            right_frame, text=" Hasil Rekaman Makro (Daftar Aksi) ", padding=15
        )
        table_card.grid(row=0, column=0, sticky="nsew")
        table_card.columnconfigure(0, weight=1)
        table_card.rowconfigure(0, weight=1)

        # Table & Scrollbar container
        table_container = ttk.Frame(table_card)
        table_container.grid(row=0, column=0, sticky="nsew")
        table_container.columnconfigure(0, weight=1)
        table_container.rowconfigure(0, weight=1)

        columns = ("index", "action", "press_dur", "delay_dur")
        self.tree = ttk.Treeview(
            table_container, columns=columns, show="headings", selectmode="browse"
        )
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.tree.heading("index", text="#")
        self.tree.heading("action", text="Tipe Aksi")
        self.tree.heading("press_dur", text="Tekan (ms)")
        self.tree.heading("delay_dur", text="Jeda (ms)")

        self.tree.column("index", width=40, anchor="center")
        self.tree.column("action", width=120, anchor="center")
        self.tree.column("press_dur", width=90, anchor="center")
        self.tree.column("delay_dur", width=90, anchor="center")

        sb = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        sb.grid(row=0, column=1, sticky="ns")

        # Edit selected action fields
        self.edit_frame = ttk.LabelFrame(table_card, text=" Edit Aksi Terpilih ", padding=10)
        self.edit_frame.grid(row=1, column=0, pady=(15, 0), sticky="ew")

        # Grid inside edit fields
        self.edit_frame.columnconfigure(1, weight=1)
        self.edit_frame.columnconfigure(3, weight=1)

        ttk.Label(self.edit_frame, text="Aksi:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.action_var = tk.StringVar()
        self.action_combo = ttk.Combobox(
            self.edit_frame,
            textvariable=self.action_var,
            values=Action.TYPES,
            state="readonly",
            width=12,
        )
        self.action_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.action_combo.bind("<<ComboboxSelected>>", self.on_field_edited)

        ttk.Label(self.edit_frame, text="Tekan (ms):").grid(
            row=0, column=2, padx=5, pady=5, sticky="e"
        )
        self.press_var = tk.IntVar()
        self.press_spin = ttk.Spinbox(
            self.edit_frame, from_=50, to=10000, increment=50, textvariable=self.press_var, width=8
        )
        self.press_spin.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.press_spin.bind("<FocusOut>", self.on_field_edited)
        self.press_spin.bind("<Return>", self.on_field_edited)

        ttk.Label(self.edit_frame, text="Jeda (ms):").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.delay_var = tk.IntVar()
        self.delay_spin = ttk.Spinbox(
            self.edit_frame, from_=0, to=60000, increment=100, textvariable=self.delay_var, width=8
        )
        self.delay_spin.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.delay_spin.bind("<FocusOut>", self.on_field_edited)
        self.delay_spin.bind("<Return>", self.on_field_edited)

        # Row actions
        row_action_frame = ttk.Frame(self.edit_frame)
        row_action_frame.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
        row_action_frame.columnconfigure(0, weight=1)
        row_action_frame.columnconfigure(1, weight=1)

        self.btn_del_row = tk.Button(
            row_action_frame,
            text="🗑️ Hapus Baris",
            font=("Segoe UI", 9, "bold"),
            bg="#ff4757",
            fg="white",
            activebackground="#ff6b81",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.delete_selected_row,
        )
        self.btn_del_row.grid(row=0, column=0, padx=2, sticky="ew")

        # Visual/Direct JSON Edit Dialog Launcher
        self.btn_json_edit = tk.Button(
            row_action_frame,
            text="⚙️ Edit JSON Mentah",
            font=("Segoe UI", 9, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.open_json_editor,
        )
        self.btn_json_edit.grid(row=0, column=1, padx=2, sticky="ew")
        self.btn_json_edit.bind(
            "<Enter>", lambda e: self.btn_json_edit.config(bg="#47475c", fg="white")
        )
        self.btn_json_edit.bind(
            "<Leave>", lambda e: self.btn_json_edit.config(bg="#272736", fg="#cbd5e1")
        )

        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

        # Initial UI configuration
        self.update_rec_ui_button_style()
        self.draw_hud()

    def update_global_mode_ui_state(self):
        """TODO: add documentation"""
        if HAS_KEYBOARD:
            self.chk_global.config(state="normal")
            self.btn_install_kb.grid_forget()
            if self.chk_global_var.get():
                self.lbl_global_status.config(
                    text="● Mode Global Aktif (Bisa Rekam Saat Main Game)", foreground="#2ed573"
                )
                self.focus_btn.config(state="disabled", text="🎮 Mode Latar Belakang Aktif")
            else:
                self.lbl_global_status.config(
                    text="● Mode Aplikasi Aktif (Fokus Aplikasi Saja)", foreground="#dec0f1"
                )
                self.focus_btn.config(state="normal", text="🔌 Klik & Ketik di Sini untuk Merekam")
        else:
            self.chk_global_var.set(False)
            self.chk_global.config(state="disabled")
            self.lbl_global_status.config(
                text="⚠️ Butuh library 'keyboard' untuk merekam game di latar belakang.",
                foreground="#ff4757",
            )
            self.btn_install_kb.grid(row=2, column=0, padx=5, pady=5, sticky="w")
            self.focus_btn.config(state="normal", text="🔌 Klik & Ketik di Sini untuk Merekam")

    def on_toggle_global_checkbox(self):
        """TODO: add documentation"""
        self.update_global_mode_ui_state()

    def start_keyboard_installation(self):
        """TODO: add documentation"""
        # Disable controls during setup
        self.btn_toggle_rec.config(state="disabled")
        self.focus_btn.config(state="disabled")
        self.btn_install_kb.config(state="disabled", text="⌛ Mengunduh & Menginstal...")
        messagebox.showinfo(
            "Instalasi Dependensi",
            "Instalasi pustaka 'keyboard' sedang berjalan di latar belakang.\nMohon tunggu sejenak, ini biasanya memakan waktu 3-10 detik...",
        )

        threading.Thread(target=self.run_keyboard_install_thread, daemon=True).start()

    def run_keyboard_install_thread(self):
        """TODO: add documentation"""
        global HAS_KEYBOARD
        success = False
        try:
            # Install package using pip
            subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
            import keyboard  # noqa: F401

            HAS_KEYBOARD = True
            success = True
        except Exception as e:
            print("Error occurred")
            success = False

        # Schedule UI update in main thread
        self.after(0, lambda: self.finish_keyboard_installation(success))

    def finish_keyboard_installation(self, success):
        """TODO: add documentation"""
        self.btn_toggle_rec.config(state="normal")
        self.focus_btn.config(state="normal")
        self.btn_install_kb.config(
            state="normal", text="🔌 Instal Library Latar Belakang (keyboard)"
        )

        if success:
            self.chk_global_var.set(True)
            self.update_global_mode_ui_state()
            messagebox.showinfo(
                "Instalasi Sukses",
                "Pustaka 'keyboard' berhasil diinstal!\n\nMode Latar Belakang (Global) sekarang AKTIF dan siap merekam ketukan tombol Anda saat Anda memainkan game.",
            )
        else:
            messagebox.showerror(
                "Instalasi Gagal",
                "Gagal menginstal pustaka otomatis.\nSilakan jalankan perintah berikut secara manual di Windows Command Prompt (CMD):\n\npip install keyboard",
            )

    def toggle_recording(self):
        """TODO: add documentation"""
        self.recording_active = not self.recording_active

        if self.recording_active:
            self.keys_down.clear()
            self.key_press_times.clear()
            self.last_release_time = None
            self.shift_pressed = False

            # Check if global mode should be activated
            if self.chk_global_var.get() and HAS_KEYBOARD:
                self.global_active = True
                self.focus_btn.config(text="🎮 Mode Latar Belakang Aktif", bg="#2ed573")
                # Register Global Hook
                try:
                    import keyboard

                    keyboard.hook(self.on_global_key_event)
                except Exception as e:
                    print("Error occurred")
                    self.global_active = False
                    messagebox.showerror("Error Hook", f"Gagal memasang low-level hook: {str(e)}")
            else:
                self.global_active = False
                self.focus_btn.focus_set()
                self.focus_btn.config(text="🟢 Perekaman Aktif (Ketuk Tombol PC!)", bg="#2ed573")
        else:
            if getattr(self, "_reload_timer", None):
                self.after_cancel(self._reload_timer)
                self._do_reload_table()

            # Unhook global listener if active
            if self.global_active:
                try:
                    import keyboard

                    keyboard.unhook(self.on_global_key_event)
                except Exception as e:
                    print("Error occurred")
                    pass
                self.global_active = False

            # Reset focus button style
            self.update_global_mode_ui_state()

        self.update_rec_ui_button_style()
        self.draw_hud()

    def update_rec_ui_button_style(self):
        """TODO: add documentation"""
        if self.recording_active:
            self.btn_toggle_rec.config(
                text="⏹ HENTIKAN PEREKAMAN", bg="#dec0f1", activebackground="#ffb142"
            )
        else:
            self.btn_toggle_rec.config(
                text="🔴 MULAI PEREKAMAN", bg="#ff4757", activebackground="#ff6b81"
            )

    def on_focus_click(self, event):
        """TODO: add documentation"""
        if self.global_active:
            return  # Ignore in global background mode
        if self.recording_active:
            self.focus_btn.focus_set()
            self.focus_btn.config(text="🟢 Perekaman Aktif (Ketuk Tombol PC!)", bg="#2ed573")
        else:
            self.focus_btn.focus_set()
            self.focus_btn.config(text="⚡ Fokus Siap (Klik 'Mulai Perekaman')", bg="#dec0f1")

    def on_focus_lost(self, event):
        """TODO: add documentation"""
        if self.global_active:
            return  # Ignore in global background mode
        if self.recording_active:
            self.focus_btn.config(
                text="⚠️ Fokus Hilang! (Klik untuk merekam kembali)", bg="#ff4757"
            )
        else:
            self.update_global_mode_ui_state()

    def on_key_press(self, event):
        """TODO: add documentation"""
        if self.global_active:
            return  # Handled by global keyboard hook instead
        if not self.recording_active:
            return
        key = event.keysym

        # Track Shift key state separately
        if key in ("Shift_L", "Shift_R"):
            self.shift_pressed = True

            # CASE B: Shift is pressed while a directional key is already held down (Direction first, then Shift)
            directional_keys = ["Left", "Right", "Up", "Down"]
            for dir_key in directional_keys:
                if self.keys_down.get(dir_key, False):
                    self.key_modifier_state[dir_key] = True
            return

        # De-duplicate repeated keypress signals from OS
        if self.keys_down.get(key, False):
            return

        # Check if the key is supported
        if key not in self.key_mapping:
            return

        self.keys_down[key] = True

        # Triple-safety Shift detection
        shift_held = False
        if HAS_KEYBOARD:
            try:
                import keyboard

                shift_held = (
                    keyboard.is_pressed("shift")
                    or keyboard.is_pressed("left shift")
                    or keyboard.is_pressed("right shift")
                )
            except Exception as e:
                print("Error occurred")
                pass
        if not shift_held:
            shift_held = ((event.state & 0x0001) != 0) or self.shift_pressed

        self.key_modifier_state[key] = shift_held
        press_time = time.time()
        self.key_press_times[key] = press_time

        # Calculate delay duration for the PREVIOUS action if applicable
        if self.last_release_time is not None and len(self.recorded_pattern) > 0:
            delay_sec = press_time - self.last_release_time
            delay_ms = int(delay_sec * 1000)
            self.recorded_pattern[-1].delay_duration = delay_ms
            self.schedule_reload_table()

        self.draw_hud(key_pressed_display=key)

    def on_key_release(self, event):
        """TODO: add documentation"""
        if self.global_active:
            return  # Handled by global keyboard hook instead
        if not self.recording_active:
            return
        key = event.keysym

        # Track Shift key state separately
        if key in ("Shift_L", "Shift_R"):
            self.shift_pressed = False
            return

        if not self.keys_down.get(key, False):
            return

        self.keys_down[key] = False
        press_time = self.key_press_times.get(key)

        if press_time is not None:
            release_time = time.time()
            press_duration = int((release_time - press_time) * 1000)

            # Map action type
            mapped_key = self.key_mapping.get(key)
            action_type = "NONE"
            if mapped_key in ("A", "SHIFT", "ALT", "SPACE"):
                action_type = mapped_key
            elif mapped_key in ("LEFT", "RIGHT", "UP", "DOWN"):
                is_blink = self.key_modifier_state.get(key, False)
                if is_blink:
                    action_type = f"BLINK_{mapped_key}"
                else:
                    action_type = mapped_key

            # Clean up modifier state
            if key in self.key_modifier_state:
                del self.key_modifier_state[key]

            press_duration = max(50, press_duration)
            new_action = Action(action_type, press_duration, 500)
            self.recorded_pattern.append(new_action)
            self.last_release_time = release_time

            self.schedule_reload_table()

        self.draw_hud()

    def on_global_key_event(self, event):
        """TODO: add documentation"""
        if not self.recording_active or not self.global_active:
            return

        key_name = event.name.lower()

        # Handle Shift keys
        if "shift" in key_name:
            if event.event_type == "down":
                self.shift_pressed = True

                # CASE B: Shift is pressed while a directional key is already held down (Direction first, then Shift)
                directional_keys = ["left", "right", "up", "down"]
                for dir_key in directional_keys:
                    if self.keys_down.get(dir_key, False):
                        self.key_modifier_state[dir_key] = True
            else:
                self.shift_pressed = False
            return

        # Check if mapped
        global_mappings = {
            "up": "UP",
            "left": "LEFT",
            "down": "DOWN",
            "right": "RIGHT",
            "a": "A",
            "shift": "SHIFT",
            "left shift": "SHIFT",
            "right shift": "SHIFT",
            "alt": "ALT",
            "left alt": "ALT",
            "right alt": "ALT",
            "space": "SPACE",
        }

        if key_name not in global_mappings:
            return

        mapped_action = global_mappings[key_name]

        if event.event_type == "down":
            if self.keys_down.get(key_name, False):
                return
            self.keys_down[key_name] = True

            # Triple-safety Shift detection for global mode
            shift_held = False
            try:
                import keyboard

                shift_held = (
                    keyboard.is_pressed("shift")
                    or keyboard.is_pressed("left shift")
                    or keyboard.is_pressed("right shift")
                )
            except Exception as e:
                print("Error occurred")
                pass
            if not shift_held:
                shift_held = self.shift_pressed

            self.key_modifier_state[key_name] = shift_held

            press_time = time.time()
            self.key_press_times[key_name] = press_time

            # Calculate delay duration for previous item
            if self.last_release_time is not None and len(self.recorded_pattern) > 0:
                delay_sec = press_time - self.last_release_time
                delay_ms = int(delay_sec * 1000)
                self.recorded_pattern[-1].delay_duration = delay_ms
                self.schedule_reload_table()

            self.draw_hud(key_pressed_display=key_name)

        elif event.event_type == "up":
            if not self.keys_down.get(key_name, False):
                return
            self.keys_down[key_name] = False

            press_time = self.key_press_times.get(key_name)
            if press_time is not None:
                release_time = time.time()
                press_duration = int((release_time - press_time) * 1000)
                press_duration = max(50, press_duration)

                if mapped_action in ("LEFT", "RIGHT", "UP", "DOWN"):
                    is_blink = self.key_modifier_state.get(key_name, False)
                    if is_blink:
                        action_type = f"BLINK_{mapped_action}"
                    else:
                        action_type = mapped_action
                else:
                    action_type = mapped_action

                # Clean up modifier state
                if key_name in self.key_modifier_state:
                    del self.key_modifier_state[key_name]

                new_action = Action(action_type, press_duration, 500)
                self.recorded_pattern.append(new_action)
                self.last_release_time = release_time

                self.schedule_reload_table()

            self.draw_hud()

    def schedule_reload_table(self):
        """TODO: add documentation"""
        if getattr(self, "_reload_timer", None) is not None:
            self.after_cancel(self._reload_timer)
        self._reload_timer = self.after(3000, self._do_reload_table)

    def _do_reload_table(self):
        """TODO: add documentation"""
        self._reload_timer = None
        self.reload_table()
        if self.recorded_pattern:
            last_idx = str(len(self.recorded_pattern) - 1)
            try:
                self.tree.selection_set(last_idx)
                self.tree.see(last_idx)
            except Exception as e:
                print("Error occurred")
                pass

    def reload_table(self):
        """TODO: add documentation"""
        # Clear table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Load values
        for i, action in enumerate(self.recorded_pattern):
            self.tree.insert(
                "",
                "end",
                iid=str(i),
                values=(i + 1, action.action_type, action.press_duration, action.delay_duration),
            )

    def on_row_select(self, event):
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        action = self.recorded_pattern[idx]

        self.action_var.set(action.action_type)
        self.press_var.set(action.press_duration)
        self.delay_var.set(action.delay_duration)

    def on_field_edited(self, event=None):
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        action = self.recorded_pattern[idx]

        try:
            action.action_type = self.action_var.get()
            action.press_duration = max(50, int(self.press_var.get()))
            action.delay_duration = max(0, int(self.delay_var.get()))

            # Update visually
            self.tree.item(
                str(idx),
                values=(idx + 1, action.action_type, action.press_duration, action.delay_duration),
            )
        except ValueError:
            pass

    def delete_selected_row(self):
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])

        self.recorded_pattern.pop(idx)
        self.reload_table()

        if self.recorded_pattern:
            new_idx = str(min(idx, len(self.recorded_pattern) - 1))
            self.tree.selection_set(new_idx)

    def clear_recording(self):
        """TODO: add documentation"""
        if not self.recorded_pattern:
            return
        if messagebox.askyesno(
            "Bersihkan Rekaman", "Apakah Anda yakin ingin menghapus seluruh hasil rekaman ini?"
        ):
            self.recorded_pattern.clear()
            self.last_release_time = None
            self.reload_table()
            self.draw_hud()

    def save_to_profile(self):
        """TODO: add documentation"""
        if not self.recorded_pattern:
            messagebox.showwarning(
                "Rekaman Kosong", "Hasil rekaman kosong. Silakan merekam tombol terlebih dahulu."
            )
            return

        if messagebox.askyesno(
            "Konfirmasi Simpan",
            f"Apakah Anda yakin ingin menyimpan {len(self.recorded_pattern)} aksi rekaman ke Manajer Profil?",
        ):
            self.profile.pattern = list(self.recorded_pattern)

            # Validasi hanya pola
            issues = []
            has_physical_action = any(act.action_type != "NONE" for act in self.profile.pattern)
            if not has_physical_action:
                issues.append(
                    "KRITIS: Pola tidak berisi aksi tombol fisik sama sekali (semua aksi adalah 'NONE')."
                )
            if len(self.profile.pattern) > 150:
                issues.append("KRITIS: Jumlah aksi melebihi batas firmware (150).")
            for idx, act in enumerate(self.profile.pattern):
                if act.action_type != "NONE" and act.press_duration < 50:
                    issues.append(
                        f"KRITIS: Aksi #{idx+1} ({act.action_type}) memiliki durasi tekan terlalu rendah ({act.press_duration}ms). Minimum adalah 50ms."
                    )
                if act.delay_duration < 0:
                    issues.append(f"KRITIS: Jeda aksi #{idx+1} tidak boleh negatif.")
            if issues:
                error_msg = "Pola makro memiliki kesalahan kritis dan tidak dapat disimpan:\n\n"
                for iss in issues:
                    error_msg += f"• {iss}\n"
                messagebox.showerror("Validasi Pola Gagal", error_msg)
                return

            import json
            import os

            file_path = getattr(self.profile, "file_path", None)

            # 1. Dapatkan JSON dasar yang akan diperbarui (untuk mempertahankan data kalibrasi)
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

            # 2. Ambil data profil saat ini, tapi pertahankan kalibrasi servos dari base_dict
            current_dict = self.profile.to_dict()
            current_dict["servos"] = base_dict.get("servos", current_dict["servos"])

            updated_json_str = json.dumps(current_dict, indent=4)

            try:
                self.profile.load_from_json(updated_json_str)
            except Exception as e:
                print("Error occurred")
                messagebox.showerror("Error", f"Gagal memuat profil setelah update pola: {str(e)}")
                return

            if file_path:
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(updated_json_str)
                    fname = os.path.basename(file_path)
                    self.connection.log(f"[Perekam] Profil berhasil disimpan ke berkas: {fname}")
                except Exception as e:
                    print("Error occurred")
                    messagebox.showerror("Error", f"Gagal menyimpan profil ke berkas: {str(e)}")
                    return
            else:
                self.connection.log("[Perekam] Pola berhasil diperbarui di memori aktif.")

            if hasattr(self, "on_profile_updated") and self.on_profile_updated:
                self.on_profile_updated()

            messagebox.showinfo(
                "Berhasil",
                "Pola makro berhasil disimpan ke Manajer Profil (Editor) tanpa menimpa kalibrasi servo!",
            )

    def open_json_editor(self):
        """TODO: add documentation"""
        # Create a premium JSON raw editor dialog
        dialog = tk.Toplevel(self)
        dialog.title("Editor JSON Makro Mentah")
        dialog.geometry("600x500")
        dialog.configure(bg="#1a1a24")
        dialog.transient(self.winfo_toplevel())
        dialog.grab_set()

        # Premium dialog title
        lbl_title = tk.Label(
            dialog,
            text="📝 Edit Pola Sebagai Teks JSON",
            font=("Helvetica", 12, "bold"),
            bg="#1a1a24",
            fg="#dec0f1",
        )
        lbl_title.pack(pady=10)

        # Frame for Text area
        text_frame = ttk.Frame(dialog, padding=10)
        text_frame.pack(fill="both", expand=True, padx=15, pady=5)
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)

        # JSON Text editor
        json_text = tk.Text(
            text_frame, bg="#13131c", fg="#2ed573", font=("Consolas", 10), wrap="none", bd=0
        )
        json_text.grid(row=0, column=0, sticky="nsew")

        # Scrollbars
        sb_y = ttk.Scrollbar(text_frame, orient="vertical", command=json_text.yview)
        sb_y.grid(row=0, column=1, sticky="ns")
        sb_x = ttk.Scrollbar(text_frame, orient="horizontal", command=json_text.xview)
        sb_x.grid(row=1, column=0, sticky="ew")

        json_text.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)

        # Convert active recorded pattern to formatted JSON string
        pattern_dict = [a.to_dict() for a in self.recorded_pattern]
        json_str = json.dumps(pattern_dict, indent=4)
        json_text.insert("1.0", json_str)

        # Action Buttons frame
        btn_frame = ttk.Frame(dialog, padding=10)
        btn_frame.pack(fill="x", pady=10)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        def apply_json():
            """TODO: add documentation"""
            raw_val = json_text.get("1.0", "end-1c").strip()
            try:
                data = json.loads(raw_val)
                if not isinstance(data, list):
                    raise ValueError("JSON teratas harus berupa sebuah LIST []")

                # Parse and validate actions
                new_actions = []
                for idx, item in enumerate(data):
                    if not isinstance(item, dict):
                        raise ValueError(f"Baris ke-{idx+1} harus berupa objek DICT {{}}")

                    act_type = item.get("action_type", "NONE")
                    if act_type not in Action.TYPES:
                        raise ValueError(
                            f"Baris ke-{idx+1}: Tipe aksi '{act_type}' tidak didukung.\nPilihan yang tersedia: {Action.TYPES}"
                        )

                    press_dur = max(50, int(item.get("press_duration", 200)))
                    delay_dur = max(0, int(item.get("delay_duration", 500)))

                    new_actions.append(Action(act_type, press_dur, delay_dur))

                self.recorded_pattern = new_actions
                self.reload_table()
                self.draw_hud()
                dialog.destroy()
                messagebox.showinfo("Berhasil", "Perubahan JSON berhasil diterapkan ke rekaman!")
            except Exception as e:
                print("Error occurred")
                messagebox.showerror(
                    "Kesalahan Validasi JSON",
                    f"Format JSON tidak valid atau ada nilai yang salah:\n\n{str(e)}",
                )

        btn_apply = tk.Button(
            btn_frame,
            text="💾 TERAPKAN PERUBAHAN JSON",
            font=("Segoe UI", 10, "bold"),
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            relief="flat",
            bd=0,
            height=2,
            command=apply_json,
        )
        btn_apply.grid(row=0, column=0, padx=5, sticky="ew")

        btn_cancel = tk.Button(
            btn_frame,
            text="❌ BATAL",
            font=("Segoe UI", 10, "bold"),
            bg="#57606f",
            fg="white",
            activebackground="#747d8c",
            relief="flat",
            bd=0,
            height=2,
            command=dialog.destroy,
        )
        btn_cancel.grid(row=0, column=1, padx=5, sticky="ew")

    def draw_hud(self, key_pressed_display=None):
        """TODO: add documentation"""
        self.hud_canvas.delete("all")
        w = self.hud_canvas.winfo_width()
        h = self.hud_canvas.winfo_height()
        if w < 10 or h < 10:
            return

        # Title
        self.hud_canvas.create_text(
            w / 2,
            30,
            text="🖥 MONITOR PEREKAMAN",
            fill="#747d8c",
            font=("Helvetica", 10, "bold"),
            anchor="center",
        )

        # Recording Status Circle Indicator
        cy = h / 2.5
        cx = w / 2

        if self.recording_active:
            if self.global_active:
                text_status = "GLOBAL RECORDING ACTIVE"
                text_color = "#2ed573"  # Bright green for global
                self.hud_canvas.create_oval(
                    cx - 45, cy - 45, cx + 45, cy + 45, fill="#2ed573", outline="", stipple="gray25"
                )
                self.hud_canvas.create_oval(
                    cx - 30, cy - 30, cx + 30, cy + 30, fill="#2ed573", outline="#ffffff", width=2
                )
            else:
                text_status = "FOCUS RECORDING ACTIVE"
                text_color = "#ff4757"
                self.hud_canvas.create_oval(
                    cx - 45, cy - 45, cx + 45, cy + 45, fill="#ff4757", outline="", stipple="gray25"
                )
                self.hud_canvas.create_oval(
                    cx - 30, cy - 30, cx + 30, cy + 30, fill="#ff2f44", outline="#ffffff", width=2
                )
        else:
            text_status = "READY TO RECORD"
            text_color = "#a4b0be"
            self.hud_canvas.create_oval(
                cx - 30, cy - 30, cx + 30, cy + 30, fill="#1a1a24", outline="#747d8c", width=2
            )

        # Status text
        self.hud_canvas.create_text(
            cx,
            cy + 60,
            text=text_status,
            fill=text_color,
            font=("Consolas", 11, "bold"),
            anchor="center",
        )

        # Stats info summary
        steps_count = len(self.recorded_pattern)
        total_time_sec = (
            sum(a.press_duration + a.delay_duration for a in self.recorded_pattern) / 1000.0
        )
        stats_text = f"Total Aksi: {steps_count} | Total Estimasi Durasi: {total_time_sec:.2f} dtk"
        self.hud_canvas.create_text(
            w / 2, h - 60, text=stats_text, fill="#ffffff", font=("Helvetica", 10), anchor="center"
        )

        # Last key HUD display
        if self.recording_active:
            key_text = (
                "Menunggu Tombol..."
                if not key_pressed_display
                else f"TEKAN: {key_pressed_display.upper()}"
            )
            k_col = "#dec0f1" if key_pressed_display else "#747d8c"
            self.hud_canvas.create_text(
                w / 2,
                h - 30,
                text=key_text,
                fill=k_col,
                font=("Consolas", 12, "bold"),
                anchor="center",
            )
        else:
            self.hud_canvas.create_text(
                w / 2,
                h - 30,
                text="Klik 'Mulai Perekaman' lalu ketik",
                fill="#747d8c",
                font=("Helvetica", 9, "italic"),
                anchor="center",
            )

    def reload_from_profile(self):
        """TODO: add documentation"""
        self.recorded_pattern = list(self.profile.pattern)
        self.reload_table()
        self.draw_hud()
