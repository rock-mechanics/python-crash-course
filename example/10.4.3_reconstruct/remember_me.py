#!/usr/bin/env python3

import json

user_name = input('what is your name : ')

fname = 'username.json'

with open(fname, 'w') as f : 
    json.dump(user_name, f)
    print('we will remember you when you come back.')
