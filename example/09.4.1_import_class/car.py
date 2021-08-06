''' This class is a representation of a car '''

class Car() : 
    def __init__(self, make, model, year) : 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name (self) : 
        name = '{} {} {}'.format(self.year, self.make, self.model)
        return name.title()
    def read_odometer(self) : 
        print('This car has {} miles on a it'.format(self.odometer_reading))
    def update_odometer(self, mileage) : 
        if mileage >= self.odometer_reading: 
            self.odomter_reading = mileage
        else :
            print("You cannot roll back the odometer!")
    def increase_odometer(self, miles):
        self.odometer_reading += miles
