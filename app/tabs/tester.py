import tkinter as tk
from tkinter import ttk

class KeyboardTesterTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        card = ttk.LabelFrame(self, text=" Penguji Keyboard Interaktif ", padding=20)
        card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        card.columnconfigure(0, weight=1)
        card.rowconfigure(2, weight=1)

        desc = ttk.Label(card, text="Klik tombol di bawah ini, lalu tekan tombol pada keyboard fisik Anda. \nTombol virtual yang sesuai akan menyala untuk memverifikasi pemetaan.", 
                         font=("Helvetica", 10), justify="center")
        desc.grid(row=0, column=0, pady=(0, 15))

        # Control Switch Frame (Horizontal row for switch + capture button)
        self.tester_active = True
        
        switch_frame = ttk.Frame(card)
        switch_frame.grid(row=1, column=0, pady=10, sticky="ew")
        switch_frame.columnconfigure(0, weight=1)
        switch_frame.columnconfigure(1, weight=1)

        self.btn_switch = tk.Button(switch_frame, text="🟢 STATUS PENGUJI: AKTIF (ON)", bg="#2ed573", fg="white",
                                    activebackground="#26af5f", activeforeground="white", font=("Helvetica", 10, "bold"),
                                    relief="flat", bd=0, height=2, command=self.toggle_tester_state)
        self.btn_switch.grid(row=0, column=0, padx=5, sticky="ew")

        # Input focus area indicator
        self.focus_btn = tk.Button(switch_frame, text="🔌 Klik untuk Menangkap Input Keyboard", bg="#3867d6", fg="white",
                                   activebackground="#4b7bec", font=("Helvetica", 10, "bold"), relief="flat", bd=0, height=2)
        self.focus_btn.grid(row=0, column=1, padx=5, sticky="ew")

        # Canvas keyboard grid
        self.canvas = tk.Canvas(card, bg="#1e272e", highlightthickness=0)
        self.canvas.grid(row=2, column=0, sticky="nsew", pady=10)

        # Bind events
        self.focus_btn.bind("<Button-1>", lambda e: (self.focus_btn.focus_set(), self.focus_btn.config(text="🟢 Penangkapan Keyboard Aktif (Tekan tombol!)", bg="#2ed573")) if self.tester_active else "break")
        self.focus_btn.bind("<FocusOut>", lambda e: self.focus_btn.config(text="🔌 Klik untuk Menangkap Input Keyboard", bg="#3867d6") if self.tester_active else "break")
        
        self.focus_btn.bind("<KeyPress>", self.on_key_press)
        self.focus_btn.bind("<KeyRelease>", self.on_key_release)

        # Key-to-servo mapping based on RobotProfile indices: LEFT=0, RIGHT=1, UP=2, DOWN=3, SHIFT=4, A=5
        self.key_to_servo = {
            "Shift_L": 4,
            "a": 5,
            "Up": 2,
            "Left": 0,
            "Down": 3,
            "Right": 1
        }

        # Layout mapping for keys: key name -> (canvas rect coordinates, label)
        # Left-top, right-bottom coordinates
        self.keys_layout = {
            "Shift_L": {"coords": (40, 110, 140, 160), "pressed": False, "label": "SHIFT"},
            "a": {"coords": (150, 110, 210, 160), "pressed": False, "label": "A"},
            "Up": {"coords": (320, 50, 380, 100), "pressed": False, "label": "▲ (UP)"},
            "Left": {"coords": (250, 110, 310, 160), "pressed": False, "label": "◀ (LEFT)"},
            "Down": {"coords": (320, 110, 380, 160), "pressed": False, "label": "▼ (DOWN)"},
            "Right": {"coords": (390, 110, 450, 160), "pressed": False, "label": "▶ (RIGHT)"}
        }

        self.canvas.bind("<Configure>", lambda e: self.draw_keys())

    def draw_keys(self):
        self.canvas.delete("all")
        
        # Center the keys rendering
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        if cw < 10 or ch < 10:
            return

        # Render instructions
        self.canvas.create_text(cw/2, 250, text="Tekan tombol fisik LEFT, RIGHT, UP, DOWN, A, atau SHIFT untuk menguji.", 
                               fill="#747d8c", font=("Helvetica", 9), anchor="center")

        # Draw virtual layout
        offset_x = (cw - 500) / 2
        offset_y = (ch - 280) / 2

        for key_code, data in self.keys_layout.items():
            x1, y1, x2, y2 = data["coords"]
            # Apply centering offset
            x1 += offset_x
            x2 += offset_x
            y1 += offset_y
            y2 += offset_y

            fill_col = "#2ed573" if data["pressed"] else "#2f3542"
            outline_col = "#ffffff" if data["pressed"] else "#57606f"
            txt_col = "#ffffff" if data["pressed"] else "#a4b0be"

            # Draw key outline
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_col, outline=outline_col, width=2)
            # Label
            self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=data["label"], fill=txt_col, font=("Helvetica", 10, "bold"))

    def on_key_press(self, event):
        if not self.tester_active:
            return
        key = event.keysym
        target_key = None
        if key in self.keys_layout:
            target_key = key
        elif key.lower() in self.keys_layout:
            target_key = key.lower()

        if target_key:
            if not self.keys_layout[target_key]["pressed"]:
                self.keys_layout[target_key]["pressed"] = True
                self.draw_keys()
                
                # Send TEST_SERVO press command if connected
                if self.connection.connected:
                    servo_idx = self.key_to_servo.get(target_key)
                    if servo_idx is not None:
                        angle = self.profile.servos[servo_idx].press_angle
                        self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")

    def on_key_release(self, event):
        if not self.tester_active:
            return
        key = event.keysym
        
        # We need to handle regular key and shift release
        released_keys = []
        if key in self.keys_layout:
            released_keys.append(key)
        elif key.lower() in self.keys_layout:
            released_keys.append(key.lower())
            
        if "Shift" in key:
            released_keys.append("Shift_L")
            
        for target_key in released_keys:
            if self.keys_layout[target_key]["pressed"]:
                self.keys_layout[target_key]["pressed"] = False
                self.draw_keys()
                
                # Send TEST_SERVO up command if connected
                if self.connection.connected:
                    servo_idx = self.key_to_servo.get(target_key)
                    if servo_idx is not None:
                        angle = self.profile.servos[servo_idx].up_angle
                        self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")

    def toggle_tester_state(self):
        self.tester_active = not self.tester_active
        if self.tester_active:
            self.btn_switch.config(text="🟢 STATUS PENGUJI: AKTIF (ON)", bg="#2ed573", activebackground="#26af5f")
            self.focus_btn.config(state="normal", text="🔌 Klik untuk Menangkap Input Keyboard", bg="#3867d6")
        else:
            self.btn_switch.config(text="🔴 STATUS PENGUJI: NONAKTIF (OFF)", bg="#ff4757", activebackground="#ff6b81")
            self.focus_btn.config(state="disabled", text="⚠️ Penguji Dinonaktifkan", bg="#2f3542")
            # Reset all keys to released state visually & physically
            for key_code in self.keys_layout:
                if self.keys_layout[key_code]["pressed"]:
                    self.keys_layout[key_code]["pressed"] = False
                    if self.connection.connected:
                        servo_idx = self.key_to_servo.get(key_code)
                        if servo_idx is not None:
                            angle = self.profile.servos[servo_idx].up_angle
                            self.connection.send_command(f"TEST_SERVO {servo_idx} {angle}")
            self.draw_keys()
