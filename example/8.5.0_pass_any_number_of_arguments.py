#!/usr/bin/env python3

def make_pizza(*toppings) : 
    print(type(toppings))
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni', 'mushrooms', 'green peppers', 'extra cheeze')

def make_pizza_better(*toppings) : 
    print('You pizza has the following toppings : ')
    for topping in toppings : 
        print(topping)

make_pizza_better('pepperoni')
make_pizza_better('pepperoni', 'mushrooms', 'green peppers', 'extra cheeze')
