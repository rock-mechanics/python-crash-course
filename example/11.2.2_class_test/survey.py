#!/usr/bin/env python3

class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []
    def show_question(self):
        print(self.question)
    def store_response(self, reply):
        self.responses.append(reply)
    def show_results(self):
        print('Survey Result :')
        for reply in self.responses : 
            print(' - ' + reply)
