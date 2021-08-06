#!/usr/bin/env python3

import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase) : 
    def test_single_reply(self):
        my_survey = AnonymousSurvey("What's your fav lang : ")
        my_survey.store_response('java')
        self.assertIn('java', my_survey.responses)
    def test_three_reply(self):
        my_survey = AnonymousSurvey("What's your fav lang : ")
        replies = ['java', 'c', 'go']
        for reply in replies : 
            my_survey.store_response(reply)
        for reply in replies : 
            self.assertIn(reply, my_survey.responses)

unittest.main()
