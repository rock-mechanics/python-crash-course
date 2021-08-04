#!/usr/bin/env python3

def get_formatted_name(first_name, middle_name, last_name) : 
    ''' 
    return the whole name
    '''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name_better(first_name, last_name, middle_name = '') : 
    ''' 
    return the whole name
    '''
    if middle_name : 
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else : 
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name_better('john', 'hooker')
print(musician)

musician = get_formatted_name_better('john', 'hooker', 'lee')
print(musician)
