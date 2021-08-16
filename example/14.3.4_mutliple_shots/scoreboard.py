#!/usr/bin/env python3

import pygame.font

class ScoreBoard() : 
    ''' a class display number of scores in the game '''
    def __init__(self, settings, screen, stats) : 
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.text_color = (30,30,30)
        # create a font object which can be rendered to image later
        self.font = pygame.font.SysFont(None, 48)

        # convert score to image
        self.convert_score()

    def convert_score(self) : 
        '''convert score to image, this function is called when score is changed '''
        score_str = str( self.stats.score )
        self.image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.image_rect = self.image.get_rect()
        # leave 20 px margin on the right side and top
        self.image_rect.right = self.screen.get_rect().right - 20
        self.image_rect.top = 20

    def show_score(self) : 
        '''draw the score on the screen'''
        self.screen.blit(self.image, self.image_rect)

