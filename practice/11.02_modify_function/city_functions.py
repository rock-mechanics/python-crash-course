#!/usr/bin/env python3

def format_city_country(city, country, population = '') : 
    if population : 
        return '{}, {}'.format(city, country).title() + '-population {}'.format(population)
    else : 
        return '{}, {}'.format(city, country).title()

