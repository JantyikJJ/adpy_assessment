from abc import abstractmethod


class Scene:
    def __init__(self, game):
        self.entities = []
        self.scroll = 0
        self.game = game

        self.game_field = False

    @abstractmethod
    def update(self):
        pass

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)
