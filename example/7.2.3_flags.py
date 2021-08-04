#!/usr/bin/env python3

msg = 'Tell me something, I will repeat it back to you : '
msg += '\nEnter "quit" to terminate the program : '

is_active = True #a flag to show the program is still running.
response = ""
while is_active : 
    response = input(msg)
    if response != 'quit' : 
        print(response)
    else : 
        is_active = False
