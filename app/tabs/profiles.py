import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import json
import os

class ProfileManagerTab(ttk.Frame):
    def __init__(self, parent, profile, connection, on_profile_loaded_callback):
        super().__init__(parent)
        self.profile = profile
        self.connection = connection
        self.on_profile_loaded = on_profile_loaded_callback

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        card = ttk.LabelFrame(self, text=" Manajer Profil & Konfigurasi ", padding=25)
        card.grid(row=0, column=0, padx=40, pady=40, sticky="n")

        desc = ttk.Label(card, text="Simpan atau muat konfigurasi lengkap robot (Kalibrasi, Pola, Pengaturan) \nsecara lokal di komputer ini.", 
                         font=("Helvetica", 10), justify="center")
        desc.pack(pady=(0, 20))

        # Standard file buttons
        btn_save = ttk.Button(card, text="💾 Simpan Profil Aktif ke PC", width=35, command=self.save_profile)
        btn_save.pack(pady=8)

        btn_load = ttk.Button(card, text="📂 Muat Profil dari PC", width=35, command=self.load_profile)
        btn_load.pack(pady=8)



    def save_profile(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("File JSON", "*.json"), ("Semua File", "*.*")],
            title="Simpan Profil"
        )
        if not file_path:
            return
        
        try:
            with open(file_path, "w") as f:
                f.write(self.profile.to_json())
            self.connection.log(f"Profil disimpan ke: {os.path.basename(file_path)}")
            messagebox.showinfo("Berhasil", "Profil berhasil disimpan!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan profil: {str(e)}")

    def load_profile(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("File JSON", "*.json"), ("Semua File", "*.*")],
            title="Muat Profil"
        )
        if not file_path:
            return
        
        try:
            with open(file_path, "r") as f:
                json_str = f.read()
            self.profile.load_from_json(json_str)
            self.connection.log(f"Profil dimuat: {os.path.basename(file_path)}")
            self.on_profile_loaded()
            messagebox.showinfo("Berhasil", "Profil berhasil dimuat!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat profil: {str(e)}")


