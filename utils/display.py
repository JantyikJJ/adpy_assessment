import tkinter as tk


class Display:
    def __init__(self):
        root = tk.Tk()

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        root.destroy()
