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

class Battery() : 
    '''battery of electric car'''
    def __init__(self, size = 70) : 
        self.battery_size = size
    def describe_battery(self) : 
        print("This car has a {}-kW battery.".format(self.battery_size))
    def get_range(self) : 
        if self.battery_size == 70 : 
            range = 240
        elif self.battery_size == 85 : 
            range = 270
        else : 
            range = 'unknown'
        print('This car can go approximately {} miles on a full charge'.format(range))

class ElectricCar(Car): 
    def __init__(self, make, model, year): 
        # get the init function in the super class.
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self) : 
        self.battery.describe_battery()
    def upgrade_battery(self) : 
        if self.battery.battery_size != 85 : 
            self.battery.battery_size = 85

tesla = ElectricCar('tesla', 'model s', 2016)
tesla.battery.get_range()
tesla.upgrade_battery()
tesla.battery.get_range()
