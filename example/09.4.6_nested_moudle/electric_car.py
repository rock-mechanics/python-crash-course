'''This class is representing electric car'''

# import module from another module.
from car import Car

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
