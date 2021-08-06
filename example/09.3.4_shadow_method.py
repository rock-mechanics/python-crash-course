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
    def fill_gas_tank(self): 
        print('Filling gas tank now.')

car = Car('audi', 'a4', 2016)
print(car.get_descriptive_name())
car.fill_gas_tank()

class ElectricCar(Car): 
    def __init__(self, make, model, year): 
        # get the init function in the super class.
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self) : 
        print('This car has a {}-kW battery.'.format(self.battery_size))
    def fill_gas_tank(self) : 
        print('This car does not have a gas tank.')


ecar = ElectricCar('tesla', 'model s', 2016)
print(ecar.get_descriptive_name())
ecar.describe_battery()
ecar.fill_gas_tank()
