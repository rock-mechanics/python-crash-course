#!/usr/bin/env python3

def greet_users(users) : 
    ''' 
    pass info to every user in the user list
    '''

    for user in users : 
        msg = 'Hello, {}!'.format(user.title())
        print(msg)

users = ['hannah', 'ty', 'margot']
greet_users(users)
