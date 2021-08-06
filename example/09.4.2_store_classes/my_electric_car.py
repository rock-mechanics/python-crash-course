#!/usr/bin/env python3

from car import ElectricCar

tesla = ElectricCar('tesla', 'model s', 2020)

print(tesla.get_descriptive_name())
tesla.odometer_reading = 23
tesla.read_odometer()

tesla.battery.describe_battery()
tesla.battery.get_range()
