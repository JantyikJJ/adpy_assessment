from models.text.animations.animation import Animation


class SwingAnimation(Animation):
    def __init__(self, progress=0, direction=1, lower=-10, upper=10):
        # Initialize basic variables for the swing animation
        self.progress = progress
        self.direction = direction

        self.bounds_lower = lower
        self.bounds_upper = upper

    def update(self, text):
        # Update rotation progress based on the delta time and direction
        self.progress += self.direction * text.game.modifier

        # If progress hits the lower or upper bound for the animation, it should switch to the other direction
        if self.progress > self.bounds_upper:
            self.direction = -1
            self.progress = self.bounds_upper
        elif self.progress < self.bounds_lower:
            self.direction = 1
            self.progress = self.bounds_lower

        # Apply current rotation to the text instance.
        text.rot = self.progress
