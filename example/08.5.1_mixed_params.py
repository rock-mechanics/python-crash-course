#!/usr/bin/env python3

# python will first match positional/keyword argument.
# python will later match extensive  argument.

def make_pizza(size, *toppings) : 
    print("Making a {}-inch pizza with the following toppings : ".format(size))
    for topping in toppings : 
        print("-{}".format(topping))


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheeze')

