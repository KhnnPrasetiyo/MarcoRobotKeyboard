"""TODO: module documentation"""

import random
import tkinter as tk
from tkinter import ttk


class SimulationTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.simulating = False
        self.current_step = 0
        self.sim_job = None

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

        self.action_to_keysym = {
            "LEFT": "Left",
            "RIGHT": "Right",
            "UP": "Up",
            "DOWN": "Down",
            "SHIFT": "Shift_L",
            "A": "a",
        }

        # Pressed state tracker: maps keysym -> boolean
        self.keys_pressed = {}
        for label, unit_x, unit_y, unit_w, unit_h, keysym in self.keyboard_layout:
            self.keys_pressed[keysym] = False

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # 1. Left side: Simulation Arena (Canvas)
        arena_frame = ttk.LabelFrame(self, text=" Arena Robot Virtual ", padding=15)
        arena_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        arena_frame.columnconfigure(0, weight=1)
        arena_frame.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            arena_frame, bg="#13131c", highlightthickness=0, width=600, height=400
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")

        side_panel = ttk.LabelFrame(self, text=" Panel Simulasi ", padding=15)
        side_panel.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        side_panel.columnconfigure(0, weight=1)
        side_panel.rowconfigure(5, weight=1)

        self.btn_run = tk.Button(
            side_panel,
            text="▶ MULAI SIMULASI",
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.toggle_simulation,
        )
        self.btn_run.pack(fill="x", pady=(0, 12))
        self.btn_run.bind(
            "<Enter>",
            lambda e: (
                self.btn_run.config(bg="#26af5f")
                if not self.simulating
                else self.btn_run.config(bg="#ff6b81")
            ),
        )
        self.btn_run.bind(
            "<Leave>",
            lambda e: (
                self.btn_run.config(bg="#2ed573")
                if not self.simulating
                else self.btn_run.config(bg="#ff4757")
            ),
        )

        # Status info cards
        info_frame = tk.Frame(side_panel, bg="#13131c", bd=1, relief="solid", padx=12, pady=10)
        info_frame.pack(fill="x", pady=(0, 10))

        self.lbl_step = tk.Label(
            info_frame,
            text="Langkah: - / -",
            font=("Consolas", 9, "bold"),
            fg="#38bdf8",
            bg="#13131c",
            anchor="w",
        )
        self.lbl_step.pack(fill="x", pady=2)

        self.lbl_action = tk.Label(
            info_frame,
            text="Aksi: None",
            font=("Consolas", 9),
            fg="#dec0f1",
            bg="#13131c",
            anchor="w",
        )
        self.lbl_action.pack(fill="x", pady=2)

        self.lbl_servo_state = tk.Label(
            info_frame,
            text="Servo: UP",
            font=("Consolas", 9),
            fg="#4ade80",
            bg="#13131c",
            anchor="w",
        )
        self.lbl_servo_state.pack(fill="x", pady=2)

        self.lbl_delay = tk.Label(
            info_frame,
            text="Jeda: 0ms",
            font=("Consolas", 9),
            fg="#94a3b8",
            bg="#13131c",
            anchor="w",
        )
        self.lbl_delay.pack(fill="x", pady=2)

        self.focus_btn = tk.Button(
            side_panel,
            text="🔌 Klik Tangkap Input Keyboard",
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
        )
        self.focus_btn.pack(fill="x", pady=(0, 10))
        self.focus_btn.bind(
            "<Button-1>",
            lambda e: (
                self.focus_btn.focus_set(),
                self.focus_btn.config(text="🟢 Aktif — Tekan Tombol!", bg="#2ed573"),
            ),
        )
        self.focus_btn.bind(
            "<FocusOut>",
            lambda e: self.focus_btn.config(text="🔌 Klik Tangkap Input Keyboard", bg="#ff75a0"),
        )
        self.focus_btn.bind("<KeyPress>", lambda e: self.on_key_press(e))
        self.focus_btn.bind("<KeyRelease>", lambda e: self.on_key_release(e))

        # macOS-styled trace log terminal
        tk.Label(
            side_panel,
            text="📋  LOG JEJAK SIMULASI",
            font=("Segoe UI", 8, "bold"),
            fg="#64748b",
            bg="#1a1a24",
            anchor="w",
        ).pack(fill="x", pady=(5, 4))

        term_wrap = tk.Frame(
            side_panel,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
            highlightcolor="#47475c",
        )
        term_wrap.pack(fill="both", expand=True)
        term_wrap.columnconfigure(0, weight=1)
        term_wrap.rowconfigure(1, weight=1)

        hdr_sim = tk.Frame(term_wrap, bg="#1b1b26", height=28)
        hdr_sim.pack(fill="x")
        dots_s = tk.Frame(hdr_sim, bg="#1b1b26")
        dots_s.pack(side="left", padx=8, pady=4)
        tk.Label(dots_s, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 9, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots_s, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 9, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots_s, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 9, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(
            hdr_sim, text="sim@kbd-robot", font=("Consolas", 8, "bold"), fg="#94a3b8", bg="#1b1b26"
        ).pack(side="left", padx=4)

        text_wrap_sim = tk.Frame(term_wrap, bg="#13131c")
        text_wrap_sim.pack(fill="both", expand=True, padx=2, pady=2)
        text_wrap_sim.columnconfigure(0, weight=1)
        text_wrap_sim.rowconfigure(0, weight=1)

        self.trace_list = tk.Text(
            text_wrap_sim,
            bg="#13131c",
            fg="#e2e8f0",
            font=("Consolas", 8),
            wrap="word",
            bd=0,
            padx=8,
            pady=6,
            spacing1=2,
            spacing3=2,
            selectbackground="#47475c",
            insertbackground="#ffffff",
        )
        self.trace_list.grid(row=0, column=0, sticky="nsew")
        sb_sim = ttk.Scrollbar(text_wrap_sim, orient="vertical", command=self.trace_list.yview)
        sb_sim.grid(row=0, column=1, sticky="ns")
        self.trace_list.configure(yscrollcommand=sb_sim.set)
        self.trace_list.tag_config("ts", foreground="#64748b")
        self.trace_list.tag_config("info", foreground="#38bdf8")
        self.trace_list.tag_config("ok", foreground="#4ade80")
        self.trace_list.tag_config("warn", foreground="#dec0f1")
        self.trace_list.tag_config("err", foreground="#f87171")
        self.trace_list.config(state="disabled")

        self.canvas.bind("<Configure>", lambda e: self.draw_arena())
        self.canvas.focus_set()

    def draw_arena(self, active_servos=None):
        """TODO: add documentation"""
        if active_servos is None:
            active_servos = {}
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 10 or h < 10:
            return
        self.canvas.create_text(
            w / 2,
            30,
            text="Simulasi Rig Servo Keyboard Arduino Nano",
            fill="#ffffff",
            font=("Helvetica", 12, "bold"),
            anchor="center",
        )
        gap = 3
        padding_x = 15
        padding_y = 15
        u_width = (w - 2 * padding_x - 22 * gap) / 23.0
        key_h = (h - 2 * padding_y - 5 * gap - 40) / 6.3
        u_width = max(10, min(u_width, 45))
        key_h = max(10, min(key_h, u_width * 0.9))
        kbd_w = 23.0 * u_width + 22 * gap
        kbd_h = 6.3 * key_h + 5 * gap
        start_x = (w - kbd_w) / 2
        start_y = (h - kbd_h - 20) / 2
        pressed_keys = set()
        for act in active_servos:
            ks = self.action_to_keysym.get(act)
            if ks:
                pressed_keys.add(ks)
        for label, unit_x, unit_y, unit_w, unit_h, keysym in self.keyboard_layout:
            key_x = start_x + unit_x * (u_width + gap)
            key_y = start_y + unit_y * (key_h + gap)
            key_w = unit_w * u_width + (unit_w - 1.0) * gap
            key_h_actual = unit_h * key_h + (unit_h - 1.0) * gap
            is_pressed = self.keys_pressed.get(keysym, False) or (keysym in pressed_keys)
            is_robot_key = keysym in self.key_to_servo
            if is_pressed:
                fill_col = "#2ed573"
                outline_col = "#ffffff"
                txt_col = "#ffffff"
            else:
                if is_robot_key:
                    fill_col = "#1a1a24"
                    outline_col = "#dec0f1"
                    txt_col = "#dec0f1"
                else:
                    fill_col = "#1a1a24"
                    outline_col = "#57606f"
                    txt_col = "#a4b0be"
            self.canvas.create_rectangle(
                key_x,
                key_y,
                key_x + key_w,
                key_y + key_h_actual,
                fill=fill_col,
                outline=outline_col,
                width=2,
            )
            font_sz = 8 if len(label) > 4 else 9
            font_weight = "bold" if (is_robot_key or is_pressed) else "normal"
            self.canvas.create_text(
                key_x + key_w / 2,
                key_y + key_h_actual / 2,
                text=label,
                fill=txt_col,
                font=("Helvetica", font_sz, font_weight),
            )

    def on_key_press(self, event):
        """TODO: add documentation"""
        key = event.keysym
        target = None
        if key in self.keys_pressed:
            target = key
        elif key.lower() in self.keys_pressed:
            target = key.lower()
        elif key in self.keysym_aliases:
            target = self.keysym_aliases[key]
        elif key.lower() in self.keysym_aliases:
            target = self.keysym_aliases[key.lower()]
        if target and not self.keys_pressed.get(target, False):
            self.keys_pressed[target] = True
            self.draw_arena()
            if self.connection.connected:
                servo_idx = self.key_to_servo.get(target)
                if servo_idx is not None:
                    angle = self.profile.servos[servo_idx].press_angle
                    self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")

    def on_key_release(self, event):
        """TODO: add documentation"""
        key = event.keysym
        released = []
        if key in self.keys_pressed:
            released.append(key)
        elif key.lower() in self.keys_pressed:
            released.append(key.lower())
        elif key in self.keysym_aliases:
            released.append(self.keysym_aliases[key])
        elif key.lower() in self.keysym_aliases:
            released.append(self.keysym_aliases[key.lower()])
        if "Shift" in key:
            released.extend(["Shift_L", "Shift_R"])
        for tgt in released:
            if self.keys_pressed.get(tgt, False):
                self.keys_pressed[tgt] = False
                self.draw_arena()
                if self.connection.connected:
                    servo_idx = self.key_to_servo.get(tgt)
                    if servo_idx is not None:
                        angle = self.profile.servos[servo_idx].up_angle
                        self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")

    def toggle_simulation(self):
        """TODO: add documentation"""
        if self.simulating:
            self.stop_simulation()
        else:
            self.start_simulation()

    def start_simulation(self):
        """TODO: add documentation"""
        if not self.profile.pattern:
            self.trace_log("Error: Pola kosong. Tambahkan aksi terlebih dahulu.")
            return
        self.simulating = True
        self.current_step = 0
        self.btn_run.config(text="⏹ HENTIKAN SIMULASI", bg="#ff4757", activebackground="#ff6b81")
        # Clear the Text widget log (not Listbox)
        self.trace_list.config(state="normal")
        self.trace_list.delete("1.0", tk.END)
        self.trace_list.config(state="disabled")
        self.trace_log("Simulasi dimulai...")
        self.run_next_step()

    def stop_simulation(self):
        """TODO: add documentation"""
        self.simulating = False
        if self.sim_job:
            self.after_cancel(self.sim_job)
            self.sim_job = None
        self.btn_run.config(text="▶ MULAI SIMULASI", bg="#2ed573", activebackground="#26af5f")
        self.lbl_step.config(text="Langkah: - / -")
        self.lbl_action.config(text="Aksi: None")
        self.lbl_servo_state.config(text="Servo: UP")
        self.lbl_delay.config(text="Jeda: 0ms")
        self.trace_log("Simulasi dihentikan.")
        self.draw_arena()

    def trace_log(self, msg):
        """TODO: add documentation"""
        import time

        self.trace_list.config(state="normal")
        t = time.strftime("%H:%M:%S")
        self.trace_list.insert(tk.END, f"[{t}] ", "ts")
        low = msg.lower()
        if "error" in low or "gagal" in low or "kosong" in low:
            self.trace_list.insert(tk.END, f"{msg}\n", "err")
        elif "selesai" in low or "berhasil" in low or "sukses" in low:
            self.trace_list.insert(tk.END, f"{msg}\n", "ok")
        elif "diacak" in low or "jeda" in low or "===" in low:
            self.trace_list.insert(tk.END, f"{msg}\n", "warn")
        else:
            self.trace_list.insert(tk.END, f"{msg}\n", "info")
        self.trace_list.see(tk.END)
        self.trace_list.config(state="disabled")

    def run_next_step(self):
        """TODO: add documentation"""
        if not self.simulating:
            return

        total_steps = len(self.profile.pattern)
        if self.current_step >= total_steps:
            # Check loop settings
            if self.profile.loop_mode == "INFINITY":
                self.current_step = 0
                self.trace_log("=== Mengulang Loop Tak Terbatas ===")
            else:
                self.stop_simulation()
                return

        action = self.profile.pattern[self.current_step]
        self.lbl_step.config(text=f"Langkah: {self.current_step + 1} / {total_steps}")
        self.lbl_action.config(text=f"Aksi: {action.action_type}")

        # Set delay for pressing duration
        def release_servos():
            """TODO: add documentation"""
            if not self.simulating:
                return
            self.lbl_servo_state.config(text="Servo: UP")
            self.draw_arena()

            # Delay duration
            delay_duration = action.delay_duration
            if self.profile.random_delay_enabled:
                delay_duration = random.randint(
                    self.profile.random_delay_min, self.profile.random_delay_max
                )
                self.trace_log(f"  Jeda (Diacak): {delay_duration}ms")
            else:
                self.trace_log(f"  Jeda: {delay_duration}ms")

            self.lbl_delay.config(text=f"Sisa jeda: {delay_duration}ms")

            def next_action_trigger():
                """TODO: add documentation"""
                self.current_step += 1
                self.run_next_step()

            self.sim_job = self.after(delay_duration, next_action_trigger)

        # Staggered logic for direction + Shift keys (BLINK actions)
        if action.action_type.startswith("BLINK_"):
            blink_key = action.action_type.replace("BLINK_", "")
            self.trace_log(f"[{action.action_type}] Menekan {blink_key} (jeda staggered)...")

            active_servos = {blink_key: True}
            self.draw_arena(active_servos)
            self.lbl_servo_state.config(text="Servo: TEKAN (Arah)")

            stagger_delay = 150
            if action.press_duration > stagger_delay:

                def step_phase_2():
                    """TODO: add documentation"""
                    if not self.simulating:
                        return
                    self.trace_log(f"[{action.action_type}] Menekan SHIFT (keduanya tertahan)")
                    active_servos["SHIFT"] = True
                    self.draw_arena(active_servos)
                    self.lbl_servo_state.config(text="Servo: TEKAN (Arah + SHIFT)")

                    remaining_press = action.press_duration - stagger_delay
                    self.sim_job = self.after(remaining_press, release_servos)

                self.sim_job = self.after(stagger_delay, step_phase_2)
            else:
                self.sim_job = self.after(action.press_duration, release_servos)
        else:
            active_servos = {}
            if action.action_type == "NONE":
                self.trace_log(
                    f"[{action.action_type}] Jeda kosong (durasi: {action.press_duration}ms)"
                )
            else:
                self.trace_log(
                    f"[{action.action_type}] Menekan {action.action_type} (durasi: {action.press_duration}ms)"
                )
                active_servos[action.action_type] = True
                self.lbl_servo_state.config(text="Servo: TEKAN")

            self.draw_arena(active_servos)
            self.sim_job = self.after(action.press_duration, release_servos)
