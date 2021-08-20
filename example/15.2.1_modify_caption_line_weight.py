import matplotlib.pyplot as pyplot

data = [1,4,9,16,25]
pyplot.plot(data, linewidth=5)
pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Values", fontsize=14)
pyplot.ylabel("Square of Values", fontsize=14)

# set the scale
# pyplot.tick_params(axis='both', labelsize=14)
pyplot.tick_params(axis='x', labelsize=14)
pyplot.show()
