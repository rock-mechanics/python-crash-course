#!/usr/bin/env python3

import json

fname = 'username.json'

def get_new_user_name() : 
    '''get and return an new user name from user'''
    user_name = input('what is your name : ')
    return user_name
def save_user_name(user_name):
    '''save the username to a file'''
    with open(fname, 'w') as f : 
        json.dump(user_name, f)
        print('we will remember you when you come back.')
def greet_user(user_name):
    '''print a personal message for the user'''
    print('Welcome back, {}!'.format(user_name.title()))
def read_saved_user():
    '''read user from the file'''
    try : 
        with open(fname) as f : 
            user_name = json.load(f)
    except : 
        return None
    else : 
        return user_name
def validate_user(): 
    '''return True if the user confirms the username'''
    yes_or_no = input('is the username correct ? (yes/no) : ')
    return yes_or_no.lower().strip() == 'yes'

username = read_saved_user()
if username : 
    greet_user(username)
    if validate_user() : 
        pass
    else :
        username = get_new_user_name()
        save_user_name(username)
else : 
    username = get_new_user_name()
    save_user_name(username)
