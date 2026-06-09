"""TODO: module documentation"""

import time
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
        self.title("Opacity Notebook Test")

        # Style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(".", background="#1a1a24", foreground="#ffffff")
        self.style.configure("TNotebook", background="#1a1a24", borderwidth=0)
        self.style.configure(
            "TNotebook.Tab", background="#13131c", foreground="#dec0f1", borderwidth=0
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", "#ff75a0")],
            foreground=[("selected", "#ffffff")],
        )
        self.style.configure("TLabelframe", background="#1a1a24", bordercolor="#ff75a0")
        self.style.configure("TLabelframe.Label", background="#1a1a24", foreground="#ff75a0")

        # Color background
        self.canvas = tk.Canvas(self, bg="#0d0d13", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.create_rectangle(50, 50, 750, 550, fill="#2b1a30", outline="#ff75a0", width=3)
        self.canvas.create_text(
            400,
            80,
            text="櫻花 SAKURA BACKGROUND WALLPAPER PREVIEW",
            fill="#ff75a0",
            font=("Arial", 18, "bold"),
        )
        self.canvas.create_oval(100, 200, 300, 400, fill="#ff75a0")

        # Tab Page (ttk.Frame)
        self.page = ttk.Frame(self)
        self.page.place(x=100, y=120, width=600, height=400)

        # Inside Page: Notebook
        self.notebook = ttk.Notebook(self.page)
        self.notebook.pack(fill="both", expand=True)

        # Tab 1
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text=" Tab 1: Calibration ")

        # LabelFrame in Tab 1
        self.lf = ttk.LabelFrame(self.tab1, text=" Servo Settings ", padding=15)
        self.lf.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self.lf, text="Servo Angle:", fg="#ffffff", bg="#1a1a24").pack(anchor="w", pady=5)
        self.scale = ttk.Scale(self.lf, from_=0, to=180)
        self.scale.pack(fill="x", pady=5)

        self.btn = tk.Button(
            self.lf, text="SAVE SETTINGS", bg="#2ed573", fg="white", bd=0, padx=10, pady=5
        )
        self.btn.pack(pady=10)

        # Apply opacity
        pywinstyles.set_opacity(self.page, value=0.8)

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
        save_path = os.path.join(artifact_dir, "opacity_notebook_result.png")
        img.save(save_path)
        print(f"Screenshot saved to: {save_path}")
        self.destroy()


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
