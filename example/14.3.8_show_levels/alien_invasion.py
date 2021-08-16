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
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game() : 
    pygame.init()
    settings = Settings()
    # pygame.display is a object that handles display.
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # create the object that holds the game stats
    stats = GameStats(settings)
    # create the ship object
    ship = Ship(screen, settings)
    # create a score board
    score = ScoreBoard(settings, screen, stats)
    # creates an empty bullet group, bullet will be added to the group when a key event occur.
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings, screen, aliens, ship)

    button = Button(settings, screen, 'Play')

    while True : 
        # check key down/up events, and modify the ship object.
        # check key down event, and create new bullet object.
        # check mouse press and the button, and modify the start flag
        # check quit event, and quit the game
        gf.check_events(ship, bullets, settings, stats, button, screen, aliens, score)

        # if the game is still active, we refresh the frames
        # if the game is not active, this code will be ignored, and ship, aliens, bullts will not be updated.
        # basically the screen frozen and redraw the same frame over and over again
        if stats.game_active : 
            ship.update()
            # if you run a method on a group of sprites, you will call the method on each of them.
            # update the positions of the fleet of bullets each cycle.
            bullets.update()
            # update the aliens
            # remove the alien from the alien group if it is hit by a bullet, so we need a function for this
            gf.update_aliens(aliens, settings, ship, stats, screen, bullets)

            # clean bullets if bullets out of screen
            # remove the bullets if it hit a alen
            # remove alien and bullets if they collide
            # restart the fleet if all aliens are shot
            gf.update_bullets(bullets, aliens, settings, screen, ship, score, stats)

        # redraw the screen with ship
        # redraw the screen with bullets.
        # redraw the screen with aliens
        gf.update_screen(settings, screen, ship, bullets, aliens, button, stats, score)
run_game()
