from models.renderable import Renderable

from models.text.animations.no_animation import NoAnimation
from models.text.animations.swing_animation import SwingAnimation

import pygame


class Text(Renderable):
    def __init__(self, font, size, game, text, color=(0, 0, 0), anim='none', x=0, y=0, rot=0, pos='midtop'):
        # Define default variables for the current Text instance
        self.font = pygame.font.Font(font, int(size))
        self.game = game
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.rot = rot
        self.pos = pos

        # Initialize animation, if provided
        if anim == 'none':
            self.animation = NoAnimation()
        elif anim == 'swing':
            self.animation = SwingAnimation()

        # Create text surface from the string that can be rendered with PyGame
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect()

        # Update position of text based on the top left or top center positions.
        self.update_rect_pos()

    def update_text(self, text):
        # Generate new text surface based on the new string provided.
        self.text = text
        self.text_surface = self.font.render(text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.update_rect_pos()

    def center(self, x_offset=0, y_offset=0):
        # Center the text to the screen
        self.x = ((self.game.settings.width - self.text_surface.get_width()) / 2) + x_offset
        self.y = ((self.game.settings.height - self.text_surface.get_height()) / 2) + y_offset

        self.text_rect.midleft = (self.x, self.y)
        return self

    def update(self):
        # Update current animation (no animation just has a 'pass' in the method.)
        self.animation.update(self)

    def render(self):
        # Render text, accounting for rotation
        # Alleviate rendering by only rotating the text surface when necessary
        if self.rot == 0:
            self.game.display.blit(self.text_surface, self.text_rect)
        else:
            self.game.display.blit(pygame.transform.rotate(self.text_surface, self.rot), self.text_rect)

    def update_rect_pos(self):
        # Update position considering the target position from where the translation should be viewed from.
        if self.pos == 'midtop':
            self.text_rect.midtop = (self.x, self.y)
        elif self.pos == 'topleft':
            self.text_rect.topleft = (self.x, self.y)
