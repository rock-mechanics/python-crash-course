#!/usr/bin/env python3

number = input("Please enter a number, I will tell you it's even or odd : ")
number = int(number)

if number % 2 == 0 : 
    print("The number {} is even.".format(number))
else : 
    print("The number {} is odd.".format(number))
