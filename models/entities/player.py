from models.entities.entity import Entity


class Player(Entity):
    def __init__(self, scene):
        super().__init__("player.png", scene, 5, 0, 0)
        self.x = (scene.game.settings.width - self.width) / 2
        self.y = scene.game.settings.height - self.height - 20

        self.decay_progress = 0

        self.update_boundaries()

    def reset_decay(self):
        self.decay_progress = 0

    def update(self):
        self.decay_progress += self.scene.game.modifier

        if self.scene.game.difficulty.current_difficulty['speed_degradation']['offset'] < self.decay_progress:
            progress = int(self.decay_progress
                           - self.scene.game.difficulty.current_difficulty['speed_degradation']['offset'])
            if (progress > 0
                    and progress % self.scene.game.difficulty.current_difficulty['speed_degradation']['rate'] == 0):
                self.speed -= self.scene.game.difficulty.current_difficulty['speed_degradation']['amount']

        self.y -= self.scene.game.player.speed * self.scene.game.modifier

        return super().update()

    def interacts(self, entity):
        return self.boundaries.colliderect(entity.boundaries)

