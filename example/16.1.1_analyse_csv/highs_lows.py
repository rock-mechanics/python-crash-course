#!/usr/bin/env python3

import csv

fname = 'sitka_weather_07-2014.csv'

with open(fname) as f : 
	# create a reader object
	reader = csv.reader(f)
	# next function calls reader.__next__, which returns a line and move the pointer to the next line
	header_row = next(reader)
	print(header_row)
