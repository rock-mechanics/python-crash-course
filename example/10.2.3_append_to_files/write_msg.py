#!/usr/bin/env python3

fname = 'programming.txt'

with open(fname, 'a') as f : 
    # python can write strings to the file
    f.write('I love finding meanings in large dataset.\n')
    f.write('I love creating creating app that can run in a browser.\n')

