#!/usr/bin/env python3

user = { 'user_name' : 'efermi', 'first' : 'enrico', 'last' : 'fermi' }

# 'items' methods return a list like object
print(type(user.items()))

# each element in the list is a tuple
for item in user.items() : 
    print (type(item))
    break

# we can enumerate the dictionary
for key, value in user.items() : 
    print("\nKey : {}".format(key))
    print("Value : {}".format(value))

fav_langs = {
    'jen' : 'python',
    'sarah' : 'c', 
    'edward' : 'ruby', 
    'phil' : 'python'
    }

print()
for name, lang in fav_langs.items():
    print("{}'s favorite languages is {}.".format(name, lang))

print("\nlet's print all the names only")

print(type(fav_langs.keys()))
for name in fav_langs.keys() :
    print("{} is a nice person".format(name))

my_friends = ['phil', 'sarah']
print("\nlet's print for our friends {} only".format(my_friends))
for my_friend in my_friends : 
    print(my_friend.title())
    print("Hi, {}, I see your favorite language is {}!".format(my_friend, fav_langs[my_friend]))
if 'erin' not in fav_langs.keys() : 
    print("Erin, please take our poll!")
