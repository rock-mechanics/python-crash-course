#!/usr/bin/env python3

from sys import argv
import csv
from datetime import datetime as dt
from matplotlib import pyplot as plt

fname = argv[1]

dates, highs, lows = [], [], []

with open(fname) as f : 

    reader = csv.reader(f)
    # skip the header row
    next (reader)

    for line_index, line in enumerate(reader) : 
        str_date = line[0]
        date = dt.strptime(str_date, '%d-%m-%Y')
        temp = float(line[2])

        if date not in dates : 
            # insert and initalize a new record
            dates.append(date)
            highs.append(temp)
            lows.append(temp)
        else : 
            if temp > highs[-1] : 
                highs[-1] = temp
            elif temp < lows[-1]  : 
                lows[-1] = temp

# setting figure parameters
fig = plt.figure(dpi = 94, figsize=(10,6))
plt.title('Temperature in 10 days for Spain city', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature Celcius', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.plot(dates, highs, color='red')
plt.plot(dates, lows, color='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)

fig.autofmt_xdate()

plt.show()



                

