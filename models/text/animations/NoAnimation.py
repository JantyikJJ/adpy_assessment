from models.text.animations.Animation import Animation


class NoAnimation(Animation):
    def update(self, text):
        return False
