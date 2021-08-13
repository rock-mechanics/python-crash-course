#!/usr/bin/env python3

class GameStats() : 
    '''track game progress and status'''
    def __init__(self, settings) : 
        self.settings = settings
        self.reset_stats()
        self.ships_left = self.settings.ship_limit
        self.game_active = True

    def reset_stats(self) : 
        ''' resume all stats to the inital values '''
        self.ships_left = self.settings.ship_limit
