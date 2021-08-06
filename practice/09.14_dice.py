#!/usr/bin/env python3

from random import randint

class Dice() : 
    def __init__(self, sides = 6) : 
        self.sides = sides
    def roll_dice(self) : 
        print('You got a {}.'.format(randint(1, self.sides)))

dice = Dice()
for i in range(10) : 
    dice.roll_dice()

print()
dice = Dice(10)
for i in range(10) : 
    dice.roll_dice()
        
