"""TODO: module documentation"""

import tkinter as tk
from tkinter import ttk

import pywinstyles
from PIL import Image, ImageGrab


class TestApp(tk.Tk):
    """TODO: add documentation"""

    def __init__(self):
        """TODO: add documentation"""
        super().__init__()
        self.geometry("800x600+100+100")
        self.title("Color Key Theme Test")

        # Style setup
        self.style = ttk.Style()
        self.style.theme_use("clam")

        trans_color = "#123456"  # Color key for transparency
        card_color = "#1a1a24"  # Solid card background

        self.style.configure(".", background=trans_color, foreground="#ffffff")
        self.style.configure("TLabel", background=trans_color, foreground="#ffffff")
        self.style.configure("TNotebook", background=trans_color, borderwidth=0)
        self.style.configure(
            "TNotebook.Tab", background="#13131c", foreground="#dec0f1", borderwidth=0
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", "#ff75a0")],
            foreground=[("selected", "#ffffff")],
        )

        # Configure LabelFrame to have solid card background
        self.style.configure(
            "TLabelframe", background=card_color, foreground="#ffffff", bordercolor="#ff75a0"
        )
        self.style.configure(
            "TLabelframe.Label",
            background=card_color,
            foreground="#ff75a0",
            font=("Helvetica", 10, "bold"),
        )

        # Canvas background (representing wallpaper)
        self.canvas = tk.Canvas(self, bg="#0d0d13", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.create_rectangle(50, 50, 750, 550, fill="#2b1a30", outline="#ff75a0", width=3)
        self.canvas.create_oval(100, 200, 300, 400, fill="#ff75a0")

        # Page container (ttk.Frame)
        self.page = ttk.Frame(self)
        self.page.place(x=100, y=100, width=600, height=450)

        # Notebook inside page
        self.notebook = ttk.Notebook(self.page)
        self.notebook.pack(fill="both", expand=True)

        # Tab 1
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text=" Tab 1: Calibration ")

        # Label inside Tab 1 (should have transparent background)
        self.lbl = ttk.Label(
            self.tab1, text="🌸 Calibration Settings (Transparent BG)", font=("Arial", 12, "bold")
        )
        self.lbl.pack(pady=10, anchor="w", padx=20)

        # LabelFrame card inside Tab 1 (should be solid card)
        self.lf = ttk.LabelFrame(self.tab1, text=" Servo 1 Control ", padding=15)
        self.lf.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(self.lf, text="Servo Angle:", fg="#ffffff", bg=card_color).pack(anchor="w", pady=5)
        self.scale = ttk.Scale(self.lf, from_=0, to=180)
        self.scale.pack(fill="x", pady=5)

        self.btn = tk.Button(
            self.lf, text="SAVE SETTINGS", bg="#2ed573", fg="white", bd=0, padx=10, pady=5
        )
        self.btn.pack(pady=10)

        # Apply color key transparency to the page frame
        pywinstyles.set_opacity(self.page, color=trans_color)

        self.after(1000, self.take_screenshot)

    def take_screenshot(self):
        """TODO: add documentation"""
        self.update()
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        w = self.winfo_width()
        h = self.winfo_height()
        bbox = (x, y, x + w, y + h)
        img = ImageGrab.grab(bbox=bbox)

        import os

        artifact_dir = (
            r"C:\Users\Admin\.gemini\antigravity-ide\brain\bbcdabdf-8378-4f22-8033-d634387fa05a"
        )
        save_path = os.path.join(artifact_dir, "colorkey_theme_result.png")
        img.save(save_path)
        print(f"Screenshot saved to: {save_path}")
        self.destroy()


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
