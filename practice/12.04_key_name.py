#!/usr/bin/env python3

import pygame
import sys

pygame.init()

while True : 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            sys.exit()
        elif event.type == pygame.KEYDOWN : 
            print(event.key)
