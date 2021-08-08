#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite

class Alien(Sprite) : 
    def __init__(self, settings, screen) : 
        '''initialize the alien'''
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # position the rect
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def draw(self, screen) : 
        '''draw the alien on the screen'''
        self.screen.blit(self.image, self.rect)
