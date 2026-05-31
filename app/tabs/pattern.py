import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.models import Action

class PatternBuilderTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Header Frame
        header = ttk.Frame(self)
        header.grid(row=0, column=0, columnspan=2, padx=15, pady=10, sticky="ew")
        
        ttk.Label(header, text="Pembuat Pola Urutan Aksi", font=("Helvetica", 14, "bold")).pack(side=tk.LEFT)

        self.lbl_duration = ttk.Label(header, text="Estimasi: 0.00 detik", font=("Helvetica", 11, "bold"), foreground="#2ed573")
        self.lbl_duration.pack(side=tk.RIGHT, padx=10)

        # Main Layout
        # Left side: Treeview table
        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=1, column=0, padx=15, pady=10, sticky="nsew")
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.rowconfigure(0, weight=1)

        columns = ("index", "action", "press_dur", "delay_dur")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.tree.heading("index", text="#")
        self.tree.heading("action", text="Tipe Aksi")
        self.tree.heading("press_dur", text="Durasi Tekan (ms)")
        self.tree.heading("delay_dur", text="Durasi Jeda (ms)")

        self.tree.column("index", width=50, anchor="center")
        self.tree.column("action", width=180, anchor="center")
        self.tree.column("press_dur", width=150, anchor="center")
        self.tree.column("delay_dur", width=150, anchor="center")

        # Scrollbar for table
        sb = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        sb.grid(row=0, column=1, sticky="ns")

        # Right side: Control & Edit Panel
        edit_panel = ttk.LabelFrame(self, text=" Pengaturan Aksi & Kontrol ", padding=15)
        edit_panel.grid(row=1, column=1, padx=15, pady=10, sticky="nsew")

        # Config fields inside Edit Panel
        ttk.Label(edit_panel, text="Tipe Aksi Terpilih:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.action_var = tk.StringVar(value="NONE")
        self.action_combo = ttk.Combobox(edit_panel, textvariable=self.action_var, values=Action.TYPES, state="readonly", width=22)
        self.action_combo.pack(anchor="w", pady=(0, 15))
        self.action_combo.bind("<<ComboboxSelected>>", self.on_fields_changed)

        ttk.Label(edit_panel, text="Durasi Tekan (ms):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.press_var = tk.IntVar(value=200)
        self.press_spin = ttk.Spinbox(edit_panel, from_=50, to=10000, increment=50, textvariable=self.press_var, width=21)
        self.press_spin.pack(anchor="w", pady=(0, 15))
        self.press_spin.bind("<FocusOut>", self.on_fields_changed)
        self.press_spin.bind("<Return>", self.on_fields_changed)

        ttk.Label(edit_panel, text="Durasi Jeda (ms):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.delay_var = tk.IntVar(value=500)
        self.delay_spin = ttk.Spinbox(edit_panel, from_=0, to=60000, increment=100, textvariable=self.delay_var, width=21)
        self.delay_spin.pack(anchor="w", pady=(0, 20))
        self.delay_spin.bind("<FocusOut>", self.on_fields_changed)
        self.delay_spin.bind("<Return>", self.on_fields_changed)

        # Buttons
        btn_grid = ttk.Frame(edit_panel)
        btn_grid.pack(fill="x", pady=5)
        btn_grid.columnconfigure(0, weight=1)
        btn_grid.columnconfigure(1, weight=1)

        btn_add = tk.Button(btn_grid, text="✨ Tambah Aksi", font=("Helvetica", 9, "bold"),
                            bg="#3867d6", fg="white", activebackground="#4b7bec", activeforeground="white",
                            relief="flat", bd=0, cursor="hand2", command=self.add_action, pady=8)
        btn_add.grid(row=0, column=0, padx=2, pady=5, sticky="ew")
        btn_add.bind("<Enter>", lambda e, b=btn_add: b.config(bg="#4b7bec"))
        btn_add.bind("<Leave>", lambda e, b=btn_add: b.config(bg="#3867d6"))

        btn_delete = tk.Button(btn_grid, text="🗑️ Hapus Aksi", font=("Helvetica", 9, "bold"),
                               bg="#ff4757", fg="white", activebackground="#ff6b81", activeforeground="white",
                               relief="flat", bd=0, cursor="hand2", command=self.delete_action, pady=8)
        btn_delete.grid(row=0, column=1, padx=2, pady=5, sticky="ew")
        btn_delete.bind("<Enter>", lambda e, b=btn_delete: b.config(bg="#ff6b81"))
        btn_delete.bind("<Leave>", lambda e, b=btn_delete: b.config(bg="#ff4757"))

        btn_dup = tk.Button(btn_grid, text="📋 Duplikat", font=("Helvetica", 9, "bold"),
                            bg="#57606f", fg="white", activebackground="#747d8c", activeforeground="white",
                            relief="flat", bd=0, cursor="hand2", command=self.duplicate_action, pady=8)
        btn_dup.grid(row=1, column=0, columnspan=2, padx=2, pady=5, sticky="ew")
        btn_dup.bind("<Enter>", lambda e, b=btn_dup: b.config(bg="#747d8c"))
        btn_dup.bind("<Leave>", lambda e, b=btn_dup: b.config(bg="#57606f"))
        
        # Up/Down Move Buttons
        btn_move_frame = ttk.Frame(edit_panel)
        btn_move_frame.pack(fill="x", pady=10)
        btn_move_frame.columnconfigure(0, weight=1)
        btn_move_frame.columnconfigure(1, weight=1)

        btn_up = tk.Button(btn_move_frame, text="⬆️ Geser Ke Atas", font=("Helvetica", 9, "bold"),
                           bg="#57606f", fg="white", activebackground="#747d8c", activeforeground="white",
                           relief="flat", bd=0, cursor="hand2", command=self.move_up, pady=8)
        btn_up.grid(row=0, column=0, padx=2, sticky="ew")
        btn_up.bind("<Enter>", lambda e, b=btn_up: b.config(bg="#747d8c"))
        btn_up.bind("<Leave>", lambda e, b=btn_up: b.config(bg="#57606f"))

        btn_down = tk.Button(btn_move_frame, text="⬇️ Geser Ke Bawah", font=("Helvetica", 9, "bold"),
                             bg="#57606f", fg="white", activebackground="#747d8c", activeforeground="white",
                             relief="flat", bd=0, cursor="hand2", command=self.move_down, pady=8)
        btn_down.grid(row=0, column=1, padx=2, sticky="ew")
        btn_down.bind("<Enter>", lambda e, b=btn_down: b.config(bg="#747d8c"))
        btn_down.bind("<Leave>", lambda e, b=btn_down: b.config(bg="#57606f"))

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.reload_table()

    def update_duration_estimation(self):
        total_ms = 0
        for action in self.profile.pattern:
            total_ms += action.press_duration + action.delay_duration

        if not self.profile.pattern:
            self.lbl_duration.config(text="Estimasi: 0.00 detik")
            return

        if self.profile.loop_mode == "INFINITY":
            duration_text = f"Estimasi: {total_ms / 1000:.2f} detik per siklus (Loop: ∞)"
        else:
            total_time = total_ms * self.profile.loop_count
            duration_text = f"Estimasi Total: {total_time / 1000:.2f} detik ({self.profile.loop_count}x loop)"
            
        self.lbl_duration.config(text=duration_text)

    def reload_table(self):
        # Clear
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for i, action in enumerate(self.profile.pattern):
            self.tree.insert("", "end", iid=str(i), values=(
                i + 1,
                action.action_type,
                action.press_duration,
                action.delay_duration
            ))
        self.update_duration_estimation()

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        action = self.profile.pattern[idx]
        self.action_var.set(action.action_type)
        self.press_var.set(action.press_duration)
        self.delay_var.set(action.delay_duration)

    def on_fields_changed(self, event=None):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        action = self.profile.pattern[idx]
        
        try:
            action.action_type = self.action_var.get()
            action.press_duration = max(50, int(self.press_var.get()))
            action.delay_duration = max(0, int(self.delay_var.get()))
            
            # Update tree item content
            self.tree.item(str(idx), values=(
                idx + 1,
                action.action_type,
                action.press_duration,
                action.delay_duration
            ))
            self.update_duration_estimation()
        except ValueError:
            pass

    def add_action(self):
        new_act = Action("NONE", 200, 500)
        self.profile.pattern.append(new_act)
        self.reload_table()
        # Select the newly added item
        new_idx = str(len(self.profile.pattern) - 1)
        self.tree.selection_set(new_idx)
        self.tree.see(new_idx)

    def delete_action(self):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        
        # Konfirmasi hapus
        if not messagebox.askyesno("Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus aksi terpilih?"):
            return
            
        self.profile.pattern.pop(idx)
        self.reload_table()
        # select next or prev
        if self.profile.pattern:
            new_idx = str(min(idx, len(self.profile.pattern) - 1))
            self.tree.selection_set(new_idx)

    def duplicate_action(self):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        original = self.profile.pattern[idx]
        copy_act = Action(original.action_type, original.press_duration, original.delay_duration)
        self.profile.pattern.insert(idx + 1, copy_act)
        self.reload_table()
        self.tree.selection_set(str(idx + 1))

    def move_up(self):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        if idx == 0:
            return
        self.profile.pattern[idx], self.profile.pattern[idx - 1] = self.profile.pattern[idx - 1], self.profile.pattern[idx]
        self.reload_table()
        self.tree.selection_set(str(idx - 1))

    def move_down(self):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        if idx >= len(self.profile.pattern) - 1:
            return
        self.profile.pattern[idx], self.profile.pattern[idx + 1] = self.profile.pattern[idx + 1], self.profile.pattern[idx]
        self.reload_table()
        self.tree.selection_set(str(idx + 1))
