#!/usr/bin/env python3

bikes = ['honda', 'yamaha', 'suzuki']

print(bikes)
print()

print("modfiy one of the elements")
bikes[0] = 'ducati'
print(bikes)

print()
print("insert elemetn at the end of the list")
bikes.append('honda')
print(bikes)

print()
print("insert element at any given position")
bikes.insert(0,'chinabike')
print(bikes)
bikes.insert(2,'japanbike')
print(bikes)

print()
print("using pop to del the last element and get the element at the same time")
last_bike = bikes.pop()
print(bikes)
print(last_bike)

print()
print("using pop to del the any element and get the element at the same time")
last_bike = bikes.pop(3)
print(bikes)
print(last_bike)

print()
print("using remove to delete the first value in the list.")
bikes.append('japanbike')
print(bikes)
bikes.remove('japanbike')
print(bikes)
bikes.remove('japanbike')
print(bikes)
# let's try to remove the item again, now it is not in the list any more. you will get a ValueError
# bikes.remove('japanbike')
