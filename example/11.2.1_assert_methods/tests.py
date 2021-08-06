#!/usr/bin/env python3

import unittest
from functions import *

class TestFunctions(unittest.TestCase): 
    def testtrue(self):
        output = booltesttrue()
        self.assertTrue(output)
    def testfalse(self):
        output = booltestfalse()
        self.assertFalse(output)
    def test_equal(self):
        output = 10
        expect = 10
        self.assertEqual(output, expect)
    def test_not_equal(self):
        output = 11
        expect = 10
        self.assertNotEqual(output, expect)
    def test_range_in(self):
        output = range_10()
        expect = 2
        self.assertIn(expect, output)
    def test_range_not_in(self):
        output = range_10()
        expect = 10
        self.assertNotIn(expect, output)

unittest.main()
