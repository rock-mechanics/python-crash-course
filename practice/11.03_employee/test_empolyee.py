#!/usr/bin/env python3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase) : 
    def setUp(self) : 
        self.employee = Employee('kobe', 'bryant', 1000)
    def test_default_raise(self) : 
        self.employee.give_raise()
        output = self.employee.salary
        expect = 6000
        self.assertEqual(output, expect)
    def test_custom_raise(self) : 
        self.employee.give_raise(9000)
        output = self.employee.salary
        expect = 10000
        self.assertEqual(output, expect)

unittest.main()
