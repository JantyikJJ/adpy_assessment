from models.text.animations.Animation import Animation


class SwingAnimation(Animation):
    def __init__(self, progress=0, direction=1, lower=-10, upper=10):
        self.progress = progress
        self.direction = direction

        self.bounds_lower = lower
        self.bounds_upper = upper

    def update(self, text):
        self.progress += self.direction * text.game.modifier

        if self.progress > self.bounds_upper:
            self.direction = -1
            self.progress = self.bounds_upper
        elif self.progress < self.bounds_lower:
            self.direction = 1
            self.progress = self.bounds_lower

        text.rot = self.progress
