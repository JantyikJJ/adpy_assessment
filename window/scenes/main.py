from window.scenes.scene import Scene
from models.text.text import Text
from utils.entity_generator import EntityGenerator


class Main(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game_field = True
        self.entity_generator = EntityGenerator(self)

        self.font_size = int(52 * game.scale)
        self.padding = int(20 * game.scale)

        self.score = Text("assets/joystix.ttf", self.font_size, game, "Score:0",
                          (255, 255, 255), x=self.padding, y=self.padding, pos='topleft')
        self.speed = Text("assets/joystix.ttf", self.font_size, game, "Speed:0m/s",
                          (255, 255, 255), x=self.padding, y=self.padding+self.padding+self.font_size, pos='topleft')

    def update(self):
        self.game.player.update()
        self.entity_generator.update()
        self.score.update_text(f'Score:{int(-self.scroll):,}')
        self.speed.update_text(f'Speed:{int(self.game.player.speed):,} m/s')

        for entity in self.entities:
            if entity.update():
                if self.game.player.interacts(entity):
                    self.game.player.speed += entity.speed
                    self.game.player.reset_decay()
                    entity.remove()
                else:
                    entity.render()
            else:
                entity.remove()

        if self.game.player.speed == 0:
            return False

        self.scroll -= self.game.player.speed * self.game.modifier
        self.game.player.render()
        self.score.render()
        self.speed.render()
        
        return True
