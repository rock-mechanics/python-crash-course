#!/usr/bin/env python3

from collections import OrderedDict
words = OrderedDict()
words['mouse'] = 'an animal that runs very fast'
words['cat'] = 'an animal that catches mouse'
words['chicken'] = 'an animal that forgot how to fly'
words['cow'] = 'an animal that produce a lot of milk'
words['person'] = 'an animal that eats all other animals'

for key, value in words.items() : 
    print('{} : {}'.format(key, value))
