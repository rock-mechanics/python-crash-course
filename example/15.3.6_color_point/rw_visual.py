import matplotlib.pyplot as plt
from random_walk import RandomWalk
import threading

while True : 

    # create an instance of the random walk
    # default number of points is 5000
    rw = RandomWalk()

    # fill the coordinates
    rw.fill_walk()

    # change the title of the graph
    plt.title('Random Walk', fontsize = 20)

    # label points index
    p_index = list(range(rw.num_points))

    # draw and assign a color map
    plt.scatter(rw.x_values, rw.y_values, c = p_index, cmap = plt.cm.Blues, s=10)
    plt.show()

    # check for user input
    keep_running = input('Make another walk (y/n) : ')
    if keep_running == 'n' : 
        break
