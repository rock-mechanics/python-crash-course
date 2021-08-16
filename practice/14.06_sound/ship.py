#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite

# play the sound as the program runs
import threading

class Ship(Sprite) : 
    def __init__(self, screen, settings) : 
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ship.bmp')
        # the default rectange is the rectangle with the image size position 0,0 probabally.
        # we will not stretch the image, so our rectange size will the same as the image
        # rectange object contains the positon info of element.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # set our rectangle
        # keeps a float number in the record
        self.x = float(self.screen_rect.centerx)

        # assign the floats to an int.
        self.rect.centerx = self.x 
        self.rect.bottom = self.screen_rect.bottom

        # movement flag to know whether ship is moving
        self.moving_right = False
        self.moving_left = False

        # inialize the sound
        pygame.mixer.init()

    def play_sound(self) : 
        ''' play the sound '''
        pygame.mixer.music.load('sounds/shoot.mp3')
        pygame.mixer.music.play()
        while(pygame.mixer.music.get_busy()) : 
            pass
    def fire_sound(self) : 
        threading.Thread(target=self.play_sound, daemon=True).start()

    def update(self):
        '''update ship's position based on flag values'''
        if self.moving_right and self.rect.right < self.screen_rect.right : 
            self.x += self.settings.ship_speed_factor
        # we cannot use elif here, because they moving_left and moving_right can be both true.
        if self.moving_left and self.rect.left > self.screen_rect.left : 
            self.x -= self.settings.ship_speed_factor
        # update rectangle.
        self.rect.centerx = self.x
        
    def blitme(self):
        # place the image into the rectangle
        self.screen.blit(self.image, self.rect)
    def center_ship(self) : 
        self.rect.centerx = self.screen_rect.centerx
