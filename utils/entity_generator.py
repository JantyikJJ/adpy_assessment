import random
from utils.utilities import Utilities
from models.entities.fruit import Fruit
from models.entities.enemy import Enemy


class EntityGenerator:
    def __init__(self, scene):
        self.scene = scene
        self.random = random.Random()
        self.difficulty = scene.game.difficulty
        self.assets = Utilities.load_file('assets/assets.json')
        self.tick = 0

        self.try_entity_spawn = False
        self.try_enemy_spawn = False

        self.fruit = self.assets['fruit']
        self.fruit_len = len(self.assets['fruit']) - 1

        self.enemy = self.assets['enemy']
        self.enemy_len = len(self.assets['enemy']) - 1

    def update(self):
        self.tick += self.scene.game.modifier

        if int(self.tick) % self.difficulty.current_difficulty['spawn_rates']['fruit_low'] == 0:
            self.try_entity_spawn = True
        elif int(self.tick) % self.difficulty.current_difficulty['spawn_rates']['fruit_high'] == 0:
            if self.try_entity_spawn:
                self.spawn_entity()
                self.try_entity_spawn = False

        if int(self.tick) % self.difficulty.current_difficulty['spawn_rates']['enemy_low'] == 0:
            self.try_enemy_spawn = True
        elif int(self.tick) % self.difficulty.current_difficulty['spawn_rates']['fruit_high'] == 0:
            if self.try_enemy_spawn:
                self.spawn_entity(True)
                self.try_enemy_spawn = False

        if self.try_entity_spawn and self.random.randint(0, 1000) > 950:
            self.spawn_entity()
            self.try_entity_spawn = False

        if self.try_enemy_spawn and self.random.randint(0, 1000) > 950:
            self.spawn_entity(True)
            self.try_enemy_spawn = False

    def spawn_entity(self, enemy=False):
        if enemy:
            data = self.enemy[self.random.randint(0, self.enemy_len)]
            entity = Enemy(data['name'], self.scene, data['speed_impact'], 0, 0)
        else:
            data = self.fruit[self.random.randint(0, self.fruit_len)]
            entity = Fruit(data['name'], self.scene, data['speed_impact'], 0, 0)

        entity.x = self.random.randint(0, self.scene.game.settings.width - entity.width)
        entity.y = -50

        entity.update_boundaries()

        self.scene.add_entity(entity)
