#!/usr/bin/env python3

class Settings():
    '''this class stores all the setting for alien invasion'''
    def __init__(self) : 
        ''' all settings values related with alien invasion '''
        # static settings, these settings will not change with the progress of the game
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60 ,60 ,60
        self.bullets_allowed = 3

        # alien settings
        self.alien_drop_speed = 10
        # how fast should we upgarde the speed of alien
        self.speed_up_scale = 3
        
        # alien points settings
        self.score_scale = 1.5
        # reset all the dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) : 
        '''reset all dynamic values to original value'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self) : 
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print('one alien is now worth {} points'.format(self.alien_points))
