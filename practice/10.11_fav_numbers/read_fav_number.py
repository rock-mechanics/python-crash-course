#!/usr/bin/env python3

import json

fname = 'fav_number.json'
try : 
    with open(fname) as f : 
        number = json.load(f)
        print('I know your fav number is {} .'.format(number))
except FileNotFoundError : 
    print('You need to save your fav number first.')
