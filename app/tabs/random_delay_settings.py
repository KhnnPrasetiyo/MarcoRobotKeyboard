import tkinter as tk
from tkinter import ttk

class RandomDelaySettingsTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        card = ttk.LabelFrame(self, text=" Pengaturan Jeda Aksi Acak ", padding=20)
        card.grid(row=0, column=0, padx=40, pady=40, sticky="n")

        # Enable checkbox
        self.enabled_var = tk.BooleanVar(value=self.profile.random_delay_enabled)
        self.chk_enabled = tk.Checkbutton(card, text="Aktifkan jeda acak di antara aksi", 
                                           variable=self.enabled_var, command=self.on_toggle_enabled,
                                           bg="#2f3542", fg="#ffffff", selectcolor="#1e272e", activebackground="#2f3542", activeforeground="#ffffff", font=("Helvetica", 10))
        self.chk_enabled.grid(row=0, column=0, columnspan=3, sticky="w", pady=15)

        # Min delay
        self.lbl_min = ttk.Label(card, text="Jeda Minimum (ms):")
        self.lbl_min.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.min_var = tk.IntVar(value=self.profile.random_delay_min)
        self.spin_min = ttk.Spinbox(card, from_=0, to=60000, increment=100, textvariable=self.min_var, width=15)
        self.spin_min.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        self.spin_min.bind("<FocusOut>", self.on_values_change)
        self.spin_min.bind("<Return>", self.on_values_change)

        # Max delay
        self.lbl_max = ttk.Label(card, text="Jeda Maksimum (ms):")
        self.lbl_max.grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.max_var = tk.IntVar(value=self.profile.random_delay_max)
        self.spin_max = ttk.Spinbox(card, from_=0, to=60000, increment=100, textvariable=self.max_var, width=15)
        self.spin_max.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        self.spin_max.bind("<FocusOut>", self.on_values_change)
        self.spin_max.bind("<Return>", self.on_values_change)

        self.on_toggle_enabled()

    def on_toggle_enabled(self):
        enabled = self.enabled_var.get()
        self.profile.random_delay_enabled = enabled
        state = "normal" if enabled else "disabled"
        self.spin_min.config(state=state)
        self.spin_max.config(state=state)
        self.lbl_min.config(state=state)
        self.lbl_max.config(state=state)

    def on_values_change(self, event=None):
        try:
            self.profile.random_delay_min = max(0, int(self.min_var.get()))
            self.profile.random_delay_max = max(self.profile.random_delay_min, int(self.max_var.get()))
            # Update spin to reflect maximum boundary constraints
            self.max_var.set(self.profile.random_delay_max)
        except ValueError:
            pass

    def reload_from_profile(self):
        self.enabled_var.set(self.profile.random_delay_enabled)
        self.min_var.set(self.profile.random_delay_min)
        self.max_var.set(self.profile.random_delay_max)
        self.on_toggle_enabled()
