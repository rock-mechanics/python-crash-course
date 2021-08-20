#!/usr/bin/env python3

import json
import pygal

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

# set up the diagram
chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
chart.title = 'Closing Price'
chart.x_labels = dates

# the major label is every 20 days
chart.x_labels_major = dates[::20]

# add the data, label it properly.
chart.add('BTC Closing Price', closes)

chart.render_to_file('BTC_closing_price.svg')
