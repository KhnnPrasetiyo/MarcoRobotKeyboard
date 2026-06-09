"""TODO: module documentation"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import tkinter as tk

import pywinstyles
from PIL import ImageGrab

from app.main import ModernApp


class AutomatedSidebarTest(ModernApp):
    """TODO: add documentation"""

    def __init__(self):
        """TODO: add documentation"""
        super().__init__()

        # Apply opacity to all children of the sidebar that have solid background
        for child in self.sidebar.winfo_children():
            if isinstance(child, (tk.Label, tk.Button)) and child != self.sidebar_bg:
                # Set background to transparent or apply pywinstyles
                try:
                    pywinstyles.set_opacity(child, value=0.7)
                except Exception as e:
                    print(f"Failed to set opacity on {child}: {e}")

        self.after(1500, self.capture)

    def capture(self):
        """TODO: add documentation"""
        self.update()
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        w = 300  # Sidebar width is 250, capture slightly wider
        h = self.winfo_height()
        bbox = (x, y, x + w, y + h)
        img = ImageGrab.grab(bbox=bbox)

        artifact_dir = (
            r"C:\Users\Admin\.gemini\antigravity-ide\brain\bbcdabdf-8378-4f22-8033-d634387fa05a"
        )
        save_path = os.path.join(artifact_dir, "sidebar_transparency_result.png")
        img.save(save_path)
        print(f"Sidebar screenshot saved to: {save_path}")
        self.destroy()


if __name__ == "__main__":
    app = AutomatedSidebarTest()
    app.mainloop()
