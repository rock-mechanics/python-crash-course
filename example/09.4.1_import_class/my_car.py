#!/usr/bin/env python3

from car import Car

audi = Car('audi', 'a4', 2016)
print(audi.get_descriptive_name())
audi.odometer_reading = 23
audi.read_odometer()
