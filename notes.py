import tkinter as tk
# version = Alpha-0
class Note:
    def __init__(self,window):
        self.note_area = tk.Text(window,bg="#FFF176",font=("Canberra",16))
        self.note_area.pack()