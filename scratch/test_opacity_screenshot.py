"""TODO: module documentation"""

import time
import tkinter as tk
from tkinter import ttk

import pywinstyles
from PIL import Image, ImageDraw, ImageGrab


class TestApp(tk.Tk):
    """TODO: add documentation"""

    def __init__(self):
        """TODO: add documentation"""
        super().__init__()
        self.geometry("600x400+100+100")
        self.title("Opacity Screenshot Test")

        # Create a colorful background canvas
        self.canvas = tk.Canvas(self, bg="#1a1a24", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Draw some shapes/text on canvas so we can see transparency
        self.canvas.create_rectangle(50, 50, 550, 350, fill="#3b3b4f", outline="#ff75a0", width=2)
        self.canvas.create_text(
            300, 80, text="WALLPAPER BACKGROUND PREVIEW", fill="#ff75a0", font=("Arial", 16, "bold")
        )
        self.canvas.create_oval(100, 150, 250, 300, fill="#ff75a0")

        # Semi-transparent frame
        self.frame = tk.Frame(self, bg="#272736")
        self.frame.place(x=200, y=120, width=350, height=200)

        # Inside the frame
        self.lbl = tk.Label(
            self.frame,
            text="Inside Transparent Frame",
            fg="#ffffff",
            bg="#272736",
            font=("Arial", 12, "bold"),
        )
        self.lbl.pack(pady=20)

        self.btn = tk.Button(
            self.frame, text="Button in Frame", bg="#ff75a0", fg="white", activebackground="#ff9ff3"
        )
        self.btn.pack(pady=10)

        # Apply opacity to the frame
        pywinstyles.set_opacity(self.frame, value=0.7)

        # Force update and schedule screenshot
        self.after(1000, self.take_screenshot)

    def take_screenshot(self):
        """TODO: add documentation"""
        self.update()
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        w = self.winfo_width()
        h = self.winfo_height()

        # Grab screenshot of the window
        bbox = (x, y, x + w, y + h)
        img = ImageGrab.grab(bbox=bbox)

        import os

        artifact_dir = (
            r"C:\Users\Admin\.gemini\antigravity-ide\brain\bbcdabdf-8378-4f22-8033-d634387fa05a"
        )
        save_path = os.path.join(artifact_dir, "opacity_test_result.png")
        img.save(save_path)
        print(f"Screenshot saved to: {save_path}")
        self.destroy()


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
