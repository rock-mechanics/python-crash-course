from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

# throw the die 1000 times
results = [die_1.roll() + die_2.roll() for i in range(1000)]

# analyse the result

freqencies = [results.count(value) for value in range(1,die_1.num_sides + die_2.num_sides + 1)]

# create a bar chart
chart = pygal.Bar()
# setting the title
chart.title = 'Rolling Two Die 1000 time'
chart.x_title = 'Result'
chart.y_title = 'Number of Occurence'
chart.x_labels = [str(i) for i in range(2,die_1.num_sides + die_2.num_sides + 1)]

# add data 
# one segment may contain multiple categories.
# for example, one month may contain sales data of different products
# we need to specify the category for the data
chart.add('D6 + D10', freqencies)
chart.render_to_file('die_visual.svg')
