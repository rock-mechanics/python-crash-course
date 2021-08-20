from die import Die

die = Die()

results = []

# throw the die 100 times
for i in range(100) : 
    result = die.roll()
    results.append(result)

print(results)
