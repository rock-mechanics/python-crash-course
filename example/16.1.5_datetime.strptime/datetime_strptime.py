#!/usr/bin/env python3

from datetime import datetime as dt

data = '2021-8-20'

# %Y matchs 4 digit year
# %m matches month
# %d matches days regardless one digit or two digit
dt_object = dt.strptime(data, '%Y-%m-%d')
print(dt_object)

data = '2021-8-2'
dt_object_01 = dt.strptime(data, '%Y-%m-%d')
print(dt_object_01)


# %y matches two digit year
data = '21-8-2'
dt_object_02 = dt.strptime(data, '%y-%m-%d')
print(dt_object_02)
# they return the same object
print(dt_object_01 == dt_object_02)

# %I indicates hours in 12 hour mode
# %M indicates minutes
data = '21-8-2-11:05'
dt_object_01 = dt.strptime(data, '%y-%m-%d-%I:%M')
print(dt_object_01)

# %H indicates hours in 24 hour mode
data = '21-8-2-11:05'
dt_object_02 = dt.strptime(data, '%y-%m-%d-%H:%M')
print(dt_object_02)

# they return the same object if the hours is less than 12
print(dt_object_01 == dt_object_02)

# %p indicates am or pm

data01 = '21-8-2-13:05'
data02 = '21-8-2-1:05:pm'

dt_object01 = dt.strptime(data01, '%y-%m-%d-%H:%M')
dt_object02 = dt.strptime(data02, '%y-%m-%d-%I:%M:%p')

print(dt_object01)
print(dt_object02)
print(dt_object01 == dt_object02)


# %B indicates month in English 
data01 = '21-8-2-13:05'
data02 = '21-August-2-1:05:pm'

dt_object01 = dt.strptime(data01, '%y-%m-%d-%H:%M')
dt_object02 = dt.strptime(data02, '%y-%B-%d-%I:%M:%p')

print(dt_object01)
print(dt_object02)
print(dt_object01 == dt_object02)

# %b indicates month in English abbreviation 
data01 = '21-8-2-13:05'
data02 = '21-Aug-2-1:05:pm'

dt_object01 = dt.strptime(data01, '%y-%m-%d-%H:%M')
dt_object02 = dt.strptime(data02, '%y-%b-%d-%I:%M:%p')

print(dt_object01)
print(dt_object02)
print(dt_object01 == dt_object02)
