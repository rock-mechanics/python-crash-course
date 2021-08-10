#!/usr/bin/env python3

import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
import time

class Drop(Sprite) : 
    def __init__(self) : 
        super().__init__()
        self.image = pygame.image.load('drop.bmp') 
        self.rect = self.image.get_rect()
        self.x = float(0)
        self.y = float(0)

    def position(self, x, y) : 
        self.x = float(x) 
        self.y = float(y)
        
    def update(self) : 
        # the drops will increase
        self.y += 10

    def draw(self, screen) : 
        # update the triangle
        self.rect.x = self.x
        self.rect.y = self.y
        # send the image to the screen
        screen.blit(self.image, self.rect)

# manage drops    
def update_drops(drops, screen) : 
    for drop in drops.sprites().copy() : 
        # if the drops out of the screen, reposition it to the top, so it will be like continuous rain drops.
        if drop.y >= screen.get_rect().bottom : 
            drop.position(drop.x, 0)
           
# start pygame
pygame.init()

# initalize screen
sc = pygame.display.set_mode((600, 400))

# get screen size and image size
sc_rect = sc.get_rect()

# create the series of drops
drops = Group()

# get a drop instance to get its property
drop = Drop()

# calculate number of items.
rows = (sc_rect.height - 2 * drop.rect.height) // drop.rect.height
cols = (sc_rect.width - 2 * drop.rect.width) // drop.rect.width

# create the fleets
for row in range(rows) : 
    for col in range(cols) : 
        new_drop = Drop()
        x = drop.rect.width + drop.rect.width * col
        y = drop.rect.height + drop.rect.height * row
        new_drop.position(x, y)
        drops.add(new_drop)

# start the event handling
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
    sc.fill((255,255,255))
    # draw the drops
    for drop in drops.sprites() : 
        drop.draw(sc)
    drops.update()
    # draw the screen
    time.sleep( 0.5 )
    pygame.display.flip()
    # remove the drops if they go out of the screen
    update_drops(drops, sc)
