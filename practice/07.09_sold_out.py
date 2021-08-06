#!/usr/bin/env python3

sandwich_orders = ['tuna', 'ham','pastrami', 'veggie', 'egg', 'avocado', 'pastrami', 'pastrami']

finished_sandwiches = []

print("\nincoming orders : \n{}".format(sandwich_orders))

# define the sold-out items.
sold_out = 'pastrami'
print("\n{} sandwiches are sold out.\n".format(sold_out))

# remove the sold-out item from the order list.
while sold_out in sandwich_orders : 
    sandwich_orders.remove(sold_out)

# make the order list.
while sandwich_orders : 
    order = sandwich_orders.pop()
    print("I made your {} sandwich".format(order))
    finished_sandwiches.append(order)

# print a summary about all the orders.
print("\nAll sandwiches are made, they are ")
for order in finished_sandwiches : 
    print("\t{}".format(order))

