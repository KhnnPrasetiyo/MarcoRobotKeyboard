import tkinter as tk
from tkinter import ttk

class DashboardTab(ttk.Frame):
    def __init__(self, parent, profile, connection, log_box):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection
        self.log_box = log_box

        # Configure styles
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # 1. Header Card
        header_card = ttk.LabelFrame(self, text=" Dashboard Sistem ", padding=15)
        header_card.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky="ew")
        
        status_lbl = ttk.Label(header_card, text="Status Robot:", font=("Helvetica", 12, "bold"))
        status_lbl.pack(side=tk.LEFT, padx=5)
        
        self.status_val = ttk.Label(header_card, text="Terputus", font=("Helvetica", 12), foreground="#ff4757")
        self.status_val.pack(side=tk.LEFT, padx=5)

        # Progress label (tampil saat eksekusi berjalan)
        self.progress_val = ttk.Label(header_card, text="", font=("Helvetica", 11), foreground="#ffa502")
        self.progress_val.pack(side=tk.LEFT, padx=15)

        self.lbl_total_time = ttk.Label(header_card, text="", font=("Helvetica", 11, "bold"), foreground="#2ed573")
        self.lbl_total_time.pack(side=tk.RIGHT, padx=15)

        # 2. Control Panel Card
        ctrl_card = ttk.LabelFrame(self, text=" Kontrol Real-Time ", padding=15)
        ctrl_card.grid(row=1, column=0, padx=15, pady=10, sticky="nsew")
        
        ttk.Label(ctrl_card, text="Kirim perintah langsung ke perangkat keras:").pack(anchor="w", pady=(0,15))

        btn_start = ttk.Button(ctrl_card, text="▶ MULAI POLA", width=22, command=self.start_pattern)
        btn_start.pack(pady=8, fill="x")

        btn_stop = ttk.Button(ctrl_card, text="⏹ HENTIKAN POLA", width=22, command=self.stop_pattern)
        btn_stop.pack(pady=8, fill="x")

        btn_estop = tk.Button(ctrl_card, text="🚨 DARURAT STOP", font=("Helvetica", 11, "bold"), 
                              bg="#ff4757", fg="white", activebackground="#ff6b81", activeforeground="white", 
                              relief="flat", bd=0, height=2, command=self.estop)
        btn_estop.pack(pady=15, fill="x")
        
        btn_status = ttk.Button(ctrl_card, text="🔄 Cek Status", width=22, command=self.check_status)
        btn_status.pack(pady=8, fill="x")

        # 3. Log Console Card (Right side)
        log_card = ttk.LabelFrame(self, text=" Output Konsol Langsung ", padding=15)
        log_card.grid(row=1, column=1, padx=15, pady=10, sticky="nsew")
        self.columnconfigure(1, weight=1)

        self.console = tk.Text(log_card, bg="#1e272e", fg="#2ed573", font=("Consolas", 10), wrap="word", bd=0, state="disabled")
        self.console.pack(fill="both", expand=True)

        # Tombol bersihkan log
        btn_clear = ttk.Button(log_card, text="🗑 Bersihkan Log", command=self.clear_log)
        btn_clear.pack(anchor="e", pady=(5, 0))
        
        # Link shared log box data
        self.update_log_loop()
        self.update_duration()

    def start_pattern(self):
        self.connection.send_command("START")

    def stop_pattern(self):
        self.connection.send_command("STOP")

    def estop(self):
        self.connection.send_command("ESTOP")
        self.connection.log("Perintah DARURAT STOP dikirim!")

    def check_status(self):
        self.connection.send_command("STATUS")

    def clear_log(self):
        self.console.config(state="normal")
        self.console.delete("1.0", tk.END)
        self.console.config(state="disabled")

    def update_status_label(self, status):
        # Handle step progress messages
        if status.startswith("STEP:"):
            try:
                step_info = status[5:]  # "3/10"
                current, total = step_info.split("/")
                self.progress_val.config(text=f"⚡ Langkah: {current} / {total}")
            except (ValueError, IndexError):
                pass
            return

        # Translate dynamic status words to Indonesian
        indonesian_status = status
        if "Disconnected" in status:
            indonesian_status = "Terputus"
        elif "Connected (Simulated)" in status:
            indonesian_status = "Terhubung (Simulasi)"
        elif "Connected" in status:
            indonesian_status = "Terhubung"
        elif "Active:" in status:
            indonesian_status = status.replace("Active:", "Aktif:")
            
        self.status_val.config(text=indonesian_status)
        if "Simulasi" in indonesian_status or "Terhubung" in indonesian_status:
            self.status_val.config(foreground="#2ed573")
        elif "Aktif" in indonesian_status:
            self.status_val.config(foreground="#ffa502")
        else:
            self.status_val.config(foreground="#ff4757")

        # Bersihkan progress saat berhenti
        if "STOPPED" in status or "IDLE" in status or "EMERGENCY" in status or "Disconnected" in status:
            self.progress_val.config(text="")

    def update_log_loop(self):
        # Read from connection log queue
        if not self.log_box.empty():
            self.console.config(state="normal")
            while not self.log_box.empty():
                line = self.log_box.get()
                self.console.insert(tk.END, line + "\n")
            self.console.see(tk.END)
            self.console.config(state="disabled")
        self.after(100, self.update_log_loop)

    def reload_table(self):
        """Method called automatically when switching to this tab."""
        self.update_duration()

    def update_duration(self):
        total_ms = sum(a.press_duration + a.delay_duration for a in self.profile.pattern)
        if not self.profile.pattern:
            self.lbl_total_time.config(text="⏱ Pola Kosong")
            return
            
        if self.profile.loop_mode == "INFINITY":
            duration_text = f"⏱ Estimasi: {total_ms / 1000:.2f} dtk/siklus (∞)"
        else:
            total_time = total_ms * self.profile.loop_count
            duration_text = f"⏱ Estimasi Total: {total_time / 1000:.2f} dtk ({self.profile.loop_count}x loop)"
            
        self.lbl_total_time.config(text=duration_text)
