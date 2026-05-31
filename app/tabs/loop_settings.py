import tkinter as tk
from tkinter import ttk

class LoopSettingsTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        card = ttk.LabelFrame(self, text=" Pengaturan Perulangan Pola ", padding=20)
        card.grid(row=0, column=0, padx=40, pady=40, sticky="n")

        # Loop Mode RadioButtons
        ttk.Label(card, text="Mode Perulangan:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
        
        self.mode_var = tk.StringVar(value=self.profile.loop_mode)
        
        rb_inf = tk.Radiobutton(card, text="Mode Tak Terbatas (Mengulang selamanya)", variable=self.mode_var, value="INFINITY", command=self.on_mode_change,
                                bg="#2f3542", fg="#ffffff", selectcolor="#1e272e", activebackground="#2f3542", activeforeground="#ffffff", font=("Helvetica", 10))
        rb_inf.grid(row=0, column=1, columnspan=2, sticky="w", padx=10, pady=10)
        
        rb_cust = tk.Radiobutton(card, text="Mode Kustom Jumlah Perulangan", variable=self.mode_var, value="CUSTOM", command=self.on_mode_change,
                                 bg="#2f3542", fg="#ffffff", selectcolor="#1e272e", activebackground="#2f3542", activeforeground="#ffffff", font=("Helvetica", 10))
        rb_cust.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=10)

        # Custom Count Entry
        self.lbl_count = ttk.Label(card, text="Jumlah Perulangan:")
        self.lbl_count.grid(row=2, column=1, sticky="e", padx=(20, 5), pady=10)
        
        self.count_var = tk.IntVar(value=self.profile.loop_count)
        self.count_spin = ttk.Spinbox(card, from_=1, to=65535, increment=1, textvariable=self.count_var, width=15)
        self.count_spin.grid(row=2, column=2, sticky="w", padx=5, pady=10)
        self.count_spin.bind("<FocusOut>", self.on_count_change)
        self.count_spin.bind("<Return>", self.on_count_change)

        # Auto Start Config
        ttk.Label(card, text="Opsi Mulai Saat Booting:", font=("Helvetica", 10, "bold")).grid(row=3, column=0, sticky="w", pady=15)
        
        self.autostart_var = tk.BooleanVar(value=self.profile.auto_start)
        self.chk_autostart = tk.Checkbutton(card, text="Mulai otomatis (Auto Start) saat Arduino dinyalakan", 
                                             variable=self.autostart_var, command=self.on_autostart_change,
                                             bg="#2f3542", fg="#ffffff", selectcolor="#1e272e", activebackground="#2f3542", activeforeground="#ffffff", font=("Helvetica", 10))
        self.chk_autostart.grid(row=3, column=1, columnspan=2, sticky="w", padx=10, pady=15)

        self.on_mode_change()

    def on_mode_change(self):
        mode = self.mode_var.get()
        self.profile.loop_mode = mode
        if mode == "INFINITY":
            self.count_spin.config(state="disabled")
            self.lbl_count.config(state="disabled")
        else:
            self.count_spin.config(state="normal")
            self.lbl_count.config(state="normal")

    def on_count_change(self, event=None):
        try:
            self.profile.loop_count = max(1, int(self.count_var.get()))
        except ValueError:
            pass

    def on_autostart_change(self):
        self.profile.auto_start = self.autostart_var.get()

    def reload_from_profile(self):
        self.mode_var.set(self.profile.loop_mode)
        self.count_var.set(self.profile.loop_count)
        self.autostart_var.set(self.profile.auto_start)
        self.on_mode_change()
