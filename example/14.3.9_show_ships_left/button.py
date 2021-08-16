#!/usr/bin/env python3

import pygame.font

class Button() : 
    def __init__(self, settings, screen, msg) : 
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # set the property of the button
        self.width, self.height = 200, 50
        self.button_color = (0,255,0) # green color
        self.text_color = (255,255,255) # white color
        # None means default system font
        self.font = pygame.font.SysFont(None, 48)
        # place the button in the middle of the screen
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center
        # convert msg to image and position it properly
        self.prepare_msg(msg)
    
    def prepare_msg(self, msg) : 
        '''render the msg on the button'''
        # system font has a method called 'render'
        # it convert txt into an image object, which can be blited to the screen
        # the arguments are 'show_text', '', 'txt_color', 'bg_color'
        self.msg_img  = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        # position the img in the center of the button
        self.msg_img_rect.center = self.rect.center

    def draw_button(self) : 
        # fill color with an area
        self.screen.fill(self.button_color, self.rect)
        # send the image to the screen
        self.screen.blit(self.msg_img, self.msg_img_rect)
