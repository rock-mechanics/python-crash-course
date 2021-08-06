#!/usr/bin/env python3

import json
numbers = [1, 3, 5, 7, 9]

fname = 'numbers'

with open(fname, 'w') as f : 
    # dump a data structure into a f object.
    # f object will be saved because of with. otherwise needs to be saved explicitly.
    json.dump(numbers, f)
