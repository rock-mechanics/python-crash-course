#!/usr/bin/env python3

person01 = {}
person01['first_name'] = 'lebron'
person01['last_name'] = 'james'
person01['age'] = 35
person01['city'] = 'LA'

person02 = {}
person02['first_name'] = 'kobe'
person02['last_name'] = 'bryant'
person02['age'] = 40
person02['city'] = 'LA'

person03 = {}
person03['first_name'] = 'nash'
person03['last_name'] = 'steve'
person03['age'] = 40
person03['city'] = 'LA'

people = [person01, person02, person03]

for person in people : 
    print(person)
