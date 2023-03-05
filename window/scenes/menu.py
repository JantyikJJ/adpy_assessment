import pygame

from window.scenes.scene import Scene
from models.text.text import Text


def quit_clicked():
    pygame.quit()
    quit()


class Menu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.keep_scene = True

        self.text = Text("assets/joystix.ttf", int(72 * game.scale), game, self.game.settings.__title__,
                         (255, 255, 255), "swing").center(y_offset=int(-550 * game.scale))

        self.menu_buttons()

    def update(self):
        self.text.update()
        self.game.player.render()
        self.text.render()

        self.game.buttons.render()

        if self.keep_scene:
            return True
        else:
            self.keep_scene = True
            return False

    def menu_buttons(self):
        for button in self.game.buttons.buttons:
            button.delete()

        self.game.buttons.create_button("Start", self.start_clicked)
        self.game.buttons.create_button("Quit", quit_clicked)

    def start_clicked(self):
        self.keep_scene = False
