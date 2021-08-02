#!/usr/bin/env python3

users = ['admin', 'zs', 'jing', 'tk', 'yld']

for user in users : 
    if user == 'admin' : 
        print("Hello admin, would you like to see a status report?")
    else : 
        print("Hello {}, Thank you for logging in again.".format(user))
