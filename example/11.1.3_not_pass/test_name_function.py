#!/usr/bin/env python3

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase) : 
    '''test name_function.py'''
    def test_first_last(self) : 
        output = get_formatted_name('janis', 'joplin')
        expect = 'Janis Joplin'
        self.assertEqual(output, expect)

# the main function in unitttest module
# it will grab all TestCase in the current module and run the test function in it.
# the default TestCase class does not have any test function inside.
# we need to define our own test functions.
# the default TestCase class provides useful functions to make our job easy.
unittest.main()
