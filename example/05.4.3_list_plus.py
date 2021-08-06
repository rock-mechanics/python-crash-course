#!/usr/bin/env python3

available_toppings = ['mushroom', 'olives', 'green peeper', 'pepperoni', 'pinapple', 'extra cheeze']
requested_toppings = ['mushroom', 'french fries', 'extra cheeze']

for requested_topping in requested_toppings : 
    if requested_topping in available_toppings : 
        print("Add {}.".format(requested_topping))
    else : 
        print("We don't have : {}.".format(requested_topping))
print("\nFinished making your pizza!")
