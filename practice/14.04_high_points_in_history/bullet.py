#!/usr/bin/env python3

import pygame

from pygame.sprite import Sprite
# Sprite is a class that organise multiple elements of the same type

class Bullet(Sprite) : 
    def __init__(self, settings, ship)  : 
        # settings give us the bullet size
        # ship gives us the bullet position

        # create a sprite object
        super() .__init__()
        # pygame.Rect creates a rect by providing coordinates of two points
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)

        # allign the bullet rectangle
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # rect is measured by pixels, to make it more precise, we need to convert it to float
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self) : 
        ''' update bullet position '''
        # change the y value in floats
        self.y -= self.speed_factor
        # resave the y value in ints
        self.rect.y = self.y

    def draw_bullet(self, screen) : 
        ''' draw it on the screen '''
        # rect is not an img object.
        # pygame.draw.rect convrets the data sturcture to a visual representation
        pygame.draw.rect(screen, self.color, self.rect)

