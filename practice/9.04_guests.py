#!/usr/bin/env python3

class Restaurant() : 
    def __init__(self, restaurant_type, restaurant_name) : 
        self.type = restaurant_type
        self.name = restaurant_name
        self.number_served = 0
    def describe_restaurant(self) : 
        print('I have a {} restaurant named {}.'.format(self.type, self.name))
    def open_restaurant(self) : 
        print('{} is now open for business'.format(self.name))
    def set_number_served(self, number) : 
        self.number_served = number
    def increase_number_served(self, number) : 
        self.number_served += number
        

res = Restaurant('italian', 'cute room')

res.describe_restaurant()
res.open_restaurant()
print('There are {} people visited in this restaurant.'.format(res.number_served))
res.number_served = 1
print('There are {} people visited in this restaurant.'.format(res.number_served))
res.set_number_served(10)
print('There are {} people visited in this restaurant.'.format(res.number_served))
res.increase_number_served(10)
print('There are {} people visited in this restaurant.'.format(res.number_served))
