#!/usr/bin/env python3

# modules
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game() : 
    pygame.init()
    settings = Settings()
    # pygame.display is a object that handles display.
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)
    while True : 
        gf.check_events()
        gf.update_screen(settings, screen, ship)

run_game()
