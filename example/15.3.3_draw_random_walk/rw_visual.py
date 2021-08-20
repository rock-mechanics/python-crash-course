import matplotlib.pyplot as plt
from random_walk import RandomWalk

# create an instance of the random walk
# default number of points is 5000
rw = RandomWalk()

# fill the coordinates
rw.fill_walk()

# change the title of the graph
plt.title('Random Walk', fontsize = 20)

# draw
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

