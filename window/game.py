import pygame
import os

from utils.settings import Settings
from utils.input import Input
from utils.difficulty_manager import Difficulty
from utils.button_manager import ButtonManager

from models.misc.scroll_background import ScrollingBackground
from models.entities.player import Player

from window.scenes.main import Main
from window.scenes.menu import Menu


class Game:
    def __init__(self):
        self.settings = Settings()
        self.settings.load()
        self.clock = pygame.time.Clock()
        self.modifier = 1

        self.scale = min(self.settings.width, self.settings.height) / 1200

        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (self.settings.__x__, self.settings.__y__)
        os.environ['SDL_VIDEO_CENTERED'] = '0'

        self.difficulty = Difficulty(self.settings)

        pygame.init()
        pygame.display.set_caption(self.settings.__title__)

        self.buttons = ButtonManager(self)
        self.display = pygame.display.set_mode((self.settings.width, self.settings.height))

        self.background = ScrollingBackground(self.settings, self.display)

        self.current_scene = Menu(self)

        self.player = Player(self.current_scene)

        pygame.mixer.music.load('assets/music.ogg', 'ogg')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.settings.volume)

        self.input = Input(self.player, self, self.settings)

    def main_game_loop(self):
        while True:
            self.clock.tick(self.settings.fps)
            self.modifier = self.clock.get_time() / 20.0

            self.background.render()

            self.input.update()

            if not self.current_scene.update():
                self.player.speed = 5
                self.player.reset_decay()
                if type(self.current_scene).__name__ == "Main":
                    self.settings.add_score(int(-self.current_scene.scroll))
                    self.current_scene = Menu(self)
                    self.player.scene = self.current_scene
                else:
                    self.current_scene = Main(self)
                    self.player.scene = self.current_scene

            self.background.set_speed(self.player.speed * self.modifier)

            pygame.display.update()
