#!/usr/bin/env python3

import pygame
import sys
from random import randint

# start pygame
pygame.init()

# load the star image
img = pygame.image.load('star.bmp')

# initalize screen
sc = pygame.display.set_mode((600, 400))

# get screen size and image size
sc_rect = sc.get_rect()
img_rect = img.get_rect()

# calculate number of items.
rows = (sc_rect.height - 2 * img_rect.height) // img_rect.height
cols = (sc_rect.width - 2 * img_rect.width) // img_rect.width

# start the event handling

filled = False
while True : 
    # for each loop, get the series of events
    events = pygame.event.get()
    # check event and respond
    for event in events : 
        if event.type == pygame.QUIT : 
            sys.exit()
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_q : 
                sys.exit()
    # clear the screen from previous cycle
    # make this code run only one time, so the screen will stay the same without updating
    if not filled : 
        sc.fill((255,255,255))
        # draw the screen
        for row in range(rows) : 
            for col in range(cols) : 
                if randint(0,5) == 1 : 
                    img_rect.top = img_rect.height + img_rect.height * row
                    img_rect.left = img_rect.width + img_rect.width * col
                    sc.blit(img, img_rect)
        filled = True
    pygame.display.flip()
