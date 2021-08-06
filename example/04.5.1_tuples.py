#!/usr/bin/env python3
'''
tuples are immutable
'''

dimensions = (200,50)

print(dimensions)

print(dimensions[0])
print(dimensions[1])


print("\nthe tuple is like nubmers, which is immutable and can be passed around.")
my_pizzas = ('pepperoni', 'chili')
friend_pizzas = my_pizzas

print(my_pizzas)
print(friend_pizzas)

my_pizzas[0] = "error"


