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
            calc_entry.delete(0, "end")
            calc_entry.insert("end", str(result))
        except:
            messagebox.showerror("Error!", "Check the correctness of data")

    elif key == "C":
        calc_entry.delete(0, "end")

    elif key == "⌫":
        current = calc_entry.get()
        if current:
            calc_entry.delete(len(current)-1, "end")

    elif key == "±":
        try:
            value = float(calc_entry.get())
            calc_entry.delete(0, "end")
            calc_entry.insert("end", str(-value))
        except:
            messagebox.showerror("Error!", "Enter a valid number")

    elif key == "π":
        calc_entry.insert("end", str(math.pi))

    elif key == "xⁿ":
        calc_entry.insert("end", "**")

    elif key == "√":
        try:
            value = float(calc_entry.get())
            calc_entry.delete(0, "end")
            calc_entry.insert("end", str(math.sqrt(value)))
        except:
            messagebox.showerror("Error!", "Enter a valid number")

    elif key == "ⁿ√":
        try:
            expr = calc_entry.get().split(",")
            if len(expr) == 2:
                n = float(expr[0])
                x = float(expr[1])
                result = x ** (1/n)
                calc_entry.delete(0, "end")
                calc_entry.insert("end", str(result))
            else:
                messagebox.showinfo("Hint", "Enter as n,x (например: 3,27)")
        except:
            messagebox.showerror("Error!", "Enter valid values")

    elif key == "sin":
        try:
            value = math.radians(float(calc_entry.get()))
            calc_entry.delete(0, "end")
            calc_entry.insert("end", str(math.sin(value)))
        except:
            messagebox.showerror("Error!", "Enter a valid number")

    elif key == "cos":
        try:
            value = math.radians(float(calc_entry.get()))
            calc_entry.delete(0, "end")
            calc_entry.insert("end", str(math.cos(value)))
        except:
            messagebox.showerror("Error!", "Enter a valid number")

    elif key == "log₁₀":
        try:
            value = float(calc_entry.get())
            calc_entry.delete(0, "end")
            calc_entry.insert("end", str(math.log10(value)))
        except:
            messagebox.showerror("Error!", "Enter a valid number")

    elif key == "n!":
        try:
            value = int(calc_entry.get())
            calc_entry.delete(0, "end")
            calc_entry.insert("end", str(math.factorial(value)))
        except:
            messagebox.showerror("Error!", "Enter a valid integer")

    else:
        calc_entry.insert("end", key)

def switch_theme():
    current = ctk.get_appearance_mode()
    if current == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),

    ("C",5,0), ("⌫",5,1), ("±",5,2), ("√",5,3),
    ("π",6,0), ("sin",6,1), ("cos",6,2), ("log₁₀",6,3),
    ("n!",7,0), ("xⁿ",7,1), ("ⁿ√",7,2), ("Theme",7,3)  
]

for (text, r, c) in buttons:
    if text == "Theme":
        cmd = switch_theme
    else:
        cmd = lambda x=text: calc(x)

    if text.isdigit() or text == ".":   
        fg = "#34495E"
        hover = "#2C3E50"
    elif text in ["+", "-", "*", "/", "="]:  
        fg = "#E67E22"
        hover = "#A04000"
    elif text == "Theme":   
        fg = "#27AE60"
        hover = "#145A32"
    else:  
        fg = "#8E44AD"
        hover = "#5B2C6F"

    btn = ctk.CTkButton(
        root, text=text, command=cmd,
        width=80, height=50, corner_radius=10,
        font=("Arial", 16),
        fg_color=fg,
        hover_color=hover
    )
    btn.grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
