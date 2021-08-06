#!/usr/bin/env python3

import json

fname = 'username.json'

def get_stored_username() : 
    '''if a user name is stored in the file, get it'''
    try : 
        with open(fname) as f : 
            user_name = json.load(f)
    except FileNotFoundError: 
        return None
    else : 
        return user_name

def greet_user() : 
    '''greet user with user name'''
    user_name = get_stored_username() 
    if user_name: 
        print('Welcome back, {}!'.format(user_name))
    else  :
        user_name = input('what is your name : ')
        save_user(user_name)

def save_user(user_name) : 
    '''save the user once user inputs his username'''
    with open(fname, 'w') as f : 
        json.dump(user_name, f)
        print('we will remember you when you come back.')

greet_user()

