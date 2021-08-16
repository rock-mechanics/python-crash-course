#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite

class Alien(Sprite) : 
    def __init__(self, settings, screen) : 
        '''initialize the alien'''
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.img = pygame.image.load('images/alien.bmp')
        self.rect = self.img.get_rect()
        # position the rect
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self) : 
        self.screen.blit(self.img, self.rect)
