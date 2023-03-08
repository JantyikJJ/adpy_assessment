from window.scenes.scene import Scene
from models.text.text import Text
from utils.entity_generator import EntityGenerator


class Main(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game_field = True

        # Initialize entity generator
        self.entity_generator = EntityGenerator(self)

        # Init stat display considering the scale of the game to keep the game looking uniform in all sizes.
        self.font_size = int(52 * game.scale)
        self.padding = int(20 * game.scale)

        # Set scheme for Score and Speed labels in the top right corner, considering the scale of the game field.
        self.score = Text("assets/joystix.ttf", self.font_size, game, "Score:0",
                          (255, 255, 255), x=self.padding, y=self.padding, pos='topleft')
        self.speed = Text("assets/joystix.ttf", self.font_size, game, "Speed:0m/s",
                          (255, 255, 255), x=self.padding, y=self.padding+self.padding+self.font_size, pos='topleft')

    def update(self):
        # Update player, so entity collisions can be updated after
        self.game.player.update()
        # Update entity generator
        self.entity_generator.update()
        # Update stat texts
        self.score.update_text(f'Score:{int(-self.scroll):,}')
        self.speed.update_text(f'Speed:{int(self.game.player.speed):,} m/s')

        # Update entities one-by-one and check for collision with the player
        for entity in self.entities:
            # Update entity
            # False: entity out of bounds, so it's best to be removed
            if entity.update():
                # If collides -> apply speed modifier and reset player's "hunger" (speed decrement delay), then remove
                # If not, render entity as usual
                if self.game.player.interacts(entity):
                    self.game.player.speed += entity.speed
                    self.game.player.reset_decay()
                    entity.remove()
                else:
                    entity.render()
            else:
                entity.remove()

        # If player's speed is 0 => return False, indicating that the run is over
        if self.game.player.speed == 0:
            return False

        # Update total scroll and render components
        self.scroll -= self.game.player.speed * self.game.modifier
        self.game.player.render()
        self.score.render()
        self.speed.render()
        
        return True
