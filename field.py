from position import Position


class Field:

    def __init__(self):
        self.drunks = {}
        self.history_path = {}

    def add_drunk(self, drunk):
        self.drunks[drunk.id] = drunk

    def get_drunk(self, drunk):
        return self.drunks[drunk.id]

    def get_drunks(self):
        return self.drunks.values()

    def walk(self, drunk, steps, print_step=False):
        self.history_path[drunk.id] = []
        self.history_path[drunk.id].append(Position(drunk.position.x, drunk.position.y))

        for i in range(1, steps + 1):
            drunk.take_a_step()
            self.history_path[drunk.id].append(Position(drunk.position.x, drunk.position.y))

            if print_step:
                print(f'Borracho {drunk.name}: X={drunk.position.x}, Y={drunk.position.y}')
                print(f'{"*" * 25} Paso {i} {"*" * 25}')

        return self.get_drunk(drunk).position

    def get_history(self, drunk):
        return self.history_path[drunk.id]
