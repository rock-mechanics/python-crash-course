#!/usr/bin/env python3

current_users = ['admin', 'zs', 'jing', 'tk', 'yld']
new_users = ['andy', 'sam', 'jackie', 'TK', 'yld']

print(current_users)
print(new_users)
print()

current_users = [ user.lower() for user in current_users ]
if new_users : 
    for new_user in new_users : 
        if new_user.lower() in current_users : 
            print("{} has been used, please select a new one".format(new_user))
        else : 
            print("{} is good to use".format(new_user))
else : 
    print("We need to find some new users!")
