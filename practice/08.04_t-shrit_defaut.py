#!/usr/bin/env python3

def make_shirts(size = 'L', msg = 'I love Python') : 
    print("making t-shirt with size {}. printed text will be '{}'.".format(size, msg))

# no arguments, it will use default value
make_shirts()

# pass one positional argument
make_shirts('M')

# using key-word argument
make_shirts(msg='I love Linux operating system.')

