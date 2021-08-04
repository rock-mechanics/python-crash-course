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

my_dog = Dog('willie', 6)
print('I have a dog, his name is {}'.format(my_dog.name.title()))
print('He is {} years old'.format(my_dog.age))

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print('I have a dog, his name is {}'.format(your_dog.name.title()))
print('He is {} years old'.format(your_dog.age))

your_dog.sit()
your_dog.roll_over()
