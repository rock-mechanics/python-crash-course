#!/usr/bin/env python3

import pygame

class Ship() : 
    def __init__(self, screen, settings) : 
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ship.bmp')
        # the default rectange is the rectangle with the image size position 0,0 probabally.
        # we will not stretch the image, so our rectange size will the same as the image
        # rectange object contains the positon info of element.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # set our rectangle
        # keeps a float number in the centerx
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        # movement flag to know whether ship is moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update ship's position based on flag values'''
        if self.moving_right : 
            self.rect.centerx += self.settings.ship_speed_factor
        # we cannot use elif here, because they moving_left and moving_right can be both true.
        if self.moving_left : 
            self.rect.centerx -= self.settings.ship_speed_factor
        
    def blitme(self):
        # place the image into the rectangle
        self.screen.blit(self.image, self.rect)
