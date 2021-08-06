#!/usr/bin/env python3

msg = 'Tell me something, I will repeat it back to you : '
msg += '\nEnter "quit" to terminate the program : '

response = ""
while response != "quit" : 
    response = input(msg)
    if response != 'quit' : 
        print(response)
