import tkinter as tk


class Display:
    def __init__(self):
        # Initialize Tkinter and get display dimensions.
        root = tk.Tk()

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        root.destroy()
