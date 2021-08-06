#!/usr/bin/env python3

from survey import AnonymousSurvey
my_survey =  AnonymousSurvey('what is your fav lang : ')
my_survey.show_question()
print('press "q" at any time to quit.\n')
while True : 
    reply = input('your fav lang : ')
    my_survey.store_response(reply)
    if reply == 'q' : 
        break
print('\nThank you everyone who participated in the survey!')
my_survey.show_results()
