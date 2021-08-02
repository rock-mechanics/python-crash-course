#!/usr/bin/env python3

import os
import re

pat = r'(\d.\d.\d)\.(.*)'
rep = r'\1_\2'
for f in os.listdir() : 
    if re.match(pat, f) : 
        new_name = re.sub(pat, rep, f)
        os.rename(f, new_name)

