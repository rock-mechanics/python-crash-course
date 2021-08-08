#!/usr/bin/env python3

# modules
import sys
import pygame

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
        # check events, and add and draw bullet object.
        gf.check_events(ship)
        ship.update()
        # if you run a method on a group of sprites, you will call the method on each of them.
        bullets.update()
        # redraw the screen with ship
        gf.update_screen(settings, screen, ship, bullets)

run_game()
