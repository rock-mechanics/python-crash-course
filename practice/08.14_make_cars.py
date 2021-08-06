#!/usr/bin/env python3

def make_car(maker, model, **info) : 
    car = {}
    car['manufacturer'] = maker
    car['model'] = model
    for key, value in info.items() : 
        car [key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)
car = make_car('tesla', 'model3', color='blue', power='electric')
print(car)
