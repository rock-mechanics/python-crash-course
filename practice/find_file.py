#!/usr/bin/env python3

from sys import argv
import os
import re

def search_directory(directory) : 
    for f in os.listdir(directory) : 
        if os.path.isdir(f) : 
            new_dir = os.path.join(directory, f)
            search_directory(new_dir)
        else : 
            if argv[1] in f : 
                print(os.path.join(directory, f))
            
if len(argv) != 2 : 
    print('Usage : {} <file-name-pattern>'.format(argv[0]))
else : 
    current_dir = os.curdir
    search_directory(current_dir)
    

