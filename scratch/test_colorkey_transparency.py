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
        self.title("Color Key Transparency Test")

        # Blue canvas background (representing wallpaper)
        self.canvas = tk.Canvas(self, bg="blue", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.create_rectangle(50, 50, 550, 350, fill="red")

        # Transparent key color
        trans_color = "#123456"

        # A frame with trans_color background
        self.frame = tk.Frame(self, bg=trans_color)
        self.frame.place(x=100, y=100, width=400, height=200)

        # Label with trans_color background (should blend/be transparent)
        self.lbl = tk.Label(
            self.frame,
            text="This is transparent background text",
            bg=trans_color,
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.lbl.pack(pady=10)

        # A solid card inside the frame
        self.card = tk.Frame(self.frame, bg="#1a1a24")
        self.card.pack(fill="both", expand=True, padx=20, pady=10)

        self.card_lbl = tk.Label(
            self.card, text="This is inside a solid card", bg="#1a1a24", fg="yellow"
        )
        self.card_lbl.pack(pady=10)

        self.btn = tk.Button(self.card, text="Opaque Button", bg="green", fg="white")
        self.btn.pack(pady=5)

        # Set color key transparency on the parent frame
        pywinstyles.set_opacity(self.frame, color=trans_color)

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
        save_path = os.path.join(artifact_dir, "colorkey_opacity_result.png")
        img.save(save_path)
        print(f"Screenshot saved to: {save_path}")
        self.destroy()


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
