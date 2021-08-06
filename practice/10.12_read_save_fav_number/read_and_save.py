#!/usr/bin/env python3

import json

fname = 'fav_number.json'
def read_fav_number() : 
    '''try to read saved fav number from the file'''
    try : 
        with open(fname) as f : 
            number = json.load(f)
    except FileNotFoundError : 
        return None
    else : 
        return number

def get_fav_number() : 
    '''get fav number from user'''
    try : 
        number = input('what is your fav number : ')
        number = int(number)
        return number
    except : 
        return None

def save_fav_number(number) : 
    '''save fav number to the file'''
    with open(fname, 'w') as f :
        json.dump(number, f)

fav_number = read_fav_number()
if fav_number : 
    print('I know your fav number is {} .'.format(fav_number))
else : 
    fav_number = get_fav_number() 
    save_fav_number(fav_number)
    print('I will remember your fav number')
    
