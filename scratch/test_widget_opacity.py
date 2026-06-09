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
        self.geometry("600x400+100+100")
        self.title("Widget Opacity Test")

        # Canvas background
        self.canvas = tk.Canvas(self, bg="blue", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.create_rectangle(50, 50, 550, 350, fill="red")

        # A frame with solid background
        self.frame = tk.Frame(self, bg="#1a1a24")
        self.frame.place(x=100, y=100, width=400, height=200)

        # Label and button inside the frame
        self.lbl = tk.Label(
            self.frame, text="This is a Label", bg="#1a1a24", fg="white", font=("Arial", 14)
        )
        self.lbl.pack(pady=10)

        self.btn = tk.Button(
            self.frame, text="This is a Button", bg="#ff75a0", fg="white", font=("Arial", 12)
        )
        self.btn.pack(pady=10)

        # Apply opacity to frame
        pywinstyles.set_opacity(self.frame, value=0.8)

        # Apply opacity to individual button inside the frame
        pywinstyles.set_opacity(self.btn, value=0.6)

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
        save_path = os.path.join(artifact_dir, "widget_opacity_result.png")
        img.save(save_path)
        print(f"Screenshot saved to: {save_path}")
        self.destroy()


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
