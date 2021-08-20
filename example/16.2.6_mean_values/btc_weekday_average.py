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
        weeks.append(int(week))
        weekdays.append(weekday)
        closes.append(close)

# getting the index of the date, we will get all values before the index
# first 49 of the week
index_week = dates.index('2017-12-11')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# slice the data, so we only extract data before the time
weekday_data = weekdays[1:index_week]
price_data = closes[1:index_week]

pair_list = zip(weekday_data, price_data)

# we use a different function to sort the data. it based on the index position of the weekday in the list.
# for the lambda function, x is the (weekday, price) pair, based on the integer value of the first item in the days list, we sort the list.
sorted_pair_list = sorted(pair_list, key=lambda x: days.index(x[0]))

# prepare empty list for every week and every week-mean-price
calculated_means = []

# lambda x : x[0] is a funcion, it will apply to every element. save the element to x and return x[0]
# this turns the tuple list to [key, tuples_having_the_key] list
for week, tuples in groupby(sorted_pair_list, key=lambda x : x[0]) : 
    # tuples is a list of (week, price) pair
    # use list comprehension to build to a list containing all the daily prices for this week
    prices_for_the_week = [p for w,p in tuples]
    mean_for_the_week = sum(prices_for_the_week) / len(prices_for_the_week)
    # the list should containing a list of a list
    calculated_means.append(mean_for_the_week)

chart = pygal.Line()
chart.title = 'weekly mean price'
chart.x_labels = days
chart.add('weekly mean', calculated_means)

chart.render_to_file('first_49_weeks_weekdays_mean.svg')
