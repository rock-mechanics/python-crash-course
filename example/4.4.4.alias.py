#!/usr/bin/env python3

my_foods = ['pizza', 'falafel', 'carrot cake']
your_foods = my_foods # both variable points to the same list.

my_foods.append('cannoli')
your_foods.append('ice cream')

print( "my foods are here : " )
print(my_foods)
print( "your foods are here : " )
print(your_foods)
