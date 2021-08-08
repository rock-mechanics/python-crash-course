#!/usr/bin/env python3

import sys
import pygame
from bullet import Bullet

# check the events, and modify ship and bullets according to settings 
def check_events(ship, bullets, settings) : 
    '''check for keyboard input and mouse move'''
    # pygame's event class has a method get.
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            sys.exit()
        elif event.type == pygame.KEYDOWN : 
            check_key_down_events(event, settings, ship, bullets)
        elif event.type == pygame.KEYUP : 
            check_key_up_events(event, ship)

def check_key_down_events(event, settings, ship, bullets) : 
    ''' handles key down events. '''
    if event.key == pygame.K_RIGHT : 
        ship.moving_right = True
    elif event.key == pygame.K_LEFT : 
        ship.moving_left = True
    elif event.key == pygame.K_SPACE : 
        if len(bullets) < settings.bullets_allowed : 
            new_bullet = Bullet(settings, ship)
            bullets.add(new_bullet)
        
def check_key_up_events(event, ship):
    ''' handles key up events. '''
    if event.key == pygame.K_RIGHT :
        ship.moving_right = False
    elif event.key == pygame.K_LEFT : 
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets) : 
    ''' redraw the screen '''
    # setting the color for the new screen.
    screen.fill(settings.bg_color)
    # draw the new screen.
    ship.blitme()
    # draw the bullets.
    # Group.spirtes() method gives us a list of bullet object (sprites). 
    for bullet in bullets.sprites() : 
        # update the screen with the fleet of bullets.
        bullet.draw_bullet(screen)
    # show the screen
    pygame.display.flip()
    
