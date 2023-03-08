from abc import abstractmethod
import pygame
from models.renderable import Renderable


class Entity(Renderable):
    def __init__(self, name, scene, speed=1, x=0, y=0):
        # Save parameters into class variables and initialise base variables
        self.x = x
        self.y = y

        self.rot = 0

        self.scene = scene
        self.speed = speed
        self.visible = True

        # Load entity asset with alpha mask on (to support transparency)
        self.asset = pygame.image.load(f'assets/{name}').convert_alpha()
        self.width = self.asset.get_width()
        self.height = self.asset.get_height()

        # Transform entity according to the game field scale.
        self.asset = pygame.transform.scale(self.asset,
                                            (self.width * self.scene.game.scale,
                                             self.height * self.scene.game.scale))

        # Update dimensions and boundaries after the asset has been scaled.
        self.width = self.asset.get_width()
        self.height = self.asset.get_height()

        self.boundaries = self.asset.get_rect()
        self.update_boundaries()

    @abstractmethod
    def update(self):
        # Update y position of entity and also the hitbox.
        self.y += self.scene.game.player.speed * self.scene.game.modifier
        self.update_boundaries()

        # Returns False if the entity is out of the screen (from bottom edge)
        return self.y < self.scene.game.settings.height

    def update_boundaries(self):
        # Update hitbox of entity
        self.boundaries = self.asset.get_rect().move(self.x, self.y)

    def remove(self):
        # Remove entity from the scene.
        self.scene.remove_entity(self)

    def render(self):
        # Render entity to the display.
        # In order to alleviate the performance requirement of the rendering, only rotate asset when rot != 0.
        if self.rot == 0:
            self.scene.game.display.blit(self.asset, (self.x, self.y, self.width, self.height))
        else:
            self.scene.game.display.blit(pygame.transform.rotate(self.asset, self.rot),
                                         (self.x, self.y, self.width, self.height))
