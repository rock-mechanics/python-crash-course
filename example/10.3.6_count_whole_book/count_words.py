#!/usr/bin/env python3

book = 'alice.txt'
try : 
    with open(book) as f : 
        content = f.read()
except FileNotFoundError : 
    print('{} is not found.'.format(book))
else : 
    words = content.split()
    print(words[:20])
    counts = len(words)
    print('The file {} has {} words in it'.format(book, counts))
    
