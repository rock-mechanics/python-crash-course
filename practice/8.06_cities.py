#!/usr/bin/env python3

def city_country(city, country) : 
    return '{}, {}'.format(city.title(), country.title())

print(city_country('shanghai', 'china'))
print(city_country('osaka', 'japan'))
print(city_country('singapore', 'singapore'))
