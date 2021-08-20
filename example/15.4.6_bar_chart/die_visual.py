from die import Die
import pygal

die = Die()

results = []

# throw the die 1000 times
for i in range(1000) : 
    result = die.roll()
    results.append(result)

# analyse the result
freqencies = []

for value in range(1,die.num_sides + 1) : 
    # count number of occurance in a list
    counts = results.count(value)
    freqencies.append(counts)

# create a bar chart
chart = pygal.Bar()
# setting the title
chart.title = 'Rolling Die 1000 time'
chart.x_title = 'Result'
chart.y_title = 'Number of Occurence'
chart.x_labels = ['1', '2', '3', '4', '5', '6']

# add data 
# one segment may contain multiple categories.
# for example, one month may contain sales data of different products
# we need to specify the category for the data
chart.add('D6', freqencies)
chart.render_to_file('die_visual.svg')
