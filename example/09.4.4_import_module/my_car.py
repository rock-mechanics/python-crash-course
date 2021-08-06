#!/usr/bin/env python3

# car.py is the module file, the module name is car
import car

audi = car.Car('audi', 'a4', 2016)
tesla = car.ElectricCar('tesla', 'model s', 2020)

print(audi.get_descriptive_name())
print(tesla.get_descriptive_name())
