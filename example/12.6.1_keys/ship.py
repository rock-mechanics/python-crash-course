#!/usr/bin/env python3

import pygame

class Ship() : 
    def __init__(self, screen) : 
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        # the default rectange is the rectangle with the image size position 0,0 probabally.
        # we will not stretch the image, so our rectange size will the same as the image
        # rectange object contains the positon info of element.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # set our rectangle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        # place the image into the rectangle
        self.screen.blit(self.image, self.rect)
