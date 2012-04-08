#!/usr/bin/python2
#-------------------------------------------------------------------------------
# Imports & Inits
import pygame
import os, sys, random, imghdr
from pygame.sprite import Sprite, Group, RenderUpdates
from pygame import *
from pygame.locals import *
init()
#-------------------------------------------------------------------------------
# Settings
WIDTH = 1120
HEIGHT = 720
FPS = 60

#-------------------------------------------------------------------------------
# Screen Setup
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
CAPTION = pygame.display.set_caption('Test')
SCREEN = pygame.display.get_surface()
TRANSPARENT = pygame.Surface([WIDTH,HEIGHT])
TRANSPARENT.set_alpha(255)
TRANSPARENT.fill((255,255,255))

def load_graphics(filename):
    fullfname = os.path.join('pictures', filename)
    try:
        image = pygame.image.load(fullfname)
    except pygame.error, message:
        print 'Cannot load', fullfname
        raise SystemExit, message
    return image, image.get_rect()


def text_render(text, x, y, color, size):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x, y))

#-------------------------------------------------------------------------------
## Tiles n Stuff ##

class Tile(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Tiletest.bmp')
        self.rect.topleft = x, y


# TILE PLACEMENT

tile_group = Group()
for y in range(0, HEIGHT, 80):
    for x in range(0, WIDTH, 80):
        tile_group.add(Tile(x,y))


#-------------------------------------------------------------------------------
# Refresh Display
pygame.display.flip()
#-------------------------------------------------------------------------------

# Main Loop
while True: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            sys.exit() 

## Draw ##   
    tile_group.draw(SCREEN)

## Update ##
    pygame.display.flip()

