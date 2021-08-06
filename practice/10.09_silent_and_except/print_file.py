#!/usr/bin/env python3

files = ['dogs.txt', 'cats.txt']

for fname in files : 
    try : 
        with open(fname) as f : 
            print(f.read(), end='')
    except FileNotFoundError : 
        pass


