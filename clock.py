import tkinter as tk
import time
# version = Alpha-0

class Clock:
    def __init__(self,window):
        def update_clock():
            current_time = time.strftime('%H:%M:%S')
            self.clock_label.config(text=current_time)
            self.clock_label.after(1000, update_clock)

        self.clock_label = tk.Label(window, font=('Helvetica', 48), bg='black', fg='white')
        self.clock_label.pack(padx=20, pady=20)

        update_clock()