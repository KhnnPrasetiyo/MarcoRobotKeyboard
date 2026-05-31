import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import json
import time
import threading
import urllib.request

class NesoTrackerTab(ttk.Frame):
    def __init__(self, parent, profile, connection):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection

        self.wallet_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "wallet_settings.json")
        self.wallet_address = tk.StringVar(value=self.load_wallet_address())

        # Session tracking state variables
        self.session_active = False
        self.session_start_time = None
        
        # Crypto balance variables
        self.current_nxpc = 0.0
        self.current_neso = 0.0
        self.initial_nxpc = None
        self.initial_neso = None
        
        self.rpc_connected = False
        self.rpc_error = ""

        # UI grid layout configuration
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Build UI Cards
        self.create_left_card()
        self.create_right_card()

        # Start background polling threads
        self.running = True
        self.lock = threading.Lock()
        
        # Start time tracking update loop
        self.update_timer_loop()
        
        # Start background thread to poll Metamask Henesys RPC
        self.poll_thread = threading.Thread(target=self.rpc_polling_loop, daemon=True)
        self.poll_thread.start()

    def destroy(self):
        self.running = False
        super().destroy()

    def load_wallet_address(self):
        if os.path.exists(self.wallet_file):
            try:
                with open(self.wallet_file, "r") as f:
                    data = json.load(f)
                    return data.get("wallet_address", "")
            except Exception:
                pass
        return ""

    def save_wallet_address(self):
        addr = self.wallet_address.get().strip()
        if addr and (not addr.startswith("0x") or len(addr) != 42):
            messagebox.showerror("Error", "Alamat wallet MetaMask tidak valid!\nAlamat harus diawali dengan '0x' dan memiliki panjang 42 karakter.")
            return

        try:
            with open(self.wallet_file, "w") as f:
                json.dump({"wallet_address": addr}, f, indent=4)
            self.connection.log(f"Alamat wallet disimpan: {addr[:6]}...{addr[-4:]}" if addr else "Alamat wallet dihapus.")
            messagebox.showinfo("Berhasil", "Alamat wallet berhasil disimpan!")
            # Reset balance state on change
            with self.lock:
                self.initial_nxpc = None
                self.initial_neso = None
            self.trigger_rpc_fetch()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan wallet: {str(e)}")

    def delete_wallet_address(self):
        self.wallet_address.set("")
        self.save_wallet_address()

    def create_left_card(self):
        # Configuration and Wallet Card Panel
        left_frame = ttk.Frame(self, padding=15)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        left_frame.columnconfigure(0, weight=1)

        card = ttk.LabelFrame(left_frame, text=" 🦊 Konfigurasi MetaMask Wallet ", padding=20)
        card.grid(row=0, column=0, sticky="nsew")
        card.columnconfigure(0, weight=1)

        desc = ttk.Label(card, text="Integrasi Blockchain Henesys (MapleStory Universe).\nMasukkan alamat dompet MetaMask Anda di bawah untuk melacak saldo\ndan akumulasi pendapatan NESO Anda secara real-time.", 
                         font=("Helvetica", 10), justify="center")
        desc.pack(pady=(0, 20))

        # Input box and buttons
        entry_frame = ttk.Frame(card)
        entry_frame.pack(fill="x", pady=10)
        
        ttk.Label(entry_frame, text="Alamat Wallet MetaMask (EVM 0x):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        
        self.entry_wallet = ttk.Entry(entry_frame, textvariable=self.wallet_address, font=("Consolas", 10))
        self.entry_wallet.pack(fill="x", ipady=6)

        # Action buttons
        btn_frame = ttk.Frame(card)
        btn_frame.pack(fill="x", pady=15)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        self.btn_save = tk.Button(btn_frame, text="💾 SIMPAN ALAMAT", bg="#3867d6", fg="white",
                                  activebackground="#4b7bec", activeforeground="white", font=("Helvetica", 10, "bold"),
                                  relief="flat", bd=0, height=2, cursor="hand2", command=self.save_wallet_address)
        self.btn_save.grid(row=0, column=0, padx=5, sticky="ew")
        self.btn_save.bind("<Enter>", lambda e: self.btn_save.config(bg="#4b7bec"))
        self.btn_save.bind("<Leave>", lambda e: self.btn_save.config(bg="#3867d6"))

        self.btn_delete = tk.Button(btn_frame, text="🗑️ HAPUS ALAMAT", bg="#ff4757", fg="white",
                                    activebackground="#ff6b81", activeforeground="white", font=("Helvetica", 10, "bold"),
                                    relief="flat", bd=0, height=2, cursor="hand2", command=self.delete_wallet_address)
        self.btn_delete.grid(row=0, column=1, padx=5, sticky="ew")
        self.btn_delete.bind("<Enter>", lambda e: self.btn_delete.config(bg="#ff6b81"))
        self.btn_delete.bind("<Leave>", lambda e: self.btn_delete.config(bg="#ff4757"))

        # Blockchain status frame
        status_frame = ttk.LabelFrame(card, text=" Hub Jaringan Henesys L1 ", padding=12)
        status_frame.pack(fill="x", pady=15)

        self.lbl_rpc_status = ttk.Label(status_frame, text="● Memeriksa Koneksi Jaringan...", font=("Helvetica", 10, "bold"), foreground="#ffa502")
        self.lbl_rpc_status.pack(anchor="w")

        self.lbl_rpc_details = ttk.Label(status_frame, text="RPC: https://subnets.avax.network/henesys\nRate: 100.000 NESO = 1 NXPC", font=("Consolas", 8), foreground="#a4b0be")
        self.lbl_rpc_details.pack(anchor="w", pady=(5, 0))

    def create_right_card(self):
        # Monitoring and Session Earnings Card Panel
        right_frame = ttk.Frame(self, padding=15)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        right_frame.columnconfigure(0, weight=1)

        card = ttk.LabelFrame(right_frame, text=" ⏳ Pemantauan Sesi Aktif Robot ", padding=20)
        card.grid(row=0, column=0, sticky="nsew")
        card.columnconfigure(0, weight=1)

        # 1. State status
        self.lbl_session_status = ttk.Label(card, text="🔴 ROBOT BERHENTI", font=("Helvetica", 12, "bold"), foreground="#ff4757")
        self.lbl_session_status.pack(anchor="center", pady=(5, 10))

        # 2. Digital Timer Card
        timer_frame = tk.Frame(card, bg="#1e272e", bd=2, relief="groove")
        timer_frame.pack(fill="x", pady=10, ipady=15)
        
        ttk.Label(timer_frame, text="DURASI ROBOT BERJALAN", font=("Helvetica", 8, "bold"), background="#1e272e", foreground="#747d8c").pack(pady=(5, 0))
        
        self.lbl_timer = ttk.Label(timer_frame, text="00:00:00", font=("Consolas", 28, "bold"), background="#1e272e", foreground="#2ed573")
        self.lbl_timer.pack(pady=5)

        # 3. Balance & Earnings Panel
        self.earn_frame = ttk.LabelFrame(card, text=" 📈 Akumulasi Hasil & Saldo MetaMask ", padding=15)
        self.earn_frame.pack(fill="both", expand=True, pady=15)
        self.earn_frame.columnconfigure(0, weight=1)
        self.earn_frame.columnconfigure(1, weight=1)

        # Labels for Balances
        ttk.Label(self.earn_frame, text="SALDO METAMASK", font=("Helvetica", 9, "bold"), foreground="#ffa502").grid(row=0, column=0, sticky="w", pady=(0, 5))
        ttk.Label(self.earn_frame, text="PEROLEHAN SESI INI", font=("Helvetica", 9, "bold"), foreground="#ffa502").grid(row=0, column=1, sticky="w", pady=(0, 5))

        # Total Wallet Balance
        self.lbl_bal_nxpc = ttk.Label(self.earn_frame, text="0.0000 NXPC", font=("Consolas", 12, "bold"))
        self.lbl_bal_nxpc.grid(row=1, column=0, sticky="w", pady=2)
        
        self.lbl_bal_neso = ttk.Label(self.earn_frame, text="0 NESO", font=("Consolas", 10), foreground="#a4b0be")
        self.lbl_bal_neso.grid(row=2, column=0, sticky="w", pady=2)

        # Earned in current run session
        self.lbl_earn_nxpc = ttk.Label(self.earn_frame, text="+0.0000 NXPC", font=("Consolas", 12, "bold"), foreground="#2ed573")
        self.lbl_earn_nxpc.grid(row=1, column=1, sticky="w", pady=2)
        
        self.lbl_earn_neso = ttk.Label(self.earn_frame, text="+0 NESO", font=("Consolas", 10), foreground="#2ed573")
        self.lbl_earn_neso.grid(row=2, column=1, sticky="w", pady=2)

        # Placeholder message when wallet address is empty
        self.lbl_no_wallet = ttk.Label(card, text="⚠️ Konfigurasi alamat wallet MetaMask di sebelah kiri\nuntuk mengaktifkan pelacak pendapatan NESO otomatis.",
                                       font=("Helvetica", 9, "bold"), foreground="#ffa502", justify="center")
        self.lbl_no_wallet.pack(pady=10)

        # Update initial visual visibility
        self.update_ui_state_visibility()

    def update_ui_state_visibility(self):
        addr = self.wallet_address.get().strip()
        if addr:
            self.lbl_no_wallet.pack_forget()
            self.earn_frame.pack(fill="both", expand=True, pady=15)
        else:
            self.earn_frame.pack_forget()
            self.lbl_no_wallet.pack(pady=10)

    def trigger_rpc_fetch(self):
        # Quick fetch trigger
        threading.Thread(target=self.query_rpc_balance, daemon=True).start()

    def update_timer_loop(self):
        if not self.running:
            return

        # Fetch parent/ModernApp state properties dynamically
        app = self.winfo_toplevel()
        is_running = False
        start_time = None
        
        if hasattr(app, "robot_running"):
            is_running = app.robot_running
            start_time = getattr(app, "robot_start_time", None)
        else:
            # Fallback based on connection status info
            if self.connection.connected:
                # Check status text
                if "Active: RUNNING" in self.connection.port or "Active: RUNNING" in self.lbl_session_status.cget("text"):
                    is_running = True

        # Handle Running Session state change
        if is_running:
            if not self.session_active:
                self.session_active = True
                self.session_start_time = start_time if start_time else time.time()
                # Clear initial balance so it captures the new run's starting point
                with self.lock:
                    self.initial_nxpc = None
                    self.initial_neso = None
                self.trigger_rpc_fetch()
                
            elapsed = time.time() - self.session_start_time
            hrs, remainder = divmod(int(elapsed), 3600)
            mins, secs = divmod(remainder, 60)
            self.lbl_timer.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
            self.lbl_session_status.config(text="🟢 ROBOT BERJALAN", foreground="#2ed573")
        else:
            self.session_active = False
            self.session_start_time = None
            self.lbl_timer.config(text="00:00:00")
            self.lbl_session_status.config(text="🔴 ROBOT BERHENTI", foreground="#ff4757")
            # If stopped, session earned is zero
            self.lbl_earn_nxpc.config(text="+0.0000 NXPC")
            self.lbl_earn_neso.config(text="+0 NESO")

        # Automatically adjust UI widgets visibility based on current configuration
        self.update_ui_state_visibility()
        self.after(1000, self.update_timer_loop)

    def query_rpc_balance(self):
        addr = self.wallet_address.get().strip()
        if not addr:
            return

        # Prepare ERC-20 balanceOf(address) call data
        clean_addr = addr.lower().replace("0x", "")
        padded_addr = clean_addr.zfill(64)
        call_data = "0x70a08231" + padded_addr

        payload = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [
                {
                    "to": "0x07E49Ad54FcD23F6e7B911C2068F0148d1827c08",  # NESO Token Contract
                    "data": call_data
                },
                "latest"
            ],
            "id": 1
        }
        
        urls = ["https://henesys-rpc.msu.io", "https://subnets.avax.network/henesys/"]
        success = False
        last_error = ""

        for url in urls:
            try:
                data = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    url,
                    data=data,
                    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
                    method="POST"
                )
                
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status == 200:
                        res_bytes = response.read()
                        res_data = json.loads(res_bytes.decode("utf-8"))
                        if "result" in res_data:
                            hex_val = res_data["result"]
                            if hex_val.startswith("0x"):
                                hex_val = hex_val[2:]
                            if not hex_val:
                                hex_val = "0"
                            wei = int(hex_val, 16)
                            
                            # NESO has 18 decimals
                            neso = wei / (10**18)
                            nxpc = neso / 100000.0
                            
                            with self.lock:
                                self.current_nxpc = nxpc
                                self.current_neso = neso
                                self.rpc_connected = True
                                self.rpc_error = ""
                                
                                # Set initial starting point balance for this active running session
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
                last_error = str(e)
        
        if not success:
            with self.lock:
                self.rpc_connected = False
                self.rpc_error = last_error

        # Update visual elements in main thread safely
        self.after(0, self.refresh_balance_labels)

    def refresh_balance_labels(self):
        with self.lock:
            # Update network connection UI status indicators
            if self.rpc_connected:
                self.lbl_rpc_status.config(text="● Terhubung ke Henesys Network", foreground="#2ed573")
            else:
                err = f" ({self.rpc_error})" if self.rpc_error else ""
                self.lbl_rpc_status.config(text=f"● Gangguan Koneksi Jaringan{err}", foreground="#ff4757")

            # Update Balances
            self.lbl_bal_nxpc.config(text=f"{self.current_nxpc:.4f} NXPC")
            self.lbl_bal_neso.config(text=f"{int(self.current_neso):,} NESO")

            # Update Session Earnings
            if self.session_active and self.initial_nxpc is not None:
                earned_nxpc = self.current_nxpc - self.initial_nxpc
                earned_neso = self.current_neso - self.initial_neso
                
                # Protect against slight balance updates / negative values
                earned_nxpc = max(0.0, earned_nxpc)
                earned_neso = max(0, int(earned_neso))
                
                self.lbl_earn_nxpc.config(text=f"+{earned_nxpc:.4f} NXPC", foreground="#2ed573")
                self.lbl_earn_neso.config(text=f"+{earned_neso:,} NESO", foreground="#2ed573")
            else:
                self.lbl_earn_nxpc.config(text="+0.0000 NXPC", foreground="#2ed573")
                self.lbl_earn_neso.config(text="+0 NESO", foreground="#2ed573")

    def rpc_polling_loop(self):
        while self.running:
            addr = self.wallet_address.get().strip()
            if addr:
                self.query_rpc_balance()
            
            # Sleep 10 seconds before next check
            for _ in range(100):
                if not self.running:
                    return
                time.sleep(0.1)

    def reload_from_profile(self):
        # Profile reload compatibility callback
        pass
