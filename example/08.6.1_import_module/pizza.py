#!/usr/bin/env python3

def make_pizza(size, *toppings) : 
    print('\nMaking a {}-inch pizza with the following toppings : '.format(size))
    for topping in toppings : 
        print(" - {}.".format(topping))
