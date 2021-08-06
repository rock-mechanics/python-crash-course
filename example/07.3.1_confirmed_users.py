#!/usr/bin/env python3

unconfirmed_user = ['alice', 'brian', 'candace']
confirmed_user = []

while unconfirmed_user: 
    current_user = unconfirmed_user.pop()
    print("Verify user : {}".format(current_user.title()))
    confirmed_user.append(current_user)

print("\nThe following users have been confirmed: ")

for user in confirmed_user : 
    print("\t{}".format(user.title()))

