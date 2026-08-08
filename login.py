import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
import ttkbootstrap as ttkbs
from datetime import datetime
from PIL import Image, ImageTk

from root import ablak
from visitor_root import latogato_ablak
from main_root import foablak

def bejelentkezes():
    def udvozlo_atmenet(nev, kovetkezo_fuggveny):
        frame = tk.Frame(ablak, bg="#F8FAFC")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        felirat = tk.Label(
            frame,
            text=f"Jó napot, {nev}!",
            font=("Space Grotesk", 25, "bold"),
            bg="#F8FAFC",
            fg="#18181B"
        )
        felirat.place(relx=0.5, rely=0.5, anchor="center")
        meret = 25
        def zoom():
            nonlocal meret
            if meret < 37:
                meret += 1
                felirat.config(
                    font=("Space Grotesk", meret, "bold")
                )
                ablak.after(32, zoom)
            else:
                ablak.after(1200, kilepes)
        def kilepes():
            frame.destroy()
            kovetkezo_fuggveny()
        zoom()
    def belepes():
        if (
            felhasznalo.get() == "admin_demo"
            and
            jelszo.get() == "admin_password"
        ):
            login_frame.destroy()
            udvozlo_atmenet("Admin", foablak)
        elif (
            felhasznalo.get() == "visitor_demo"
            and
            jelszo.get() == "visitor_password"
        ):
            login_frame.destroy()
            latogato_ablak()     
        else:
            messagebox.showerror(
                "Hiba",
                "Hibás felhasználónév vagy jelszó!"
            )

    login_frame = tk.Frame(ablak)
    login_frame.pack(expand=True)
  
    logo_kep = Image.open("logo.png")

    logo_kep.thumbnail((300, 300))

    logo_photo = ImageTk.PhotoImage(logo_kep)

    logo_label = tk.Label(
        login_frame,
        image=logo_photo,
        borderwidth=0
    )
    logo_label.image = logo_photo
    logo_label.pack(pady=(0, 25))
    tk.Label(
        login_frame,
        text="COFFEE ERP SYSTEM",
        font=("Space Grotesk", 22, "bold")
    ).pack(pady=(40,5))
    tk.Label(
        login_frame,
        text="Tapolca",
        font=("Space Grotesk", 12)
    ).pack(pady=(0,25))
    tk.Label(login_frame,text="Felhasználónév").pack()
    felhasznalo = tk.Entry(login_frame,width=30)
    felhasznalo.pack(pady=5)
    tk.Label(login_frame,text="Jelszó").pack()
    jelszo = tk.Entry(
        login_frame,
        width=30,
        show="*"
    )
    jelszo.pack(pady=5)
    tk.Button(
    login_frame,
    text="🔓 Bejelentkezés",
    command=belepes
    ).pack(pady=20)
    jelszo.bind(
        "<Return>",
        lambda event: belepes()
    )
