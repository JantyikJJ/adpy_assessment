import pygame.font
from models.menu.button import Button


class ButtonManager:
    def __init__(self, game):
        # Initialize base variables
        self.game = game
        self.buttons = []
        self.font = pygame.font.Font("assets/joystix.ttf", int(48 * game.scale))
        self.button_count = 0
        self.selected_button = 0

        # Initialize variables for Button generation
        self._default_width = int(250 * game.scale)
        self.button_width = self._default_width
        self.button_height = int(100 * game.scale)

        self.button_x = (game.settings.width - self.button_width) / 2
        self.button_gap = int(20 * game.scale)

        self.button_base_y = 700 * game.scale

    def purge_buttons(self):
        # Clear all buttons from the list and reset initial width
        self.buttons.clear()
        self.button_count = 0
        self.selected_button = 0
        self.update_button_width(self._default_width)

    def set_initial_y(self, y):
        self.button_base_y = y

    def button_offset(self):
        # Calculate Y offset based on the amount of buttons currently defined.
        return self.button_base_y + (self.button_height + self.button_gap) * self.button_count

    def update_button_width(self, width):
        # Update button width and position for further Button creation, also update already existing Buttons.
        self.button_width = width
        self.button_x = (self.game.settings.width - self.button_width) / 2

        for button in self.buttons:
            button.update_rect(self.button_x, button.y, self.button_width, button.height)

    def create_button(self, text, click):
        # Create a button instance
        button = Button(self, text, self.button_x, self.button_offset(), click, self.button_width, self.button_height)

        # Add the new button to the button list
        self.buttons.append(button)

        # Increase count (so len() builtin does not have to be used)
        self.button_count += 1

        # Update button width if it's too small to contain the text.
        if button.rendered_text_rect.width > self.button_width:
            self.update_button_width(button.rendered_text_rect.width + (4 * self.button_gap))

        # Return new button for ease of access
        return button

    def delete_button(self, button):
        # Delete button from the list and update button count.
        self.buttons.remove(button)
        self.button_count -= 1

    def render(self):
        # Render each button, accounting for the currently selected one via keyboard (to show it as hovered)
        for index, button in enumerate(self.buttons):
            if index == self.selected_button:
                button.hovered = True
            button.render()
