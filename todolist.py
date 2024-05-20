import tkinter as tk
# version = Alpha-0
class Todolist:
    def __init__(self,window):
        self.task_index =""
        self.task = ""
        def add_task():
            self.task = self.entry.get()
            if len(self.task) == 0:
                pass
            else:
                self.listbox.insert(tk.END, self.task)
                self.entry.delete(0, tk.END)

        def delete_task():
            try:
                self.task_index = self.listbox.curselection()[0]
                self.listbox.delete(self.task_index)
            except IndexError:
                pass

        self.listbox = tk.Listbox(window, width=50)
        self.listbox.pack(pady=20)

        self.frame = tk.Frame(window)
        self.frame.pack(pady=10)

        self.entry = tk.Entry(self.frame, width=40)
        self.entry.grid(row=0, column=0)

        self.add_button = tk.Button(self.frame, text="Add Task", command=add_task)
        self.add_button.grid(row=0, column=1)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=delete_task)
        self.delete_button.grid(row=0, column=2)