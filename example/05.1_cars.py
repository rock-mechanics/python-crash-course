#!/usr/bin/env python3

cars = ['audi', 'bmw', 'subaru', 'byd', 'toyota']

for car in cars : 
    if car == 'bmw' or car == 'byd' : 
        print(car.upper())
    else : 
        print(car.title())


