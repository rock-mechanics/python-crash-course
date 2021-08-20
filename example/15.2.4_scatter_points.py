import matplotlib.pyplot as pyplot

# draw one point
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

# pass in the x_values and y_values
pyplot.scatter(x_values, y_values, s=200)
pyplot.title('Square Numbers', fontsize=24)
pyplot.xlabel('Values', fontsize=14)
pyplot.ylabel('Square of Values', fontsize=14)

# set scale text
# pyplot.tick_params(axis='both', **kwargs)
pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)
pyplot.show()
