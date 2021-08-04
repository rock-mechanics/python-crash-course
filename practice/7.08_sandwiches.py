#!/usr/bin/env python3

sandwich_orders = ['tuna', 'ham', 'veggie', 'egg', 'avocado']

finished_sandwiches = []

while sandwich_orders : 
    order = sandwich_orders.pop()
    print("I made your {} sandwich".format(order))
    finished_sandwiches.append(order)

print("\nAll sandwiches are made, they are ")
for order in finished_sandwiches : 
    print("\t{}".format(order))

