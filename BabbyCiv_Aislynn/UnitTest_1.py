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
## Units ##

unit_group = Group()

class Player1_Unit(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Unittest.bmp')
        self.rect.x = x
        self.rect.y = y
        self.add(unit_group)
        self.health = 10
    
    def attack(self):
        for enemy in pygame.sprite.groupcollide(Player2_Unit, Player1_Unit, False, True):
            enemy.hurt(1)

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount



Player1_Unit(300,300)



#-------------------------------------------------------------------------------
# Refresh Display
pygame.display.flip()
#-------------------------------------------------------------------------------

done = False
grabbed = False

# Main Loop
while not done: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            done = True

        elif event.type == MOUSEBUTTONDOWN:
            grabbed = True
        elif event.type == MOUSEBUTTONUP:
            grabbed = False

## Draw ##
    if grabbed == True:
        Player1_Unit.center = pygame.mouse.get_pos()    

    unit_group.draw(SCREEN)

## Update ##
    pygame.display.flip()

