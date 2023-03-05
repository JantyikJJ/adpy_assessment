import pygame.font
from models.menu.button import Button


class ButtonManager:
    def __init__(self, game):
        self.game = game
        self.buttons = []
        self.font = pygame.font.Font("assets/joystix.ttf", int(48 * game.scale))
        self.button_count = 0
        self.selected_button = 0

        # Button variables
        self.button_width = int(250 * game.scale)
        self.button_height = int(100 * game.scale)

        self.button_x = (game.settings.width - self.button_width) / 2
        self.button_gap = int(20 * game.scale)

        self.button_base_y = 700 * game.scale

    def set_initial_y(self, y):
        self.button_base_y = y

    def button_offset(self):
        return self.button_base_y + (self.button_height + self.button_gap) * self.button_count

    def create_button(self, text, click):
        button = Button(self, text, self.button_x, self.button_offset(), click, self.button_width, self.button_height)
        self.buttons.append(button)
        self.button_count += 1
        return button

    def delete_button(self, button):
        self.buttons.remove(button)
        self.button_count -= 1

    def render(self):
        for index, button in enumerate(self.buttons):
            if index == self.selected_button:
                button.hovered = True
            button.render()
