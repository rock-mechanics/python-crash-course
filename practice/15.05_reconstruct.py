#!/usr/bin/env python3

from random import choice as select
import matplotlib.pyplot as plt

dots = 50

xs = [0]
ys = [0]

def get_random_vector() : 
    direction = select([1, -1])
    distance = select(list(range(1,50)))
    return direction * distance
    
while len(xs) < dots : 
    # we force the direction to positive
    x_delta = get_random_vector()
    x = xs[-1] + x_delta
    xs.append(x)

    y_delta = get_random_vector()
    y = ys[-1] + y_delta
    ys.append(y)

plt.title('Random Movement')
plt.axis('off')
plt.plot (xs, ys, linewidth=1)
plt.show()

