#!/usr/bin/env python3

import sys
import pygame

def check_key_down_events(event, ship) : 
    if event.key == pygame.K_RIGHT : 
        ship.moving_right = True
    elif event.key == pygame.K_LEFT : 
        ship.moving_left = True

def check_key_up_event(event, ship):
    if event.key == pygame.K_RIGHT :
        ship.moving_right = False
    elif event.key == pygame.K_LEFT : 
        ship.moving_left = False

def check_events(ship) : 
    '''check for keyboard input and mouse move'''
    # pygame's event class has a method get.
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            sys.exit()
        elif event.type == pygame.KEYDOWN : 
            check_key_down_events(event, ship)
        elif event.type == pygame.KEYUP : 
            check_key_up_events(event, ship)

def update_screen(settings, screen, ship) : 
    # setting the color for the new screen.
    screen.fill(settings.bg_color)
    # redraw the new screen.
    ship.blitme()
    pygame.display.flip()
    
