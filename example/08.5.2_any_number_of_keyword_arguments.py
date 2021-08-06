#!/usr/bin/env python3

def build_profile(first, last, **info): 
    print(type(info))
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key,value in info.items() :
        if key not in profile.keys() : 
            profile[key] = value

    return profile

user = build_profile('albert', 'einstein', location = 'princeton', fields = 'physics')

print(user)

