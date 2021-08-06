#!/usr/bin/env python3

import json

number = input('what is your fav number : ')
f_name = 'fav_number.json'
try : 
    number = int(number)
    with open(f_name, 'w') as f :
        json.dump(number, f)
except : 
    print('please enter a number.')
