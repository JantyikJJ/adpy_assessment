import pygame

from window.scenes.scene import Scene
from models.text.text import Text


class Menu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.keep_scene = True

        # Init game title label.

        self.text = Text("assets/joystix.ttf", int(72 * game.scale), game, self.game.settings.__title__,
                         (255, 255, 255), "swing").center(y_offset=int(-550 * game.scale))

        self.score_texts = []

        # Set initial layout to be the default menu buttons
        self.menu_buttons()

    def update(self):
        # Update text animation, render player, then render the text (so it overlaps for sure).
        self.text.update()
        self.game.player.render()
        self.text.render()

        # Render score texts (if there are any).
        for text in self.score_texts:
            text.update()
            text.render()

        # Render buttons (if there are any).
        self.game.buttons.render()

        # If the play button is clicked, keep scene is set to false, indicating the need of scene switching.
        # However, if the implementation keeps the current instance of the menu, leaving it on False would cause bugs.
        if self.keep_scene:
            return True
        else:
            self.keep_scene = True
            return False

    # Generate menu buttons
    def menu_buttons(self, _=None):
        # Clear rendered scores and purge previous buttons
        self.score_texts.clear()
        self.game.buttons.purge_buttons()

        # Create main menu buttons
        self.game.buttons.create_button("Start", self.start_clicked)
        self.game.buttons.create_button("Settings", self.settings_clicked)
        self.game.buttons.create_button("Scores", self.scores_clicked)
        self.game.buttons.create_button("Quit", self.quit_clicked)

    # Main -> Start clicked
    def start_clicked(self, _=None):
        # Purge buttons and indicate scene change
        self.game.buttons.purge_buttons()

        self.keep_scene = False

    # Main -> Settings clicked
    def settings_clicked(self, _=None):
        # Purge buttons
        self.game.buttons.purge_buttons()
        # Create buttons for volume, difficulty and fps changes, also back button to go back to the main menu
        self.game.buttons.create_button(f"Volume: {int(self.game.settings.volume * 100)}%", self.volume_clicked)
        self.game.buttons.create_button(f"Difficulty: {self.game.difficulty.current_difficulty['name']}",
                                        self.iter_diff)
        self.game.buttons.create_button(f"FPS: {self.game.settings.fps}", self.iter_fps)
        self.game.buttons.create_button("Back", self.menu_buttons)

    # Main -> Scores clicked
    def scores_clicked(self, _=None):
        # Purge buttons.
        self.game.buttons.purge_buttons()

        # Create button for going back to the main menu and create Text entities for scores.
        back_button = self.game.buttons.create_button("Back", self.menu_buttons)
        offset = back_button.y_bottom + self.game.buttons.button_gap

        # Get first 10 scores. If there are not any, add "No scores!" predefined text.
        scores = self.game.settings.scores[:10]
        if len(scores) == 0:
            scores.append("No scores!")
        else:
            scores = map(lambda item: str(item), scores)

        # Generate score labels under each other, and add them to the score label list.
        self.generate_scores(scores, offset)

    # Main -> Quit clicked
    def quit_clicked(self, _=None):
        # Quit game
        self.game.buttons.purge_buttons()

        pygame.quit()
        quit()

    # Settings -> Volume clicked
    def volume_clicked(self, button):
        # Iterate volume and update text, save settings and set main volume
        self.game.settings.volume -= 0.1
        if self.game.settings.volume < 0:
            self.game.settings.volume = 1

        button.update_text(f"Volume: {int(self.game.settings.volume * 100)}%")

        self.game.settings.save()
        pygame.mixer.music.set_volume(self.game.settings.volume)

    # Settings -> Difficulty clicked
    def iter_diff(self, button):
        # Iterate difficulty and set it as the current one, then update the button and save the settings
        self.game.settings.difficulty = (self.game.settings.difficulty + 1) % len(self.game.difficulty.difficulties)
        self.game.difficulty.set_difficulty(self.game.settings.difficulty)

        button.update_text(f"Difficulty: {self.game.difficulty.current_difficulty['name']}")

        self.game.settings.save()

    # Settings -> FPS clicked
    def iter_fps(self, button):
        # Update FPS and set it as the current one, then update the button and save the settings
        self.game.settings.__current_fps__ = (self.game.settings.__current_fps__ + 1)\
                                             % self.game.settings.__fps_options_len__
        self.game.settings.fps = self.game.settings.__fps_options__[self.game.settings.__current_fps__]

        button.update_text(f"FPS: {self.game.settings.fps}")

        self.game.settings.save()

    # Scores

    def generate_scores(self, scores, y_offset):
        prev_offset = y_offset

        # Iterate through the scores, create new labels for them and position them under each other.
        # Eventually, add them to the score texts list which is rendered in the update method.
        for score in scores:
            text = Text("assets/joystix.ttf", 36 * self.game.scale, self.game, score, (255, 255, 255))
            text.center(0, 0)
            text.text_rect.y = prev_offset
            prev_offset += text.text_rect.height + 8 * self.game.scale

            self.score_texts.append(text)
