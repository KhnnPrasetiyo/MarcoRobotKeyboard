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

        # Konfigurasi grid pembungkus untuk memusatkan kartu secara estetis
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)  # Kolom kartu tetap
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)     # Baris kartu tetap
        self.rowconfigure(2, weight=1)

        card = ttk.LabelFrame(self, text=" Manajer Profil & Konfigurasi ", padding=30)
        card.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        desc = ttk.Label(card, text="Simpan atau muat konfigurasi lengkap robot (Kalibrasi, Pola, Pengaturan)\nsecara lokal di komputer Anda sebagai file berkas JSON.", 
                         font=("Helvetica", 10), justify="center")
        desc.pack(pady=(0, 25))

        # File buttons
        self.btn_save = tk.Button(card, text="💾 SIMPAN PROFIL AKTIF KE PC", bg="#3867d6", fg="white", 
                                  activebackground="#4b7bec", font=("Helvetica", 11, "bold"), relief="flat", bd=0, 
                                  height=2, width=32, cursor="hand2", command=self.save_profile)
        self.btn_save.pack(pady=10)
        self.btn_save.bind("<Enter>", lambda e: self.btn_save.config(bg="#4b7bec"))
        self.btn_save.bind("<Leave>", lambda e: self.btn_save.config(bg="#3867d6"))

        self.btn_load = tk.Button(card, text="📂 MUAT PROFIL DARI PC", bg="#2ed573", fg="white", 
                                  activebackground="#26af5f", font=("Helvetica", 11, "bold"), relief="flat", bd=0, 
                                  height=2, width=32, cursor="hand2", command=self.load_profile)
        self.btn_load.pack(pady=10)
        self.btn_load.bind("<Enter>", lambda e: self.btn_load.config(bg="#26af5f"))
        self.btn_load.bind("<Leave>", lambda e: self.btn_load.config(bg="#2ed573"))



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


