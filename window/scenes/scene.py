class Scene:
    def __init__(self, name, config):
        self.objects = []
        self.width = config.width
        self.height = config.height
        self.name = name

    def apply(self):
        for item in self.objects:
            item.pack()

    def add_item(self, item):
        self.objects.append(item)
        return len(self.objects) - 1

    def remove_item(self, item):
        self.objects.remove(item)
