#!/usr/bin/env python3

import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

fname = 'sitka_weather_07-2014.csv'

with open(fname) as f : 
    # create a reader object
    reader = csv.reader(f)
    # create a list holding all max temperature
    dates, highs = [], []

    # skip the header row
    next(reader)

    # csv reader object is iterable from the cursor position
    for row in reader : 
        # each row in csv reader is a list, which is indexable
        high = int(row[1])
        date = dt.strptime(row[0], '%Y-%m-%d')
        highs.append(high)
        dates.append(date)

    # setting the figure parameter
    fig = plt.figure(dpi = 94, figsize=(10,6))
    # setting some other items
    plt.title('Daily high temperature, July 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # modify the figure so the dates are not cluster together
    fig.autofmt_xdate()

    # plot the graph and show
    plt.plot(dates, highs, color='red')
    plt.show()


