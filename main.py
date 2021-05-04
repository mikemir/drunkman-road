from drunkman import Drunkman
from field import Field

def main():
    steps = [10, 100, 1000, 10000, 100000]

    myfield = Field()
    myfield.add_drunkman(Drunkman('Martha Peña'))
    myfield.add_drunkman(Drunkman('Michael Reynosa'))
    myfield.add_drunkman(Drunkman('Katya Peña'))
    myfield.add_drunkman(Drunkman('Ronald Marroquin'))
    myfield.add_drunkman(Drunkman('Tatiana Peña'))

    for step in steps:
        for drunkman in myfield.get_drunkmans():
            myfield.walk(drunkman, step, True)
            print('\n')

    for drunkman in myfield.get_drunkmans():
        print(f'Borracho {drunkman.name} está en x={drunkman.position.x}, y={drunkman.position.y}')
        distance = drunkman.position.distance(0, 0)
        print(f'Distancia recorrida: {distance}')
        print(f'{"=" * 50}')

if __name__ == '__main__':
    main()