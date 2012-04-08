#!/usr/bin/python2
#-------------------------------------------------------------------------------
# Imports & Inits
import pygame, sys, random, imghdr
from pygame.sprite import Sprite, Group, RenderUpdates
from pygame.locals import *
pygame.init()
#-------------------------------------------------------------------------------
# Settings
WIDTH = 1200
HEIGHT = 800
FPS = 60
# Tile Width and Tile Height
TW = 80 
TH = 80
#-------------------------------------------------------------------------------
# Screen Setup
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
CAPTION = pygame.display.set_caption('Test')
SCREEN = pygame.display.get_surface()
TRANSPARENT = pygame.Surface([WIDTH,HEIGHT])
TRANSPARENT.set_alpha(255)
TRANSPARENT.fill((255,255,255))
#-------------------------------------------------------------------------------
## Tiles n Stuff ##

class Map_Tile(Sprite):
    def __init__(self, x = 80, y = 80):
        Sprite.__init__(self)


# TILE PLACEMENT

#Row One
rect1 = pygame.draw.rect(SCREEN, (255, 0, 255), (0,0, TW,TH))
rect2 = pygame.draw.rect(SCREEN, (255, 255, 255), (80,0, TW,TH))
rect3 = pygame.draw.rect(SCREEN, (255, 255, 255), (160,0, TW,TH))
rect4 = pygame.draw.rect(SCREEN, (255, 255, 255), (240,0, TW,TH))
rect5 = pygame.draw.rect(SCREEN, (255, 255, 255), (320,0, TW,TH))
rect6 = pygame.draw.rect(SCREEN, (255, 255, 255), (400,0, TW,TH))
rect7 = pygame.draw.rect(SCREEN, (255, 255, 255), (480,0, TW,TH))
rect8 = pygame.draw.rect(SCREEN, (255, 255, 255), (560,0, TW,TH))
rect9 = pygame.draw.rect(SCREEN, (255, 255, 255), (640,0, TW,TH))
rect10 = pygame.draw.rect(SCREEN, (255, 255, 255), (720,0, TW,TH))
rect11 = pygame.draw.rect(SCREEN, (255, 255, 255), (800,0, TW,TH))
rect12 = pygame.draw.rect(SCREEN, (255, 255, 255), (880,0, TW,TH))
rect13 = pygame.draw.rect(SCREEN, (255, 255, 255), (960,0, TW,TH))
rect14 = pygame.draw.rect(SCREEN, (255, 255, 255), (1040,0, TW,TH))
rect15 = pygame.draw.rect(SCREEN, (255, 0, 255), (1120,0, TW,TH))

#Row Two
rect16 = pygame.draw.rect(SCREEN, (255, 0, 255), (0,80, TW,TH))
rect17 = pygame.draw.rect(SCREEN, (255, 255, 255), (80,80, TW,TH))
rect18 = pygame.draw.rect(SCREEN, (255, 255, 255), (160,0, TW,TH))
rect19 = pygame.draw.rect(SCREEN, (255, 255, 255), (240,0, TW,TH))
rect20 = pygame.draw.rect(SCREEN, (255, 255, 255), (320,0, TW,TH))
rect21 = pygame.draw.rect(SCREEN, (255, 255, 255), (400,0, TW,TH))
rect22 = pygame.draw.rect(SCREEN, (255, 255, 255), (480,0, TW,TH))
rect23 = pygame.draw.rect(SCREEN, (255, 255, 255), (560,0, TW,TH))
rect24 = pygame.draw.rect(SCREEN, (255, 255, 255), (640,0, TW,TH))
rect25 = pygame.draw.rect(SCREEN, (255, 255, 255), (720,0, TW,TH))
rect26 = pygame.draw.rect(SCREEN, (255, 255, 255), (800,0, TW,TH))
rect27 = pygame.draw.rect(SCREEN, (255, 255, 255), (880,0, TW,TH))
rect28 = pygame.draw.rect(SCREEN, (255, 255, 255), (960,0, TW,TH))
rect29 = pygame.draw.rect(SCREEN, (255, 255, 255), (1040,0, TW,TH))
rect30 = pygame.draw.rect(SCREEN, (255, 0, 255), (1120,0, TW,TH))

#-------------------------------------------------------------------------------
# Refresh Display
pygame.display.flip()
#-------------------------------------------------------------------------------
# Main Loop
while True: 
    pos = pygame.mouse.get_pos()
    mouse = pygame.draw.circle(TRANSPARENT, (0, 0, 0), pos , 0)
    # Event Detection---------------
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            sys.exit() 
        elif event.type == MOUSEBUTTONDOWN:
            if rect1.contains(mouse):
                rect1 = pygame.draw.rect(SCREEN, (155, 155, 155), (0,0, 50, 50))
                pygame.display.flip()
