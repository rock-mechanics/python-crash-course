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

class Admin(User) : 
    def __init__(self, first , last,  **params): 
        # user provide a argument sequence.
        # **params match the sequence and pack them into params
        # to call the method __init__ in super class, we need to provided the sequences
        super().__init__(first, last, **params)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self) : 
        print('You have the following privileges : ')
        for p in self.privileges: 
            print(" - {}".format(p))

kobe = Admin('kobe', 'bryant', hobby='basketball', height=210)
kobe.describe_user()
kobe.show_privileges()
            
