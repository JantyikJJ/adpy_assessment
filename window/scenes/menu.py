import pygame

from window.scenes.scene import Scene
from models.text.text import Text


class Menu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.keep_scene = True

        self.text = Text("assets/joystix.ttf", int(72 * game.scale), game, self.game.settings.__title__,
                         (255, 255, 255), "swing").center(y_offset=int(-550 * game.scale))

        self.score_texts = []

        self.menu_buttons()

    def update(self):
        self.text.update()
        self.game.player.render()
        self.text.render()

        for text in self.score_texts:
            text.update()
            text.render()

        self.game.buttons.render()

        if self.keep_scene:
            return True
        else:
            self.keep_scene = True
            return False

    def menu_buttons(self, _=None):
        self.score_texts.clear()
        self.game.buttons.purge_buttons()

        self.game.buttons.create_button("Start", self.start_clicked)
        self.game.buttons.create_button("Settings", self.settings_clicked)
        self.game.buttons.create_button("Scores", self.scores_clicked)
        self.game.buttons.create_button("Quit", self.quit_clicked)

    # Default screen buttons
    def start_clicked(self, _=None):
        self.game.buttons.purge_buttons()

        self.keep_scene = False

    def settings_clicked(self, _=None):
        self.game.buttons.purge_buttons()

        self.game.buttons.create_button(f"Volume: {int(self.game.settings.volume * 100)}%", self.volume_clicked)
        self.game.buttons.create_button(f"Difficulty: {self.game.difficulty.current_difficulty['name']}",
                                        self.iter_diff)
        self.game.buttons.create_button(f"FPS: {self.game.settings.fps}", self.iter_fps)
        self.game.buttons.create_button("Back", self.menu_buttons)

    def scores_clicked(self, _=None):
        self.game.buttons.purge_buttons()

        back_button = self.game.buttons.create_button("Back", self.menu_buttons)
        offset = back_button.y_bottom + self.game.buttons.button_gap

        scores = self.game.settings.scores[:10]
        if len(scores) == 0:
            scores.append("No scores!")
        else:
            scores = map(lambda item: str(item), scores)

        self.generate_scores(scores, offset)

    def quit_clicked(self, _=None):
        self.game.buttons.purge_buttons()

        pygame.quit()
        quit()

    # Settings buttons
    def volume_clicked(self, button):
        self.game.settings.volume -= 0.1
        if self.game.settings.volume < 0:
            self.game.settings.volume = 1

        button.update_text(f"Volume: {int(self.game.settings.volume * 100)}%")

        self.game.settings.save()
        pygame.mixer.music.set_volume(self.game.settings.volume)

    def iter_diff(self, button):
        self.game.settings.difficulty = (self.game.settings.difficulty + 1) % len(self.game.difficulty.difficulties)
        self.game.difficulty.set_difficulty(self.game.settings.difficulty)

        button.update_text(f"Difficulty: {self.game.difficulty.current_difficulty['name']}")

        self.game.settings.save()

    def iter_fps(self, button):
        self.game.settings.__current_fps__ = (self.game.settings.__current_fps__ + 1)\
                                             % self.game.settings.__fps_options_len__
        self.game.settings.fps = self.game.settings.__fps_options__[self.game.settings.__current_fps__]

        button.update_text(f"FPS: {self.game.settings.fps}")

        self.game.settings.save()

    # Scores

    def generate_scores(self, scores, y_offset):
        prev_offset = y_offset

        for score in scores:
            text = Text("assets/joystix.ttf", 48 * self.game.modifier, self.game, score, (255, 255, 255))
            text.center(0, 0)
            text.text_rect.y = prev_offset
            prev_offset += text.text_rect.height + 20 * self.game.modifier

            self.score_texts.append(text)
