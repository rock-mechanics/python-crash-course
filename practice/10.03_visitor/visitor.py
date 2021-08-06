#!/usr/bin/env python3

name = input('Please enter your name : ')

with open('guests.txt', 'a') as f : 
    f.write(name + '\n')

