#!/usr/bin/env python3

fav_numbers = {}

fav_numbers['kobe'] = [24, 23, 8]
fav_numbers['jordan'] = [23]
fav_numbers['irving'] = [2, 0, 33]
fav_numbers['james'] = [6, 23]
fav_numbers['allen'] = [33, 0, 99]

for name, numbers in fav_numbers.items(): 
    print ("{}'s favorite numbers are {}".format(name, numbers))
