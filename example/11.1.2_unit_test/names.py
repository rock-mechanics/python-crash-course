#!/usr/bin/env python3

from name_function import get_formatted_name

print('Enter "q" at any time to quit.')

while True : 
    first = input('Please give me your first name : ')
    if first == 'q' : 
        break
    last = input('Please give me your last name : ')
    if last == 'q' : 
        break
    full_name = get_formatted_name(first, last)
    print('Neatly formated name is {}.\n'.format(full_name))
