from models.entities.entity import Entity


class Player(Entity):
    def __init__(self, scene):
        # Initialize Entity parent with some default variables
        super().__init__("player.png", scene, 5, 0, 0)

        # Update default position and define speed decay auxiliary variable
        self.x = (scene.game.settings.width - self.width) / 2
        self.y = scene.game.settings.height - self.height - 20

        self.decay_progress = 0

        # Update hitbox
        self.update_boundaries()

    def reset_decay(self):
        # Reset speed decay
        self.decay_progress = 0

    def update(self):
        # Update decay progress
        self.decay_progress += self.scene.game.modifier

        # Check if speed degradation offset is hit by the decay progress.
        if self.scene.game.difficulty.current_difficulty['speed_degradation']['offset'] < self.decay_progress:
            # If so, check if the progress reached the penalty tick.
            progress = int(self.decay_progress
                           - self.scene.game.difficulty.current_difficulty['speed_degradation']['offset'])
            if (progress > 0
                    and progress % self.scene.game.difficulty.current_difficulty['speed_degradation']['rate'] == 0):
                # Penalty tick reached, reduce player's speed.
                self.speed -= self.scene.game.difficulty.current_difficulty['speed_degradation']['amount']

                # self.scene.game.modifier is less than 1 second.
                # If the refresh rate is high, it results in int(decay_progress) remaining the same for multiple frames.
                # To avoid multiple speed reduction, change decay progress to the offset.
                self.decay_progress = self.scene.game.difficulty.current_difficulty['speed_degradation']['offset']

        # Shift entity's Y coordinate, because rendering is also offset due to ease of fruit / enemy rendering.
        # This is to keep the player at the bottom part of the game field.
        self.y -= self.scene.game.player.speed * self.scene.game.modifier

        # Return the result of the Entity class' default update function
        return super().update()

    def interacts(self, entity):
        # Check if an entity is colliding with the player.
        return self.boundaries.colliderect(entity.boundaries)

