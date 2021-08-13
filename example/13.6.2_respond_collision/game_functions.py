#!/usr/bin/env python3

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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

def update_bullets(bullets, aliens, settings, screen, ship) : 
    ''' remove bullets if bullet run out of the screen '''
    # we should not delete list element when we are in for loop
    # this will cause chaos for the index of the element during for loop execution.
    for bullet in bullets.copy() : 
        if bullet.rect.bottom < 0 : 
            # remove the elemnts from the sprite group
            bullets.remove(bullet)
    # check collisons and update if necessary
    check_bullet_alien_collision(bullets, aliens, settings, screen, ship)

def check_bullet_alien_collision(bullets, aliens, settings, screen, ship) : 
    '''check the collision between two groups and delete them once a collision is found'''
    # groupcollide(first_group, second_group, delete_first_if_collide?, delete_second_if_collide?)
    # check the collision between two groups and delete them once a collision is found
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True )
    if len(aliens) == 0 : 
        # game restarted, previously shot bullets will be erased.
        bullets.empty()
        create_fleet(settings, screen, aliens, ship)

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

def update_aliens(aliens, settings, ship, stats, screen, bullets) : 
    check_fleet_edges(settings, aliens)
    aliens.update()
    # check collisions between ship and alien
    # pygame.sprite.sprtiecollideany takes one sprite and one group and check if there is any collision
    if pygame.sprite.spritecollideany(ship, aliens) : 
        ship_hit(settings, stats, screen, ship, aliens, bullets)

def ship_hit(settings, stats, screen, ship, aliens, bullets) : 
    ''' action when the ship is hit the alien '''
    stats.ships_left -= 1
    # empty existing objects on screen
    aliens.empty()
    bullets.empty()
    # create new alien fleet
    create_fleet(settings, screen, aliens, ship)
    # center the ship
    ship.center_ship()
    # pause for a moment
    sleep(0.5)

def check_fleet_edges(settings, aliens) : 
    ''' check if any of the aliens touch the edges, if so, chagne direction for all the fleets '''
    for alien in aliens.sprites() : 
        if alien.check_edges() : 
            change_fleet_direction(settings, aliens) 
            break

def change_fleet_direction(settings, aliens) : 
    ''' move down aliens by the vertical speed defined in settings '''
    for alien in aliens.sprites() : 
        alien.rect.y += settings.alien_drop_speed
    settings.fleet_direction *= -1
