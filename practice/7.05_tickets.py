#!/usr/bin/env python3

age = ''

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
