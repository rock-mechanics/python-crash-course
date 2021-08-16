#!/usr/bin/env python3

class GameStats() : 
    '''track game progress and status'''
    def __init__(self, settings) : 
        self.settings = settings
        self.reset_stats()
        # high score is static.
        # load high score from a file
        try : 
            with open('high_score.txt') as f :
                score_string = f.read()
                self.high_score = int(score_string)
        except : 
            self.high_score = 0

    def reset_stats(self) : 
        ''' resume all stats to the inital values '''
        self.ships_left = self.settings.ship_limit
        self.game_active = False
        self.score = 0
        self.level = 1
