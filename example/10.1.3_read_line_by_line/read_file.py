#!/usr/bin/env python3

with open('pi.txt') as file_object : 
    count = 1
    for line in file_object : 
    # file object is a list-like data structure.
    # which can be enumerated like list.
        print('line {} : {}'.format(count, line), end='')
        count += 1

