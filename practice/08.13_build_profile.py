#!/usr/bin/env python3

def build_profile(first, last, **info) : 
    profile = {}
    profile['first_name'] = first
    profile['last_name' ] = last
    for key, value in info.items() : 
        profile[key] = value
    return profile

print(build_profile('lebron', 'james', sport='basketball', occupation='athelet'))
