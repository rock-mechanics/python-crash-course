#!/usr/bin/env python3

import json
fname = 'numbers'

with open( fname ) as f : 
    numbers = json.load(f)

for number in numbers : 
    print(number)
