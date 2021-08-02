#!/usr/bin/env python3

langs = ['english', 'french', 'japanese', 'mandrin', 'korean']

print(langs)

for i, item in enumerate(langs):
    langs[i] = item.title()
print(langs)

for i, item in enumerate(langs):
    langs[i] = item.upper()
print(langs)

for i, item in enumerate(langs):
    langs[i] = item.lower()
print(langs)

langs.reverse()
print(langs)

langs.sort()
print(langs)

langs.sort(reverse=True)
print(langs)

sort_langs = sorted(langs)
print(langs)
print(sort_langs)
