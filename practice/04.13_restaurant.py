#!/usr/bin/env python3

restaurant = ('pizza', 'burger', 'pasta', 'fries')

for food in restaurant : 
    print(food)

restaurant = ('noodle', 'rice', 'pasta', 'fries')

for food in restaurant : 
    print(food)


print("\nlet's trigger an error")

restaurant[0] = 'cake'
