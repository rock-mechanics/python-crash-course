#!/usr/bin/env python3

from sys import argv
import csv

fname = argv[1]

with open(fname) as f : 
    # create csv reader
    r = csv.reader(f)
    headers = next(r)

    # loop through the headers
    for index, header in enumerate(headers) : 
        print(index, header)

