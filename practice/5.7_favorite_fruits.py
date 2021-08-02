#!/usr/bin/env python3

favorite_fruits = ['apple', 'watermelon', 'pear', 'lychi', 'durian']

fruits_to_check = ['apple', 'pear', 'banana', 'orange']

print(fruits_to_check)

if fruits_to_check[0] in favorite_fruits : 
    print("You really like {}".format(fruits_to_check[0]))
if fruits_to_check[1] in favorite_fruits : 
    print("You really like {}".format(fruits_to_check[1]))
if fruits_to_check[2] in favorite_fruits : 
    print("You really like {}".format(fruits_to_check[2]))
if fruits_to_check[3] in favorite_fruits : 
    print("You really like {}".format(fruits_to_check[3]))
