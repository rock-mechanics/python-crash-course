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

    # draw
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    # check for user input
    keep_running = input('Make another walk (y/n) : ')
    if keep_running == 'n' : 
        break
