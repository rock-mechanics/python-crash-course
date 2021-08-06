#!/usr/bin/env python3

def describe_city(city, country='china') : 
    print("{} is in {}.".format(city.title(), country.title()))

describe_city('guangzhou')
describe_city('shenzhen')
describe_city('reykjavik', 'iceland')
