#!/usr/bin/env python3

name = input ("Please enter your name : ")
print("Hello, {}!".format(name))

msg = 'If you tell us who you are, we can personalize the message you see.'
msg += '\nWhat is your first name? '

first_name = input(msg)

print("\nHello, " + first_name)
