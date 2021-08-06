#!/usr/bin/env python3

import unittest
from city_functions import format_city_country
class TestCityCountry(unittest.TestCase) : 
    '''test the city_functions.py'''
    def test_city_country(self) : 
        ''' test <city, country> formatting'''
        output = format_city_country('santiago', 'chile') 
        expect = 'Santiago, Chile'
        self.assertEqual(output, expect)

unittest.main()
