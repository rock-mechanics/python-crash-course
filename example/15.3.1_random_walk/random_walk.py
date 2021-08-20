from random import choice

class RandomWalk() : 
    def __init__(self, num_points = 5000) : 
        # define number of points we need to draw
        self.num_points = num_points
        # create empty coordinate collection.
        self.x_values = []
        self.y_values = []

