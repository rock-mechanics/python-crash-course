#!/usr/bin/env python3

class Dog() : 
    ''' try to behave like a dog '''
    def __init__(self, name, age) : 
        '''initalize dog with name and age'''
        self.name = name
        self.age = age
    def sit(self) : 
        '''simulate sit'''
        print(self.name.title() + ' is now sitting.') 
    def roll_over(self) : 
        '''simulate roll over'''
        print(self.name.title() + ' rolled over.')


        
