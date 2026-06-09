"""TODO: module documentation"""

import os
import tkinter as tk
from tkinter import messagebox, ttk

from app.tabs.auto_farm import AutoFarmTab


class FirmwareFlasherFrame(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection
        self._custom_hex_path = None

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Firmware Card
        fw_card = ttk.LabelFrame(self, text=" ⚡ Unggah Firmware Arduino Nano ", padding=20)
        fw_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        fw_card.columnconfigure(1, weight=1)
        fw_card.rowconfigure(4, weight=1)

        # Bootloader
        ttk.Label(fw_card, text="Tipe Bootloader:", font=("Helvetica", 10, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )
        self.bootloader_var = tk.StringVar(value="ATmega328P (Old Bootloader) (57600)")
        self.bootloader_combo = ttk.Combobox(
            fw_card,
            textvariable=self.bootloader_var,
            values=[
                "ATmega328P (New Bootloader) (115200)",
                "ATmega328P (Old Bootloader) (57600)",
                "ATmega168 (19200)",
            ],
            state="readonly",
            width=32,
        )
        self.bootloader_combo.grid(row=0, column=1, padx=(10, 0), pady=(0, 5), sticky="ew")

        # Hex file select
        ttk.Label(fw_card, text="Berkas Firmware (.hex):", font=("Helvetica", 10, "bold")).grid(
            row=1, column=0, sticky="w", pady=10
        )

        fw_select_frame = ttk.Frame(fw_card)
        fw_select_frame.grid(row=1, column=1, padx=(10, 0), pady=10, sticky="ew")
        fw_select_frame.columnconfigure(0, weight=1)

        self.hex_var = tk.StringVar()
        self.hex_combo = ttk.Combobox(fw_select_frame, textvariable=self.hex_var, state="readonly")
        self.hex_combo.grid(row=0, column=0, sticky="ew")

        self.btn_refresh_hex = tk.Button(
            fw_select_frame,
            text="🔄",
            font=("Segoe UI", 9, "bold"),
            bg="#57606f",
            fg="white",
            activebackground="#747d8c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.refresh_hex_files,
            width=3,
        )
        self.btn_refresh_hex.grid(row=0, column=1, padx=(5, 0))

        self.btn_browse_hex = tk.Button(
            fw_select_frame,
            text="📂 Pilih File...",
            font=("Segoe UI", 9, "bold"),
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.browse_custom_hex,
        )
        self.btn_browse_hex.grid(row=0, column=2, padx=(5, 0))

        # Flash button
        self.btn_flash = tk.Button(
            fw_card,
            text="⚡ UNGGAH FIRMWARE",
            bg="#dec0f1",
            fg="white",
            activebackground="#ffb142",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.start_firmware_flash,
        )
        self.btn_flash.grid(row=2, column=0, columnspan=2, pady=15, sticky="ew")

        self.lbl_operation_status = ttk.Label(
            fw_card, text="", font=("Segoe UI", 9), foreground="#747d8c"
        )
        self.lbl_operation_status.grid(row=3, column=0, columnspan=2, pady=(0, 5), sticky="w")

        # Flashing logs console (macOS styled)
        fw_log_frame = ttk.Frame(fw_card)
        fw_log_frame.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=(5, 0))
        fw_log_frame.columnconfigure(0, weight=1)
        fw_log_frame.rowconfigure(0, weight=1)

        term_container_fw = tk.Frame(
            fw_log_frame,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
        )
        term_container_fw.grid(row=0, column=0, sticky="nsew")
        term_container_fw.columnconfigure(0, weight=1)
        term_container_fw.rowconfigure(1, weight=1)

        term_header_fw = tk.Frame(term_container_fw, bg="#1b1b26", height=32)
        term_header_fw.grid(row=0, column=0, sticky="ew")
        term_header_fw.columnconfigure(2, weight=1)

        # dots
        dots = tk.Frame(term_header_fw, bg="#1b1b26")
        dots.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(dots, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 10, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 10, "bold")).pack(
            side="left", padx=2
        )
        tk.Label(dots, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 10, "bold")).pack(
            side="left", padx=2
        )

        tk.Label(
            term_header_fw,
            text="avrdude - flash@kbd-robot",
            font=("Consolas", 9, "bold"),
            fg="#94a3b8",
            bg="#1b1b26",
        ).grid(row=0, column=1, padx=(5, 10), pady=5, sticky="w")

        btn_frame_fw = tk.Frame(term_header_fw, bg="#1b1b26")
        btn_frame_fw.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        btn_copy_fw = tk.Button(
            btn_frame_fw,
            text="📋 Salin",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.copy_fw_log,
            padx=8,
        )
        btn_copy_fw.pack(side="left", padx=3)

        btn_clear_fw = tk.Button(
            btn_frame_fw,
            text="🗑️ Hapus",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#ef4444",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.clear_fw_log,
            padx=8,
        )
        btn_clear_fw.pack(side="left", padx=3)

        text_container_fw = tk.Frame(term_container_fw, bg="#13131c")
        text_container_fw.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        text_container_fw.columnconfigure(0, weight=1)
        text_container_fw.rowconfigure(0, weight=1)

        self.fw_console = tk.Text(
            text_container_fw,
            bg="#13131c",
            fg="#e2e8f0",
            font=("Consolas", 9),
            wrap="word",
            bd=0,
            padx=12,
            pady=12,
        )
        self.fw_console.grid(row=0, column=0, sticky="nsew")

        sb = ttk.Scrollbar(text_container_fw, orient="vertical", command=self.fw_console.yview)
        sb.grid(row=0, column=1, sticky="ns")
        self.fw_console.configure(yscrollcommand=sb.set)

        self.fw_console.tag_config("timestamp", foreground="#64748b")
        self.fw_console.tag_config("info", foreground="#38bdf8")
        self.fw_console.tag_config("success", foreground="#4ade80")
        self.fw_console.tag_config("error", foreground="#f87171")
        self.fw_console.tag_config("warning", foreground="#dec0f1")
        self.fw_console.tag_config("progress", foreground="#c084fc")
        self.fw_console.config(state="disabled")

        self.clear_fw_log()
        self.refresh_hex_files()

    def refresh_hex_files(self):
        """TODO: add documentation"""
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        firmware_dir = os.path.join(base_dir, "firmware")
        hex_files = []
        if os.path.exists(firmware_dir):
            for f in os.listdir(firmware_dir):
                if f.endswith(".hex"):
                    hex_files.append(f)
        if hasattr(self, "_custom_hex_path") and self._custom_hex_path:
            hex_files.append(f"📂 [Kustom] {os.path.basename(self._custom_hex_path)}")
        if hex_files:
            self.hex_combo["values"] = hex_files
            self.hex_combo.current(0)
        else:
            self.hex_combo["values"] = ["[Tidak ada berkas .hex di folder firmware/]"]
            self.hex_combo.current(0)

    def browse_custom_hex(self):
        """TODO: add documentation"""
        from tkinter import filedialog

        file_path = filedialog.askopenfilename(
            title="Pilih Berkas Firmware (.hex)",
            filetypes=[("Hex Files", "*.hex"), ("All Files", "*.*")],
        )
        if file_path:
            self._custom_hex_path = file_path
            filename = os.path.basename(file_path)
            custom_entry = f"📂 [Kustom] {filename}"
            vals = list(self.hex_combo["values"])
            if "[Tidak ada berkas .hex di folder firmware/]" in vals:
                vals = []
            if custom_entry not in vals:
                vals.append(custom_entry)
                self.hex_combo["values"] = vals
            self.hex_var.set(custom_entry)

    def start_firmware_flash(self):
        """TODO: add documentation"""
        # We need target port - we can query from connection manager or connection.port
        # If not connected, we can ask user COM port choice or check connection port.
        port = self.connection.port or "COM_SIMULATOR"
        if not self.connection.connected:
            # Flashing requires physical port. We can prompt or use a default
            # Let's search if connection port is set, or if we can get list of ports
            ports = self.connection.get_available_ports()
            if not ports:
                messagebox.showerror(
                    "Error", "Harap hubungkan Arduino Nano Anda terlebih dahulu di Dashboard Utama."
                )
                return
            port = ports[0]

        is_simulation = port == "COM_SIMULATOR"
        bootloader_type = self.bootloader_var.get()
        if "Old Bootloader" in bootloader_type:
            baudrate = 57600
            mcu = "m328p"
        elif "ATmega168" in bootloader_type:
            baudrate = 19200
            mcu = "m168p"
        else:
            baudrate = 115200
            mcu = "m328p"
        selected_hex = self.hex_var.get()
        if not selected_hex or "Tidak ada" in selected_hex:
            messagebox.showerror("Error", "Harap pilih berkas .hex yang valid.")
            return

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        hex_path = (
            self._custom_hex_path
            if selected_hex.startswith("📂 [Kustom]")
            else os.path.join(base_dir, "firmware", selected_hex)
        )

        confirm_msg = (
            f"Unggah firmware '{selected_hex}' ke Arduino di port {port}?\n\n"
            f"Bootloader: {bootloader_type}\n\n"
            "Data pada Arduino akan ditimpa."
        )
        if not messagebox.askyesno("Konfirmasi Flash", confirm_msg, icon="warning"):
            return

        self.btn_flash.config(state="disabled", text="⏳ FLASHING...")
        self.clear_fw_log()

        def log_cb(msg):
            """TODO: add documentation"""
            self.log_fw_message(msg)

        def completion_cb(success, msg):
            """TODO: add documentation"""
            self.btn_flash.config(state="normal", text="⚡ UNGGAH FIRMWARE")
            self.connection.disconnect()
            if success:
                self.log_fw_message("PROSES FLASHING SELESAI DENGAN SUKSES!")
                messagebox.showinfo("Sukses", "Firmware berhasil diunggah!")
            else:
                self.log_fw_message(f"PROSES FLASHING GAGAL: {msg}")
                messagebox.showerror("Gagal", f"Flashing gagal:\n\n{msg}")

        self.connection.flash_firmware(
            port=port,
            baudrate=baudrate,
            hex_path=hex_path,
            mcu=mcu,
            log_callback=log_cb,
            completion_callback=completion_cb,
        )

    def log_fw_message(self, message):
        """TODO: add documentation"""
        self.fw_console.config(state="normal")
        lower_msg = message.lower()
        if "memulai" in lower_msg or "=== " in lower_msg:
            self.fw_console.insert(tk.END, f"{message}\n", "timestamp")
        elif "error" in lower_msg or "failed" in lower_msg or "gagal" in lower_msg:
            self.fw_console.insert(tk.END, f"{message}\n", "error")
        elif "success" in lower_msg or "verified" in lower_msg or "thank you" in lower_msg:
            self.fw_console.insert(tk.END, f"{message}\n", "success")
        elif (
            "writing" in lower_msg
            or "reading" in lower_msg
            or "flashing" in lower_msg
            or "%" in lower_msg
            or "###" in lower_msg
        ):
            self.fw_console.insert(tk.END, f"{message}\n", "progress")
        else:
            self.fw_console.insert(tk.END, f"{message}\n", "info")
        self.fw_console.see(tk.END)
        self.fw_console.config(state="disabled")

    def clear_fw_log(self):
        """TODO: add documentation"""
        self.fw_console.config(state="normal")
        self.fw_console.delete("1.0", tk.END)
        self.fw_console.insert(tk.END, "=== KONSOL AKTIVITAS PENGUNGGAHAN ===\n", "timestamp")
        self.fw_console.config(state="disabled")

    def copy_fw_log(self):
        """TODO: add documentation"""
        self.clipboard_clear()
        self.clipboard_append(self.fw_console.get("1.0", tk.END).strip())
        messagebox.showinfo("Sukses", "Log berhasil disalin!")


class AutoFarmFirmwareTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection, reload_callback):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.auto_farm = AutoFarmTab(self.notebook, profile, connection)
        self.flasher = FirmwareFlasherFrame(self.notebook, profile, connection)

        self.notebook.add(self.auto_farm, text=" 🤖 Auto Rune & Boss ")
        self.notebook.add(self.flasher, text=" ⚡ Unggah Firmware ")

    @property
    def on_profile_updated(self):
        """TODO: add documentation"""
        return getattr(self, "_on_profile_updated", None)

    @on_profile_updated.setter
    def on_profile_updated(self, value):
        """TODO: add documentation"""
        self._on_profile_updated = value
        self.auto_farm.on_profile_updated = value
        self.flasher.on_profile_updated = value

    def reload_table(self):
        """TODO: add documentation"""
        if hasattr(self.auto_farm, "reload_table"):
            self.auto_farm.reload_table()

    def reload_from_profile(self):
        """TODO: add documentation"""
        if hasattr(self.auto_farm, "reload_from_profile"):
            self.auto_farm.reload_from_profile()
        elif hasattr(self.auto_farm, "reload_table"):
            self.auto_farm.reload_table()
