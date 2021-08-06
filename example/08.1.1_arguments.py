#!/usr/bin/env python3

def greet_user( name ) : 
    '''
    This is the doc string or documentation string, which will be displayed when using help(function_name)
    '''
    print('hello, {}!'.format(name.title()))

greet_user("james")
