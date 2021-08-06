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


class Battery() : 
    def __init__(self, battery_size = 70) : 
        self.battery_size = battery_size
    def describe_battery(self) : 
        print("This car has a {}-kW battery.".format(self.battery_size))
    def get_range(self) : 
        if self.battery_size == 70 : 
            range = 240
        elif self.battery_size == 85 : 
            range = 270
        print('This car can go approximately {} miles on a full charge'.format(range))

class ElectricCar(Car) : 
    def __init__(self, make, model, year) : 
        super().__init__(make, model, year)
        self.battery = Battery()
