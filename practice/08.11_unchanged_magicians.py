#!/usr/bin/env python3

magicians = ['david', 'mike', 'eric']

def show_magicians(names) : 
    for name in names : 
        print(name)

def make_great(names) : 
    great_names = []
    for name in names : 
        great_names.append("the Great {}".format(name.title()))
    return great_names

show_magicians(make_great(magicians))
show_magicians(magicians)


