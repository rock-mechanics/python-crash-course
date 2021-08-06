#!/usr/bin/env python3

class Restaurant() : 
    def __init__(self, restaurant_type, restaurant_name) : 
        self.type = restaurant_type
        self.name = restaurant_name
    def describe_restaurant(self) : 
        print('I have a {} restaurant named {}.'.format(self.type, self.name))
    def open_restaurant(self) : 
        print('{} is now open for business'.format(self.name))

res1 = Restaurant('italian', 'cute room')
res2 = Restaurant('french', 'elegant room')
res3 = Restaurant('chinese', 'spicy room')

res1.describe_restaurant()
res1.open_restaurant()
print()
res2.describe_restaurant()
res2.open_restaurant()
print()
res3.describe_restaurant()
res3.open_restaurant()
