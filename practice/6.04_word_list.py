#!/usr/bin/env python3

words = {}
words['mouse'] = 'an animal that runs very fast'
words['cat'] = 'an animal that catches mouse'
words['chicken'] = 'an animal that forgot how to fly'
words['cow'] = 'an animal that produce a lot of milk'
words['person'] = 'an animal that eats all other animals'
words['list'] = 'an python object that is able to be enumerated'
words['tuple'] = 'an python object that is able to be enumerated'
words['set'] = 'an python object that is able to be enumerated'
words['dictionary'] = 'an python object that is able to be enumerated'
words['dict_items'] = 'an python object that is able to be enumerated'


for word , meaning in words.items() : 
    print("{} : ".format(word.title()))
    print("\t{}".format(meaning))
