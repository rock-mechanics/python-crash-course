#!/usr/bin/env python3

alien = { 'color' : 'green' , 'points' : 5 }

print(alien)

# insert new key-value pair to the dictionary
alien['x_position'] = 0
alien['y_position'] = 25

print(alien)

# build an empty dictionary and populate it.
new_alien = {}
new_alien['color'] = 'green'
new_alien['points'] = 5

print(new_alien)

# modify the content of an entry of the dictionary
new_alien['yellow'] = 'yellow'
print(new_alien)

# simulate movement of an alien
alien['speed'] = 'medium'

print("\nlet's move the alien in {} speed".format(alien['speed']))
print("Alien's current position : {}".format(alien['x_position']))

if alien['speed'] == 'slow' : 
    alien['x_position'] += 1
elif alien['speed'] == 'medium' : 
    alien['x_position'] += 2
else : 
    alien['x_position'] += 3
print("Alien's current position : {}".format(alien['x_position']))

alien['speed'] = 'fast'
print("\nlet's move the alien in {} speed".format(alien['speed']))

if alien['speed'] == 'slow' : 
    alien['x_position'] += 1
elif alien['speed'] == 'medium' : 
    alien['x_position'] += 2
else : 
    alien['x_position'] += 3

print("Alien's current position : {}".format(alien['x_position']))

# delete an key-value pair
print()
print(alien)
del( alien['color'] )
print(alien)

