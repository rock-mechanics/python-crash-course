#!/usr/bin/env python3

import sys
import pygame

def check_events(ship) : 
    '''check for keyboard input and mouse move'''
    # pygame's event class has a method get.
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            sys.exit()
        elif event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_RIGHT : 
                ship.moving_right = True
        elif event.type == pygame.KEYUP : 
            if event.key == pygame.K_RIGHT :
                ship.moving_right = False

def update_screen(settings, screen, ship) : 
    # setting the color for the new screen.
    screen.fill(settings.bg_color)
    # redraw the new screen.
    ship.blitme()
    pygame.display.flip()
    
