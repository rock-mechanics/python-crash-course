#!/usr/bin/env python3

aliens = []

# construct 30 aliens

for index in range(30) : 
    # construct a totally new alien and assign to the variable.
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# display the first 5 aliens

for alien in aliens[:5] : 
    print(alien)
print("...")
print("Total number of aliens : {}.".format(len(aliens)))

# change the first 3 aliens
for alien in aliens[:3] : 
    if alien['color'] == 'green' : 
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow' : 
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
 

for alien in aliens[:5] : 
    print(alien)
print("...")
print("Total number of aliens : {}.".format(len(aliens)))

# repeat
for alien in aliens[:3] : 
    if alien['color'] == 'green' : 
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow' : 
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
 

for alien in aliens[:5] : 
    print(alien)
print("...")
print("Total number of aliens : {}.".format(len(aliens)))
