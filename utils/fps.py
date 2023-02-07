from datetime import datetime


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
