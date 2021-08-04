#!/usr/bin/env python3

class User() : 
    def __init__(self, first, last, **params): 
        self.first_name = first
        self.last_name = last
        self.info = params
    def describe_user(self): 
        print('{} {}'.format(self.first_name.title(), self.last_name.title()))
        for key, value in self.info.items() : 
            print('\t{} : {}'.format(key, value))
    def greet_user(self): 
        print('hi, {}'.format(self.first_name.title()))

kobe = User('kobe', 'bryant', hobby='basketball', favorite_food='pizza', number_of_children=3)
lebron = User('lebron', 'james', height='2.1', weight='100', number_of_rings=4)

kobe.greet_user()
kobe.describe_user()

lebron.greet_user()
lebron.describe_user()
