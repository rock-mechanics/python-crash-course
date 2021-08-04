#!/usr/bin/env python3

class Car() : 
    def __init__(self, make, model, year) : 
        self.make = make
        self.model = model
        self.year = year
        # assign a default property
        self.odometer = 0
    def get_descriptive_name(self) : 
        name = '{} {} {}\nIt has travelled {} miles.'.format(self.year, self.make, self.model, self.odometer)
        return name.title()
    def travel(self, miles) : 
        self.odometer += miles
    def update_odometer(self, miles) : 
        if miles >= self.odometer : 
            self.odometer = miles 
        else : 
            print("You can't roll back odometer.")

new_car = Car('audi', 'a4', 2016)
print(new_car.get_descriptive_name())

# modify property directly
new_car.odometer = 100
print(new_car.get_descriptive_name())

# update using a method
new_car.travel(100)
print(new_car.get_descriptive_name())

new_car.update_odometer(300)
print(new_car.get_descriptive_name())

new_car.update_odometer(100)
