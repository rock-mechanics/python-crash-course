#!/usr/bin/env python3

requested_toppings = ['mushroom', 'green peppers', 'extra cheeze']

print("{}\n".format(requested_toppings))

for requested_topping in requested_toppings : 
    print("Add {}.".format(requested_topping))
print("\nFinished making your pizza!")

requested_toppings = ['mushroom', 'green peppers', 'extra cheeze']

print("\n{}\n".format(requested_toppings))

for requested_topping in requested_toppings : 
    if requested_topping == 'green peppers' : 
        print("Sorry, we are out of green pepper")
    else : 
        print("Add {}.".format(requested_topping))
print("\nFinished making your pizza!")

