from utils.utilities import Utilities


class Difficulty:
    def __init__(self, settings):
        self.difficulties = Utilities.load_file('assets/difficulties.json')
        self.current_difficulty = self.difficulties[settings.difficulty]

    def set_difficulty(self, difficulty):
        self.current_difficulty = self.difficulties[difficulty]
