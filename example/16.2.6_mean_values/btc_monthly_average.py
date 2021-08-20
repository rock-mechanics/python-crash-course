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
index_month = dates.index('2017-12-01')

# slice the data, so we only extract data before the time
month_data = months[:index_month]
price_data = closes[:index_month]

# form a (month, daily-price) list, roughly 30 items will have the same 'month' value
pair_list = zip(month_data, price_data)

# by default, it sorts the tuple list based on the first value of the tuple, and return a copy of the list.
sorted_pair_list = sorted(pair_list)

# prepare empty list for every month and every month-mean-price
included_months, calculated_means = [] , []

# lambda x : x[0] is a funcion, it will apply to every element. save the element to x and return x[0]
# this turns the tuple list to [key, tuples_having_the_key] list
for month, tuples in groupby(sorted_pair_list, key=lambda x : x[0]) : 
    # tuples is a list of (month, price) pair
    # use list comprehension to build to a list containing all the daily prices for this month
    prices_for_the_month = [p for m,p in tuples]
    mean_for_the_month = sum(prices_for_the_month) / len(prices_for_the_month)
    # the list should containing a list of a list
    included_months.append(month)
    calculated_means.append(mean_for_the_month)

chart = pygal.Line()
chart.title = 'monthly mean price'
chart.x_labels = included_months
chart.add('monthly mean', calculated_means)

chart.render_to_file('first_11_months_monthly_mean.svg')
