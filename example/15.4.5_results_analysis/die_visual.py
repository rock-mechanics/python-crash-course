from die import Die

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

print(freqencies)
