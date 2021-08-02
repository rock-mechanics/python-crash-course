#!/usr/bin/env python3

my_pizzas = ['pepperoni', 'cheeze', 'beef']
friend_pizzas = my_pizzas[:]

my_pizzas.append('chilli')
friend_pizzas.append('hawai')

print("My favorite pizzas are : ")
for pizza in my_pizzas : 
    print(pizza)
print("My friend's favorite pizzas are : ")
for pizza in friend_pizzas : 
    print(pizza)

