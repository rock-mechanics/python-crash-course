#!/usr/bin/env python3
'''
This program demonstrate different ways to get out of a loop
'''
age = ''

# check condition
while age != 'quit' : 
    age = input("What is your age : ")
    if age != 'quit' : 
        age = int(age)
        if age < 3 : 
            price = 0
        elif age <= 12 : 
            price = 10
        else : 
            price = 15
        print("You ticket price is ${}.".format(price))

# using flags
is_continue = True

while is_continue : 
    age = input("What is your age : ")
    if age != 'quit' : 
        age = int(age)
        if age < 3 : 
            price = 0
        elif age <= 12 : 
            price = 10
        else : 
            price = 15
        print("You ticket price is ${}.".format(price))
    else : 
        is_continue = False
    
# using break

while True : 
    age = input("What is your age : ")
    if age != 'quit' : 
        age = int(age)
        if age < 3 : 
            price = 0
        elif age <= 12 : 
            price = 10
        else : 
            price = 15
        print("You ticket price is ${}.".format(price))
    else : 
        break
