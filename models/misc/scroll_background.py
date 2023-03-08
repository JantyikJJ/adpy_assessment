import math
import pygame
from models.renderable import Renderable


class ScrollingBackground(Renderable):
    def __init__(self, settings, display):
        # Initialize default variables and load background which is to be tiled.
        self.y = 0
        self.speed = 6
        self.asset = pygame.image.load('assets/background.jpg').convert()
        self.vertical_tiles = 0
        self.horizontal_tiles = 0
        self.settings = settings
        self.display = display

        # Calculated the amount of tiles required, considering the size of the asset and the game window.
        self.vertical_tiles = math.ceil(self.settings.height / self.asset.get_height()) + 1
        self.horizontal_tiles = math.ceil(self.settings.width / self.asset.get_width()) + 1

    def set_speed(self, speed):
        # Set scrolling speed of the background
        self.speed = speed

    def update(self):
        # Update does not have a role in this render-able object, thus it is just passed.
        pass

    def render(self):
        i = 0

        # Check direction from speed and negate it if it's going downwards (fallback, should not happen)
        multiplier = 1
        if self.speed > 0:
            multiplier = -1

        # Render both vertical and horizontal tiles while offsetting them into their proper positions
        while i < self.vertical_tiles:
            j = 0
            while j < self.horizontal_tiles:
                self.display.blit(self.asset,
                                  (self.asset.get_width() * j * multiplier,
                                   self.asset.get_height() * i * multiplier + self.y))
                j += 1
            i += 1

        # Update Y offset for the scrolling background
        self.y += self.speed

        # Loop Y offset by the asset height, so the background does not just flow out of screen.
        if abs(self.y) > self.asset.get_height():
            self.y = 0
