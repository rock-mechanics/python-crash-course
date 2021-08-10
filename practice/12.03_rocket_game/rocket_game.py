#!/usr/bin/env python3

import pygame
import sys

# setting up flags for image handling
is_moving_right = False
is_moving_left = False
is_moving_up = False
is_moving_down = False

# setting up some game parameters
speed = 2

def responds_key_down(event) : 
    global is_moving_right
    global is_moving_left
    global is_moving_up
    global is_moving_down

    if event.key == pygame.K_RIGHT : 
        is_moving_right = True
    elif event.key == pygame.K_LEFT : 
        is_moving_left = True
    elif event.key == pygame.K_UP : 
        is_moving_up = True
    elif event.key == pygame.K_DOWN : 
        is_moving_down = True
            
def responds_key_up(event) : 
    ''' stop moving once the key is up '''
    global is_moving_right
    global is_moving_left
    global is_moving_up
    global is_moving_down

    if event.key == pygame.K_RIGHT : 
        is_moving_right = False
    elif event.key == pygame.K_LEFT : 
        is_moving_left = False
    elif event.key == pygame.K_UP : 
        is_moving_up = False
    elif event.key == pygame.K_DOWN : 
        is_moving_down = False

def check_events(event) : 
    ''' check keyboard events and modify the img_rect (which defines img position) accordingly'''
    if event.type == pygame.QUIT : 
        sys.exit()
    elif event.type == pygame.KEYDOWN : 
        responds_key_down(event)
    elif event.type == pygame.KEYUP :  
        responds_key_up(event)

def update_img(img_rect, screen_rect) : 
    if is_moving_left and img_rect.left > screen_rect.left:  
        img_rect.centerx -= speed
    if is_moving_right and img_rect.right < screen_rect.right :  
        img_rect.centerx += speed
    if is_moving_up and img_rect.top > screen_rect.top:  
        img_rect.centery -= speed
    if is_moving_down and img_rect.bottom < screen_rect.bottom:  
        img_rect.centery += speed
    return img_rect
# prepare the game.
pygame.init()

# set the screen
screen = pygame.display.set_mode((400, 300))
# set the cpation
pygame.display.set_caption('Rocket Game by Jing Chen')

# set the img object 
img = pygame.image.load('rocket.bmp')
# initialize the img_rect
img_rect = img.get_rect()
# get the screen_rect
screen_rect = screen.get_rect()
# position the img_rect based on the screen rect.
img_rect.centerx = screen_rect.centerx
img_rect.centery = screen_rect.centery

# start the refresh loop
while True : 
    for event in pygame.event.get() : 
        check_events(event)
    img_rect = update_img(img_rect, screen_rect)
    screen.fill((246,246,246))
    screen.blit(img, img_rect)
    pygame.display.flip()
