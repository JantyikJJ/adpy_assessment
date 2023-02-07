from utils.display import Display
import os.path as path
import json


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

            print(cfg)

            self.width = cfg['width']
            self.height = cfg['height']
            self.x = cfg['x']
            self.y = cfg['y']
        else:
            self.save()

    def save(self):
        content = self.to_json()
        file = open(self.location, "w")
        file.write(content)
        file.close()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
