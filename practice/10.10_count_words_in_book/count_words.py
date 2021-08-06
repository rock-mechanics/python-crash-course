#!/usr/bin/env python3

fname = 'alice.txt'
check = 'the'

with open(fname) as f : 
    content = f.read().lower()

print('{} has appeared {} times.'.format(check, content.count(check)))
