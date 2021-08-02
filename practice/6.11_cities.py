#!/usr/bin/env python3

cities = {}

cities['beijing'] = { 'country' : 'china', 'population' : 10000000, 'facts': 'captical of china in the acient times' }
cities['athens'] = { 'country' : 'greece', 'population' : 5000000, 'facts': 'the birth place of Olympics' }
cities['california'] = { 'country' : 'america', 'population' : 10000000, 'facts': 'the place is where silicon valley located' }

for city in cities.keys() : 
    print(cities[city])

