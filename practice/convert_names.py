#!/usr/bin/env python3

import os
import re

pattern = r"([1-9]+)\.([1-9])[_.](.*)"
for f in os.listdir() : 
    if re.match(pattern, f) : 
        new_name = re.sub(pattern, r"\1.0\2_\3", f)
        os.rename(f, new_name)

