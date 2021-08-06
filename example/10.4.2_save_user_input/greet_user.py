#!/usr/bin/env python3

import json

fname = 'username.json'

with open(fname) as f : 
    user_name = json.load(f)

print('Welcome back, {}!'.format(user_name))
