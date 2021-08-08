#!/usr/bin/env python3

# modules
import sys
import pygame
import time

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game() : 
    pygame.init()
    settings = Settings()
    # pygame.display is a object that handles display.
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, settings)
    # creates an empty bullet group, bullet will be added to the group when a key event occur.
    bullets = Group()
    while True : 
        # check events, and modify the ship object.
        # check events, and create new bullet object.
        gf.check_events(ship, bullets, settings)
        ship.update()
        # if you run a method on a group of sprites, you will call the method on each of them.
        # update the positions of the fleet of bullets each cycle.
        bullets.update()
        # we should not delete list element when we are in for loop, this will cause chaos for the index of the element during for loop execution.
        for bullet in bullets.copy() : 
            if bullet.rect.bottom < 0 : 
                # remove the elemnts from the sprite group
                bullets.remove(bullet)

        # sleep for 0.01 seconds so that the delta time difference of while loop is not significant.
        time.sleep(0.01)

        # redraw the screen with ship
        # redraw the screen with bullets.
        gf.update_screen(settings, screen, ship, bullets)

run_game()
