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
WIDTH = 1200
HEIGHT = 800
FPS = 60

#-------------------------------------------------------------------------------
# Screen Setup
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
CAPTION = pygame.display.set_caption('Test')
SCREEN = pygame.display.get_surface()

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

tile_group = Group()

class Tile(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Tiletest.bmp')
        self.add(tile_group)

# TILE PLACEMENT

#Row One
rect1 = Tile(0,0)
rect2 = Tile(80,0)
rect3 = Tile(160,0)
rect4 = Tile(240,0)
rect5 = Tile(320,0)
rect6 = Tile(400,0)
rect7 = Tile(480,0)
rect8 = Tile(560,0)
rect9 = Tile(640,0)
rect10 = Tile(720,0)
rect11 = Tile(800,0)
rect12 = Tile(880,0)
rect13 = Tile(960,0)
rect14 = Tile(1040,0)
rect15 = Tile(1120,0)

#Row Two
rect16 = Tile(0,80)
rect17 = Tile(80,80)
rect18 = Tile(160,0)
rect19 = Tile(240,0)
rect20 = Tile(320,0)
rect21 = Tile(400,0)
rect22 = Tile(480,0)
rect23 = Tile(560,0)
rect24 = Tile(640,0)
rect25 = Tile(720,0)
rect26 = Tile(800,0)
rect27 = Tile(880,0)
rect28 = Tile(960,0)
rect29 = Tile(1040,0)
rect30 = Tile(1120,0)

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

