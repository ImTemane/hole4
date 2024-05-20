import tkinter as tk
# version = Alpha-0
class Calculator:
    def __init__(self,window):
        def on_click(event):
            text = event.widget.cget("text")
            if text == "=":
                try:
                    result = eval(entry.get())
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, str(result))
                except:
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, "Error")
            elif text == "C":
                entry.delete(0, tk.END)
            else:
                entry.insert(tk.END, text)

        i = 0
        while i < 5:
            window.rowconfigure(i, weight=1)
            if i < 4:
                window.columnconfigure(i, weight=1)
            i += 1

        entry = tk.Entry(window,font=("Arial", 16))
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        ]

        row = 1
        col = 0
        for button_text in buttons:
            if button_text == "C":
                button = tk.Button(window, text=button_text, font=("Arial", 12),bg="#AB2B2C")
                button.grid(row=row, column=col,columnspan=5,sticky=tk.E+tk.W+tk.N+tk.S)
                button.bind("<Button-1>", on_click)
            elif button_text in ["/","*","+","-"]:
                button = tk.Button(window, text=button_text, font=("Arial", 12),bg="#358615")
                button.grid(row=row, column=col,columnspan=5,sticky=tk.E+tk.W+tk.N+tk.S)
                button.bind("<Button-1>", on_click)
            else:
                button = tk.Button(window, text=button_text, font=("Arial", 12))
                button.grid(row=row, column=col,sticky=tk.E+tk.W+tk.N+tk.S)
                button.bind("<Button-1>", on_click)
            col += 1
            if col > 3:
                col = 0
                row += 1