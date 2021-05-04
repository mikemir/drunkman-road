from position import Position
class Field:

    def __init__(self):
        self.drunkmans = {}
        self.history_path = {}

    def add_drunkman(self, drunkman):
        self.drunkmans[drunkman.id] = drunkman

    def get_drunkman(self, drunkman):
        return self.drunkmans[drunkman.id]

    def get_drunkmans(self):
        return self.drunkmans.values()

    def walk(self, drunkman, steps, print_step = False):
        self.history_path[drunkman.id] = []
        self.history_path[drunkman.id].append(Position(drunkman.position.x, drunkman.position.y))

        for i in range(1, steps + 1):
            drunkman.walk()
            self.history_path[drunkman.id].append(Position(drunkman.position.x, drunkman.position.y))

            if print_step:
                print(f'Borracho {drunkman.name}: X={drunkman.position.x}, Y={drunkman.position.y}')
                print(f'{"*" * 25} Paso {i} {"*" * 25}')

        return self.get_drunkman(drunkman).position

    def get_history(self, drunkman):
        return self.history_path[drunkman.id]
