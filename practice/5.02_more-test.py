#!/usr/bin/env python3

lcar = 'subaru'
ucar = 'Subaru'

print("Is lcar == ucar, I think it is False")
print(lcar == ucar)
print("\nIs lcar != ucar, I think it is True")
print(lcar != ucar)
print("\nIs lcar.lower() == ucar.lower(), I think it is True")
print(lcar.lower() == ucar.lower())
print("\nIs lcar.title() == ucar and lcar.upper() == ucar.upper(), I think it is True")
print(lcar.title() == ucar and lcar.upper() == ucar.upper())
print("\nIs lcar < ucar and lcar.upper() == ucar.upper(), I think it is False")
print(lcar < ucar and lcar.upper() == ucar.upper())
print("\nIs lcar < ucar or lcar.upper() == ucar.upper(), I think it is True")
print(lcar < ucar or lcar.upper() == ucar.upper())

cars = ['honda', 'subaru', 'byd', 'cherry']
print("\nis 'honda' in the list, I think it is True")
print('honda' in cars)

print("\nis 'BMW' not in the list, I think it is True")
print('BMW' not in cars)



