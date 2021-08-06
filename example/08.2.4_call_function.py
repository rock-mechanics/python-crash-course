#!/usr/bin/env python3

# argument with value is optional, they must be placed after the required arguments. 
# optional argument will disturb the position of the position arugments. thus they must be placed after. 

def describe_pet_cat(pet_name, animal_type = 'cat') : 
    '''
    show info about the pet
    '''
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}.".format(animal_type, pet_name.title()))

# call function using standard way.
describe_pet_cat(pet_name='jon', animal_type = 'cat')
describe_pet_cat(animal_type = 'cat', pet_name='jon')

# omit the optional arugment
describe_pet_cat(pet_name='jon')
describe_pet_cat('jon')

# key-word argument can be used as positional argument ? 
describe_pet_cat('jon', 'cat')

