#!/usr/bin/env python3

fav_langs = {
    'jen' : 'python',
    'sarah' : 'c', 
    'edward' : 'ruby', 
    'phil' : 'python'
    }

invited = ['jen', 'phil', 'jackie', 'jeffery']

for person in invited : 
    if person in fav_langs.keys() : 
        print("Thank you for participating {}!".format(person.title()))
    else : 
        print("You are invited to participate our poll, {}.".format(person.title()))
