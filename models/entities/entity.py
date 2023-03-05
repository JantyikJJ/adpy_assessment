from abc import abstractmethod
import pygame
from models.renderable import Renderable


class Entity(Renderable):
    def __init__(self, name, scene, speed=1, x=0, y=0):
        self.x = x
        self.y = y

        self.rot = 0

        self.scene = scene
        self.speed = speed
        self.visible = True

        self.asset = pygame.image.load(f'assets/{name}').convert_alpha()
        self.width = self.asset.get_width()
        self.height = self.asset.get_height()

        self.asset = pygame.transform.scale(self.asset,
                                            (self.width * self.scene.game.scale,
                                             self.height * self.scene.game.scale))

        self.width = self.asset.get_width()
        self.height = self.asset.get_height()

        self.boundaries = self.asset.get_rect()
        self.update_boundaries()

    @abstractmethod
    def update(self):
        self.y += self.scene.game.player.speed * self.scene.game.modifier
        self.update_boundaries()

        return self.y < self.scene.game.settings.height

    def update_boundaries(self):
        self.boundaries = self.asset.get_rect().move(self.x, self.y)

    def remove(self):
        self.scene.remove_entity(self)

    def render(self):
        if self.rot == 0:
            self.scene.game.display.blit(self.asset, (self.x, self.y, self.width, self.height))
        else:
            self.scene.game.display.blit(pygame.transform.rotate(self.asset, self.rot),
                                         (self.x, self.y, self.width, self.height))
