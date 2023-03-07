from models.text.animations.animation import Animation


class NoAnimation(Animation):
    def update(self, text):
        return False
