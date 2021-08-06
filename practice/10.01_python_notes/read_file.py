#!/usr/bin/env python3

with open('learning_python.txt') as f : 
    content = f.read()
    print(content, end='')
print()
with open('learning_python.txt') as f : 
    for line in f : 
        print(line, end='')
print()
with open('learning_python.txt') as f : 
    lines = f.readlines()
for line in lines : 
    print(line, end='')
