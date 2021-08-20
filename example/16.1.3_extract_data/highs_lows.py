#!/usr/bin/env python3

import csv

fname = 'sitka_weather_07-2014.csv'

with open(fname) as f : 
    # create a reader object
    reader = csv.reader(f)
    # create a list holding all max temperature
    highs = []

    # skip the header row
    next(reader)

    # csv reader object is iterable from the cursor position
    for row in reader : 
        # each row in csv reader is a list, which is indexable
        high = int(row[1])
        highs.append(high)

    # print all highs
    print(highs)
