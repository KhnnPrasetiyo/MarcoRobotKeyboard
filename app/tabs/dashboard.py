"""TODO: module documentation"""

import json
import os
import threading
import time
import tkinter as tk
import urllib.request
from tkinter import messagebox, ttk

from app.driver_manager import (detect_connected_chips,
                                download_and_install_driver)


class DashboardTab(ttk.Frame):
    """TODO: add documentation"""

    def __init__(self, parent, profile, connection, log_box):
        """TODO: add documentation"""
        super().__init__(parent)
        self.profile = profile
        self.connection = connection
        self.log_box = log_box

        # State files & variables
        import sys

        if getattr(sys, "frozen", False):
            _settings_dir = os.path.dirname(sys.executable)
        else:
            _settings_dir = os.path.abspath(".")
        self.wallet_file = os.path.join(_settings_dir, "wallet_settings.json")
        self.wallet_address = tk.StringVar(value=self.load_wallet_address())
        self.session_active = False
        self.session_start_time = None
        self.current_nxpc = 0.0
        self.current_neso = 0.0
        self.initial_nxpc = None
        self.initial_neso = None
        self.rpc_connected = False
        self.rpc_error = ""
        self.running = True
        self.lock = threading.Lock()
        self._last_chips = []

        # Configure columns: Left Column (Controls & Settings), Right Column (Console Logs)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Create Left side scrollable content
        left_container = ttk.Frame(self)
        left_container.grid(row=0, column=0, sticky="nsew", padx=(15, 10), pady=10)
        left_container.columnconfigure(0, weight=1)
        left_container.rowconfigure(0, weight=1)

        # Scrollable Canvas
        left_scroll = tk.Canvas(left_container, borderwidth=0, highlightthickness=0, bg="#1a1a24")
        scrollbar = ttk.Scrollbar(left_container, orient="vertical", command=left_scroll.yview)

        self.scrollable_left = ttk.Frame(left_scroll)
        self.scrollable_left.bind(
            "<Configure>", lambda e: left_scroll.configure(scrollregion=left_scroll.bbox("all"))
        )
        canvas_window = left_scroll.create_window((0, 0), window=self.scrollable_left, anchor="nw")
        left_scroll.configure(yscrollcommand=scrollbar.set)
        left_scroll.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.scrollable_left.columnconfigure(0, weight=1)

        # Make scrollable frame stretch to canvas width on window resize
        left_scroll.bind(
            "<Configure>",
            lambda e: (
                left_scroll.itemconfigure(canvas_window, width=e.width),
                left_scroll.configure(scrollregion=left_scroll.bbox("all")),
            ),
        )

        # --- Left Panel Cards ---
        self.create_serial_card(self.scrollable_left)
        self.create_control_card(self.scrollable_left)
        self.create_wallet_card(self.scrollable_left)

        # --- Right Panel (Direct Log Console Card) ---
        self.create_log_card(self)

        # Start periodic loops & background tasks
        self.clear_log()
        self.update_log_loop()
        self.update_duration()
        self.update_timer_loop()
        self.refresh_ports()
        self.poll_usb_hardware()

        # Start metamask RPC thread
        self.poll_thread = threading.Thread(target=self.rpc_polling_loop, daemon=True)
        self.poll_thread.start()

    def destroy(self):
        """TODO: add documentation"""
        self.running = False
        super().destroy()

    def load_wallet_address(self):
        """TODO: add documentation"""
        if os.path.exists(self.wallet_file):
            try:
                with open(self.wallet_file, "r") as f:
                    data = json.load(f)
                    return data.get("wallet_address", "")
            except Exception as e:
                print("Error occurred")
                pass
        return ""

    def save_wallet_address(self):
        """TODO: add documentation"""
        addr = self.wallet_address.get().strip()
        if addr and (not addr.startswith("0x") or len(addr) != 42):
            messagebox.showerror(
                "Error",
                "Alamat wallet MetaMask tidak valid!\nAlamat harus diawali dengan '0x' dan memiliki panjang 42 karakter.",
            )
            return

        try:
            with open(self.wallet_file, "w") as f:
                json.dump({"wallet_address": addr}, f, indent=4)
            self.connection.log(
                f"Alamat wallet disimpan: {addr[:6]}...{addr[-4:]}"
                if addr
                else "Alamat wallet dihapus."
            )
            messagebox.showinfo("Berhasil", "Alamat wallet berhasil disimpan!")
            with self.lock:
                self.initial_nxpc = None
                self.initial_neso = None
            self.trigger_rpc_fetch()
            self.update_ui_state_visibility()
        except Exception as e:
            print("Error occurred")
            messagebox.showerror("Error", f"Gagal menyimpan wallet: {str(e)}")

    def delete_wallet_address(self):
        """TODO: add documentation"""
        self.wallet_address.set("")
        self.save_wallet_address()

    # --- Left Card 1: Serial Manager & USB Status ---
    def create_serial_card(self, parent):
        """TODO: add documentation"""
        card = ttk.LabelFrame(parent, text=" 🔌 Koneksi Serial & Perangkat ", padding=15)
        card.pack(fill="x", pady=10, padx=10)
        card.columnconfigure(1, weight=1)

        # Port selection
        ttk.Label(card, text="Port COM:", font=("Helvetica", 9, "bold")).grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.port_var = tk.StringVar()
        self.port_combo = ttk.Combobox(card, textvariable=self.port_var, width=15, state="readonly")
        self.port_combo.bind("<<ComboboxSelected>>", lambda e: self.check_connection_readiness())
        self.port_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Refresh port button
        self.btn_refresh = tk.Button(
            card,
            text="🔄",
            font=("Segoe UI", 9, "bold"),
            bg="#57606f",
            fg="white",
            activebackground="#747d8c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.refresh_ports,
            padx=6,
        )
        self.btn_refresh.grid(row=0, column=2, padx=5, pady=5)

        # Baudrate
        ttk.Label(card, text="Baud Rate:", font=("Helvetica", 9, "bold")).grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.baud_var = tk.StringVar(value="9600")
        self.baud_combo = ttk.Combobox(
            card,
            textvariable=self.baud_var,
            values=["9600", "19200", "38400", "57600", "115200"],
            width=15,
            state="readonly",
        )
        self.baud_combo.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # Connect button
        self.btn_connect = tk.Button(
            card,
            text="🔌 HUBUNGKAN PERANGKAT",
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.toggle_connect,
        )
        self.btn_connect.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")

        # USB hardware scan status
        self.driver_status_frame = ttk.Frame(card)
        self.driver_status_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=5)

        self.lbl_hw_status = ttk.Label(
            self.driver_status_frame,
            text="Memindai USB...",
            font=("Segoe UI", 8),
            foreground="#747d8c",
        )
        self.lbl_hw_status.pack(side="left", anchor="w")

        self.btn_install_driver = tk.Button(
            self.driver_status_frame,
            text="Pasang Driver",
            font=("Segoe UI", 8, "bold"),
            bg="#dec0f1",
            fg="white",
            activebackground="#ffb142",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=6,
        )

    # --- Left Card 2: Control Panel ---
    def create_control_card(self, parent):
        """TODO: add documentation"""
        card = ttk.LabelFrame(parent, text=" 🚀 Kontrol Real-Time & Status ", padding=15)
        card.pack(fill="x", pady=10, padx=10)
        card.columnconfigure(1, weight=1)

        # Status labels
        status_frame = ttk.Frame(card)
        status_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        ttk.Label(status_frame, text="Status Robot:", font=("Helvetica", 10, "bold")).pack(
            side=tk.LEFT, padx=2
        )
        self.status_val = ttk.Label(
            status_frame, text="Terputus", font=("Helvetica", 10), foreground="#ff4757"
        )
        self.status_val.pack(side=tk.LEFT, padx=5)

        self.progress_val = ttk.Label(
            status_frame, text="", font=("Helvetica", 9), foreground="#dec0f1"
        )
        self.progress_val.pack(side=tk.LEFT, padx=10)

        self.lbl_total_time = ttk.Label(
            card, text="⏱ Pola Kosong", font=("Helvetica", 9, "bold"), foreground="#2ed573"
        )
        self.lbl_total_time.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 10))

        # Control Buttons
        btn_frame = ttk.Frame(card)
        btn_frame.grid(row=2, column=0, columnspan=2, sticky="ew")
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        btn_start = tk.Button(
            btn_frame,
            text="🚀 JALANKAN ROBOT",
            font=("Segoe UI", 9, "bold"),
            bg="#2ed573",
            fg="white",
            activebackground="#26af5f",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.start_pattern,
        )
        btn_start.grid(row=0, column=0, padx=3, pady=4, sticky="ew")

        btn_stop = tk.Button(
            btn_frame,
            text="⏹️ HENTIKAN ROBOT",
            font=("Segoe UI", 9, "bold"),
            bg="#dec0f1",
            fg="white",
            activebackground="#ffb142",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.stop_pattern,
        )

        btn_stop.grid(row=0, column=1, padx=3, pady=4, sticky="ew")

        btn_estop = tk.Button(
            btn_frame,
            text="🚨 DARURAT STOP (E-STOP)",
            font=("Segoe UI", 9, "bold"),
            bg="#ff4757",
            fg="white",
            activebackground="#ff6b81",
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.estop,
        )
        btn_estop.grid(row=1, column=0, columnspan=2, padx=3, pady=6, sticky="ew")

    # --- Left Card 3: MetaMask & NESO Tracker ---
    def create_wallet_card(self, parent):
        """TODO: add documentation"""
        card = ttk.LabelFrame(parent, text=" 🦊 MetaMask & Saldo NESO ", padding=15)
        card.pack(fill="x", pady=10, padx=10)
        card.columnconfigure(0, weight=1)

        # Wallet address input
        tk.Label(
            card, text="Alamat MetaMask:", font=("Segoe UI", 9, "bold"), fg="#dec0f1", bg="#1a1a24"
        ).pack(anchor="w", pady=(0, 2))
        self.entry_wallet = ttk.Entry(card, textvariable=self.wallet_address, font=("Consolas", 9))
        self.entry_wallet.pack(fill="x", ipady=4, pady=(0, 8))

        # Save/delete buttons
        btn_wallet_frame = ttk.Frame(card)
        btn_wallet_frame.pack(fill="x", pady=(0, 8))
        btn_wallet_frame.columnconfigure(0, weight=1)
        btn_wallet_frame.columnconfigure(1, weight=1)

        self.btn_save_wallet = tk.Button(
            btn_wallet_frame,
            text="💾 Simpan",
            bg="#ff75a0",
            fg="white",
            activebackground="#ff9ff3",
            font=("Segoe UI", 8, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.save_wallet_address,
        )
        self.btn_save_wallet.grid(row=0, column=0, padx=2, sticky="ew")

        self.btn_delete_wallet = tk.Button(
            btn_wallet_frame,
            text="🗑️ Hapus",
            bg="#ff4757",
            fg="white",
            activebackground="#ff6b81",
            font=("Segoe UI", 8, "bold"),
            relief="flat",
            bd=0,
            height=2,
            cursor="hand2",
            command=self.delete_wallet_address,
        )
        self.btn_delete_wallet.grid(row=0, column=1, padx=2, sticky="ew")

        # Blockchain status L1
        self.lbl_rpc_status = ttk.Label(
            card,
            text="● Memeriksa Koneksi Jaringan...",
            font=("Helvetica", 8, "bold"),
            foreground="#dec0f1",
        )
        self.lbl_rpc_status.pack(anchor="w", pady=4)

        # Digital Timer session
        self.timer_frame = tk.Frame(
            card,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
        )
        self.timer_frame.pack(fill="x", pady=6, ipady=8)

        tk.Label(
            self.timer_frame,
            text="DURASI BERJALAN SESI INI",
            font=("Segoe UI", 7, "bold"),
            background="#0d1117",
            foreground="#64748b",
        ).pack(pady=(4, 0))
        self.lbl_timer = tk.Label(
            self.timer_frame,
            text="00:00:00",
            font=("Consolas", 20, "bold"),
            background="#0d1117",
            foreground="#4ade80",
        )
        self.lbl_timer.pack(pady=2)

        # Earnings Display
        self.earn_frame = ttk.Frame(card)
        self.earn_frame.pack(fill="x", pady=5)
        self.earn_frame.columnconfigure(0, weight=1)
        self.earn_frame.columnconfigure(1, weight=1)

        ttk.Label(
            self.earn_frame, text="SALDO WALLET", font=("Segoe UI", 7, "bold"), foreground="#dec0f1"
        ).grid(row=0, column=0, sticky="w")
        ttk.Label(
            self.earn_frame,
            text="PENDAPATAN SESI INI",
            font=("Segoe UI", 7, "bold"),
            foreground="#4ade80",
        ).grid(row=0, column=1, sticky="w")

        self.lbl_bal_nxpc = ttk.Label(
            self.earn_frame, text="0.0000 NXPC", font=("Consolas", 10, "bold")
        )
        self.lbl_bal_nxpc.grid(row=1, column=0, sticky="w", pady=1)
        self.lbl_bal_neso = ttk.Label(
            self.earn_frame, text="0 NESO", font=("Consolas", 8), foreground="#a4b0be"
        )
        self.lbl_bal_neso.grid(row=2, column=0, sticky="w", pady=1)

        self.lbl_earn_nxpc = ttk.Label(
            self.earn_frame,
            text="+0.0000 NXPC",
            font=("Consolas", 10, "bold"),
            foreground="#2ed573",
        )
        self.lbl_earn_nxpc.grid(row=1, column=1, sticky="w", pady=1)
        self.lbl_earn_neso = ttk.Label(
            self.earn_frame, text="+0 NESO", font=("Consolas", 8), foreground="#2ed573"
        )
        self.lbl_earn_neso.grid(row=2, column=1, sticky="w", pady=1)

        self.lbl_no_wallet = ttk.Label(
            card,
            text="⚠️ Masukkan wallet MetaMask Anda.",
            font=("Helvetica", 8, "bold"),
            foreground="#dec0f1",
        )

        self.update_ui_state_visibility()

    def update_ui_state_visibility(self):
        """TODO: add documentation"""
        addr = self.wallet_address.get().strip()
        if addr:
            self.lbl_no_wallet.pack_forget()
            self.timer_frame.pack(fill="x", pady=6, ipady=8)
            self.earn_frame.pack(fill="x", pady=5)
        else:
            self.timer_frame.pack_forget()
            self.earn_frame.pack_forget()
            self.lbl_no_wallet.pack(pady=5)

    # --- Right Card: Logs Console Terminal ---
    def create_log_card(self, parent):
        """TODO: add documentation"""
        log_card = ttk.LabelFrame(parent, text=" Output Konsol Langsung ", padding=15)
        log_card.grid(row=0, column=1, padx=(10, 15), pady=10, sticky="nsew")
        log_card.columnconfigure(0, weight=1)
        log_card.rowconfigure(0, weight=1)

        term_container = tk.Frame(
            log_card,
            bg="#13131c",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#47475c",
            highlightcolor="#47475c",
        )
        term_container.grid(row=0, column=0, sticky="nsew")
        term_container.columnconfigure(0, weight=1)
        term_container.rowconfigure(1, weight=1)

        term_header = tk.Frame(term_container, bg="#1b1b26", height=32)
        term_header.grid(row=0, column=0, sticky="ew")
        term_header.columnconfigure(2, weight=1)

        # macOS style dots
        dots_frame = tk.Frame(term_header, bg="#1b1b26")
        dots_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(
            dots_frame, text="●", fg="#ff5f56", bg="#1b1b26", font=("Helvetica", 10, "bold")
        ).pack(side="left", padx=2)
        tk.Label(
            dots_frame, text="●", fg="#ffbd2e", bg="#1b1b26", font=("Helvetica", 10, "bold")
        ).pack(side="left", padx=2)
        tk.Label(
            dots_frame, text="●", fg="#27c93f", bg="#1b1b26", font=("Helvetica", 10, "bold")
        ).pack(side="left", padx=2)

        tk.Label(
            term_header,
            text="bash - dashboard@kbd-robot",
            font=("Consolas", 9, "bold"),
            fg="#94a3b8",
            bg="#1b1b26",
        ).grid(row=0, column=1, padx=(5, 10), pady=5, sticky="w")

        btn_frame = tk.Frame(term_header, bg="#1b1b26")
        btn_frame.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        btn_copy_log = tk.Button(
            btn_frame,
            text="📋 Salin",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#47475c",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.copy_log,
            padx=8,
        )
        btn_copy_log.pack(side="left", padx=3)

        btn_clear_log = tk.Button(
            btn_frame,
            text="🗑️ Hapus",
            font=("Segoe UI", 8, "bold"),
            bg="#272736",
            fg="#cbd5e1",
            activebackground="#ef4444",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.clear_log,
            padx=8,
        )
        btn_clear_log.pack(side="left", padx=3)

        text_container = tk.Frame(term_container, bg="#13131c")
        text_container.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        text_container.columnconfigure(0, weight=1)
        text_container.rowconfigure(0, weight=1)

        self.console = tk.Text(
            text_container,
            bg="#13131c",
            fg="#e2e8f0",
            font=("Consolas", 9),
            wrap="word",
            bd=0,
            padx=12,
            pady=12,
            spacing1=2,
            spacing2=1,
            spacing3=2,
            selectbackground="#47475c",
            selectforeground="#ffffff",
            insertbackground="#ffffff",
        )
        self.console.grid(row=0, column=0, sticky="nsew")

        sb_log = ttk.Scrollbar(text_container, orient="vertical", command=self.console.yview)
        sb_log.grid(row=0, column=1, sticky="ns")
        self.console.configure(yscrollcommand=sb_log.set)

        self.console.tag_config("timestamp", foreground="#64748b")
        self.console.tag_config("info", foreground="#38bdf8")
        self.console.tag_config("success", foreground="#4ade80")
        self.console.tag_config("error", foreground="#f87171")
        self.console.tag_config("warning", foreground="#dec0f1")
        self.console.tag_config("driver", foreground="#fb923c")
        self.console.config(state="disabled")

    # --- Dashboard Action Methods ---
    def start_pattern(self):
        """TODO: add documentation"""
        self.connection.send_command("START")

    def stop_pattern(self):
        """TODO: add documentation"""
        self.connection.send_command("STOP")

    def estop(self):
        """TODO: add documentation"""
        self.connection.send_command("ESTOP")
        self.connection.log("Perintah DARURAT STOP dikirim!")

    def check_status(self):
        """TODO: add documentation"""
        self.connection.send_command("STATUS")

    def clear_log(self):
        """TODO: add documentation"""
        self.console.config(state="normal")
        self.console.delete("1.0", tk.END)
        self.console.insert(tk.END, "=== OUTPUT KONSOL ROBOT ===\n", "timestamp")
        self.console.config(state="disabled")

    def copy_log(self):
        """TODO: add documentation"""
        self.clipboard_clear()
        self.clipboard_append(self.console.get("1.0", tk.END).strip())
        messagebox.showinfo("Sukses", "Konsol output langsung berhasil disalin!")

    def log_message(self, message):
        """TODO: add documentation"""
        t_str = time.strftime("%H:%M:%S")
        self.console.config(state="normal")
        self.console.insert(tk.END, f"[{t_str}] ", "timestamp")
        lower_msg = message.lower()
        if (
            "error" in lower_msg
            or "failed" in lower_msg
            or "gagal" in lower_msg
            or "estop" in lower_msg
            or "darurat" in lower_msg
        ):
            self.console.insert(tk.END, f"{message}\n", "error")
        elif (
            "success" in lower_msg
            or "berhasil" in lower_msg
            or "connected to" in lower_msg
            or "terhubung" in lower_msg
            or "start" in lower_msg
        ):
            self.console.insert(tk.END, f"{message}\n", "success")
        elif "warning" in lower_msg or "peringatan" in lower_msg:
            self.console.insert(tk.END, f"{message}\n", "warning")
        elif "driver" in lower_msg or "instal" in lower_msg:
            self.console.insert(tk.END, f"{message}\n", "driver")
        else:
            self.console.insert(tk.END, f"{message}\n", "info")
        self.console.see(tk.END)
        self.console.config(state="disabled")

    def update_status_label(self, status):
        """TODO: add documentation"""
        if status.startswith("STEP:"):
            try:
                step_info = status[5:]
                current, total = step_info.split("/")
                self.progress_val.config(text=f"⚡ Langkah: {current} / {total}")
            except (ValueError, IndexError):
                pass
            return

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
            self.status_val.config(foreground="#dec0f1")
        else:
            self.status_val.config(foreground="#ff4757")

        if (
            "STOPPED" in status
            or "IDLE" in status
            or "EMERGENCY" in status
            or "Disconnected" in status
        ):
            self.progress_val.config(text="")

    def update_log_loop(self):
        """TODO: add documentation"""
        if not self.log_box.empty():
            while not self.log_box.empty():
                line = self.log_box.get()
                self.log_message(line)
        self.after(100, self.update_log_loop)

    def reload_table(self):
        """TODO: add documentation"""
        self.update_duration()

    def reload_from_profile(self):
        """TODO: add documentation"""
        self.update_duration()

    def update_duration(self):
        """TODO: add documentation"""
        total_ms = sum(a.press_duration + a.delay_duration for a in self.profile.pattern)
        if not self.profile.pattern:
            self.lbl_total_time.config(text="⏱ Pola Kosong")
            return
        if self.profile.loop_mode == "INFINITY":
            duration_text = f"⏱ Estimasi: {total_ms / 1000:.2f} dtk/siklus (∞)"
        else:
            total_time = total_ms * self.profile.loop_count
            duration_text = (
                f"⏱ Estimasi Total: {total_time / 1000:.2f} dtk ({self.profile.loop_count}x loop)"
            )
        self.lbl_total_time.config(text=duration_text)

    # --- Serial Logic Methods ---
    def poll_usb_hardware(self):
        """TODO: add documentation"""
        try:
            if not self.winfo_exists() or not self.running:
                return
        except Exception as e:
            print("Error occurred")
            return

        def bg_scan():
            """TODO: add documentation"""
            chips = detect_connected_chips()
            try:
                if self.winfo_exists() and self.running:
                    self.after(0, lambda: self.update_hw_status_ui(chips))
            except Exception as e:
                print("Error occurred")
                pass

        threading.Thread(target=bg_scan, daemon=True).start()
        self.after(3000, self.poll_usb_hardware)

    def update_hw_status_ui(self, chips):
        """TODO: add documentation"""
        self._last_chips = chips
        self.btn_install_driver.pack_forget()
        if not chips:
            self.lbl_hw_status.config(text="🔌 Menunggu perangkat Arduino...", foreground="#747d8c")
            self.check_connection_readiness()
            return
        missing_driver_chip = next((c for c in chips if not c["has_driver"]), None)
        working_chip = next((c for c in chips if c["has_driver"]), None)
        if missing_driver_chip:
            chip_name = missing_driver_chip["chip_type"]
            self.lbl_hw_status.config(
                text=f"⚠️ Driver {chip_name} belum terpasang!", foreground="#dec0f1"
            )
            self.btn_install_driver.config(
                text=f"⚡ Pasang Driver {chip_name}",
                command=lambda: self.trigger_driver_install(chip_name),
            )
            self.btn_install_driver.pack(side="right", padx=5)
        elif working_chip:
            self.lbl_hw_status.config(
                text=f"✅ {working_chip['chip_type']} terdeteksi di {working_chip['port']}.",
                foreground="#2ed573",
            )
        self.check_connection_readiness()

    def check_connection_readiness(self):
        """TODO: add documentation"""
        selected_port = self.port_var.get()
        if not selected_port:
            self.btn_connect.grid_forget()
            return
        if self.connection.connected:
            self.btn_connect.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")
            self.btn_connect.config(
                state="normal",
                text="🔌 PUTUSKAN PERANGKAT",
                bg="#ff4757",
                activebackground="#ff6b81",
            )
            return
        self.btn_connect.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")
        self.btn_connect.config(
            state="normal", text="🔌 HUBUNGKAN PERANGKAT", bg="#2ed573", activebackground="#26af5f"
        )

    def trigger_driver_install(self, chip_name):
        """TODO: add documentation"""
        self.btn_install_driver.config(state="disabled", text="⏳ Mengunduh...")
        self.log_message(f"[Driver] Memulai instalasi otomatis {chip_name}...")
        download_and_install_driver(
            chip_name,
            lambda msg: self.log_message(f"[Driver] {msg}"),
            lambda success, msg: (
                self.btn_install_driver.config(
                    state="normal", text=f"⚡ Pasang Driver {chip_name}"
                ),
                (
                    messagebox.showinfo("Sukses", "Installer driver diluncurkan!")
                    if success
                    else messagebox.showerror("Gagal", msg)
                ),
            ),
        )

    def refresh_ports(self):
        """TODO: add documentation"""
        ports = self.connection.get_available_ports()
        self.port_combo["values"] = ports
        if ports:
            self.port_combo.current(0)
        self.check_connection_readiness()

    def toggle_connect(self):
        """TODO: add documentation"""
        if not self.connection.connected:
            port = self.port_var.get()
            baud = int(self.baud_var.get())
            if not port:
                return
            if self.connection.connect(port, baud):
                self.btn_connect.config(
                    text="🔌 PUTUSKAN PERANGKAT", bg="#ff4757", activebackground="#ff6b81"
                )
                self.log_message(f"Connected to {port} at {baud} baud")
                if port != "COM_SIMULATOR":
                    self.connection.send_command("STATUS")
        else:
            self.connection.disconnect()
            self.btn_connect.config(
                text="🔌 HUBUNGKAN PERANGKAT", bg="#2ed573", activebackground="#26af5f"
            )
            self.log_message("Disconnected from serial port")
        self.check_connection_readiness()

    # --- MetaMask Tracker RPC Methods ---
    def trigger_rpc_fetch(self):
        """TODO: add documentation"""
        threading.Thread(target=self.query_rpc_balance, daemon=True).start()

    def update_timer_loop(self):
        """TODO: add documentation"""
        if not self.running:
            return
        app = self.winfo_toplevel()
        is_running = getattr(app, "robot_running", False)
        start_time = getattr(app, "robot_start_time", None)

        if is_running:
            if not self.session_active:
                self.session_active = True
                self.session_start_time = start_time if start_time else time.time()
                with self.lock:
                    self.initial_nxpc = None
                    self.initial_neso = None
                self.trigger_rpc_fetch()
            elapsed = time.time() - self.session_start_time
            hrs, remainder = divmod(int(elapsed), 3600)
            mins, secs = divmod(remainder, 60)
            self.lbl_timer.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
        else:
            self.session_active = False
            self.session_start_time = None
            self.lbl_timer.config(text="00:00:00")
            self.lbl_earn_nxpc.config(text="+0.0000 NXPC")
            self.lbl_earn_neso.config(text="+0 NESO")

        self.update_ui_state_visibility()
        self.after(1000, self.update_timer_loop)

    def query_rpc_balance(self):
        """TODO: add documentation"""
        addr = self.wallet_address.get().strip()
        if not addr:
            return
        clean_addr = addr.lower().replace("0x", "")
        padded_addr = clean_addr.zfill(64)
        call_data = "0x70a08231" + padded_addr
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [
                {"to": "0x07E49Ad54FcD23F6e7B911C2068F0148d1827c08", "data": call_data},
                "latest",
            ],
            "id": 1,
        }
        urls = ["https://henesys-rpc.msu.io", "https://subnets.avax.network/henesys/"]
        success, last_error = False, ""
        for url in urls:
            try:
                data = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    url,
                    data=data,
                    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status == 200:
                        res_data = json.loads(response.read().decode("utf-8"))
                        if "result" in res_data:
                            hex_val = res_data["result"].replace("0x", "") or "0"
                            wei = int(hex_val, 16)
                            neso = wei / (10**18)
                            nxpc = neso / 100000.0
                            with self.lock:
                                self.current_nxpc = nxpc
                                self.current_neso = neso
                                self.rpc_connected = True
                                self.rpc_error = ""
                                if self.session_active and self.initial_nxpc is None:
                                    self.initial_nxpc = nxpc
                                    self.initial_neso = neso
                            success = True
                            break
                        else:
                            last_error = res_data.get("error", {}).get("message", "Error RPC")
                    else:
                        last_error = f"HTTP {response.status}"
            except Exception as e:
                print("Error occurred")
                last_error = str(e)
        if not success:
            with self.lock:
                self.rpc_connected = False
                self.rpc_error = last_error
        self.after(0, self.refresh_balance_labels)

    def refresh_balance_labels(self):
        """TODO: add documentation"""
        with self.lock:
            if self.rpc_connected:
                self.lbl_rpc_status.config(
                    text="● Terhubung ke Henesys Network L1", foreground="#2ed573"
                )
            else:
                self.lbl_rpc_status.config(
                    text=f"● Gangguan Jaringan ({self.rpc_error})", foreground="#ff4757"
                )
            self.lbl_bal_nxpc.config(text=f"{self.current_nxpc:.4f} NXPC")
            self.lbl_bal_neso.config(text=f"{int(self.current_neso):,} NESO")
            if self.session_active and self.initial_nxpc is not None:
                earned_nxpc = max(0.0, self.current_nxpc - self.initial_nxpc)
                earned_neso = max(0, int(self.current_neso - self.initial_neso))
                self.lbl_earn_nxpc.config(text=f"+{earned_nxpc:.4f} NXPC")
                self.lbl_earn_neso.config(text=f"+{earned_neso:,} NESO")
            else:
                self.lbl_earn_nxpc.config(text="+0.0000 NXPC")
                self.lbl_earn_neso.config(text="+0 NESO")

    def rpc_polling_loop(self):
        """TODO: add documentation"""
        while self.running:
            if self.wallet_address.get().strip():
                self.query_rpc_balance()
            for _ in range(100):
                if not self.running:
                    return
                time.sleep(0.1)
