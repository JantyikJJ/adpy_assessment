from datetime import datetime
import os.path as path
import tkinter as tk
import json


class Display:
    def __init__(self):
        root = tk.Tk()

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        root.destroy()


class Settings:
    def __init__(self):
        self.location = "config.json"

        display = Display()

        self.width = 1280
        self.height = 720

        self.x = (display.screen_width - self.width) / 2
        self.y = (display.screen_height - self.height) / 2

    def load(self):
        if path.exists(self.location):
            file = open(self.location, "r")
            content = file.read()
            file.close()
            cfg = json.loads(content)
            self.width = cfg.width
            self.height = cfg.height
            self.x = cfg.x
            self.y = cfg.y
        else:
            self.save()

    def save(self):
        content = json.dumps(self)
        file = open(self.location, "w")
        file.write(content)
        file.close()


class Fps:
    def __init__(self, callback):
        self.cb = callback
        self.counter = 0
        self.date = datetime.now()

    def update(self):
        sub = datetime.now() - self.date
        if sub.seconds >= 1:
            self.date = datetime.now()
            self.cb(self.counter)
            self.counter = 0
            return

        self.counter = self.counter + 1
