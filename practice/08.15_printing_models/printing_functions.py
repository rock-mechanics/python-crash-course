#!/usr/bin/env python3

def print_design(unprinted_designs , completed_designs) : 
    '''
    This function clear the unprinted_design and process each of it.
    It will add to the compeleted_designs after process the item.
    '''
    while unprinted_designs : 
        current_design = unprinted_designs.pop()
        print("Printing model : " + current_design)
        completed_designs.append(current_design)

def summary_completed(completed_designs) : 
    '''
    prints a summary of a list
    '''
    print('The following designs have been printed : ')
    for design in completed_designs : 
        print(design)
