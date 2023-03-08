from models.text.animations.animation import Animation


# Define an auxiliary class for ease of handling in code.
class NoAnimation(Animation):
    def update(self, text):
        return False
