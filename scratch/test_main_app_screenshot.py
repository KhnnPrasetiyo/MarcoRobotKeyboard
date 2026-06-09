"""TODO: module documentation"""

import os
import sys

# Add root path to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import tkinter as tk

from PIL import ImageGrab

from app.main import ModernApp


class AutomatedScreenshotApp(ModernApp):
    """TODO: add documentation"""

    def __init__(self):
        """TODO: add documentation"""
        super().__init__()
        # Wait 1.5 seconds, switch page to Robot Configuration (which has Calibration), then screenshot
        self.after(1500, self.navigate_and_screenshot)

    def navigate_and_screenshot(self):
        """TODO: add documentation"""
        # Switch to robot settings page
        self.show_page("Konfigurasi Robot")
        self.update()

        # Wait another 1 second for render
        self.after(1000, self.capture)

    def capture(self):
        """TODO: add documentation"""
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        w = self.winfo_width()
        h = self.winfo_height()
        bbox = (x, y, x + w, y + h)
        img = ImageGrab.grab(bbox=bbox)

        artifact_dir = (
            r"C:\Users\Admin\.gemini\antigravity-ide\brain\bbcdabdf-8378-4f22-8033-d634387fa05a"
        )
        save_path = os.path.join(artifact_dir, "app_transparency_result.png")
        img.save(save_path)
        print(f"App screenshot saved to: {save_path}")
        self.destroy()


if __name__ == "__main__":
    app = AutomatedScreenshotApp()
    app.mainloop()
