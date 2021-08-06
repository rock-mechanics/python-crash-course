#!/usr/bin/env python3

from car import Car, ElectricCar

audi = Car('audi', 'a4', 2016)
tesla = ElectricCar('tesla', 'model s', 2020)

print(audi.get_descriptive_name())
print(tesla.get_descriptive_name())
