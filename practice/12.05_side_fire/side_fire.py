#!/usr/bin/env python3

import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

class Bullet(Sprite) : 
    def __init__(self, inital_x, inital_y) : 
        super().__init__()
        self.x = float(inital_x)
        self.y = inital_y
        self.rect = pygame.Rect(0,0,20, 5)
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def update(self) : 
        self.x += 1.5
        self.rect.centerx = self.x
    def draw(self, screen) : 
        pygame.draw.rect(screen,(0,0,0),self.rect)


screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Side Fire by Jing Chen')

img = pygame.image.load('rocket270.bmp')
img_rect = img.get_rect()
screen_rect = screen.get_rect()

# position the image
img_rect.centery = screen_rect.centery

# flags for rocket
is_moving_up = False
is_moving_down = False

# collection of bullets
bullets = Group()

while True : 
    # handling all the events.
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            sys.exit()
        elif event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_UP :
                is_moving_up = True
            elif event.key == pygame.K_DOWN :
                is_moving_down = True
            elif event.key == pygame.K_SPACE : 
                bullet = Bullet(img_rect.centerx, img_rect.centery)
                bullets.add(bullet)
        elif event.type == pygame.KEYUP : 
            if event.key == pygame.K_UP :
                is_moving_up = False
            elif event.key == pygame.K_DOWN :
                is_moving_down = False

    # prepare the screen
    screen.fill((236,236,236))
    # prepare the rocket
    screen.blit(img, img_rect)
    # prepare the rocket
    if is_moving_up and img_rect.top > screen_rect.top : 
        img_rect.centery -= 1
    if is_moving_down and img_rect.bottom < screen_rect.bottom : 
        img_rect.centery += 1
    # prepare the bullet
    bullets.update()
    for bullet in bullets.sprites() : 
        bullet.draw(screen)
    # clean up the bullets when they are out of the screen
    for bullet in bullets.sprites().copy() : 
        if bullet.rect.left > screen_rect.right : 
            bullets.remove(bullet)
    print(len(bullets))
    # draw the screen
    pygame.display.flip()

