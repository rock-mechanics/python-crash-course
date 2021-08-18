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

        # convert high score
        self.convert_high_score()

        # convert level to image
        self.convert_level()

    def convert_score(self) : 
        '''convert score to image, this function is called when score is changed '''
        # when you assign -1, you are rounded to neareset 10
        rounded_score = round(self.stats.score, -1)
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        # leave 20 px margin on the right side and top
        self.score_image_rect.right = self.screen.get_rect().right - 20
        self.score_image_rect.top = 20

    def convert_high_score(self) : 
        '''convert high_score to high_image, this function is called when high_score is changed '''
        # when you assign -1, you are rounded to neareset 10
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = '{:,}'.format(rounded_high_score)
        self.high_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_image_rect = self.high_image.get_rect()
        # leave 20 px margin on the right side and top
        self.high_image_rect.centerx = self.screen.get_rect().centerx
        self.high_image_rect.top = 20

    def show_score(self) : 
        '''draw the score on the screen'''
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_image, self.high_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)

    def convert_level(self) : 
        '''convert score to image, this function is called when score is changed '''
        # when you assign -1, you are rounded to neareset 10

        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        # put the image below the score with 10 px gap
        self.level_image_rect.right = self.screen.get_rect().right - 20
        self.level_image_rect.top = self.score_image_rect.bottom + 10


