#!/usr/bin/env python3

# modules
import sys
import pygame

def run_game() : 
    pygame.init()
    # pygame.display is a object that handles display.
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')

    while True : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                sys.exit()
        pygame.display.flip()

run_game()
