#!/usr/bin/env python3

fav_langs = {
    'jen' : 'python',
    'sarah' : 'c', 
    'edward' : 'ruby', 
    'phil' : 'python'
    }

print("The following langs are mentioned : ")

for lang in fav_langs.values() : 
    print("\t" + lang)

print("Let's eliminate the dumplicates")

print(type(set(fav_langs.values())))
for lang in set(fav_langs.values()) : 
    print("\t" + lang)
