#!/usr/bin/env python3

import greeting_functions

athletes = ['lebron', 'kobe', 'lining']
for athlete in athletes : 
    greeting_functions.greeting_a_person(athlete)

print()
import greeting_functions as gtlib
athletes = ['lebron', 'kobe', 'lining']
for athlete in athletes : 
    gtlib.greeting_a_person(athlete)

print()
from greeting_functions import greeting_a_person
for athlete in athletes : 
    greeting_a_person(athlete)

print()
from greeting_functions import greeting_a_person as g
for athlete in athletes : 
    g(athlete)

print()
from greeting_functions import *
for athlete in athletes : 
    greeting_a_person(athlete)
