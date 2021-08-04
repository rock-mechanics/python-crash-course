#!/usr/bin/env python3

def print_design(unprinted_designs , completed_designs) : 
    while unprinted_designs : 
        current_design = unprinted_designs.pop()
        print("Printing model : " + current_design)
        completed_designs.append(current_design)
def summary_completed(completed_designs) : 
    print('The following designs have been printed : ')
    for design in completed_designs : 
        print(design)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs = []

print_design(unprinted_designs, completed_designs)
summary_completed(completed_designs)


