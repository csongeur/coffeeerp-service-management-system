import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
import ttkbootstrap as ttkbs

ablak=ttkbs.Window(themename="flatly")

alap_font = tkfont.nametofont("TkDefaultFont")
alap_font.configure(
    family="Space Grotesk",
    size=13
)

ablak.title("CoffeeERP")
ablak.state("zoomed")
