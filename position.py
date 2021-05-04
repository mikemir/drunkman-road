class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

    def distance(self, x, y):
        delta_x = self.x - x
        delta_y = self.y - y

        return round((delta_x ** 2 + delta_y ** 2) ** 0.5, 1)