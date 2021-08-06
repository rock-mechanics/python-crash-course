#!/usr/bin/env python3

def make_pizza(size, *toppings) : 
    print('\nMaking a {}-inch pizza with the following toppings : '.format(size))
    print_list(toppings)

def print_list(items) : 
    for topping in items : 
        print(" - {}.".format(topping))
