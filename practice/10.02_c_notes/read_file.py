#!/usr/bin/env python3

with open('learning_python.txt') as f : 
    content = f.read()
    print(content.replace('Python', 'C'), end='')
print()
with open('learning_python.txt') as f : 
    for line in f : 
        print(line.replace('Python', 'C'), end='')
print()
with open('learning_python.txt') as f : 
    lines = f.readlines()
for line in lines : 
    print(line.replace('Python', 'C'), end='')
