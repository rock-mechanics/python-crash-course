#!/usr/bin/env python3

import json

fname = 'username.json'

try : 
    with open(fname) as f : 
        user_name = json.load(f)
        print('Welcome back, {}!'.format(user_name))
except : 
    user_name = input('what is your name : ')
    with open(fname, 'w') as f : 
        json.dump(user_name, f)
        print('we will remember you when you come back.')

