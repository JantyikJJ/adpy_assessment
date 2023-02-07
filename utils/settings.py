from utils.display import Display
import os.path as path
import json


class Settings:
    def __init__(self):
        self._location = "config.json"

        self.width = 1280
        self.height = 720

        self.__x__ = 0
        self.__y__ = 0
        self.center()

    def load(self):
        if path.exists(self._location):
            file = open(self._location, "r")
            content = file.read()
            file.close()
            cfg = json.loads(content)

            self.width = cfg['width']
            self.height = cfg['height']

            self.center()
        else:
            self.save()

    def center(self):
        display = Display()

        self.__x__ = (display.screen_width - self.width) / 2
        self.__y__ = (display.screen_height - self.height) / 2

    def save(self):
        content = self.to_json()
        file = open(self._location, "w")
        file.write(content)
        file.close()

    def to_json(self):
        filtered = dict(filter(lambda elem: not elem[0].startswith("_"), self.__dict__.items()))
        print(filtered)
        return json.dumps(filtered, default=lambda o: o, sort_keys=True, indent=4)
