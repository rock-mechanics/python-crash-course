from random import choice

class RandomWalk() : 
    def __init__(self, num_points = 5000) : 
        # define number of points we need to draw
        self.num_points = num_points
        # create empty coordinate collection.
        # they start from 0,0 point
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self) : 
        # fill the coordinates until it reaches the designed number
        while(len(self.x_values) < self.num_points) : 
            #random.choice function takes a list and choose one from them
            x_direction = choice([1,-1])
            x_distance = choice(list(range(5)))
            x_delta = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice(list(range(5)))
            y_delta = y_direction * y_distance

            if x_delta == 0 and y_delta == 0 : 
                # we ignore this point as it is not moving
                continue

            # calculate the point value
            # fetch the last point and move from there
            x_value = self.x_values[-1] + x_delta
            y_value = self.y_values[-1] + y_delta

            self.x_values.append(x_value)
            self.y_values.append(y_value)
            


