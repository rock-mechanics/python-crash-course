#!/usr/bin/env python3

def make_shirts(size, msg) : 
    print("making t-shirt with size {}. printed text will be '{}'.".format(size, msg))

# using positional argument.
make_shirts('m', 'welcome to beijing')

# using key-word argument
make_shirts(msg = "Welcome to tokyo, it's hot here.", size = 'L')
