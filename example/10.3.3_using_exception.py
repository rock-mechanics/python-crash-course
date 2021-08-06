#!/usr/bin/env python3

print('Give me two numbers, and I will divide them : ')
print('enter "q" to quit')

while True : 
    first_num = input("\nfirst number : ")
    if first_num == 'q' : 
        break
    second_num = input("\nsecond number : ")
    if second_num == 'q' : 
        break
    answer = int(first_num) / int(second_num)
    print('answer is {}.'.format(answer))
