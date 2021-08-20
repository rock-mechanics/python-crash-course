#!/usr/bin/env python3

import json
import pygal
import math
from itertools import groupby

filename = 'btc_close_2017.json'

with open(filename) as f : 
    # load json into a data structure, this gives us a list
    btc_data = json.load(f)

    dates, months, weeks, weekdays, closes = [], [], [], [], []

    for btc_dict in btc_data : 
        date = btc_dict['date']
        month = btc_dict['month']
        week = btc_dict['week']
        weekday = btc_dict['weekday']
        # python cannot convert float string to int
        close = int(float(btc_dict['close']))

        # put data into sperate lists
        dates.append(date)
        months.append(month)
        weeks.append(week)
        weekdays.append(weekday)
        closes.append(close)

# getting the index of the date, we will get all values before the index
# first 49 of the week
index_week = dates.index('2017-12-11')

# slice the data, so we only extract data before the time
week_data = weeks[1:index_week]
price_data = closes[1:index_week]

pair_list = zip(week_data, price_data)

# by default, it sorts the tuple list based on the first value of the tuple, and return a copy of the list.
sorted_pair_list = sorted(pair_list, key=lambda x : int(x[0]))

# prepare empty list for every week and every week-mean-price
included_weeks, calculated_means = [] , []

# lambda x : x[0] is a funcion, it will apply to every element. save the element to x and return x[0]
# this turns the tuple list to [key, tuples_having_the_key] list
for week, tuples in groupby(sorted_pair_list, key=lambda x : x[0]) : 
    # tuples is a list of (week, price) pair
    # use list comprehension to build to a list containing all the daily prices for this week
    prices_for_the_week = [p for w,p in tuples]
    mean_for_the_week = sum(prices_for_the_week) / len(prices_for_the_week)
    # the list should containing a list of a list
    included_weeks.append(week)
    calculated_means.append(mean_for_the_week)

chart = pygal.Line()
chart.title = 'weekly mean price'
chart.x_labels = included_weeks
chart.add('weekly mean', calculated_means)

chart.render_to_file('first_49_weeks_weekly_mean.svg')
