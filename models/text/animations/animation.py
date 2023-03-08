from abc import abstractmethod


# Define a scheme for Animations.
class Animation:
    @abstractmethod
    def update(self, text):
        return False
