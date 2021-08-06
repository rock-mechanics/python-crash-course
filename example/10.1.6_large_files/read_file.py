#!/usr/bin/env python3

with open('pi_million_digits.txt') as file_object : 
    lines = file_object.readlines()

pi = ''

for line in lines : 
    pi += line.strip()

print(pi[:52])
print(len(pi))

