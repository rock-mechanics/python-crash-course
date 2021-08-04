#!/usr/bin/env python3

class Car() : 
    def __init__(self, make, model, year) : 
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self) : 
        name = '{} {} {}'.format(self.year, self.make, self.model)
        return name.title()

car = Car('audi', 'a4', 2016)
print(car.get_descriptive_name())
