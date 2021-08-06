#!/usr/bin/env python3

f_name = 'alice.txt'

try : 
    with open(f_name, 'r') as f : 
        pass
except FileNotFoundError : 
    print('Sorry, {} does not exist'.format(f_name))
