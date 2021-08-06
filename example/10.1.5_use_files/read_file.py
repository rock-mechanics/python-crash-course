#!/usr/bin/env python3

with open('pi.txt') as file_object : 
    lines = file_object.readlines()

pi = ''

for line in lines : 
    pi += line.strip()

print(pi)
print(len(pi))

