#!/usr/bin/env python3

# it is not recommended, because you may introduce conflicts you are not aware of.
from car import *

audi = Car('audi', 'a4', 2016)
tesla = ElectricCar('tesla', 'model s', 2020)

print(audi.get_descriptive_name())
print(tesla.get_descriptive_name())
