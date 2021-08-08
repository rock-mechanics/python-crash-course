#!/usr/bin/env python3

import sys
import pygame

def check_events() : 
    '''check for keyboard input and mouse move'''
    # pygame's event class has a method get.
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            sys.exit()

def update_screen(settings, screen, ship) : 
    # setting the color for the new screen.
    screen.fill(settings.bg_color)
    # redraw the new screen.
    ship.blitme()
    pygame.display.flip()
    
