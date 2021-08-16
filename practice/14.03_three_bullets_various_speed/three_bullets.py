#!/usr/bin/env python3

import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

class Ship(Sprite) : 
    def __init__(self, screen) : 
        super().__init__()
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.reset()
        self.moving_up = False
        self.moving_down = False
    def reset(self) : 
        ''' reposition the ship to the center left of the screen '''
        self.rect.centery = self.screen_rect.centery
    def blitme(self) : 
        ''' draw the ship on the screen object '''
        self.screen.blit(self.image, self.rect)
    def move(self, speed_factor = 1) : 
        if self.moving_up and self.rect.y > 0: 
           self.rect.y -= 10 * speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.height: 
           self.rect.y += 10 * speed_factor

class Target(Sprite) : 
    def __init__(self, screen) : 
        super().__init__()
        self.rect = pygame.Rect(0,0,100,100)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.moving_direction = 1
        self.reset()
    def move(self, speed_factor) : 
        self.check_edge()
        self.rect.y += self.moving_direction * speed_factor
        print(speed_factor)
    def draw(self) : 
        self.screen.fill((0,0,0), self.rect)
    def reset(self) : 
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
    def check_edge(self) : 
        if self.rect.bottom > self.screen_rect.bottom or self.rect.top < 0 : 
            self.moving_direction *= -1

class Bullet(Sprite) : 
    def __init__(self, ship, target, screen) : 
        super().__init__()
        self.rect = pygame.Rect(0,0,10,10)
        self.ship = ship
        self.target = target
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.reset_tries()

        # define an flag to check whether the bullet is out of screen
        self.out_of_screen = False
        # define an internal flag to see whether user has fired the bullet
        self.is_fire = False

    def fire(self) : 
        self.reset()
        self.is_fire = True

    def reset(self) : 
        self.rect.centery = self.ship.rect.centery
        self.rect.right = self.ship.rect.right

    def hit(self) : 
        self.is_fire = False
        # a bug fix, after a hit, remove the collison status by resetting the bullets under the ship
        self.reset()
    
    def reset_tries(self) : 
        self.tries_left = 3

    def move(self, speed_factor) : 
        if self.is_fire : 
            self.rect.x += 1 * speed_factor
            self.check_edge()

    def check_edge(self) : 
        if self.rect.left >= self.screen_rect.right : 
            self.out_of_screen = True
            self.tries_left -= 1
            self.is_fire = False

    def draw(self) : 
        if self.is_fire : 
            self.screen.fill((0,0,0), self.rect)
class Button() : 
    def __init__(self, width, height, font_size, screen) : 
        self.rect = pygame.Rect(0,0,width, height)
        self.font = pygame.font.SysFont(None, font_size)
        self.screen = screen

    def draw(self, msg, font_color, bg_color) : 
        self.img = self.font.render(msg, True, font_color, bg_color)
        self.screen.blit(self.img, self.rect)

# initialize pygame
pygame.init()

# get the screen
sc = pygame.display.set_mode((500,300))

# initalize the object
ship = Ship(sc)
target = Target(sc)
bullet = Bullet(ship, target, sc)

# flag to see whether game is active
game_active = False

# construct buttons
# number of tries button
tries_button = Button(50, 50, 40, sc )
# position the button
tries_button.rect.y = 0
tries_button.rect.centerx = sc.get_rect().centerx
# start button
start_button = Button(100, 50, 40, sc )
start_button.rect.centerx = sc.get_rect().centerx
start_button.rect.centery = sc.get_rect().centery

# initalize speed factor
speed_factor = 1
speed_up_factor = 1.1

while True : 
    events = pygame.event.get()
    for event in events : 
        if event.type == pygame.QUIT : 
            sys.exit()
        elif event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_q : 
                sys.exit()
            elif event.key == pygame.K_UP : 
                ship.moving_up = True
            elif event.key == pygame.K_DOWN : 
                ship.moving_down = True
            elif event.key == pygame.K_SPACE : 
                # introduce the bullet to the screen
                if not bullet.is_fire and bullet.tries_left > 0 : 
                    bullet.fire()
        elif event.type == pygame.KEYUP : 
            if event.key == pygame.K_UP : 
                ship.moving_up = False
            elif event.key == pygame.K_DOWN : 
                ship.moving_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            # pygame has a 'mouse' class containing the clicked mouse positions
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if start_button.rect.collidepoint(mouse_x, mouse_y) : 
                bullet.reset_tries()
                game_active = True

    # check if player lost
    if bullet.tries_left <= 0 : 
        game_active = False
        speed_factor = 1
    # repaint the screen
    sc.fill((230,230,230))
    # draw the button
    tries_button.draw(str(bullet.tries_left), (0,0,0), (230,230,230))
    # draw the start button
    if not game_active : 
       start_button.draw('START', (255,255,255), (0,255,0))
    
    if game_active : 
        # draw the ship based on internal flags
        ship.move(speed_factor)
        ship.blitme()
        # draw the target
        target.move(speed_factor)
        target.draw()
        # draw the bullet
        bullet.move(speed_factor)
        bullet.draw()
        # check collision 
        if pygame.sprite.collide_rect(bullet, target) : 
            bullet.hit()
            # increase the speed
            speed_factor *= speed_up_factor
    # refresh the screen
    pygame.display.flip()
