"""TODO: module documentation"""

import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Per-monitor DPI aware
except Exception as e:
    print("Error occurred")
    try:
        ctypes.windll.user32.SetProcessDPIAware()  # Fallback
    except Exception as e:
        print("Error occurred")
        pass

import queue
import time
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from app.connection import SerialConnectionManager
from app.models import RobotProfile
from app.tabs.auto_farm_firmware import AutoFarmFirmwareTab
from app.tabs.dashboard import DashboardTab
from app.tabs.pattern import PatternBuilderTab
from app.tabs.profiles import ProfileManagerTab
from app.tabs.robot_settings import RobotSettingsTab

# ==============================================================================
# CONFIGURASI TRANSPARANSI UI (GLASSMORPHISM)
# ==============================================================================
# Ubah nilai di bawah ini untuk mengatur tingkat transparansi seluruh aplikasi.
# Rentang nilai: 0.0 (transparan penuh) hingga 1.0 (buram total/solid)
OPACITY_HALAMAN_UTAMA = 0.70  # Untuk seluruh halaman/tab utama dan sub-tab
OPACITY_ELEMENT_SIDEBAR = 0.70  # Untuk label dan tombol navigasi di sidebar
# ==============================================================================


class WallpaperManager:
    """TODO: add documentation"""

    def __init__(self):
        """TODO: add documentation"""
        import os

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.wallpaper_path = os.path.join(base_dir, "assets", "wibu_wallpaper.jpg")
        self.original_img = None
        self.cache = {}
        self.registered_widgets = []
        self.load_image()

    def load_image(self):
        """TODO: add documentation"""
        import os

        try:
            if os.path.exists(self.wallpaper_path):
                self.original_img = Image.open(self.wallpaper_path)
            else:
                fallback_path = r"C:\Users\Admin\Pictures\download (1).jpg"
                if os.path.exists(fallback_path):
                    self.original_img = Image.open(fallback_path)
        except Exception as e:
            print(f"[WallpaperManager] Gagal memuat gambar: {e}")

    def register(self, widget, is_sidebar=False):
        """TODO: add documentation"""
        self.registered_widgets.append((widget, is_sidebar))
        widget.bind("<Configure>", lambda e, w=widget: self.on_widget_resize(w))
        # Initial draw delayed slightly to let widget dimensions settle
        widget.after(50, lambda: self.trigger_draw(widget))

    def on_widget_resize(self, widget):
        """TODO: add documentation"""
        if hasattr(widget, "_resize_after_id"):
            widget.after_cancel(widget._resize_after_id)
        widget._resize_after_id = widget.after(150, lambda: self.trigger_draw(widget))

    def trigger_draw(self, widget):
        """TODO: add documentation"""
        if not self.original_img:
            return
        w = widget.winfo_width()
        h = widget.winfo_height()
        if w <= 1 or h <= 1:
            return

        is_sidebar = False
        for reg_widget, sb_flag in self.registered_widgets:
            if reg_widget == widget:
                is_sidebar = sb_flag
                break

        key = (w, h, is_sidebar)
        if key not in self.cache:
            try:
                img_w, img_h = self.original_img.size
                img_ratio = img_w / img_h

                if is_sidebar:
                    # Sidebar uses left-crop cover fit
                    scale_factor = h / img_h
                    new_w = int(img_w * scale_factor)
                    new_h = h
                    resized = self.original_img.resize((new_w, new_h), Image.Resampling.BILINEAR)
                    cropped = resized.crop((0, 0, w, h))
                    # Apply a dark semi-transparent overlay to match the tab theme (#13131c at 80% strength)
                    overlay = Image.new("RGB", cropped.size, "#13131c")
                    cropped = Image.blend(cropped, overlay, alpha=0.80)
                else:
                    # Centered cover fit
                    widget_ratio = w / h
                    if widget_ratio > img_ratio:
                        new_w = w
                        new_h = int(w / img_ratio)
                    else:
                        new_h = h
                        new_w = int(h * img_ratio)

                    resized = self.original_img.resize((new_w, new_h), Image.Resampling.BILINEAR)
                    x_offset = (new_w - w) // 2
                    y_offset = (new_h - h) // 2
                    cropped = resized.crop((x_offset, y_offset, x_offset + w, y_offset + h))

                self.cache[key] = ImageTk.PhotoImage(cropped)
            except Exception as e:
                print(f"[WallpaperManager] Resize error: {e}")
                return

        photo = self.cache[key]
        widget.delete("wallpaper")
        widget.create_image(0, 0, image=photo, anchor="nw", tags="wallpaper")
        widget.image = photo


class ModernApp(tk.Tk):
    """TODO: add documentation"""

    def __init__(self):
        """TODO: add documentation"""
        super().__init__()
        self.title("Logitech G HUB Audio Service")
        # Set a larger default size and start maximized for better visibility
        self.geometry("1400x900")
        self.state("zoomed")  # Open window maximized on Windows

        # Inisialisasi Wallpaper Manager terpusat
        self.wallpaper_manager = WallpaperManager()

        # Configure overall themes and styles
        self.configure(bg="#1a1a24")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Setup modern dark wibu sakura colors
        self.style.configure(
            ".", background="#1a1a24", foreground="#ffffff", fieldbackground="#1a1a24"
        )
        self.style.configure("TLabel", background="#1a1a24", foreground="#ffffff")

        # Style TNotebook and TNotebook.Tab for sakura theme alignment
        self.style.configure("TNotebook", background="#1a1a24", borderwidth=0, highlightthickness=0)
        self.style.configure(
            "TNotebook.Tab",
            background="#13131c",
            foreground="#dec0f1",
            borderwidth=0,
            padding=[12, 6],
            font=("Segoe UI", 9, "bold"),
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", "#ff75a0"), ("active", "#1e1e2d")],
            foreground=[("selected", "#ffffff"), ("active", "#ff75a0")],
        )

        self.style.configure(
            "TLabelframe", background="#1a1a24", foreground="#ffffff", bordercolor="#ff75a0"
        )
        self.style.configure(
            "TLabelframe.Label",
            background="#1a1a24",
            foreground="#ff75a0",
            font=("Helvetica", 10, "bold"),
        )
        self.style.configure(
            "TButton",
            background="#ff75a0",
            foreground="#ffffff",
            borderwidth=0,
            font=("Helvetica", 9, "bold"),
        )
        self.style.map("TButton", background=[("active", "#ff9ff3")])
        self.style.configure("TCheckbutton", background="#1a1a24", foreground="#ffffff")
        self.style.configure("TRadiobutton", background="#1a1a24", foreground="#ffffff")

        # Enhanced inputs & tables visibility configuration
        self.style.configure(
            "TCombobox",
            fieldbackground="#272736",
            background="#ff75a0",
            foreground="#ffffff",
            arrowcolor="#ffffff",
        )
        self.style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#272736")],
            foreground=[("readonly", "#ffffff")],
        )

        self.style.configure(
            "TSpinbox",
            fieldbackground="#272736",
            foreground="#ffffff",
            arrowcolor="#ffffff",
            buttonbackground="#ff75a0",
        )
        self.style.map(
            "TSpinbox",
            fieldbackground=[("readonly", "#272736")],
            foreground=[("readonly", "#ffffff")],
        )

        self.style.configure("TEntry", fieldbackground="#272736", foreground="#ffffff")

        self.style.configure(
            "Treeview", background="#272736", fieldbackground="#272736", foreground="#ffffff"
        )
        self.style.configure(
            "Treeview.Heading",
            background="#1a1a24",
            foreground="#ff75a0",
            font=("Helvetica", 10, "bold"),
        )

        # Models and Communication Shared Instances
        self.profile = RobotProfile()
        self.robot_running = False
        self.robot_start_time = None
        self.log_queue = queue.Queue()
        self.connection = SerialConnectionManager(
            log_callback=self.connection_logger, status_callback=self.connection_status_handler
        )

        # Build Side Navigation Panel (Wibu style dark purple/indigo)
        self.sidebar = tk.Frame(self, bg="#13131c", width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Wallpaper Background for Sidebar
        self.sidebar_bg = tk.Canvas(self.sidebar, highlightthickness=0, bg="#13131c")
        self.sidebar_bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.wallpaper_manager.register(self.sidebar_bg, is_sidebar=True)

        # Title / Branding
        lbl_brand = tk.Label(
            self.sidebar,
            text="🌸 KBD ROBOT LITE",
            font=("Helvetica", 15, "bold"),
            bg="#13131c",
            fg="#ff75a0",
        )
        lbl_brand.pack(pady=20, padx=10, anchor="w")

        lbl_sub = tk.Label(
            self.sidebar,
            text="Studio Kontroler Sakura v1.2.0",
            font=("Helvetica", 8),
            bg="#13131c",
            fg="#dec0f1",
        )
        lbl_sub.pack(pady=(0, 20), padx=15, anchor="w")

        # Container for main pages
        self.container = tk.Frame(self, bg="#1a1a24", padx=10, pady=10)
        self.container.pack(side="right", fill="both", expand=True)

        # Wallpaper Background for Container
        self.container_bg = tk.Canvas(self.container, highlightthickness=0, bg="#1a1a24")
        self.container_bg.place(x=0, y=0, relwidth=1, relheight=1)
        self.wallpaper_manager.register(self.container_bg, is_sidebar=False)

        self.pages = {}
        self.nav_buttons = {}

        # Dictionary describing Tab mappings categorized
        self.categories = [
            (
                "📊 MONITORING",
                [
                    ("Dashboard Utama", DashboardTab, "📊"),
                ],
            ),
            (
                "🧱 MAKRO",
                [
                    ("Pembuat Makro", PatternBuilderTab, "🧱"),
                ],
            ),
            (
                "🔧 PENGATURAN",
                [
                    ("Konfigurasi Robot", RobotSettingsTab, "🔧"),
                ],
            ),
            (
                "🤖 OTOMATISASI",
                [
                    ("Fitur Auto & Jaringan", AutoFarmFirmwareTab, "🤖"),
                ],
            ),
            (
                "📁 PROFIL",
                [
                    ("Manajer Profil", ProfileManagerTab, "📁"),
                ],
            ),
        ]

        # Instantiation
        for cat_name, tabs in self.categories:
            # Elegant category section header
            lbl_cat = tk.Label(
                self.sidebar,
                text=f"  {cat_name}",
                font=("Helvetica", 8, "bold"),
                bg="#13131c",
                fg="#ff75a0",
                anchor="w",
            )
            lbl_cat.pack(fill="x", padx=10, pady=(12, 2))

            for name, cls, icon in tabs:
                # Inject appropriate constructor signatures
                if cls == DashboardTab:
                    frame = cls(self.container, self.profile, self.connection, self.log_queue)
                elif cls == AutoFarmFirmwareTab or cls == ProfileManagerTab:
                    frame = cls(self.container, self.profile, self.connection, self.reload_all_tabs)
                else:
                    frame = cls(self.container, self.profile, self.connection)

                # Inject a universal reload callback
                frame.on_profile_updated = self.reload_all_tabs

                # Apply semi-transparency using pywinstyles for Sakura glassmorphism look
                try:
                    import pywinstyles

                    pywinstyles.set_opacity(frame, value=OPACITY_HALAMAN_UTAMA)
                except Exception as e:
                    print(f"[ModernApp] Gagal menyetel transparansi halaman {name}: {e}")

                self.pages[name] = frame

                # Nav button on sidebar with aligned icon and clean Segoe UI font
                btn = tk.Button(
                    self.sidebar,
                    text=f" {icon}   {name}",
                    anchor="w",
                    font=("Segoe UI", 9, "bold"),
                    bg="#13131c",
                    fg="#dec0f1",
                    activebackground="#1a1a24",
                    activeforeground="#ff75a0",
                    relief="flat",
                    bd=0,
                    height=2,
                    command=lambda n=name: self.show_page(n),
                )
                btn.pack(fill="x", padx=10, pady=1)

                # Hover bindings
                btn.bind("<Enter>", lambda e, b=btn: self.on_nav_enter(b))
                btn.bind("<Leave>", lambda e, b=btn: self.on_nav_leave(b))

                self.nav_buttons[name] = btn

        # Footer connection label on sidebar
        self.lbl_conn_status = tk.Label(
            self.sidebar,
            text="● Terputus",
            font=("Helvetica", 9, "bold"),
            bg="#13131c",
            fg="#ff4757",
            anchor="w",
        )
        self.lbl_conn_status.pack(side="bottom", fill="x", padx=15, pady=20)

        # Apply semi-transparency using pywinstyles to sidebar labels and buttons to expose wallpaper
        try:
            import pywinstyles

            for child in self.sidebar.winfo_children():
                if isinstance(child, (tk.Label, tk.Button)) and child != self.sidebar_bg:
                    pywinstyles.set_opacity(child, value=OPACITY_ELEMENT_SIDEBAR)
        except Exception as e:
            print(f"[ModernApp] Gagal menyetel transparansi widget sidebar: {e}")

        # Show Dashboard initially
        self.show_page("Dashboard Utama")

    def show_page(self, name):
        """TODO: add documentation"""
        # Hide all frames
        for frame in self.pages.values():
            frame.pack_forget()

        # Show targeted frame
        self.pages[name].pack(fill="both", expand=True)

        # Update navigation highlights
        for k, btn in self.nav_buttons.items():
            if k == name:
                btn.config(bg="#ff75a0", fg="#ffffff")
            else:
                btn.config(bg="#13131c", fg="#dec0f1")

        # Specific tab reloads if necessary
        if hasattr(self.pages[name], "reload_table"):
            self.pages[name].reload_table()

    def on_nav_enter(self, btn):
        """TODO: add documentation"""
        if btn["bg"] != "#ff75a0":
            btn.config(bg="#1a1a24", fg="#ff75a0")

    def on_nav_leave(self, btn):
        """TODO: add documentation"""
        if btn["bg"] != "#ff75a0":
            btn.config(bg="#13131c", fg="#dec0f1")

    def reload_all_tabs(self):
        """TODO: add documentation"""
        # Sync tab UI states with current RobotProfile data after updates/loads
        for name, frame in self.pages.items():
            if hasattr(frame, "reload_from_profile"):
                frame.reload_from_profile()
            elif hasattr(frame, "reload_table"):
                frame.reload_table()

    def connection_logger(self, msg):
        """TODO: add documentation"""
        self.log_queue.put(msg)

    def connection_status_handler(self, status):
        """TODO: add documentation"""
        # Update dashboard state and sidebar label in Indonesian
        if hasattr(self, "lbl_conn_status"):
            # Handle STEP progress messages
            if status.startswith("STEP:"):
                try:
                    step_info = status[5:]  # "3/10"
                    current, total = step_info.split("/")
                    self.lbl_conn_status.config(text=f"⚡ Langkah {current}/{total}", fg="#dec0f1")
                except (ValueError, IndexError):
                    pass
            elif "Disconnected" in status:
                indonesian_status = "Terputus"
                self.lbl_conn_status.config(text=f"● {indonesian_status}", fg="#ff4757")
            elif "Connected (Simulated)" in status or "Connected" in status:
                indonesian_status = (
                    "Terhubung"
                    if "Connected" in status and "Simulated" not in status
                    else "Terhubung (Simulasi)"
                )
                self.lbl_conn_status.config(text=f"● {indonesian_status}", fg="#2ed573")
            elif "Active" in status:
                indonesian_status = status.replace("Active:", "Aktif:")
                self.lbl_conn_status.config(text=f"● {indonesian_status}", fg="#dec0f1")

        # Track robot running state for time and earnings tracker
        if "RUNNING" in status or status.startswith("STEP:"):
            if not self.robot_running:
                self.robot_running = True
                self.robot_start_time = time.time()
        elif any(x in status for x in ["STOPPED", "IDLE", "EMERGENCY", "Disconnected"]):
            self.robot_running = False
            self.robot_start_time = None

        if "Dashboard Utama" in self.pages:
            self.pages["Dashboard Utama"].update_status_label(status)

    def on_connection_state_changed(self, connected):
        """TODO: add documentation"""
        # Trigger full refresh
        pass


if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()
