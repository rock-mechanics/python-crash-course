#!/usr/bin/env python3

magicians = ['david', 'mike', 'eric']

def show_magicians(names) : 
    for name in names : 
        print(name)

def make_great(names) : 
    print(type(enumerate(names)))
    for index, name in enumerate(names) : 
        names[index] = "the Great {}".format(name.title())

make_great(magicians)
show_magicians(magicians)


