#!/usr/bin/env python3

import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

fname = 'sitka_weather_2014.csv'

with open(fname) as f : 
    # create a reader object
    reader = csv.reader(f)
    # create a list holding all max temperature
    dates, highs, lows, diffs = [], [] , [], []

    # skip the header row
    next(reader)

    # csv reader object is iterable from the cursor position
    for row in reader : 
        # each row in csv reader is a list, which is indexable
        high = int(row[1])
        low = int(row[3])
        date = dt.strptime(row[0], '%Y-%m-%d')
        highs.append(high)
        dates.append(date)
        lows.append(low)
        diffs.append(high - low)


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
    plt.plot(dates, lows, color='blue')

    # alpha is the transparency factor
    # facecolor is the filling color for the surface
    # x coordinates is dates
    # y coordinates takes two argument list
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.plot(dates, diffs, color='yellow')
    plt.show()

