#!/usr/bin/env python3

msg = 'Please input your selected topping ( type quit to finish ) : '

topping = ""

while topping != 'quit' : 
    topping = input(msg)
    if topping != 'quit' : 
        print("We will add {} to your pizza.".format(topping))
