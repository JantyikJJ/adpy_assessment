from utils.utilities import Utilities


class Difficulty:
    def __init__(self):
        self.difficulties = Utilities.load_file('assets/difficulties.json')
        self.current_difficulty = self.difficulties[0]
        self.difficulties = filter(lambda item: item.name, self.difficulties)
