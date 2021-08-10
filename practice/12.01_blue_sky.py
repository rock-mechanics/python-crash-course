#!/usr/bin/env python3

import pygame
import sys

screen_width = 500
screen_height = 300

# initalize pygame
pygame.init()

# get the surface
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('blue sky')


while True : 
    # pygame.event.get() returns a list of events
    # check each of them to see whether their is a quit
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT:
            sys.exit()
    # fill the screen
    screen.fill((0,255,255))
    # draw the screen
    pygame.display.flip()
