#!/usr/bin/env python3

msg = "\nPlease enter the name of a city you have visitied."
msg += "\nEnter 'quit' when you are finished : "

while True : 
    city = input(msg)
    if city == 'quit' : 
        break
    else : 
        print("I'd love to go to {}!".format(city.title()))
