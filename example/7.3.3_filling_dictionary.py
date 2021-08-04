#!/usr/bin/env python3

result = {}

is_continue = True

while is_continue : 
    name = input("\nWhat is your name : ")
    if name in result : 
        print("name is taken, using a different one.")
        continue
    info = input("\nWhat is your message : ")
    result[name] = info
    cont = input("\nWould you like input for another person (yes / no)")
    if cont.lower() == 'yes' : 
        continue
    else : 
        is_continue = False

print("\n---Polling Result---")
for name, msg in result.items() : 
    print("{} would like to say {}.".format(name, msg))
    

