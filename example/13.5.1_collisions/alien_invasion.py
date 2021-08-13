#!/usr/bin/env python3

# modules
import sys
import pygame
import time

from settings import Settings
from ship import Ship
from alien import Alien
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
    aliens = Group()
    gf.create_fleet(settings, screen, aliens, ship)

    while True : 
        # check events, and modify the ship object.
        # check events, and create new bullet object.
        gf.check_events(ship, bullets, settings)
        ship.update()
        # if you run a method on a group of sprites, you will call the method on each of them.
        # update the positions of the fleet of bullets each cycle.
        bullets.update()
        # update the aliens
        # remove the alien from the alien group if it is hit by a bullet, so we need a function for this
        gf.update_aliens(aliens, settings)

        # clean bullets if bullets out of screen
        # remove the bullets if it hit a alen
        gf.update_bullets(bullets, aliens)

        # redraw the screen with ship
        # redraw the screen with bullets.
        # redraw the screen with aliens
        gf.update_screen(settings, screen, ship, bullets, aliens)

run_game()
