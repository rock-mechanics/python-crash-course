#!/usr/bin/env python3

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheeze']
    }
print("You ordered a {}-crust pizza with the following toppings: ".format(pizza['crust']))
for topping in pizza['toppings'] : 
    print("\t" + topping)

print()
fav_langs = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell']
    }
for name, langs in fav_langs.items() : 
    print("{}'s favorite languages are : ".format(name.title()))
    for lang in langs : 
        print("\t{}".format(lang.title()))

print()
for name, langs in fav_langs.items() : 
    if len(langs) == 1 : 
        print("{}'s favorite languages is {}.".format(name.title(), langs[0].title()))
    else : 
        print("{}'s favorite languages are : ".format(name.title()))
        for lang in langs : 
            print("\t{}".format(lang.title()))
