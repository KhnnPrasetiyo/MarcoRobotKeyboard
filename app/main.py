import tkinter as tk
from tkinter import ttk
import queue

from app.models import RobotProfile
from app.connection import SerialConnectionManager

from app.tabs.dashboard import DashboardTab
from app.tabs.calibration import CalibrationTab
from app.tabs.pattern import PatternBuilderTab
from app.tabs.loop_settings import LoopSettingsTab
from app.tabs.random_delay_settings import RandomDelaySettingsTab
from app.tabs.simulation import SimulationTab
from app.tabs.validator import ValidatorTab
from app.tabs.tester import KeyboardTesterTab
from app.tabs.profiles import ProfileManagerTab
from app.tabs.serial_manager import SerialManagerTab

class ModernApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Studio Kontroler Robot Keyboard Arduino Nano")
        self.geometry("1100x700")
        
        # Configure overall themes and styles
        self.configure(bg="#2f3542")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Setup modern dark colors
        self.style.configure(".", background="#2f3542", foreground="#ffffff", fieldbackground="#2f3542")
        self.style.configure("TLabel", background="#2f3542", foreground="#ffffff")
        self.style.configure("TLabelframe", background="#2f3542", foreground="#ffffff", bordercolor="#57606f")
        self.style.configure("TLabelframe.Label", background="#2f3542", foreground="#ffa502", font=("Helvetica", 10, "bold"))
        self.style.configure("TButton", background="#3867d6", foreground="#ffffff", borderwidth=0, font=("Helvetica", 9, "bold"))
        self.style.map("TButton", background=[("active", "#4b7bec")])
        self.style.configure("TCheckbutton", background="#2f3542", foreground="#ffffff")
        self.style.configure("TRadiobutton", background="#2f3542", foreground="#ffffff")
        
        # Enhanced inputs & tables visibility configuration
        self.style.configure("TCombobox", fieldbackground="#1e272e", background="#3867d6", foreground="#ffffff", arrowcolor="#ffffff")
        self.style.map("TCombobox", fieldbackground=[("readonly", "#1e272e")], foreground=[("readonly", "#ffffff")])
        
        self.style.configure("TSpinbox", fieldbackground="#1e272e", foreground="#ffffff", arrowcolor="#ffffff", buttonbackground="#3867d6")
        self.style.map("TSpinbox", fieldbackground=[("readonly", "#1e272e")], foreground=[("readonly", "#ffffff")])
        
        self.style.configure("TEntry", fieldbackground="#1e272e", foreground="#ffffff")
        
        self.style.configure("Treeview", background="#1e272e", fieldbackground="#1e272e", foreground="#ffffff")
        self.style.configure("Treeview.Heading", background="#2f3542", foreground="#ffffff", font=("Helvetica", 10, "bold"))
        
        # Models and Communication Shared Instances
        self.profile = RobotProfile()
        self.log_queue = queue.Queue()
        self.connection = SerialConnectionManager(
            log_callback=self.connection_logger,
            status_callback=self.connection_status_handler
        )
        
        # Start background HTTP server for mobile remote control Wi-Fi bridge
        import threading
        self.http_thread = threading.Thread(target=self.start_http_bridge, daemon=True)
        self.http_thread.start()
        
        # Build Side Navigation Panel
        self.sidebar = tk.Frame(self, bg="#1e272e", width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Title / Branding
        lbl_brand = tk.Label(self.sidebar, text="🤖 KBD ROBOT", font=("Helvetica", 16, "bold"), bg="#1e272e", fg="#ffa502")
        lbl_brand.pack(pady=20, padx=10, anchor="w")
        
        lbl_sub = tk.Label(self.sidebar, text="Studio Kontroler Arduino", font=("Helvetica", 8), bg="#1e272e", fg="#747d8c")
        lbl_sub.pack(pady=(0, 20), padx=15, anchor="w")

        # Container for main pages
        self.container = tk.Frame(self, bg="#2f3542", padx=10, pady=10)
        self.container.pack(side="right", fill="both", expand=True)

        self.pages = {}
        self.nav_buttons = {}

        # Dictionary describing Tab mappings
        self.tab_info = [
            ("Dashboard", DashboardTab),
            ("Kalibrasi Servo", CalibrationTab),
            ("Pembuat Pola", PatternBuilderTab),
            ("Pengaturan Loop", LoopSettingsTab),
            ("Jeda Aksi Acak", RandomDelaySettingsTab),
            ("Simulasi Robot", SimulationTab),
            ("Validasi & Safety", ValidatorTab),
            ("Penguji Tombol", KeyboardTesterTab),
            ("Manajer Profil", ProfileManagerTab),
            ("Koneksi Serial", SerialManagerTab)
        ]

        # Instantiation
        for name, cls in self.tab_info:
            # Inject appropriate constructor signatures
            if cls == DashboardTab:
                frame = cls(self.container, self.profile, self.connection, self.log_queue)
            elif cls == ProfileManagerTab:
                frame = cls(self.container, self.profile, self.connection, self.reload_all_tabs)
            elif cls == SerialManagerTab:
                frame = cls(self.container, self.profile, self.connection, self.on_connection_state_changed)
                frame.set_reload_callback(self.reload_all_tabs)
            else:
                frame = cls(self.container, self.profile, self.connection)
            
            self.pages[name] = frame
            
            # Nav button on sidebar
            btn = tk.Button(self.sidebar, text=f"  {name}", anchor="w", font=("Helvetica", 10),
                            bg="#1e272e", fg="#a4b0be", activebackground="#2f3542", activeforeground="#ffffff",
                            relief="flat", bd=0, height=2, command=lambda n=name: self.show_page(n))
            btn.pack(fill="x", padx=10, pady=2)
            self.nav_buttons[name] = btn

        # Footer connection label on sidebar
        self.lbl_conn_status = tk.Label(self.sidebar, text="● Terputus", font=("Helvetica", 9, "bold"),
                                        bg="#1e272e", fg="#ff4757", anchor="w")
        self.lbl_conn_status.pack(side="bottom", fill="x", padx=15, pady=20)

        # Show Dashboard initially
        self.show_page("Dashboard")

    def show_page(self, name):
        # Hide all frames
        for frame in self.pages.values():
            frame.pack_forget()

        # Show targeted frame
        self.pages[name].pack(fill="both", expand=True)

        # Update navigation highlights
        for k, btn in self.nav_buttons.items():
            if k == name:
                btn.config(bg="#3867d6", fg="#ffffff")
            else:
                btn.config(bg="#1e272e", fg="#a4b0be")

        # Specific tab reloads if necessary
        if hasattr(self.pages[name], "reload_table"):
            self.pages[name].reload_table()

    def reload_all_tabs(self):
        # Sync tab UI states with current RobotProfile data after updates/loads
        for name, frame in self.pages.items():
            if hasattr(frame, "reload_from_profile"):
                frame.reload_from_profile()
            elif hasattr(frame, "reload_table"):
                frame.reload_table()

    def connection_logger(self, msg):
        self.log_queue.put(msg)

    def connection_status_handler(self, status):
        # Update dashboard state and sidebar label in Indonesian
        if hasattr(self, "lbl_conn_status"):
            # Handle STEP progress messages
            if status.startswith("STEP:"):
                try:
                    step_info = status[5:]  # "3/10"
                    current, total = step_info.split("/")
                    self.lbl_conn_status.config(text=f"⚡ Langkah {current}/{total}", fg="#ffa502")
                except (ValueError, IndexError):
                    pass
            elif "Disconnected" in status:
                indonesian_status = "Terputus"
                self.lbl_conn_status.config(text=f"● {indonesian_status}", fg="#ff4757")
            elif "Connected (Simulated)" in status or "Connected" in status:
                indonesian_status = "Terhubung" if "Connected" in status and "Simulated" not in status else "Terhubung (Simulasi)"
                self.lbl_conn_status.config(text=f"● {indonesian_status}", fg="#2ed573")
            elif "Active" in status:
                indonesian_status = status.replace("Active:", "Aktif:")
                self.lbl_conn_status.config(text=f"● {indonesian_status}", fg="#ffa502")

        if "Dashboard" in self.pages:
            self.pages["Dashboard"].update_status_label(status)

    def on_connection_state_changed(self, connected):
        # Trigger full refresh
        pass

    def start_http_bridge(self):
        import http.server
        import socketserver
        import urllib.parse
        import json
        import os
        
        class BridgeHandler(http.server.SimpleHTTPRequestHandler):
            connection_manager = self.connection
            
            def do_GET(self):
                parsed_url = urllib.parse.urlparse(self.path)
                
                # API Endpoint for commands
                if parsed_url.path == "/api/command":
                    query = urllib.parse.parse_qs(parsed_url.query)
                    cmd = query.get("cmd", [None])[0]
                    if cmd:
                        # Forward command directly to active serial connection
                        if self.connection_manager.connected:
                            self.connection_manager.send_command(cmd)
                            status = "ok"
                        else:
                            self.connection_manager.log(f"[Wi-Fi Bridge] Menerima perintah: {cmd}")
                            status = "ok"
                        
                        self.send_response(200)
                        self.send_header("Content-Type", "application/json")
                        self.send_header("Access-Control-Allow-Origin", "*")
                        self.end_headers()
                        self.wfile.write(json.dumps({"status": status}).encode("utf-8"))
                    else:
                        self.send_response(400)
                        self.end_headers()
                    return
                
                # Serve standard files from the 'mobile' directory
                return super().do_GET()
                
            def translate_path(self, path):
                # Translate path to the local mobile directory
                parsed_url = urllib.parse.urlparse(path)
                path_str = parsed_url.path
                if path_str == "/" or path_str == "":
                    path_str = "/index.html"
                
                # Strip leading slash
                if path_str.startswith("/"):
                    path_str = path_str[1:]
                    
                local_path = os.path.join(os.getcwd(), "mobile", path_str)
                return local_path
                
        # Run Server on all interfaces (0.0.0.0) at port 8000
        server_address = ('0.0.0.0', 8000)
        try:
            if hasattr(http.server, "ThreadingHTTPServer"):
                httpd = http.server.ThreadingHTTPServer(server_address, BridgeHandler)
            else:
                class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
                    pass
                httpd = ThreadedHTTPServer(server_address, BridgeHandler)
                
            self.connection.log("Wi-Fi Remote Bridge Server aktif di port 8000.")
            httpd.serve_forever()
        except Exception as e:
            self.connection.log(f"Gagal memulai Bridge Server: {str(e)}")

if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()
