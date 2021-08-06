#!/usr/bin/env python3

print('Give me two numbers, and I will divide them : ')
print('enter "q" to quit')

while True : 
    first_num = input("\nfirst number : ")
    if first_num == 'q' : 
        break
    second_num = input("second number : ")
    if second_num == 'q' : 
        break
    try : 
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError : 
        print('you cannot divide by zero, bro')
    except ValueError : 
        print('please provide two numbers, bro')
    # if until now, no except object is obtained. 
    # run the else block
    else : 
        print('answer is {}.'.format(answer))
