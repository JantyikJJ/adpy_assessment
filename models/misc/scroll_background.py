import math
import pygame
from models.renderable import Renderable


class ScrollingBackground(Renderable):
    def __init__(self, settings, display):
        self.x = 0
        self.speed = 6
        self.asset = pygame.image.load('assets/background.jpg').convert()
        self.vertical_tiles = 0
        self.horizontal_tiles = 0
        self.settings = settings
        self.display = display

        self.vertical_tiles = math.ceil(self.settings.height / self.asset.get_height()) + 1
        self.horizontal_tiles = math.ceil(self.settings.width / self.asset.get_width()) + 1

    def set_speed(self, speed):
        self.speed = speed

    def update(self):
        pass

    def render(self):
        i = 0
        multiplier = 1
        if self.speed > 0:
            multiplier = -1
        while i < self.vertical_tiles:
            j = 0
            while j < self.horizontal_tiles:
                self.display.blit(self.asset,
                                  (self.asset.get_width() * j * multiplier,
                                   self.asset.get_height() * i * multiplier + self.x))
                j += 1
            i += 1

        self.x += self.speed

        if abs(self.x) > self.asset.get_height():
            self.x = 0
