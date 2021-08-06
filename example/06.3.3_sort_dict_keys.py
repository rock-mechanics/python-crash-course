#!/usr/bin/env python3

fav_langs = {
    'jen' : 'python',
    'sarah' : 'python',
    'edward' : 'python',
    'phil' : 'python',
    }

print(type(sorted(fav_langs.keys())))
for name in sorted(fav_langs.keys()) : 
    print("{}, thank you for taking the poll!".format(name.title()))
