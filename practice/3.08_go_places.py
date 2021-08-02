#!/usr/bin/env python3

places = ['tokyo', 'osaka', 'beijing', 'chengdu', 'shanghai']

print(places)

places_sorted = sorted(places)

print("original places")
print(places)

print("sorted places")
print(places_sorted)

places_reversed = sorted(places, reverse=True)
print("original places")

print(places)
print("reversed sorted places")
print(places_reversed)


print("original places")
print(places)

places.reverse()
print("original places")
print(places)

places.sort()
print("original places")
print(places)

places.sort(reverse=True)
print("original places")
print(places)
