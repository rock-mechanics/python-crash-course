#!/usr/bin/env python3

def describe_pet(animal_type, pet_name) : 
    '''
    show info about the pet
    '''
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}.".format(animal_type, pet_name.title()))

# there is no need to follow any sequence. 
describe_pet(pet_name='jon', animal_type='cat')
