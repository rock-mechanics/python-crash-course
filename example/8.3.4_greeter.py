#!/usr/bin/env python3

def get_formatted_name(first_name, last_name) : 
    '''
    return full name
    '''
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True : 
    print('\nPlease tell me your name : ')
    print("Enter 'q' any time to quit")
    f_name = input('First name : ')
    if f_name == 'q' : break
    l_name = input('Last name  : ')
    if l_name == 'q' : break
    full_name = get_formatted_name(f_name, l_name)
    print('Hello, ' + full_name + '!')

