#!/usr/bin/env python3

with open('pi.txt') as file_object : 
    content = file_object.read()
    print(type(content))
    # print will add a newline character at the end of the string
    print(content)
    # customize the ending with 'end' keyword argument
    print(content, end='')
