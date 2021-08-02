#!/usr/bin/env python3

car_a = 'bmw'
car_b = 'BMW'
car_c = 'bmw'

print(car_a == car_c)
print(car_a == car_b)
print(car_a.lower() == car_b.lower())
print(car_a != car_b)
print(3==5)

if 3!=5 : 
    print("3 is not equal to 5")
if 3 < 5 and 3 > 1 : 
    print("3 is between 1 and 5")
if 2 == 2 or 2 == 3 : 
    print("for or, one condition is required to be true")

basket = ['apple', 'pear', 'banana']

if 'apple' in basket : 
    print ("I have an apple in the basket")
if 'durian' not in basket : 
    print ("There is no durian in the basket")
    
