#!/usr/bin/env python3

class Employee() : 
    def __init__(self, last, first, salary) : 
        self.last_name = last
        self.first_name = first
        self.salary = salary
    def give_raise(self, amount = 5000) : 
        self.salary += amount
