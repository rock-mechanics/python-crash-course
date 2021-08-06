#!/usr/bin/env python3

place_count = {}

while True : 

    place = input("What is your dream place : ")    
    if place not in place_count.keys() : 
        place_count[place] = 1
    else : 
        place_count[place] += 1

    check = input("Would you like to input for another person (yes/no) : ")
    if check.lower() == 'yes' : 
        continue
    else : 
        break

print("\n---Polling Result---\n")

# print all values (sorted by the number of occurance)
# sorted only know how to sort numbers
# key parameter is the device to convert the entity into sortable values. 
# lambda input : output , where input is the value in the original list. output is the value used for sort.

for place in sorted(place_count.keys() , reverse=True , key = lambda x : place_count[x]) : 
    print("{} got {} votes".format(place, place_count[place]))
