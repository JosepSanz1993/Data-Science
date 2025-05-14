import tkinter as tk
from tkinter import ttk

class TimeIntervalWindow:
    def __init__(self):
        self.time = None
        self.intervals = None
        self.root = tk.Tk()
        self.root.title("INPUT DATA")
        self.root.geometry("250x150")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Time:").pack(pady=(10, 0))
        self.time_var = tk.IntVar()
        self.time_spinbox = ttk.Spinbox(self.root, from_=0, to=100, textvariable=self.time_var)
        self.time_spinbox.pack()

        ttk.Label(self.root, text="Intervals:").pack(pady=(10, 0))
        self.intervals_var = tk.IntVar()
        self.intervals_spinbox = ttk.Spinbox(self.root, from_=0, to=100, textvariable=self.intervals_var)
        self.intervals_spinbox.pack()

        ttk.Button(self.root, text="OK", command=self.submit).pack(pady=10)

    def submit(self):
        self.time = self.time_var.get()
        self.intervals = self.intervals_var.get()
        self.root.quit()   
        self.root.destroy()


    def get_inputs(self):
        self.root.mainloop()
        return self.time, self.intervals