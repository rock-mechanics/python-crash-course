#!/usr/bin/env python3

class Restaurant() : 
    def __init__(self, restaurant_type, restaurant_name) : 
        self.type = restaurant_type
        self.name = restaurant_name
    def describe_restaurant(self) : 
        print('I have a {} restaurant named {}.'.format(self.type, self.name.title()))
    def open_restaurant(self) : 
        print('{} is now open for business'.format(self.name.title()))

class IceCreamStand(Restaurant) : 
    def __init__(self, restaurant_type, restaurant_name) : 
        super().__init__(restaurant_type, restaurant_name)
        self.flavors = []
    def add_flavor(self, flavor) : 
        if flavor not in self.flavors : 
            self.flavors.append(flavor)
    def advertise(self) : 
        print('hi, welcome to {}!'.format(self.name.title()))
        print('we have a lot of nice ice-creams : ')
        for flavor in self.flavors : 
            print(" - {}".format(flavor))

ice_shop = IceCreamStand('ice-cream-shop', 'ice-dreams')
ice_shop.describe_restaurant()
ice_shop.open_restaurant()
ice_shop.add_flavor('vanilla')
ice_shop.add_flavor('peppermint')
ice_shop.add_flavor('sugar')
ice_shop.add_flavor('milk')
ice_shop.add_flavor('chocolate')
ice_shop.advertise()
    
