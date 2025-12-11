import customtkinter as ctk
import math
from tkinter import messagebox

ctk.set_appearance_mode("dark")   
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Calculator")
root.geometry("370x500")

calc_entry = ctk.CTkEntry(root, width=350, height=50, font=("Arial", 20))
calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def calc(key):
    if key == "=":
        try:
            result = eval(calc_entry.get())
            calc_entry.insert("end", "=" + str(result))
        except:
            messagebox.showerror("Error!", "Check the correctness of data")
    elif key == "C":
        calc_entry.delete(0, "end")
    elif key == "±":
        if calc_entry.get().startswith("-"):
            calc_entry.delete(0)
        else:
            calc_entry.insert(0, "-")
    elif key == "π":
        calc_entry.insert("end", math.pi)
    elif key == "xⁿ":
        calc_entry.insert("end", "**")
    elif key == "sin":
        try:
            calc_entry.insert("end", "=" + str(math.sin(float(calc_entry.get()))))
        except:
            messagebox.showerror("Error!", "Enter a valid number")
    elif key == "cos":
        try:
            calc_entry.insert("end", "=" + str(math.cos(float(calc_entry.get()))))
        except:
            messagebox.showerror("Error!", "Enter a valid number")
    elif key == "n!":
        try:
            calc_entry.insert("end", "=" + str(math.factorial(int(calc_entry.get()))))
        except:
            messagebox.showerror("Error!", "Enter a valid integer")
    elif key == "√":
        try:
            calc_entry.insert("end", "=" + str(math.sqrt(float(calc_entry.get()))))
        except:
            messagebox.showerror("Error!", "Enter a valid number")
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, "end")
        calc_entry.insert("end", key)

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
    ("C",5,0), ("±",5,1), ("xⁿ",5,2), ("√",5,3),
    ("π",6,0), ("sin",6,1), ("cos",6,2), ("n!",6,3),
]

for (text, r, c) in buttons:
    cmd=lambda x=text: calc(x)
    btn = ctk.CTkButton(
        root, text=text, command=cmd,
        width=80, height=50, corner_radius=10,
        font=("Arial", 16),
        fg_color="#00A824",      
        hover_color="#2C721B"     
    )
    btn.grid(row=r, column=c, padx=5, pady=5)

def switch_theme():
    current = ctk.get_appearance_mode()
    if current == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

theme_btn = ctk.CTkButton(
    root, text="Theme", command=switch_theme,
    width=350, height=40, corner_radius=10,
    fg_color="#27AE60", hover_color="#145A32"
)
theme_btn.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
