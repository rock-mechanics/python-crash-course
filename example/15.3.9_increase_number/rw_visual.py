import matplotlib.pyplot as plt
from random_walk import RandomWalk
import threading

# create an instance of the random walk
# default number of points is 5000
rw = RandomWalk(50000)

# fill the coordinates
rw.fill_walk()

# change the title of the graph
plt.title('Random Walk', fontsize = 20)

# label points index
p_index = list(range(rw.num_points))


# getting the axes object
# turn off the axis
plt.axis('off')

# draw and assign a color map
plt.scatter(rw.x_values, rw.y_values, c = p_index, cmap = plt.cm.Blues, edgecolor='none', s=1)
# redraw the stating point and ending point
plt.scatter(rw.x_values[0], rw.y_values[0], c = 'red', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', s=30)

# show the plot
plt.show()

