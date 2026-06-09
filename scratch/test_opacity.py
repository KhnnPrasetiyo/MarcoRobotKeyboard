"""TODO: module documentation"""

import tkinter as tk
from tkinter import ttk

import pywinstyles


class TestApp(tk.Tk):
    """TODO: add documentation"""

    def __init__(self):
        """TODO: add documentation"""
        super().__init__()
        self.geometry("600x400")
        self.title("Opacity Test")
        self.configure(bg="black")

        # Red canvas background
        self.canvas = tk.Canvas(self, bg="red", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.create_text(
            300, 50, text="BACKGROUND TEXT (RED CANVAS)", fill="white", font=("Arial", 16, "bold")
        )

        # Semi-transparent frame
        self.frame = tk.Frame(self, bg="#1a1a24")
        self.frame.place(x=50, y=100, width=500, height=200)

        # Label and button inside the frame
        self.label = tk.Label(
            self.frame,
            text="This is inside the Frame",
            fg="white",
            bg="#1a1a24",
            font=("Arial", 12),
        )
        self.label.pack(pady=20)

        self.btn = tk.Button(self.frame, text="Click Me", bg="green", fg="white")
        self.btn.pack(pady=10)

        # Apply opacity to the frame
        pywinstyles.set_opacity(self.frame, value=0.6)


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()
