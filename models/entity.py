class Entity:
    def __init__(self, asset, x=0, y=0):
        self.asset = None
        self.x = x
        self.y = y
        self.load_asset(asset)

    def load_asset(self, asset):
        self.asset = asset
