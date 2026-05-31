import tkinter as tk
from tkinter import ttk
import random
from app.models import Action

class SimulationTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection
        
        self.simulating = False
        self.current_step = 0
        self.sim_job = None
        
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # 1. Left side: Simulation Arena (Canvas)
        arena_frame = ttk.LabelFrame(self, text=" Arena Robot Virtual ", padding=15)
        arena_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        arena_frame.columnconfigure(0, weight=1)
        arena_frame.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(arena_frame, bg="#1e272e", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # 2. Right side: Controls & Info Panel
        side_panel = ttk.LabelFrame(self, text=" Panel Simulasi ", padding=15)
        side_panel.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.btn_run = tk.Button(side_panel, text="▶ MULAI SIMULASI", bg="#2ed573", fg="white", 
                                 activebackground="#26af5f", font=("Helvetica", 11, "bold"), relief="flat", bd=0, 
                                 height=2, command=self.toggle_simulation)
        self.btn_run.pack(fill="x", pady=10)

        # Information labels
        self.lbl_step = ttk.Label(side_panel, text="Langkah: - / -", font=("Helvetica", 10, "bold"))
        self.lbl_step.pack(anchor="w", pady=10)

        self.lbl_action = ttk.Label(side_panel, text="Aksi Aktif: None", font=("Helvetica", 10))
        self.lbl_action.pack(anchor="w", pady=5)

        self.lbl_servo_state = ttk.Label(side_panel, text="Status Servo: UP", font=("Helvetica", 10))
        self.lbl_servo_state.pack(anchor="w", pady=5)

        self.lbl_delay = ttk.Label(side_panel, text="Sisa jeda: 0ms", font=("Helvetica", 10))
        self.lbl_delay.pack(anchor="w", pady=5)

        # Simulated logs listbox
        ttk.Label(side_panel, text="Log Jejak Simulasi:", font=("Helvetica", 9, "bold")).pack(anchor="w", pady=(20, 5))
        self.trace_list = tk.Listbox(side_panel, bg="#2f3542", fg="#ffffff", font=("Consolas", 9), bd=0)
        self.trace_list.pack(fill="both", expand=True, pady=5)

        # Virtual keys/servos coordinates mapping
        self.servos_ui = {
            "LEFT": {"x": 80, "y": 200, "color": "#1e90ff", "label": "LEFT (D2)"},
            "RIGHT": {"x": 280, "y": 200, "color": "#2ed573", "label": "RIGHT (D3)"},
            "UP": {"x": 180, "y": 100, "color": "#ffa502", "label": "UP (D4)"},
            "DOWN": {"x": 180, "y": 200, "color": "#ff4757", "label": "DOWN (D5)"},
            "SHIFT": {"x": 80, "y": 300, "color": "#9b59b6", "label": "SHIFT (D6)"},
            "A": {"x": 280, "y": 300, "color": "#f1c40f", "label": "A (D7)"}
        }

        self.canvas.bind("<Configure>", lambda e: self.draw_arena())

    def draw_arena(self, active_servos=None):
        if active_servos is None:
            active_servos = {}
            
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 10 or h < 10:
            return

        self.canvas.create_text(w/2, 30, text="Simulasi Rig Servo Keyboard Arduino Nano", 
                               fill="#ffffff", font=("Helvetica", 12, "bold"), anchor="center")

        # Draw each servo rig mockup
        for name, data in self.servos_ui.items():
            cx = data["x"]
            cy = data["y"]
            
            # Active status color
            is_pressed = active_servos.get(name, False)
            bg_color = data["color"] if is_pressed else "#2f3542"
            outline_color = "#ffffff" if is_pressed else "#747d8c"
            text_color = "#ffffff" if is_pressed else "#a4b0be"

            # Draw key switch footprint
            self.canvas.create_rectangle(cx-40, cy-35, cx+40, cy+35, fill=bg_color, outline=outline_color, width=2, tags=name)
            # Draw key character
            self.canvas.create_text(cx, cy-5, text=name, fill=text_color, font=("Helvetica", 12, "bold"), tags=name)
            # Draw servo attachment arm
            arm_color = "#eccc68" if is_pressed else "#57606f"
            self.canvas.create_line(cx-20, cy+20, cx+20, cy+20, fill=arm_color, width=4)
            # Label
            self.canvas.create_text(cx, cy+50, text=data["label"], fill="#747d8c", font=("Helvetica", 8))

    def toggle_simulation(self):
        if self.simulating:
            self.stop_simulation()
        else:
            self.start_simulation()

    def start_simulation(self):
        if not self.profile.pattern:
            self.trace_log("Error: Pola kosong. Tambahkan aksi terlebih dahulu.")
            return
        
        self.simulating = True
        self.current_step = 0
        self.btn_run.config(text="⏹ HENTIKAN SIMULASI", bg="#ff4757", activebackground="#ff6b81")
        self.trace_list.delete(0, tk.END)
        self.trace_log("Simulasi dimulai...")
        self.run_next_step()

    def stop_simulation(self):
        self.simulating = False
        if self.sim_job:
            self.after_cancel(self.sim_job)
            self.sim_job = None
        self.btn_run.config(text="▶ MULAI SIMULASI", bg="#2ed573", activebackground="#26af5f")
        self.lbl_step.config(text="Langkah: - / -")
        self.lbl_action.config(text="Aksi Aktif: None")
        self.lbl_servo_state.config(text="Status Servo: UP")
        self.lbl_delay.config(text="Sisa jeda: 0ms")
        self.trace_log("Simulasi dihentikan.")
        self.draw_arena() # Redraw default state

    def trace_log(self, msg):
        self.trace_list.insert(tk.END, msg)
        self.trace_list.see(tk.END)

    def run_next_step(self):
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
        self.lbl_action.config(text=f"Aksi Aktif: {action.action_type}")
        
        # Set delay for pressing duration
        def release_servos():
            if not self.simulating:
                return
            self.lbl_servo_state.config(text="Status Servo: UP")
            self.draw_arena() # All UP
            
            # Delay duration
            delay_duration = action.delay_duration
            if self.profile.random_delay_enabled:
                delay_duration = random.randint(self.profile.random_delay_min, self.profile.random_delay_max)
                self.trace_log(f"  Jeda (Diacak): {delay_duration}ms")
            else:
                self.trace_log(f"  Jeda: {delay_duration}ms")
                
            self.lbl_delay.config(text=f"Sisa jeda: {delay_duration}ms")

            def next_action_trigger():
                self.current_step += 1
                self.run_next_step()
                
            self.sim_job = self.after(delay_duration, next_action_trigger)

        # Staggered logic for direction + Shift keys (BLINK actions)
        if action.action_type.startswith("BLINK_"):
            blink_key = action.action_type.replace("BLINK_", "")
            self.trace_log(f"[{action.action_type}] Menekan {blink_key} (jeda staggered)...")
            
            active_servos = {blink_key: True}
            self.draw_arena(active_servos)
            self.lbl_servo_state.config(text="Status Servo: TEKAN (Arah)")
            
            stagger_delay = 150
            if action.press_duration > stagger_delay:
                def step_phase_2():
                    if not self.simulating:
                        return
                    self.trace_log(f"[{action.action_type}] Menekan SHIFT (keduanya tertahan)")
                    active_servos["SHIFT"] = True
                    self.draw_arena(active_servos)
                    self.lbl_servo_state.config(text="Status Servo: TEKAN (Arah + SHIFT)")
                    
                    remaining_press = action.press_duration - stagger_delay
                    self.sim_job = self.after(remaining_press, release_servos)
                
                self.sim_job = self.after(stagger_delay, step_phase_2)
            else:
                self.sim_job = self.after(action.press_duration, release_servos)
        else:
            active_servos = {}
            if action.action_type == "NONE":
                self.trace_log(f"[{action.action_type}] Jeda kosong (durasi: {action.press_duration}ms)")
            else:
                self.trace_log(f"[{action.action_type}] Menekan {action.action_type} (durasi: {action.press_duration}ms)")
                active_servos[action.action_type] = True
                self.lbl_servo_state.config(text="Status Servo: TEKAN")
                
            self.draw_arena(active_servos)
            self.sim_job = self.after(action.press_duration, release_servos)
