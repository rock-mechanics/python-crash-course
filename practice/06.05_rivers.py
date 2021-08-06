#!/usr/bin/env python3

rivers = {}
rivers ['nile'] = 'egypt'
rivers ['yellow river'] = 'china'
rivers ['missisipi'] = 'usa'

for river, country in rivers.items() : 
    print("The {} runs through {}.".format(river.title(), country.title()))

print("\nFollowing rivers are mentioned : ")
for river in rivers.keys() : 
    print("\t" + river)

print("\nFollowing countries are mentioned : ")
for country in rivers.values() : 
    print("\t" + country)

