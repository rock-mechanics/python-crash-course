#!/usr/bin/env python3

while True :
    name = input("Please enter your name [ press 'q' to quit ] : ")

    if name == 'q' : 
        break
    with open('guests.txt', 'a') as f : 
        f.write(name + '\n')


