#!/usr/bin/env python3

from random import choice
import pygal
import sys
import os

def show_usage() : 
    print('Usage ./{} <integer>'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if len(sys.argv) != 2 : 
    show_usage()
try : 
    tries = int(sys.argv[1])
except : 
    show_usage() 

# the program
class Die() : 
    def __init__(self, sides = 6) : 
        self.sides = sides
    def roll(self) : 
        return choice(list(range(1,self.sides + 1)))

def min_value(*args) : 
    return len(args)
die1 = Die()
die2 = Die()
die3 = Die()

max_sides = die1.sides + die2.sides + die3.sides
min_sides = min_value(die1, die2, die3)


results = [die1.roll() + die2.roll() + die3.roll() for i in range(tries)]
frequencies = [results.count(value) for value in range(min_sides, max_sides + 1)]

# create a bar chart
bar = pygal.Bar()

bar.title = '{}-die and {}-die for {} times'.format(die1.sides, die2.sides, tries)

# setting the x label
bar.x_labels = [str(i) for i in range(min_sides, max_sides + 1)]
# add the data
bar.add('sum of {} dice'.format(min_sides), frequencies)
bar.render_to_file('result.svg')

