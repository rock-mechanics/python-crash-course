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

class ElectricCar(Car): 
    def __init__(self, make, model, year): 
        # get the init function in the super class.
        super().__init__(make, model, year)

ecar = ElectricCar('tesla', 'model s', 2016)
print(ecar.get_descriptive_name())
