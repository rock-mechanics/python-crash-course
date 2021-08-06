#!/usr/bin/env python3
import re
with open('pi_million_digits.txt') as file_object : 
    lines = file_object.readlines()

pi = ''

for line in lines : 
    pi += line.strip()

birthday = input('please enter your birthday : in the form of ddmmyy : ')

pattern = '^\d{6}$'

if re.match(pattern, birthday) : 
    if birthday in pi : 
        print('Your birthday appears in the first million digits of pi')
    else : 
        print('Your birthday doesn not appears in the first million digits of pi')
else : 
    print('your input is not in the correct format')

