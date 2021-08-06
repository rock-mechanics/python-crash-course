#!/usr/bin/env python3

import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase) : 
    def setUp(self):
        self.survey = AnonymousSurvey("What's your fav lang : ") 
        self.replies = ['java', 'c', 'go']
    def test_single_reply(self):
        ''' 
            input one value
        '''
        self.survey.store_response(self.replies[0])
        self.assertIn(self.replies[0], self.survey.responses)
    def test_three_input(self):
        ''' 
            input three values
        '''
        for reply in self.replies : 
            self.survey.store_response(reply)
        for reply in self.replies : 
            self.assertIn(reply, self.survey.responses)
    def test_interference(self):
        '''
           what the function does to the setup class will be erased once function terminates, 
           so the list becomes empty again
           this ensure all test functions are independent of each other.
        '''
        self.assertEqual([], self.survey.responses)

unittest.main()
