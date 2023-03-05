from abc import abstractmethod


class Animation:
    @abstractmethod
    def update(self, text):
        return False
