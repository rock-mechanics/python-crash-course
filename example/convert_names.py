#!/usr/bin/env python3

import os
import re

# if a file using d.d.d.name format, change it to d.d.d_name format
pat = r'(\d.\d.\d)\.(.*)'
rep = r'\1_\2'
for f in os.listdir() : 
    if re.match(pat, f) : 
        new_name = re.sub(pat, rep, f)
        os.rename(f, new_name)

# if file starts with a number and a dot, append a zero in front of it.
pat = r'^(\d\..*)'
rep = r'0\1'
for f in os.listdir() : 
    if re.match(pat, f) : 
        new_name = re.sub(pat, rep, f)
        os.rename(f, new_name)

# if file is directory, remove the .py extension
pat = r'^(.*)\.py'
rep = r'\1'
for f in os.listdir() : 
    if os.path.isdir(f) : 
        if re.match(pat, f): 
            new_name = re.sub(pat, rep, f)
            os.rename(f, new_name)
            

