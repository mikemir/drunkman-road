class Field:

    def __init__(self):
        self.drunkmans = {}

    def add_drunkman(self, drunkman):
        self.drunkmans[drunkman.id] = drunkman

    def get_drunkman(self, drunkman):
        return self.drunkmans[drunkman.id]

    def get_drunkmans(self):
        return self.drunkmans.values()

    def walk(self, drunkman, steps, print_step = False):
        for i in range(1, steps + 1):
            drunkman.walk()

            if print_step:
                print(f'Borracho {drunkman.name}: X={drunkman.position.x}, Y={drunkman.position.y}')
                print(f'{"*" * 25} Paso {i} {"*" * 25}')

        return self.get_drunkman(drunkman).position
