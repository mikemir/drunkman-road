from drunkman import Drunkman
from field import Field
from position import Position

def main():
    walk_steps = [10, 100, 1000, 10000, 100000]
    cantidad = 100

    myfield = Field()
    myfield.add_drunkman(Drunkman('Martha Peña'))
    # myfield.add_drunkman(Drunkman('Michael Reynosa'))
    # myfield.add_drunkman(Drunkman('Katya Peña'))
    # myfield.add_drunkman(Drunkman('Ronald Marroquin'))
    # myfield.add_drunkman(Drunkman('Tatiana Peña'))

    for drunkman in myfield.get_drunkmans():
        print(f'Prueba con borracho {drunkman.name}')
        print(f'{"*" * 75}')

        for steps in walk_steps:
            print(f'Prueba con {steps} paso/os')
            walking_distances = []

            for _ in range(cantidad):
                origin = Position(drunkman.position.x, drunkman.position.y)
                myfield.walk(drunkman, steps)
                distance = drunkman.position.distance(origin)
                walking_distances.append(distance)
                drunkman.reset()

            print(f'Media: {round(sum(walking_distances) / len(walking_distances), 2)}')
            print(f'Cantidad de veces: {len(walking_distances)}')
            print(f'Maximo: {max(walking_distances)}')
            print(f'Minimo: {min(walking_distances)}')
            print(f'{"=" * 60}')

        print('\n')


if __name__ == '__main__':
    main()