import json

import pygame

from models.renderable import Renderable


class Button(Renderable):
    def __init__(self, manager, text, x, y, click, width=140, height=50):
        # Save parameters into class variables
        self.manager = manager
        self.text = text
        self.font = manager.font
        self.click_event = click
        self.hovered = False

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Calculate some hitbox-related coordinates
        self.x_right = x + width
        self.y_bottom = y + height

        # Define default values
        self.hover_background_color = (175, 255, 175)
        self.background_color = (114, 165, 114)

        # Render text and update text position
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rendered_text_rect = self.rendered_text.get_rect()

        self._text_pos = (x + ((width - self.rendered_text_rect.width) / 2),
                          y + ((height - self.rendered_text_rect.height) / 2))

    def update_text(self, text):
        # Update text and text position
        self.rendered_text = self.font.render(text, True, (255, 255, 255))
        self.rendered_text_rect = self.rendered_text.get_rect()

        self._text_pos = (self.x + ((self.width - self.rendered_text_rect.width) / 2),
                          self.y + ((self.height - self.rendered_text_rect.height) / 2))

    def update_rect(self, x, y, width, height):
        # Update position and size of the button, aligning the text with it.
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.x_right = x + width
        self.y_bottom = y + height

        self._text_pos = (x + ((width - self.rendered_text_rect.width) / 2),
                          y + ((height - self.rendered_text_rect.height) / 2))

    def delete(self):
        # Delete button from the button manager
        self.manager.delete_button(self)

    def update_hovered(self, x, y):
        # Handle hover check (simple rectangle-point collision check)
        self.hovered = self.x <= x <= self.x_right and self.y <= y <= self.y_bottom
        return self.hovered

    def click(self):
        # Simulate click event with providing the current Button instance as required parameter
        self.click_event(self)

    def update(self):
        # Buttons do not require parameterless update as they do not have animations or anything else.
        pass

    def render(self):
        # Render different background based on hover state
        if self.hovered:
            pygame.draw.rect(self.manager.game.display, self.hover_background_color,
                             [self.x, self.y, self.width, self.height])
        else:
            pygame.draw.rect(self.manager.game.display, self.background_color,
                             [self.x, self.y, self.width, self.height])

        # Render text over the button background.
        self.manager.game.display.blit(self.rendered_text, self._text_pos)
