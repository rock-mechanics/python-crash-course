import matplotlib.pyplot as pyplot

input_values = [1,2,3,4,5]
output_values = [1,4,9,16,25]

# function pyplot.plot takes a few fixed arguments and optional arguments.
# for arguments not in order, we need to specify the keyword 
pyplot.plot(input_values, output_values, linewidth=5)
pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Values", fontsize=14)
pyplot.ylabel("Square of Values", fontsize=14)

# set the scale
# pyplot.tick_params(axis='both', labelsize=14)
pyplot.tick_params(axis='x', labelsize=14)
pyplot.tick_params(axis='y', labelsize=14)
pyplot.show()
