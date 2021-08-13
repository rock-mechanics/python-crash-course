#!/usr/bin/env python3

import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

class Ball(Sprite) : 
    ''' represents the ball class '''

    def __init__(self) : 
        super().__init__()
        self.image = pygame.image.load('ball.bmp')
        self.rect = self.image.get_rect()
    def reset(self, screen_rect) : 
        '''initalize the ball position'''
        self.rect.x = randint(0, screen_rect.width - self.rect.width)
        self.rect.top = screen_rect.top
    def blitme(self, sc) : 
        '''sends the ball to the screen'''
        sc.blit(self.image, self.rect)
    def fall(self, screen_rect) : 
        self.rect.y += 1

class Character(Sprite) : 
    ''' represents the game character '''

    def __init__(self) : 
        super().__init__()
        self.image = pygame.image.load('klee.bmp')
        self.rect = self.image.get_rect()
        self.moving_left = False
        self.moving_right = False

    def blitme(self, sc) : 
        '''sends to the screen'''
        sc.blit(self.image, self.rect)

def update_char(chars, sc_rect) : 
    ''' updates the position of char based on internal moving flags. '''
    for char in chars.sprites() : 
        if char.moving_left and char.rect.left > sc_rect.left: 
            char.rect.x -= 3
        if char.moving_right and char.rect.right < sc_rect.right : 
            char.rect.x += 3
    
def handling_key_down(event, chars, screen_rect) : 
    ''' key handling with key down '''
    if event.key == pygame.K_q : 
        sys.exit()
    elif event.key == pygame.K_LEFT : 
        for char in chars.sprites() : 
            if char.rect.left > screen_rect.left : 
                # set the internal moving flag
                char.moving_left = True
    elif event.key == pygame.K_RIGHT : 
        for char in chars.sprites() : 
            if char.rect.right < screen_rect.right : 
                # set the internal moving flag
                char.moving_right = True

def handling_key_up(event, chars, screen_rect) : 
    if event.key == pygame.K_LEFT : 
        for char in chars.sprites() : 
            # reset the internal moving flag
            char.moving_left = False
    elif event.key == pygame.K_RIGHT : 
        for char in chars.sprites() : 
            # reset the internal moving flag
            char.moving_right = False

def set_new_balls(balls, screen_rect) : 
    ''' restart the balls collection '''
    ball = Ball()
    ball.reset(screen_rect)
    balls.empty()
    balls.add(ball)

def handling_collision(balls, chars, screen_rect) : 
    '''restart the ball if a collison happens or when it reaches to the end.'''
    collisions = pygame.sprite.groupcollide(balls, chars, True, False)
    # if there is a collison, then reset the ball collection
    if len(collisions) != 0 : 
        set_new_balls(balls, screen_rect)
    # if there is a ball falling out of screen, reset the ball collection
    for ball in balls.sprites().copy() : 
        if ball.rect.top >= screen_rect.bottom : 
            set_new_balls(balls, screen_rect)
            # set the number of tries
            global tries_left
            tries_left -= 1

pygame.init()

# setting up the screen
sc = pygame.display.set_mode((600, 400))
sc_rect = sc.get_rect()

# adding the ball
balls = Group()
ball = Ball()
ball.reset(sc_rect)
balls.add(ball)

# adding the character
chars = Group()
char = Character()
char.rect.centerx = sc_rect.centerx
char.rect.bottom = sc_rect.bottom
chars.add(char)

# setting the number of tries
tries_left = 3

# starting the refreshing loop
while True : 
    events = pygame.event.get()

    # set the internal flags based on key events.
    for event in events : 
        if event.type == pygame.QUIT : 
            sys.exit()
        elif event.type == pygame.KEYDOWN : 
            handling_key_down(event, chars, sc_rect)
        elif event.type == pygame.KEYUP : 
            handling_key_up(event, chars, sc_rect)

    if tries_left > 0 : 
        # update the character base on internal moving flags
        update_char(chars, sc_rect)
        # check for collision and do correspondily if there is one
        handling_collision(balls, chars, sc_rect)

        # prepare the screen
        sc.fill((255,255,255))

        # draw the ball and character
        for ball_sprite in balls.sprites() : 
            ball_sprite.blitme(sc)
            ball_sprite.fall(sc_rect)
        for char_sprite in chars.sprites() : 
            char_sprite.blitme(sc)
        
    # show the screen
    pygame.display.flip()
