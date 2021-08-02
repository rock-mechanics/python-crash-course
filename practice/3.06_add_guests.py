#!/usr/bin/env python3

guests = ['lebron', 'kobe', 'yao']

print(guests[0] + " is invited to the dinner");
print(guests[1] + " is invited to the dinner");
print(guests[2] + " is invited to the dinner");

print()
print(guests[1] + " cannot attend the dinner")

guests[1] = "o'neal"
print()
print(guests[0] + " is invited to the dinner");
print(guests[1] + " is invited to the dinner");
print(guests[2] + " is invited to the dinner");


print()
guests.insert(0, 'nash')
guests.insert(2, 'carter')
guests.append('jordan')


print(guests[0] + " is invited to the dinner");
print(guests[1] + " is invited to the dinner");
print(guests[2] + " is invited to the dinner");
print(guests[3] + " is invited to the dinner");
print(guests[4] + " is invited to the dinner");
print(guests[5] + " is invited to the dinner");
