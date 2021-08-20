#!/usr/bin/env python3

from random import choice as select
import matplotlib.pyplot as plt

dots = 5000

xs = [0]
ys = [0]

while len(xs) < dots : 
    x_dir = select([1,-1])
    x_dist = select(list(range(1,5)))
    x_delta = x_dir * x_dist
    x = xs[-1] + x_delta
    xs.append(x)

    y_dir = select([1,-1])
    y_dist = select(list(range(1,5)))
    y_delta = y_dir * y_dist
    y = ys[-1] + y_delta
    ys.append(y)

plt.title('Random Movement')
plt.axis('off')
plt.plot (xs, ys, linewidth=3)
plt.show()

