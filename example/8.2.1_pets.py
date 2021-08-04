#!/usr/bin/env python3

def describe_pet(animal_type, pet_name) : 
    '''
    show info about the pet
    '''
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}.".format(animal_type, pet_name.title()))

describe_pet('hamster', 'harry')
describe_pet('cat', 'sansa')
describe_pet('cat', 'jonjon')
describe_pet('cat', 'aray')
