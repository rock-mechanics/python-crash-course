#!/usr/bin/env python3

from random import choice as select
import matplotlib.pyplot as plt

dots = 50

xs = [0]
ys = [0]

while len(xs) < dots : 
    # we force the direction to positive
    x_dir = select([1])
    x_dist = select(list(range(1,50)))
    x_delta = x_dir * x_dist
    x = xs[-1] + x_delta
    xs.append(x)

    y_dir = select([1])
    y_dist = select(list(range(1,50)))
    y_delta = y_dir * y_dist
    y = ys[-1] + y_delta
    ys.append(y)

plt.title('Random Movement')
plt.axis('off')
plt.plot (xs, ys, linewidth=1)
plt.show()

