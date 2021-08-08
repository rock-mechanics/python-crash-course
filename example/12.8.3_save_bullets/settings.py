#!/usr/bin/env python3

class Settings():
    '''this class stores all the setting for alien invasion'''
    def __init__(self) : 
    ''' all settings values related with alien invasion '''
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60 ,60 ,60


