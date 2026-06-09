"""TODO: module documentation"""

import tkinter as tk
from tkinter import messagebox, ttk

from app.models import Action
from app.tabs.recorder import RecorderTab
from app.tabs.simulation import SimulationTab


class PatternEditorFrame(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Header Frame
        header = tk.Frame(self, bg="#13131c")
        header.grid(row=0, column=0, columnspan=2, padx=15, pady=(12, 4), sticky="ew")
        header.columnconfigure(1, weight=1)

        tk.Label(
            header,
            text="🎮  Pembuat Pola Urutan Aksi",
            font=("Segoe UI", 12, "bold"),
            fg="#e2e8f0",
            bg="#13131c",
        ).grid(row=0, column=0, sticky="w")

        self.lbl_duration = tk.Label(
            header,
            text="⏱  Estimasi: 0.00 detik",
            font=("Consolas", 10, "bold"),
            fg="#4ade80",
            bg="#272736",
            padx=10,
            pady=4,
        )
        self.lbl_duration.grid(row=0, column=2, sticky="e", padx=5)

        # Main Layout
        # Left side: Treeview table
        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=1, column=0, padx=15, pady=10, sticky="nsew")
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.rowconfigure(0, weight=1)

        columns = ("index", "action", "press_dur", "delay_dur")
        self.tree = ttk.Treeview(
            self.table_frame, columns=columns, show="headings", selectmode="browse"
        )
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
        tk.Label(
            edit_panel,
            text="Tipe Aksi Terpilih:",
            font=("Segoe UI", 9, "bold"),
            fg="#94a3b8",
            bg="#1a1a24",
        ).pack(anchor="w", pady=(0, 4))
        self.action_var = tk.StringVar(value="NONE")
        self.action_combo = ttk.Combobox(
            edit_panel,
            textvariable=self.action_var,
            values=Action.TYPES,
            state="readonly",
            width=22,
        )
        self.action_combo.pack(anchor="w", pady=(0, 14))
        self.action_combo.bind("<<ComboboxSelected>>", self.on_fields_changed)

        tk.Label(
            edit_panel,
            text="Durasi Tekan (ms):",
            font=("Segoe UI", 9, "bold"),
            fg="#94a3b8",
            bg="#1a1a24",
        ).pack(anchor="w", pady=(0, 4))
        self.press_var = tk.IntVar(value=200)
        self.press_spin = ttk.Spinbox(
            edit_panel, from_=50, to=10000, increment=50, textvariable=self.press_var, width=21
        )
        self.press_spin.pack(anchor="w", pady=(0, 14))
        self.press_spin.bind("<FocusOut>", self.on_fields_changed)
        self.press_spin.bind("<Return>", self.on_fields_changed)

        tk.Label(
            edit_panel,
            text="Durasi Jeda (ms):",
            font=("Segoe UI", 9, "bold"),
            fg="#94a3b8",
            bg="#1a1a24",
        ).pack(anchor="w", pady=(0, 4))
        self.delay_var = tk.IntVar(value=500)
        self.delay_spin = ttk.Spinbox(
            edit_panel, from_=0, to=60000, increment=100, textvariable=self.delay_var, width=21
        )
        self.delay_spin.pack(anchor="w", pady=(0, 20))
        self.delay_spin.bind("<FocusOut>", self.on_fields_changed)
        self.delay_spin.bind("<Return>", self.on_fields_changed)

        # Buttons
        btn_grid = ttk.Frame(edit_panel)
        btn_grid.pack(fill="x", pady=5)
        btn_grid.columnconfigure(0, weight=1)
        btn_grid.columnconfigure(1, weight=1)

        btn_add = tk.Button(
            btn_grid,
            text="✨ Tambah Aksi",
            font=("Segoe UI", 9, "bold"),
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.add_action,
            pady=8,
        )
        btn_add.grid(row=0, column=0, padx=2, pady=5, sticky="ew")
        btn_add.bind("<Enter>", lambda e, b=btn_add: b.config(bg="#ff9ff3"))
        btn_add.bind("<Leave>", lambda e, b=btn_add: b.config(bg="#ff75a0"))

        btn_delete = tk.Button(
            btn_grid,
            text="🗑️ Hapus Aksi",
            font=("Segoe UI", 9, "bold"),
            bg="#ff4757",
            fg="white",
            activebackground="#ff6b81",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.delete_action,
            pady=8,
        )
        btn_delete.grid(row=0, column=1, padx=2, pady=5, sticky="ew")
        btn_delete.bind("<Enter>", lambda e, b=btn_delete: b.config(bg="#ff6b81"))
        btn_delete.bind("<Leave>", lambda e, b=btn_delete: b.config(bg="#ff4757"))

        btn_dup = tk.Button(
            btn_grid,
            text="📋 Duplikat Aksi",
            font=("Segoe UI", 9, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.duplicate_action,
            pady=8,
        )
        btn_dup.grid(row=1, column=0, columnspan=2, padx=2, pady=5, sticky="ew")
        btn_dup.bind("<Enter>", lambda e, b=btn_dup: b.config(bg="#47475c", fg="white"))
        btn_dup.bind("<Leave>", lambda e, b=btn_dup: b.config(bg="#272736", fg="#cbd5e1"))

        # Up/Down Move Buttons
        btn_move_frame = ttk.Frame(edit_panel)
        btn_move_frame.pack(fill="x", pady=10)
        btn_move_frame.columnconfigure(0, weight=1)
        btn_move_frame.columnconfigure(1, weight=1)

        btn_up = tk.Button(
            btn_move_frame,
            text="⬆️ Geser Ke Atas",
            font=("Segoe UI", 9, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.move_up,
            pady=8,
        )
        btn_up.grid(row=0, column=0, padx=2, sticky="ew")
        btn_up.bind("<Enter>", lambda e, b=btn_up: b.config(bg="#47475c", fg="white"))
        btn_up.bind("<Leave>", lambda e, b=btn_up: b.config(bg="#272736", fg="#cbd5e1"))

        btn_down = tk.Button(
            btn_move_frame,
            text="⬇️ Geser Ke Bawah",
            font=("Segoe UI", 9, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.move_down,
            pady=8,
        )
        btn_down.grid(row=0, column=1, padx=2, sticky="ew")
        btn_down.bind("<Enter>", lambda e, b=btn_down: b.config(bg="#47475c", fg="white"))
        btn_down.bind("<Leave>", lambda e, b=btn_down: b.config(bg="#272736", fg="#cbd5e1"))

        # Premium Save Pattern Button
        btn_save = tk.Button(
            edit_panel,
            text="💾  SAVE",
            font=("Segoe UI", 10, "bold"),
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.save_profile,
            pady=10,
        )
        btn_save.pack(fill="x", pady=(15, 0))
        btn_save.bind("<Enter>", lambda e, b=btn_save: b.config(bg="#26af5f"))
        btn_save.bind("<Leave>", lambda e, b=btn_save: b.config(bg="#2ed573"))

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.reload_table()

    def update_duration_estimation(self):
        """TODO: add documentation"""
        total_ms = sum(
            action.press_duration + action.delay_duration for action in self.profile.pattern
        )

        if not self.profile.pattern:
            self.lbl_duration.config(text="Estimasi: 0.00 detik")
            return

        if self.profile.loop_mode == "INFINITY":
            duration_text = f"Estimasi: {total_ms / 1000:.2f} detik per siklus (Loop: ∞)"
        else:
            total_time = total_ms * self.profile.loop_count
            duration_text = (
                f"Estimasi Total: {total_time / 1000:.2f} detik ({self.profile.loop_count}x loop)"
            )

        self.lbl_duration.config(text=duration_text)

    def reload_table(self):
        """TODO: add documentation"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, action in enumerate(self.profile.pattern):
            self.tree.insert(
                "",
                "end",
                iid=str(i),
                values=(i + 1, action.action_type, action.press_duration, action.delay_duration),
            )
        self.update_duration_estimation()

    def on_select(self, event):
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        action = self.profile.pattern[idx]
        self.action_var.set(action.action_type)
        self.press_var.set(action.press_duration)
        self.delay_var.set(action.delay_duration)

    def on_fields_changed(self, event=None):
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        action = self.profile.pattern[idx]

        try:
            action.action_type = self.action_var.get()
            action.press_duration = max(50, int(self.press_var.get()))
            action.delay_duration = max(0, int(self.delay_var.get()))

            self.tree.item(
                str(idx),
                values=(idx + 1, action.action_type, action.press_duration, action.delay_duration),
            )
            self.update_duration_estimation()
        except ValueError:
            pass

    def add_action(self):
        """TODO: add documentation"""
        new_act = Action("NONE", 200, 500)
        self.profile.pattern.append(new_act)
        self.reload_table()
        new_idx = str(len(self.profile.pattern) - 1)
        self.tree.selection_set(new_idx)
        self.tree.see(new_idx)

    def delete_action(self):
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        if not messagebox.askyesno(
            "Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus aksi terpilih?"
        ):
            return
        self.profile.pattern.pop(idx)
        self.reload_table()
        if self.profile.pattern:
            new_idx = str(min(idx, len(self.profile.pattern) - 1))
            self.tree.selection_set(new_idx)

    def duplicate_action(self):
        """TODO: add documentation"""
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
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        if idx == 0:
            return
        self.profile.pattern[idx], self.profile.pattern[idx - 1] = (
            self.profile.pattern[idx - 1],
            self.profile.pattern[idx],
        )
        self.reload_table()
        self.tree.selection_set(str(idx - 1))

    def move_down(self):
        """TODO: add documentation"""
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        if idx >= len(self.profile.pattern) - 1:
            return
        self.profile.pattern[idx], self.profile.pattern[idx + 1] = (
            self.profile.pattern[idx + 1],
            self.profile.pattern[idx],
        )
        self.reload_table()
        self.tree.selection_set(str(idx + 1))

    def save_profile(self):
        """TODO: add documentation"""
        # Validasi hanya pola
        issues = []
        if not self.profile.pattern:
            issues.append(
                "KRITIS: Pembuat Pola berisi 0 aksi. Arduino tidak memiliki apa pun untuk dijalankan!"
            )
        else:
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
                self.connection.log(f"[Pembuat Makro] Profil berhasil disimpan ke berkas: {fname}")
            except Exception as e:
                print("Error occurred")
                messagebox.showerror("Error", f"Gagal menyimpan profil ke berkas: {str(e)}")
                return
        else:
            self.connection.log("[Pembuat Makro] Pola berhasil diperbarui di memori aktif.")

        # Pemicu pembaruan sinkronisasi pada editor Manajer Profil dan tab lainnya
        if hasattr(self, "on_profile_updated") and self.on_profile_updated:
            self.on_profile_updated()

        messagebox.showinfo(
            "Berhasil",
            "Pola makro berhasil disimpan ke Manajer Profil (Editor) tanpa menimpa kalibrasi servo!",
        )


class PatternBuilderTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.editor = PatternEditorFrame(self.notebook, profile, connection)
        self.recorder = RecorderTab(self.notebook, profile, connection)
        self.simulation = SimulationTab(self.notebook, profile, connection)

        self.notebook.add(self.editor, text=" 🧱 Pembuat Pola ")
        self.notebook.add(self.recorder, text=" 🔴 Perekam Aksi ")
        self.notebook.add(self.simulation, text=" 🎹 Uji Coba & Simulasi ")

    @property
    def on_profile_updated(self):
        """TODO: add documentation"""
        return getattr(self, "_on_profile_updated", None)

    @on_profile_updated.setter
    def on_profile_updated(self, value):
        """TODO: add documentation"""
        self._on_profile_updated = value
        self.editor.on_profile_updated = value
        self.recorder.on_profile_updated = value
        self.simulation.on_profile_updated = value

    def reload_table(self):
        """TODO: add documentation"""
        if hasattr(self.editor, "reload_table"):
            self.editor.reload_table()
        if hasattr(self.recorder, "reload_table"):
            self.recorder.reload_table()
        if hasattr(self.simulation, "reload_table"):
            self.simulation.reload_table()

    def reload_from_profile(self):
        """TODO: add documentation"""
        if hasattr(self.editor, "reload_from_profile"):
            self.editor.reload_from_profile()
        elif hasattr(self.editor, "reload_table"):
            self.editor.reload_table()

        if hasattr(self.recorder, "reload_from_profile"):
            self.recorder.reload_from_profile()
        elif hasattr(self.recorder, "reload_table"):
            self.recorder.reload_table()

        if hasattr(self.simulation, "reload_from_profile"):
            self.simulation.reload_from_profile()
        elif hasattr(self.simulation, "reload_table"):
            self.simulation.reload_table()
