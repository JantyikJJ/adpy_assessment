from utils.utilities import Utilities


class Difficulty:
    def __init__(self, settings):
        # Load difficulties and set currently active difficulty.
        self.difficulties = Utilities.load_file('assets/difficulties.json')
        self.current_difficulty = self.difficulties[settings.difficulty]

    def set_difficulty(self, difficulty):
        # Change the currently active difficulty.
        self.current_difficulty = self.difficulties[difficulty]
