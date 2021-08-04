#!/usr/bin/env python3

class Car() : 
    def __init__(self, make, model, year) : 
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def get_descriptive_name(self) : 
        name = '{} {} {}'.format(self.year, self.make, self.model)
        return name.title()

car = Car('audi', 'a4', 2016)
print(car.get_descriptive_name())

class Battery() : 
    '''battery of electric car'''
    def __init__(self, size = 70) : 
        self.battery_size = size
    def describe_battery(self) : 
        print("This car has a {}-kW battery.".format(self.battery_size))

class ElectricCar(Car): 
    def __init__(self, make, model, year): 
        # get the init function in the super class.
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self) : 
        self.battery.describe_battery()

ecar = ElectricCar('tesla', 'model s', 2016)
print(ecar.get_descriptive_name())
ecar.describe_battery()
