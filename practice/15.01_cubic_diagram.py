import matplotlib.pyplot as plt

# set up x values and y values

x_values = list(range(5000))
y_values = [x**3 for x in x_values]

# set the title of the plot
plt.title('Cubic Values', fontsize=15)

# set the axes of the plot
plt.xlabel('Values', fontsize=10)
plt.ylabel('Cubic Values', fontsize=10)

# set the scale
plt.tick_params(axis='both', which='major', labelsize=5)
# draw the plot
plt.scatter(x_values, y_values, color='red', s=20)
plt.show()



