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
        # Load settings.
        self.settings = Settings()
        self.settings.load()
        self.clock = pygame.time.Clock()
        self.modifier = 1  # Variable for FPS-independent updates.

        self.scale = min(self.settings.width, self.settings.height) / 1200  # Scale for objects.

        # PyGame does not support natively specifying window position, so environmental variables have to be specified.
        # PyGame uses SDL as its main window manager, which has these properties to specify the default window location.
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (self.settings.__x__, self.settings.__y__)
        os.environ['SDL_VIDEO_CENTERED'] = '0'

        # Initialize difficulty manager.
        self.difficulty = Difficulty(self.settings)

        # Initialize PyGame, button manager, scrolling background, default scene and player.
        pygame.init()
        pygame.display.set_caption(self.settings.__title__)

        self.buttons = ButtonManager(self)
        self.display = pygame.display.set_mode((self.settings.width, self.settings.height))

        self.background = ScrollingBackground(self.settings, self.display)

        self.current_scene = Menu(self)

        self.player = Player(self.current_scene)

        # Load game theme song, apply volume from settings, and play the song in loop.
        pygame.mixer.music.load('assets/music.ogg', 'ogg')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.settings.volume)

        # Finally, initialize the input handler after everything is loaded and set up.
        self.input = Input(self.player, self, self.settings)

    def main_game_loop(self):
        while True:
            # Sync clock with target FPS and calculate delta time for FPS-independent updating.
            self.clock.tick(self.settings.fps)
            self.modifier = self.clock.get_time() / 20.0

            # Render background first, as it needs to be in the background.
            self.background.render()

            # Update user inputs which are to be used by different entities in the scene.
            self.input.update()

            # Update scene (update and render entities)
            # If scene update returns false, it indicates the need to switch to a different scene.
            if not self.current_scene.update():
                # Reset player speed and speed decay.
                self.player.speed = 5
                self.player.reset_decay()

                # Determine which scene is the proceeding one, then initialize it.
                if type(self.current_scene).__name__ == "Main":
                    # If the current one was the play field, add the achieved score to the score list.
                    self.settings.add_score(int(-self.current_scene.scroll))
                    self.current_scene = Menu(self)
                    self.player.scene = self.current_scene
                else:
                    self.current_scene = Main(self)
                    self.player.scene = self.current_scene

            # Sync background speed with player * delta time.
            # This way, the background animation is invariant amongst refresh rates.
            self.background.set_speed(self.player.speed * self.modifier)

            # Finally, swap the render buffers and show the freshly rendered one.
            pygame.display.update()
