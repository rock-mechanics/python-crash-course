#!/usr/bin/env python3

fav_places = {
                'james' : ['osaka', 'tokyo', 'singapore'] , 
                'cathie': ['chengdu', 'shanghai'] , 
                'sansa' : ['singapore']
                }

for name, places in fav_places.items() : 
    if len(places) == 1 : 
        print("{}'s favorite palce is {}.".format(name.title(), places[0].title()))
    else : 
        print("{}'s favorite palces are : ".format(name.title()))
        for place in places : 
            print("\t{}".format(place.title()))
