#!/usr/bin/env python3

class Restaurant() : 
    def __init__(self, restaurant_type, restaurant_name) : 
        self.type = restaurant_type
        self.name = restaurant_name
    def describe_restaurant(self) : 
        print('I have a {} restaurant named {}.'.format(self.type, self.name))
    def open_restaurant(self) : 
        print('{} is now open for business'.format(self.name))

res = Restaurant('italian', 'cute room')

res.describe_restaurant()
res.open_restaurant()
