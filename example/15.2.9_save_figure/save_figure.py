import matplotlib.pyplot as pyplot

# draw one point
# use list function to convert enumerable to list
x_values = list(range(1,1000))
# use list comprehension to create a new list
y_values = [ x**2 for x in x_values ]

# pass in the x_values and y_values
# assign color to a list of y-values using c keyword, this value will be overwritten by color map function
# use a projection (builtin) to calculate color based on the y value
# pyplot.cm provides a series of function to calcualte color, blues is one of the function focus on various of blue color
pyplot.scatter(x_values, y_values, c=y_values, cmap = pyplot.cm.Blues, edgecolor='none', s=20)

pyplot.title('Square Numbers', fontsize=24)
pyplot.xlabel('Values', fontsize=14)
pyplot.ylabel('Square of Values', fontsize=14)

# setting the range of the axis
# a list containin [ min_x_value, max_x_value, min_y_value, max_y_value ]
pyplot.axis([0,1100,0,1100000])
# set scale text
# pyplot.tick_params(axis='both', **kwargs)
pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)
#pyplot.show()
pyplot.savefig('squares_plot.png')
