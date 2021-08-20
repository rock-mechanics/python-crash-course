#!/usr/bin/env python3

import csv
from datetime import datetime as dt
from matplotlib import pyplot as plt

def plot_file(fname, fcolor, label) : 
    dates = []
    rains = []
    with open(fname) as f : 

        reader = csv.reader(f)
        next(reader)

        for index, line in enumerate(reader, start = 2) : 
            try : 
                date = dt.strptime(line[0], '%Y-%m-%d')
                rain = float(line[19])
            except : 
                print("row {} : invalid data".format(index))
            else : 
                dates.append(date)
                rains.append(rain)

    plt.plot(dates, rains, color=fcolor, label = label)
    plt.legend()

# setting up the plot
fig = plt.figure(dpi=94, figsize=(10,6))
plt.title('rainfall comparison', fontsize=10)

# plot the files
plot_file ('sitka_weather_2014.csv', 'blue', 'sitka')
plot_file ('death_valley_2014.csv', 'red', 'death valley')

# format and show the graph
fig.autofmt_xdate()
plt.show()

