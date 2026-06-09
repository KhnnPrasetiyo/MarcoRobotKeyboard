"""TODO: module documentation"""

import tkinter as tk
from tkinter import ttk


class KeyboardTesterTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        card = ttk.LabelFrame(self, text=" Penguji Keyboard Interaktif (Full Layout) ", padding=20)
        card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        card.columnconfigure(0, weight=1)
        card.rowconfigure(2, weight=1)

        desc = tk.Label(
            card,
            text="Klik tombol biru di bawah, lalu ketik tombol apa saja di keyboard fisik Anda.\nTombol virtual akan menyala hijau untuk memverifikasi pemetaan dan koneksi.",
            font=("Segoe UI", 9),
            fg="#94a3b8",
            bg="#1a1a24",
            justify="center",
        )
        desc.grid(row=0, column=0, pady=(0, 15))

        # Control Switch Frame
        self.tester_active = True

        switch_frame = ttk.Frame(card)
        switch_frame.grid(row=1, column=0, pady=10, sticky="ew")
        switch_frame.columnconfigure(0, weight=1)
        switch_frame.columnconfigure(1, weight=1)

        self.btn_switch = tk.Button(
            switch_frame,
            text="🟢 STATUS PENGUJI: AKTIF (ON)",
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.toggle_tester_state,
        )
        self.btn_switch.grid(row=0, column=0, padx=5, sticky="ew")
        self.btn_switch.bind(
            "<Enter>",
            lambda e: (
                self.btn_switch.config(bg="#26af5f")
                if self.tester_active
                else self.btn_switch.config(bg="#ff6b81")
            ),
        )
        self.btn_switch.bind(
            "<Leave>",
            lambda e: (
                self.btn_switch.config(bg="#2ed573")
                if self.tester_active
                else self.btn_switch.config(bg="#ff4757")
            ),
        )

        # Input focus area indicator
        self.focus_btn = tk.Button(
            switch_frame,
            text="🔌 Klik Tangkap Input Keyboard",
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
        )
        self.focus_btn.grid(row=0, column=1, padx=5, sticky="ew")
        self.focus_btn.bind(
            "<Enter>", lambda e: self.focus_btn.config(bg="#ff9ff3") if self.tester_active else None
        )
        self.focus_btn.bind(
            "<Leave>", lambda e: self.focus_btn.config(bg="#ff75a0") if self.tester_active else None
        )

        # Canvas keyboard grid
        self.canvas = tk.Canvas(card, bg="#13131c", highlightthickness=0)
        self.canvas.grid(row=2, column=0, sticky="nsew", pady=10)

        # Bind events
        self.focus_btn.bind(
            "<Button-1>",
            lambda e: (
                (
                    self.focus_btn.focus_set(),
                    self.focus_btn.config(text="🟢 Aktif — Tekan Tombol!", bg="#2ed573"),
                )
                if self.tester_active
                else "break"
            ),
        )
        self.focus_btn.bind(
            "<FocusOut>",
            lambda e: (
                self.focus_btn.config(text="🔌 Klik Tangkap Input Keyboard", bg="#ff75a0")
                if self.tester_active
                else "break"
            ),
        )

        self.focus_btn.bind("<KeyPress>", self.on_key_press)
        self.focus_btn.bind("<KeyRelease>", self.on_key_release)

        # Key-to-servo mapping based on RobotProfile indices: LEFT=0, RIGHT=1, UP=2, DOWN=3, SHIFT=4, A=5
        self.key_to_servo = {"Shift_L": 4, "a": 5, "Up": 2, "Left": 0, "Down": 3, "Right": 1}

        # Flat 100% Keyboard Layout definition
        # Each item is (label, unit_x, unit_y, unit_w, unit_h, keysym)
        self.keyboard_layout = [
            # --- Function Row (y = 0.0) ---
            ("Esc", 0.0, 0.0, 1.0, 1.0, "Escape"),
            ("F1", 2.0, 0.0, 1.0, 1.0, "F1"),
            ("F2", 3.0, 0.0, 1.0, 1.0, "F2"),
            ("F3", 4.0, 0.0, 1.0, 1.0, "F3"),
            ("F4", 5.0, 0.0, 1.0, 1.0, "F4"),
            ("F5", 6.5, 0.0, 1.0, 1.0, "F5"),
            ("F6", 7.5, 0.0, 1.0, 1.0, "F6"),
            ("F7", 8.5, 0.0, 1.0, 1.0, "F7"),
            ("F8", 9.5, 0.0, 1.0, 1.0, "F8"),
            ("F9", 11.0, 0.0, 1.0, 1.0, "F9"),
            ("F10", 12.0, 0.0, 1.0, 1.0, "F10"),
            ("F11", 13.0, 0.0, 1.0, 1.0, "F11"),
            ("F12", 14.0, 0.0, 1.0, 1.0, "F12"),
            ("PrtSc", 15.5, 0.0, 1.0, 1.0, "Print"),
            ("ScrLk", 16.5, 0.0, 1.0, 1.0, "Scroll_Lock"),
            ("Pause", 17.5, 0.0, 1.0, 1.0, "Pause"),
            # --- Row 1 (y = 1.3) ---
            ("~", 0.0, 1.3, 1.0, 1.0, "grave"),
            ("1", 1.0, 1.3, 1.0, 1.0, "1"),
            ("2", 2.0, 1.3, 1.0, 1.0, "2"),
            ("3", 3.0, 1.3, 1.0, 1.0, "3"),
            ("4", 4.0, 1.3, 1.0, 1.0, "4"),
            ("5", 5.0, 1.3, 1.0, 1.0, "5"),
            ("6", 6.0, 1.3, 1.0, 1.0, "6"),
            ("7", 7.0, 1.3, 1.0, 1.0, "7"),
            ("8", 8.0, 1.3, 1.0, 1.0, "8"),
            ("9", 9.0, 1.3, 1.0, 1.0, "9"),
            ("0", 10.0, 1.3, 1.0, 1.0, "0"),
            ("-", 11.0, 1.3, 1.0, 1.0, "minus"),
            ("=", 12.0, 1.3, 1.0, 1.0, "equal"),
            ("Backspace", 13.0, 1.3, 2.0, 1.0, "BackSpace"),
            ("Ins", 15.5, 1.3, 1.0, 1.0, "Insert"),
            ("Home", 16.5, 1.3, 1.0, 1.0, "Home"),
            ("PgUp", 17.5, 1.3, 1.0, 1.0, "Prior"),
            ("Num", 19.0, 1.3, 1.0, 1.0, "Num_Lock"),
            ("/", 20.0, 1.3, 1.0, 1.0, "KP_Divide"),
            ("*", 21.0, 1.3, 1.0, 1.0, "KP_Multiply"),
            ("-", 22.0, 1.3, 1.0, 1.0, "KP_Subtract"),
            # --- Row 2 (y = 2.3) ---
            ("Tab", 0.0, 2.3, 1.5, 1.0, "Tab"),
            ("Q", 1.5, 2.3, 1.0, 1.0, "q"),
            ("W", 2.5, 2.3, 1.0, 1.0, "w"),
            ("E", 3.5, 2.3, 1.0, 1.0, "e"),
            ("R", 4.5, 2.3, 1.0, 1.0, "r"),
            ("T", 5.5, 2.3, 1.0, 1.0, "t"),
            ("Y", 6.5, 2.3, 1.0, 1.0, "y"),
            ("U", 7.5, 2.3, 1.0, 1.0, "u"),
            ("I", 8.5, 2.3, 1.0, 1.0, "i"),
            ("O", 9.5, 2.3, 1.0, 1.0, "o"),
            ("P", 10.5, 2.3, 1.0, 1.0, "p"),
            ("[", 11.5, 2.3, 1.0, 1.0, "bracketleft"),
            ("]", 12.5, 2.3, 1.0, 1.0, "bracketright"),
            ("\\", 13.5, 2.3, 1.5, 1.0, "backslash"),
            ("Del", 15.5, 2.3, 1.0, 1.0, "Delete"),
            ("End", 16.5, 2.3, 1.0, 1.0, "End"),
            ("PgDn", 17.5, 2.3, 1.0, 1.0, "Next"),
            ("7", 19.0, 2.3, 1.0, 1.0, "KP_7"),
            ("8", 20.0, 2.3, 1.0, 1.0, "KP_8"),
            ("9", 21.0, 2.3, 1.0, 1.0, "KP_9"),
            ("+", 22.0, 2.3, 1.0, 2.0, "KP_Add"),
            # --- Row 3 (y = 3.3) ---
            ("Caps", 0.0, 3.3, 1.75, 1.0, "Caps_Lock"),
            ("A", 1.75, 3.3, 1.0, 1.0, "a"),
            ("S", 2.75, 3.3, 1.0, 1.0, "s"),
            ("D", 3.75, 3.3, 1.0, 1.0, "d"),
            ("F", 4.75, 3.3, 1.0, 1.0, "f"),
            ("G", 5.75, 3.3, 1.0, 1.0, "g"),
            ("H", 6.75, 3.3, 1.0, 1.0, "h"),
            ("J", 7.75, 3.3, 1.0, 1.0, "j"),
            ("K", 8.75, 3.3, 1.0, 1.0, "k"),
            ("L", 9.75, 3.3, 1.0, 1.0, "l"),
            (";", 10.75, 3.3, 1.0, 1.0, "semicolon"),
            ("'", 11.75, 3.3, 1.0, 1.0, "apostrophe"),
            ("Enter", 12.75, 3.3, 2.25, 1.0, "Return"),
            ("4", 19.0, 3.3, 1.0, 1.0, "KP_4"),
            ("5", 20.0, 3.3, 1.0, 1.0, "KP_5"),
            ("6", 21.0, 3.3, 1.0, 1.0, "KP_6"),
            # --- Row 4 (y = 4.3) ---
            ("Shift L", 0.0, 4.3, 2.25, 1.0, "Shift_L"),
            ("Z", 2.25, 4.3, 1.0, 1.0, "z"),
            ("X", 3.25, 4.3, 1.0, 1.0, "x"),
            ("C", 4.25, 4.3, 1.0, 1.0, "c"),
            ("V", 5.25, 4.3, 1.0, 1.0, "v"),
            ("B", 6.25, 4.3, 1.0, 1.0, "b"),
            ("N", 7.25, 4.3, 1.0, 1.0, "n"),
            ("M", 8.25, 4.3, 1.0, 1.0, "m"),
            (",", 9.25, 4.3, 1.0, 1.0, "comma"),
            (".", 10.25, 4.3, 1.0, 1.0, "period"),
            ("/", 11.25, 4.3, 1.0, 1.0, "slash"),
            ("Shift R", 12.25, 4.3, 2.75, 1.0, "Shift_R"),
            ("▲", 16.5, 4.3, 1.0, 1.0, "Up"),
            ("1", 19.0, 4.3, 1.0, 1.0, "KP_1"),
            ("2", 20.0, 4.3, 1.0, 1.0, "KP_2"),
            ("3", 21.0, 4.3, 1.0, 1.0, "KP_3"),
            ("Ent", 22.0, 4.3, 1.0, 2.0, "KP_Enter"),
            # --- Row 5 (y = 5.3) ---
            ("Ctrl L", 0.0, 5.3, 1.25, 1.0, "Control_L"),
            ("Win", 1.25, 5.3, 1.25, 1.0, "Win_L"),
            ("Alt L", 2.5, 5.3, 1.25, 1.0, "Alt_L"),
            ("Spacebar", 3.75, 5.3, 6.25, 1.0, "space"),
            ("Alt R", 10.0, 5.3, 1.25, 1.0, "Alt_R"),
            ("Win", 11.25, 5.3, 1.25, 1.0, "Win_R"),
            ("Menu", 12.5, 5.3, 1.25, 1.0, "Menu"),
            ("Ctrl R", 13.75, 5.3, 1.25, 1.0, "Control_R"),
            ("◀", 15.5, 5.3, 1.0, 1.0, "Left"),
            ("▼", 16.5, 5.3, 1.0, 1.0, "Down"),
            ("▶", 17.5, 5.3, 1.0, 1.0, "Right"),
            ("0", 19.0, 5.3, 2.0, 1.0, "KP_0"),
            (".", 21.0, 5.3, 1.0, 1.0, "KP_Decimal"),
        ]

        # Shift / alternate physical key mapping aliases to main keysyms
        self.keysym_aliases = {
            "exclam": "1",
            "at": "2",
            "numbersign": "3",
            "dollar": "4",
            "percent": "5",
            "asciicircum": "6",
            "ampersand": "7",
            "asterisk": "8",
            "parenleft": "9",
            "parenright": "0",
            "underscore": "minus",
            "plus": "equal",
            "braceleft": "bracketleft",
            "braceright": "bracketright",
            "bar": "backslash",
            "colon": "semicolon",
            "quotedbl": "apostrophe",
            "less": "comma",
            "greater": "period",
            "question": "slash",
            "tilde": "grave",
            "asciitilde": "grave",
            "quoteleft": "grave",
            # NumLock OFF mapping to standard keypad keysyms
            "KP_Home": "KP_7",
            "KP_Up": "KP_8",
            "KP_Prior": "KP_9",
            "KP_Left": "KP_4",
            "KP_Begin": "KP_5",
            "KP_Right": "KP_6",
            "KP_End": "KP_1",
            "KP_Down": "KP_2",
            "KP_Next": "KP_3",
            "KP_Insert": "KP_0",
            "KP_Delete": "KP_Decimal",
        }

        # Pressed state tracker: maps keysym -> boolean
        self.keys_pressed = {}
        for label, unit_x, unit_y, unit_w, unit_h, keysym in self.keyboard_layout:
            self.keys_pressed[keysym] = False

        self.canvas.bind("<Configure>", lambda e: self.draw_keys())

    def draw_keys(self):
        """TODO: add documentation"""
        self.canvas.delete("all")

        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        if cw < 10 or ch < 10:
            return

        # Render instructions
        self.canvas.create_text(
            cw / 2,
            ch - 25,
            text="Tombol oranye = tombol fisik dikontrol motor servo robot Anda.",
            fill="#64748b",
            font=("Segoe UI", 9),
            anchor="center",
        )

        # Procedural dimensions based on 23.0 unit width and 6.3 unit height
        gap = 3
        padding_x = 15
        padding_y = 15

        # Determine spacing based on canvas size
        u_width = (cw - 2 * padding_x - 22 * gap) / 23.0
        key_h = (ch - 2 * padding_y - 5 * gap - 40) / 6.3

        # Make key square or slightly rectangular for best aesthetics
        u_width = max(10, min(u_width, 45))
        key_h = max(10, min(key_h, u_width * 0.9))

        # Calculate keyboard total width and height for centering
        kbd_w = 23.0 * u_width + 22 * gap
        kbd_h = 6.3 * key_h + 5 * gap

        # Centering offsets
        start_x = (cw - kbd_w) / 2
        start_y = (ch - kbd_h - 20) / 2

        for label, unit_x, unit_y, unit_w, unit_h, keysym in self.keyboard_layout:
            key_x = start_x + unit_x * (u_width + gap)
            key_y = start_y + unit_y * (key_h + gap)
            key_w = unit_w * u_width + (unit_w - 1.0) * gap
            key_h_actual = unit_h * key_h + (unit_h - 1.0) * gap

            # Colors based on pressed and mapping status
            is_pressed = self.keys_pressed.get(keysym, False)
            is_robot_key = keysym in self.key_to_servo

            if is_pressed:
                fill_col = "#4ade80"  # Bright green
                outline_col = "#ffffff"
                txt_col = "#0d1117"
            else:
                if is_robot_key:
                    fill_col = "#162032"  # Deep navy for robot keys
                    outline_col = "#dec0f1"  # Orange border for robot's mapped keys
                    txt_col = "#dec0f1"
                else:
                    fill_col = "#161b22"
                    outline_col = "#47475c"
                    txt_col = "#64748b"

            border_w = 2 if is_robot_key else 1
            self.canvas.create_rectangle(
                key_x,
                key_y,
                key_x + key_w,
                key_y + key_h_actual,
                fill=fill_col,
                outline=outline_col,
                width=border_w,
            )

            # Adjust text size for long labels
            font_sz = 8 if len(label) > 4 else 9
            font_weight = "bold" if (is_robot_key or is_pressed) else "normal"

            self.canvas.create_text(
                key_x + key_w / 2,
                key_y + key_h_actual / 2,
                text=label,
                fill=txt_col,
                font=("Helvetica", font_sz, font_weight),
                anchor="center",
            )

    def on_key_press(self, event):
        """TODO: add documentation"""
        if not self.tester_active:
            return
        key = event.keysym

        # Determine target keysym
        target_key = None
        if key in self.keys_pressed:
            target_key = key
        elif key.lower() in self.keys_pressed:
            target_key = key.lower()
        elif key in self.keysym_aliases:
            target_key = self.keysym_aliases[key]
        elif key.lower() in self.keysym_aliases:
            target_key = self.keysym_aliases[key.lower()]

        if target_key:
            if not self.keys_pressed[target_key]:
                self.keys_pressed[target_key] = True
                self.draw_keys()

                # Send TEST_SERVO press command if connected
                if self.connection.connected:
                    servo_idx = self.key_to_servo.get(target_key)
                    if servo_idx is not None:
                        angle = self.profile.servos[servo_idx].press_angle
                        self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")

    def on_key_release(self, event):
        """TODO: add documentation"""
        if not self.tester_active:
            return
        key = event.keysym

        released_keys = []
        if key in self.keys_pressed:
            released_keys.append(key)
        elif key.lower() in self.keys_pressed:
            released_keys.append(key.lower())
        elif key in self.keysym_aliases:
            released_keys.append(self.keysym_aliases[key])
        elif key.lower() in self.keysym_aliases:
            released_keys.append(self.keysym_aliases[key.lower()])

        # Handle Shift keys robustly
        if "Shift" in key:
            released_keys.append("Shift_L")
            released_keys.append("Shift_R")

        for target_key in released_keys:
            if target_key in self.keys_pressed and self.keys_pressed[target_key]:
                self.keys_pressed[target_key] = False
                self.draw_keys()

                # Send TEST_SERVO up command if connected
                if self.connection.connected:
                    servo_idx = self.key_to_servo.get(target_key)
                    if servo_idx is not None:
                        angle = self.profile.servos[servo_idx].up_angle
                        self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")

    def toggle_tester_state(self):
        """TODO: add documentation"""
        self.tester_active = not self.tester_active
        if self.tester_active:
            self.btn_switch.config(
                text="🟢 STATUS PENGUJI: AKTIF (ON)", bg="#2ed573", activebackground="#26af5f"
            )
            self.focus_btn.config(
                state="normal", text="🔌 Klik untuk Menangkap Input Keyboard", bg="#ff75a0"
            )
        else:
            self.btn_switch.config(
                text="🔴 STATUS PENGUJI: NONAKTIF (OFF)", bg="#ff4757", activebackground="#ff6b81"
            )
            self.focus_btn.config(state="disabled", text="⚠️ Penguji Dinonaktifkan", bg="#272736")

            # Reset all keys to released state
            for key_code in self.keys_pressed:
                if self.keys_pressed[key_code]:
                    self.keys_pressed[key_code] = False
                    if self.connection.connected:
                        servo_idx = self.key_to_servo.get(key_code)
                        if servo_idx is not None:
                            angle = self.profile.servos[servo_idx].up_angle
                            self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")
            self.draw_keys()
