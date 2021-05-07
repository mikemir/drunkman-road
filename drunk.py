import uuid
import random
from position import Position


class Drunk:

    def __init__(self, name):
        self.name = name
        self.position = Position(0, 0)
        self.id = str(uuid.uuid4())

    def take_a_step(self):
        x = random.choice([1, -1])
        y = random.choice([1, -1])

        return self.position.move(x, y)

    def reset(self):
        self.position = Position(0, 0)
