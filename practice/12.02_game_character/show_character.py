#!/usr/bin/env python3

import sys
import pygame

pygame.init()
# the display includes screen and captions and something else.
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('klee in genshin impact')

# load the image to image object
img = pygame.image.load('klee.bmp')
# setting up an rect object to save the display info for the image. it first retieve the default values of the image.
# we will change the property of this rectangle to draw the image in a new position
img_rect = img.get_rect()
# getting the screen rect. so we can place our image relative to it.
screen_rect = screen.get_rect()

# allign the img_rect to the center of the screen rect
img_rect.centerx = screen_rect.centerx
img_rect.centery = screen_rect.centery

# starting the cycle of drawing
while True : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            sys.exit()
    # fill the screen object.
    screen.fill((255,255,255))
    # blit means send data, send the img data to the screen object.
    screen.blit(img, img_rect)
    # redraw the display.
    pygame.display.flip()

