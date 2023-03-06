from utils.display import Display
from utils.utilities import Utilities
import os.path as path
import json


class Settings:
    def __init__(self):
        self._location = "config.json"

        self.width = 1280
        self.height = 720
        self.fps = 144
        self.volume = 0.8
        self.difficulty = 0
        self.scores = []

        self.__x__ = 0
        self.__y__ = 0
        self.__speed__ = 10
        self.__title__ = "Jumpie Junkie"
        self.__screen_center_width__ = self.width / 2
        self.__screen_center_height__ = self.height / 2
        self.__fps_options__ = [30, 60, 90, 120, 144, 240, 960]
        self.__fps_options_len__ = len(self.__fps_options__)

        try:
            self.__current_fps__ = self.__fps_options__.index(self.fps)
        except ValueError:
            self.__current_fps__ = 4
            self.fps = self.__fps_options__[self.__current_fps__]

        self.center()

    def load(self):
        if path.exists(self._location):
            cfg = Utilities.load_file(self._location)

            for item in cfg.keys():
                self.__dict__[item] = cfg[item]

            self.center()
        else:
            self.save()

    def add_score(self, score):
        self.scores.append(score)
        self.scores.sort()
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
        return json.dumps(filtered, default=lambda o: o, sort_keys=True, indent=4)
