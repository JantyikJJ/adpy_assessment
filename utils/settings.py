from utils.display import Display
from utils.utilities import Utilities
import os.path as path
import json


class Settings:
    def __init__(self):
        self._location = "config.json"

        # Define changeable variables.
        self.width = 1280
        self.height = 720
        self.fps = 144
        self.volume = 0.8
        self.difficulty = 0
        self.scores = []

        # Define constant variables, which are not intended to be changed.
        self.__x__ = 0
        self.__y__ = 0
        self.__speed__ = 10
        self.__title__ = "Jumpie Junkie"
        self.__screen_center_width__ = self.width / 2
        self.__screen_center_height__ = self.height / 2
        self.__fps_options__ = [30, 60, 90, 120, 144, 240, 960]
        self.__fps_options_len__ = len(self.__fps_options__)

        # Parse currently selected FPS from the config, then fall back to 144fps if it was not possible.
        try:
            self.__current_fps__ = self.__fps_options__.index(self.fps)
        except ValueError:
            self.__current_fps__ = 4
            self.fps = self.__fps_options__[self.__current_fps__]

        # Calculate the center of the screen to make the game window centered.
        self.center()

    def load(self):
        # Load config, or generate the default one, then save it.
        if path.exists(self._location):
            cfg = Utilities.load_file(self._location)

            # Dynamically assign the variables from the config file to the current instance.
            for item in cfg.keys():
                self.__dict__[item] = cfg[item]

            # Recenter the game window
            self.center()
        else:
            self.save()

    def add_score(self, score):
        # Add score to the score list, and make sure that the best score is on top.
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.save()

    def center(self):
        # Get display size, then claculate the center of the screen-
        display = Display()

        self.__x__ = (display.screen_width - self.width) / 2
        self.__y__ = (display.screen_height - self.height) / 2

    def save(self):
        # Convert current instance to json (excluding variables starting with _) and save it to the config file.
        content = self.to_json()
        file = open(self._location, "w")
        file.write(content)
        file.close()

    def to_json(self):
        # Dynamically iterate through all class variables excluding the ones starting with _, then create JSON.
        filtered = dict(filter(lambda elem: not elem[0].startswith("_"), self.__dict__.items()))
        return json.dumps(filtered, default=lambda o: o, sort_keys=True, indent=4)
