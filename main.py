import tkinter as tk
from tkinter import ttk
from calculator import *
from notes import *
from todolist import *
from clock import *
from tkinter import messagebox
import webbrowser

# Made by @Temane with ❤️ and with the help of ChatGPT and Youtube // hole4.co 😉
# Thanks for your help 🫡 (if you are here, you are a programmer)
# This code is very easy to understand 😊
# A fews updates are coming soon...
# version = Alpha-0

def update_checker():
    messagebox.askyesno(title="Redirection", message="Do you want to be redirected to the update checker website ?",detail="Click no to quit")
    if False:
        pass
    else:
        webbrowser.open("https://hole4.readthedocs.io/en/latest/update-checker/#alpha-0")

def about_me():
    messagebox.askyesno(title="About me/Redirection", message="By @ImTemane, do you want to be redirected to the Github project page ? ",detail="Click no to quit")
    if False:
        pass
    else:
        webbrowser.open("https://github.com/ImTemane/hole4")

root = tk.Tk()
root.title("Hole4")
root.geometry("800x400")
root.iconbitmap("_internal/logohole4.ico")


calculator = Calculator
note = Note
tdl = Todolist
clock = Clock

menubar = tk.Menu(root)

moremenu = tk.Menu(menubar)
moremenu.add_command(label="Update Checker",command=update_checker)
moremenu.add_separator()
moremenu.add_command(label="About me",command=about_me)
menubar.add_cascade(label="More", menu=moremenu)

root.config(menu=menubar)

frame_left = tk.Frame(root)
frame_right = tk.Frame(root)

frame_left.pack(side="left",expand=True,fill="both")
frame_right.pack(side="right",expand=True,fill="both")

notebook_left = ttk.Notebook(frame_left)
notebook_right = ttk.Notebook(frame_right)

notebook_left.pack(expand=True,fill="both")
notebook_right.pack(expand=True,fill="both")

tdl_frame = tk.Frame(notebook_left) #tdl = To-do-list
tdl_frame.pack(fill="both",expand=True)
tdl(tdl_frame)

clock_frame = tk.Frame(notebook_left)
clock_frame.pack(fill="both",expand=True)
clock(clock_frame)

calculator_frame = tk.Frame(notebook_right)
calculator_frame.pack(fill="both",expand=True)
calculator(calculator_frame)


note_frame = tk.Frame(notebook_right)
note_frame.pack(fill="both",expand=True)
note(note_frame)

notebook_left.add(tdl_frame,text="To-do-list")
notebook_left.add(clock_frame,text="Clock")

notebook_right.add(calculator_frame,text="Calculator")
notebook_right.add(note_frame,text="Note")

root.mainloop()
