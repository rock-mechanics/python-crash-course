#!/usr/bin/env python3

import os 
import re

pattern = r'.*\.py$'

def count_file(f) : 
    try : 
        with open(f) as f_obj : 
            return len(f_obj.readlines())
    except : 
        return 0
def count_directory(directory) : 
    dirlines = 0
    for f in os.listdir(directory) : 
        if os.path.isdir(f) : 
            dirlines += count_directory(os.path.join(directory, f))
        elif re.match(pattern, f) : 
            dirlines += count_file(os.path.join(directory, f))
    return dirlines

cwd = os.getcwd()
num_py_lines = count_directory(cwd)
print('You have written {} lines of python code in this directory. great job!'.format(num_py_lines))

        
    
