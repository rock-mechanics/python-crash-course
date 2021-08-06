#!/usr/bin/env python3


def count_words(book) : 
    try : 
        with open(book) as f : 
            content = f.read()
    except FileNotFoundError : 
        print('{} is not found.'.format(book))
    else : 
        words = content.split()
        counts = len(words)
        print('The file {} has {} words in it'.format(book, counts))
    
books = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']

for book in books : 
    count_words(book)
