#!/usr/bin/env python3

try : 
    print(5/0)
    # when python runs into problem, it creates an instance of the excption class. this instance will be passed to the code. 
    # if it is handled, the code will run normally. otherwise the intepreter will stop working.
except ZeroDivisionError: 
    print('you cannot divide by zero, bro!')
