class Scene:
    def __init__(self):
        self.objects = []

    def apply(self):
        for item in self.objects:
            item.pack()

    def add_item(self, item):
        self.objects.append(item)
        return len(self.objects) - 1

    def remove_item(self, item):
        self.objects.remove(item)