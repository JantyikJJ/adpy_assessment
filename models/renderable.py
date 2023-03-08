from abc import abstractmethod


# Scheme for render-able entities by making update and render required parameters.
class Renderable:
    @abstractmethod
    def update(self):
        pass

    def render(self):
        pass
