#!/usr/bin/env python3

import sys
import pygame
from bullet import Bullet
from alien import Alien

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
        fire_bullet(settings, bullets, ship)
    elif event.key == pygame.K_q : 
        sys.exit()

def fire_bullet(settings, bullets, ship) : 
    if len(bullets) < settings.bullets_allowed : 
        new_bullet = Bullet(settings, ship)
        bullets.add(new_bullet)
    
def check_key_up_events(event, ship):
    ''' handles key up events. '''
    if event.key == pygame.K_RIGHT :
        ship.moving_right = False
    elif event.key == pygame.K_LEFT : 
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets, aliens) : 
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
    # draw the alien
    aliens.draw(screen)
    # show the screen
    pygame.display.flip()

def update_bullets(bullets) : 
    ''' remove bullets if bullet run out of the screen '''
    # we should not delete list element when we are in for loop
    # this will cause chaos for the index of the element during for loop execution.
    for bullet in bullets.copy() : 
        if bullet.rect.bottom < 0 : 
            # remove the elemnts from the sprite group
            bullets.remove(bullet)

def create_fleet(settings, screen, aliens, ship) : 
    ''' creates a fleet on the screen '''
    # calculate number of aliens in a row
    alien = Alien(settings, screen)
    columns = get_number_aliens_x(settings, alien.rect.width)
    rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row in range(rows) : 
        for column in range(columns)  : 
            create_alien(settings, screen, aliens, row, column)

def get_number_aliens_x(settings, alien_width) : 
    space_x = settings.screen_width - alien_width * 2
    number_aliens_x = space_x // ( 2 * alien_width )
    return number_aliens_x

def create_alien(settings, screen, aliens, row, column) : 
    # create an alien and get its inital property
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    # reposition the alien
    # there is a margin of one alien on the screen
    alien.x = alien_width + 2 * alien_width * column
    alien.y = alien_height + 2 * alien_height * row

    # assign to the alien property
    alien.rect.x = alien.x
    alien.rect.y = alien.y

    # add to the fleet
    aliens.add(alien)

def get_number_rows(settings, ship_height, alien_height) : 
    '''calculate how many aliens can be shown on screen'''
    available_y = settings.screen_height - 3 * alien_height - ship_height
    number_rows = available_y // (2 * alien_height)
    return number_rows
