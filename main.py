from drunk import Drunk
from field import Field
from position import Position
from bokeh.plotting import figure, show


def graph(x, y):
    graphic = figure(title='Camino de borrachos', x_axis_label='Pasos dados', y_axis_label='Distancia recorrida')
    graphic.line(x, y, legend_label='distancia media')

    show(graphic)


def graph_path(x, y):
    graphic = figure(title='Random path')
    graphic.line(x, y)

    show(graphic)


def main():
    walk_steps = [10, 100, 1000]
    cantidad = 100

    myfield = Field()
    myfield.add_drunk(Drunk('Martha Peña'))
    # myfield.add_drunkman(Drunkman('Michael Reynosa'))
    # myfield.add_drunkman(Drunkman('Katya Peña'))
    # myfield.add_drunkman(Drunkman('Ronald Marroquin'))
    # myfield.add_drunkman(Drunkman('Tatiana Peña'))

    for drunk in myfield.get_drunks():
        walking_media_distances = []
        print(f'Prueba con borracho {drunk.name}')
        print(f'{"*" * 75}')

        for steps in walk_steps:
            print(f'Prueba con {steps} paso/os')
            walking_distances = []

            for _ in range(cantidad):
                origin = Position(drunk.position.x, drunk.position.y)
                myfield.walk(drunk, steps)
                distance = drunk.position.distance(origin)
                walking_distances.append(distance)
                drunk.reset()

            walking_media_distance = round(sum(walking_distances) / len(walking_distances), 2)
            walking_media_distances.append(walking_media_distance)
            print(f'Media: {walking_media_distance}')
            print(f'Cantidad de veces: {len(walking_distances)}')
            print(f'Maximo: {max(walking_distances)}')
            print(f'Minimo: {min(walking_distances)}')
            print(f'{"=" * 65}')

        drunk_history = myfield.get_history(drunk)
        graph_path([p.x for p in drunk_history], [p.y for p in drunk_history])

        for i, p in enumerate(drunk_history):
            print(f'Paso {i} X={p.x} Y={p.y}')
        # graph(walk_steps, walking_media_distances)
        print('\n')


if __name__ == '__main__':
    main()
