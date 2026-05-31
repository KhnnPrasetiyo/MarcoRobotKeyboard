import tkinter as tk
from tkinter import ttk

class CalibrationTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Main frame
        main_scroll = tk.Canvas(self, borderwidth=0, highlightthickness=0, bg="#2f3542")
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=main_scroll.yview)
        scrollable_frame = ttk.Frame(main_scroll)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_scroll.configure(
                scrollregion=main_scroll.bbox("all")
            )
        )

        main_scroll.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_scroll.configure(yscrollcommand=scrollbar.set)

        main_scroll.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        # Add title
        ttk.Label(scrollable_frame, text="Kalibrasi Sudut Servo", font=("Helvetica", 14, "bold")).pack(anchor="w", pady=(10, 20))

        # We have 6 servos
        self.servo_rows = []
        for i, servo in enumerate(self.profile.servos):
            card = ttk.LabelFrame(scrollable_frame, text=f" Servo {i+1}: {servo.name} (Pin D{servo.pin}) ", padding=15)
            card.pack(fill="x", expand=True, pady=10, padx=5)

            card.columnconfigure(1, weight=1)

            # --- ROW 0: Sudut UP ---
            ttk.Label(card, text="Sudut UP (°):", font=("Helvetica", 10, "bold")).grid(row=0, column=0, padx=5, pady=8, sticky="e")
            up_val = tk.IntVar(value=servo.up_angle)
            up_scale = ttk.Scale(card, from_=0, to=180, variable=up_val, orient="horizontal")
            up_scale.grid(row=0, column=1, padx=10, pady=8, sticky="ew")
            
            # Decrement button
            btn_up_minus = tk.Button(card, text="-", font=("Helvetica", 9, "bold"), bg="#57606f", fg="white",
                                     activebackground="#747d8c", activeforeground="white", relief="flat", bd=0, width=3,
                                     command=lambda v=up_val: v.set(max(0, v.get() - 1)))
            btn_up_minus.grid(row=0, column=2, padx=2, pady=8)
            btn_up_minus.bind("<Enter>", lambda e, b=btn_up_minus: b.config(bg="#747d8c"))
            btn_up_minus.bind("<Leave>", lambda e, b=btn_up_minus: b.config(bg="#57606f"))
            
            up_lbl = ttk.Label(card, text=str(servo.up_angle), width=4, font=("Helvetica", 10, "bold"), foreground="#2ed573", anchor="center")
            up_lbl.grid(row=0, column=3, padx=5, pady=8)
            
            # Increment button
            btn_up_plus = tk.Button(card, text="+", font=("Helvetica", 9, "bold"), bg="#57606f", fg="white",
                                    activebackground="#747d8c", activeforeground="white", relief="flat", bd=0, width=3,
                                    command=lambda v=up_val: v.set(min(180, v.get() + 1)))
            btn_up_plus.grid(row=0, column=4, padx=2, pady=8)
            btn_up_plus.bind("<Enter>", lambda e, b=btn_up_plus: b.config(bg="#747d8c"))
            btn_up_plus.bind("<Leave>", lambda e, b=btn_up_plus: b.config(bg="#57606f"))
            
            btn_test_up = tk.Button(card, text="Posisi UP", font=("Helvetica", 9, "bold"), bg="#2ed573", fg="white",
                                    activebackground="#26af5f", activeforeground="white", relief="flat", bd=0, cursor="hand2",
                                    command=lambda idx=i, v=up_val: self.test_angle(idx, v.get()), padx=10)
            btn_test_up.grid(row=0, column=5, padx=10, pady=8)
            btn_test_up.bind("<Enter>", lambda e, b=btn_test_up: b.config(bg="#26af5f"))
            btn_test_up.bind("<Leave>", lambda e, b=btn_test_up: b.config(bg="#2ed573"))

            # Link scale motion to update label
            def make_up_callback(lbl, var, s_idx):
                return lambda *args: (lbl.config(text=str(var.get())), self.update_profile_servo_angle(s_idx, "up", var.get()))
            up_val.trace_add("write", make_up_callback(up_lbl, up_val, i))

            # --- ROW 1: Sudut PRESS ---
            ttk.Label(card, text="Sudut PRESS (°):", font=("Helvetica", 10, "bold")).grid(row=1, column=0, padx=5, pady=8, sticky="e")
            press_val = tk.IntVar(value=servo.press_angle)
            press_scale = ttk.Scale(card, from_=0, to=180, variable=press_val, orient="horizontal")
            press_scale.grid(row=1, column=1, padx=10, pady=8, sticky="ew")
            
            # Decrement button
            btn_press_minus = tk.Button(card, text="-", font=("Helvetica", 9, "bold"), bg="#57606f", fg="white",
                                        activebackground="#747d8c", activeforeground="white", relief="flat", bd=0, width=3,
                                        command=lambda v=press_val: v.set(max(0, v.get() - 1)))
            btn_press_minus.grid(row=1, column=2, padx=2, pady=8)
            btn_press_minus.bind("<Enter>", lambda e, b=btn_press_minus: b.config(bg="#747d8c"))
            btn_press_minus.bind("<Leave>", lambda e, b=btn_press_minus: b.config(bg="#57606f"))
            
            press_lbl = ttk.Label(card, text=str(servo.press_angle), width=4, font=("Helvetica", 10, "bold"), foreground="#ffa502", anchor="center")
            press_lbl.grid(row=1, column=3, padx=5, pady=8)
            
            # Increment button
            btn_press_plus = tk.Button(card, text="+", font=("Helvetica", 9, "bold"), bg="#57606f", fg="white",
                                       activebackground="#747d8c", activeforeground="white", relief="flat", bd=0, width=3,
                                       command=lambda v=press_val: v.set(min(180, v.get() + 1)))
            btn_press_plus.grid(row=1, column=4, padx=2, pady=8)
            btn_press_plus.bind("<Enter>", lambda e, b=btn_press_plus: b.config(bg="#747d8c"))
            btn_press_plus.bind("<Leave>", lambda e, b=btn_press_plus: b.config(bg="#57606f"))
            
            btn_test_press = tk.Button(card, text="Posisi PRESS", font=("Helvetica", 9, "bold"), bg="#ffa502", fg="white",
                                       activebackground="#ffb142", activeforeground="white", relief="flat", bd=0, cursor="hand2",
                                       command=lambda idx=i, v=press_val: self.test_angle(idx, v.get()), padx=10)
            btn_test_press.grid(row=1, column=5, padx=10, pady=8)
            btn_test_press.bind("<Enter>", lambda e, b=btn_test_press: b.config(bg="#ffb142"))
            btn_test_press.bind("<Leave>", lambda e, b=btn_test_press: b.config(bg="#ffa502"))

            def make_press_callback(lbl, var, s_idx):
                return lambda *args: (lbl.config(text=str(var.get())), self.update_profile_servo_angle(s_idx, "press", var.get()))
            press_val.trace_add("write", make_press_callback(press_lbl, press_val, i))

            # --- ROW 2: Wide Test sequence button ---
            btn_test = tk.Button(card, text="⚡ JALANKAN UJI TEKAN (PRESS & RELEASE SEQUENCE)", font=("Helvetica", 10, "bold"),
                                 bg="#3867d6", fg="white", activebackground="#4b7bec", activeforeground="white",
                                 relief="flat", bd=0, cursor="hand2", command=lambda idx=i, u=up_val, p=press_val: self.run_test_sequence(idx, u.get(), p.get()), pady=8)
            btn_test.grid(row=2, column=1, columnspan=5, padx=10, pady=10, sticky="ew")
            btn_test.bind("<Enter>", lambda e, b=btn_test: b.config(bg="#4b7bec"))
            btn_test.bind("<Leave>", lambda e, b=btn_test: b.config(bg="#3867d6"))

            self.servo_rows.append({
                "up_val": up_val,
                "press_val": press_val
            })

    def update_profile_servo_angle(self, index, angle_type, val):
        if angle_type == "up":
            self.profile.servos[index].up_angle = val
        else:
            self.profile.servos[index].press_angle = val

    def test_angle(self, index, angle):
        # Arduino pins are defined. We send TEST_SERVO <index> <angle> command
        self.connection.send_command(f"TEST_SERVO {index} {angle}")

    def run_test_sequence(self, index, up_angle, press_angle):
        self.connection.log(f"Mensimulasikan uji tekan untuk servo {index+1} ({self.profile.servos[index].name})...")
        # Direct rapid tests
        self.test_angle(index, press_angle)
        self.after(250, lambda: self.test_angle(index, up_angle))

    def reload_from_profile(self):
        for i, servo in enumerate(self.profile.servos):
            self.servo_rows[i]["up_val"].set(servo.up_angle)
            self.servo_rows[i]["press_val"].set(servo.press_angle)
