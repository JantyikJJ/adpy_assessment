import random
from utils.utilities import Utilities
from models.entities.fruit import Fruit
from models.entities.enemy import Enemy


class EntityGenerator:
    def __init__(self, scene):
        # Assign basic variables, a common random variable for better RNG.
        self.scene = scene
        self.random = random.Random()
        self.difficulty = scene.game.difficulty
        self.tick = 0

        self.try_entity_spawn = False
        self.try_enemy_spawn = False

        # Load assets from which the entity generator makes the different entities with their specified attributes.
        self.assets = Utilities.load_file('assets/assets.json')

        self.fruit = self.assets['fruit']
        self.fruit_len = len(self.assets['fruit']) - 1

        self.enemy = self.assets['enemy']
        self.enemy_len = len(self.assets['enemy']) - 1

    def update(self):
        # Update internal tick counter for entity generation
        # Anything above 1FPS results in less than 1 for the modifier, thus modulo matching is viable in this scenario.
        self.tick += self.scene.game.modifier

        # Create auxiliary variable to prevent multiple spawns from int(tick) being the same through multiple frames
        temp_tick = self.tick

        # Check if the current tick can be divided with no remainders for lower bounds.
        # If yes, fruit generation can happen *once* between fruit_low and fruit_high at any random point.
        if int(temp_tick) % self.difficulty.current_difficulty['spawn_rates']['fruit_low'] == 0:
            self.try_entity_spawn = True
            self.tick += 1
        elif int(temp_tick) % self.difficulty.current_difficulty['spawn_rates']['fruit_high'] == 0:
            # If the high limit has been reached, force fruit spawning.
            if self.try_entity_spawn:
                self.spawn_entity()
                self.try_entity_spawn = False

        # Check if the current tick can be divided with no remainders for lower bounds.
        # If yes, enemy generation can happen *once* between enemy_low and fruit_high at any random point.
        if int(temp_tick) % self.difficulty.current_difficulty['spawn_rates']['enemy_low'] == 0:
            self.try_enemy_spawn = True
            if self.tick == temp_tick:
                self.tick += 1
        elif int(temp_tick) % self.difficulty.current_difficulty['spawn_rates']['enemy_high'] == 0:
            # If the high limit has been reached, force enemy spawning.
            if self.try_enemy_spawn:
                self.spawn_entity(True)
                self.try_enemy_spawn = False

        # Randomly generate fruit / junk when it is due.
        if self.try_entity_spawn and self.random.randint(0, 1000) > 950:
            self.spawn_entity()
            self.try_entity_spawn = False

        if self.try_enemy_spawn and self.random.randint(0, 1000) > 950:
            self.spawn_entity(True)
            self.try_enemy_spawn = False

    # Generic method for spawning a randomly selected fruit or junk at a random position
    def spawn_entity(self, enemy=False):
        # Randomly select an enemy / fruit from the list, and create an instance
        if enemy:
            data = self.enemy[self.random.randint(0, self.enemy_len)]
            entity = Enemy(data['name'], self.scene, data['speed_impact'], 0, 0)
        else:
            data = self.fruit[self.random.randint(0, self.fruit_len)]
            entity = Fruit(data['name'], self.scene, data['speed_impact'], 0, 0)

        # Update random position for generated entity, update its boundaries then add entity to the scene.
        entity.x = self.random.randint(0, self.scene.game.settings.width - entity.width)
        entity.y = -50

        entity.update_boundaries()

        self.scene.add_entity(entity)
