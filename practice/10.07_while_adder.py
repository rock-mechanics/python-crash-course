#!/usr/bin/env python3

print('please give me two integers, I will add them for you.')

while True:
    try : 
        num1 = int(input('please input the first number : '))
        num2 = int(input('please input the second number : '))
    except ValueError : 
        print('please input numbers only, please re-enter the integers.')
        continue
    else : 
        print('the sum of the two numbers is {}. '.format(num1 + num2))
        break
