#!/usr/bin/env python3

import csv
from datetime import datetime as dt
from matplotlib import pyplot as plt

def plot_file(fname, fcolor, label) : 
    dates, highs, lows = [], [], []

    with open(fname) as f : 

        reader = csv.reader(f)
        next(reader)

        for index, line in enumerate(reader, start = 2) : 
            try : 
                date = dt.strptime(line[0], '%Y-%m-%d')
                high = int(line[1])
                low = int(line[3])
            except : 
                print("row {} : invalid data".format(index))
            else : 
                dates.append(date)
                highs.append(high)
                lows.append(low)

    plt.plot(dates, highs, color=fcolor)
    plt.plot(dates, lows, color=fcolor, label = label)
    plt.fill_between(dates, highs, lows, facecolor=fcolor, alpha = 0.1)
    plt.legend()

# setting up the plot
fig = plt.figure(dpi=94, figsize=(10,6))
plt.title('temperature comparison', fontsize=10)

# plot the files
plot_file ('sitka_weather_2014.csv', 'blue', 'sitka')
plot_file ('death_valley_2014.csv', 'red', 'death valley')

# format and show the graph
fig.autofmt_xdate()
plt.show()

