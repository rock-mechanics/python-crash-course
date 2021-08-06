#!/usr/bin/env python3

cars = ['bmw', 'audi', 'toyota', 'byd', 'subaru']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("\nlet's create a new list")
new_list = sorted(cars)
print(new_list)
print("\noriginal list is not changed")
print(cars)

print("\nlet's reverse the new list")
new_list = sorted(cars, reverse=True)
print(new_list)

cars = ['bmw', 'audi', 'toyota', 'byd', 'subaru']
print("\nlet's get back our original list")
print(cars)
print("\nread list from last to the first.")
cars.reverse()
print(cars)

print("the length of the list is {}".format(len(cars)))

