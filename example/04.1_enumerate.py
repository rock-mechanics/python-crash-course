#!/usr/bin/env python3

names = ['alice', 'david', 'brian']

for name in names : 
    print(name)

print()

for name in names : 
    print("{}, that was a great trick!".format(name.title()))
    print("I cannot wait to see your next trick, {}".format(name.title()))

print("Thank you, everyone. That was a great magic show!")
