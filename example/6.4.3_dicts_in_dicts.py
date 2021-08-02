#!/usr/bin/env python3

users = {
    'aeinstei' :  {
                    'first' : 'albert', 
                    'last' : 'einstein',
                    'location' : 'princeton'
                  } , 

    'mcurie' :    {
                    'first' : 'marie',
                    'last' : 'curie', 
                    'location' : 'paris'
                  }
}

for user_name, user_info in users.items(): 
    print("\nUsername : {}".format(user_name))
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull Name: " + full_name.title())
    print("\tLoation: " + location.title())
