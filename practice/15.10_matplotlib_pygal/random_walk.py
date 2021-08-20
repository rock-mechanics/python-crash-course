import pygal
from random import choice

def get_vector(distance) : 
    return choice([1,-1]) * choice(list(range(1, distance + 1)))

tries = 1000
points = [(0,0)]

while len(points) < tries : 

    # previous point
    px, py = points[-1]

    x_delta = get_vector(5)
    x = px + x_delta

    y_delta = get_vector(5)
    y = py + y_delta
    points.append((x,y))

xy_chart = pygal.XY()
xy_chart.title = 'Random Walk'
xy_chart.add('random walk', points)
xy_chart.render_to_file('walk.svg')

