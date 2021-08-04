#!/usr/bin/env python3
'''
This program counts from 1 to 5
'''
current_number = 0

while current_number < 10 : 
    current_number += 1
    if current_number % 2 == 0 : 
        continue
    else :
        print(current_number)
