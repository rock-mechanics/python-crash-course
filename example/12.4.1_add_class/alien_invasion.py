#!/usr/bin/env python3

# modules
import sys
import pygame

from settings import Settings

def run_game() : 
    pygame.init()
    settings = Settings()
    # pygame.display is a object that handles display.
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    while True : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                sys.exit()
        # setting the color for the new screen.
        screen.fill(settings.bg_color)
        # redraw the new screen.
        pygame.display.flip()

run_game()
