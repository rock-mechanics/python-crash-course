import matplotlib.pyplot as pyplot

# draw one point
pyplot.scatter(2,4, s=200)
pyplot.title('Square Numbers', fontsize=24)
pyplot.xlabel('Values', fontsize=14)
pyplot.ylabel('Square of Values', fontsize=14)

# set scale text
# pyplot.tick_params(axis='both', **kwargs)
pyplot.tick_params(axis='both', which='major', labelsize=20)
pyplot.tick_params(axis='both', which='minor', labelsize=20)
pyplot.show()
