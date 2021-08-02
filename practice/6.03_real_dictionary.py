#!/usr/bin/env python3

words = {}
words['mouse'] = 'an animal that runs very fast'
words['cat'] = 'an animal that catches mouse'
words['chicken'] = 'an animal that forgot how to fly'
words['cow'] = 'an animal that produce a lot of milk'
words['person'] = 'an animal that eats all other animals'

word = 'mouse'
print("{} : \n\t{}".format(word, words[word]))
word = 'cat'
print("{} : \n\t{}".format(word, words[word]))
word = 'chicken'
print("{} : \n\t{}".format(word, words[word]))
word = 'cow'
print("{} : \n\t{}".format(word, words[word]))
word = 'person'
print("{} : \n\t{}".format(word, words[word]))
