#!/usr/bin/env python3

def make_sandwich(*ingredients) : 
    print("To make sandwich, you need to prepare : ")
    for ingredient in ingredients : 
        print(' - {}'.format(ingredient))

make_sandwich('bread', 'ham', 'lettice', 'fried egg')
make_sandwich('flat bread', 'pepperoni')
make_sandwich('whole wheat bread', 'avacado', 'tuna')
