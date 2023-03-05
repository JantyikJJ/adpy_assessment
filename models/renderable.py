from abc import abstractmethod


class Renderable:
    @abstractmethod
    def update(self):
        pass

    def render(self):
        pass
