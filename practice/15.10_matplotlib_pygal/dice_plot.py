import matplotlib.pyplot as plt
from random import choice
class Die() : 
    def __init__(self, sides = 6) : 
        self.sides = sides
    def roll(self) : 
        return choice(list(range(1,self.sides + 1)))

tries = 100000

d1 = Die()
d2 = Die()

results = [d1.roll() + d2.roll() for i in range(tries)]

values = list(range(2, d1.sides + d2.sides + 1))

occurances = [results.count(value) for value in values] 
plt.title('Rolling Two Dice')
plt.xlabel('Values')
plt.ylabel('Occurances')

plt.plot(values, occurances)
plt.show()
