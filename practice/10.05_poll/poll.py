#!/usr/bin/env python3

while True : 
    reason = input('Why do you love programming ? [ press "q" to quit ] : ')
    if reason == 'q' : 
        break
    with open('reasons.txt', 'a') as f : 
        f.write(reason + '\n')
