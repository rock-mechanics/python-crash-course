#!/usr/bin/env python3

print('please give me two integers, I will add them for you.')

try : 
    num1 = int(input('please input the first number : '))
    num2 = int(input('please input the second number : '))
except ValueError : 
    print('please input numbers only .')
else : 
    print('the sum of the two numbers is {}. '.format(num1 + num2))
