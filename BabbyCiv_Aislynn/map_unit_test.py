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

## Units ##

unit1_group = Group()
unit2_group = Group()

## PLAYER ONE
class Player1_Unit(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('SpaceBunny_small.bmp')
        self.rect.x = x
        self.rect.y = y
        self.add(unit1_group)
        self.health = 10

    def update(self, dx, dy):
        ## Setting Left to Right Side Boundaries
        if dx > 0 and self.rect.x + dx < 1200-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x + dx > -80:
            self.rect.x += dx
        if dy > 0 and self.rect.y + dy < 1200-self.rect.h:
            self.rect.y += dy 
        if dy < 0 and self.rect.y + dy > -80:
            self.rect.y += dy 
        
        ## Setting Up Boundaries
        if dx > 0 and self.rect.x + dx < 800-self.rect.w:
           self.rect.x += dx
        if dx < 0 and self.rect.x + dx > -80:
           self.rect.x += dx
        if dy > 0 and self.rect.y + dy < 800-self.rect.h:
           self.rect.y += dy 
        if dy < 0 and self.rect.y + dy > -80:
           self.rect.y += dy 
    
    def attack(self):
        for enemy in pygame.sprite.groupcollide(Player2_Unit, Player1_Unit, False, True):
            enemy.hurt(1)

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount


## PLAYER TWO
class Player2_Unit(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Unittest.bmp')
        self.rect.x = x
        self.rect.y = y
        self.add(unit2_group)
        self.health = 10

    def update(self, dx, dy):
        ## Setting Left to Right Side Boundaries
        if dx > 0 and self.rect.x + dx < 1200-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x + dx > -80:
            self.rect.x += dx
        if dy > 0 and self.rect.y + dy < 1200-self.rect.h:
            self.rect.y += dy 
        if dy < 0 and self.rect.y + dy > -80:
            self.rect.y += dy 
        
        ## Setting Up Boundaries
        if dx > 0 and self.rect.x + dx < 800-self.rect.w:
           self.rect.x += dx
        if dx < 0 and self.rect.x + dx > -80:
           self.rect.x += dx
        if dy > 0 and self.rect.y + dy < 800-self.rect.h:
           self.rect.y += dy 
        if dy < 0 and self.rect.y + dy > -80:
           self.rect.y += dy 
    
    def attack(self):
        for enemy in pygame.sprite.groupcollide(Player1_Unit, Player2_Unit, False, True):
            enemy.hurt(1)

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount


Player1_Unit(0,400)
Player2_Unit(1040,400)


## Cites ##

city1_group = Group()
city2_group = Group()

## Player One City
class Player1_City(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Citytest.bmp')
        self.rect.x = x
        self.rect.y = y
        self.add(city1_group)
        self.health = 10

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount

## Player Two City
class Player2_City(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Citytest.bmp')
        self.rect.x = x
        self.rect.y = y
        self.add(city2_group)
        self.health = 10

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount

Player1_City(0, 320)
Player2_City(1040, 320)




#-------------------------------------------------------------------------------
# Refresh Display
pygame.display.flip()
#-------------------------------------------------------------------------------

done = False

## Main Loop ##
while done == False: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            done = True
## Player Movement Controls
        elif event.type == KEYDOWN:
            if event.key == K_d:
                unit1_group.update(80,0)
            if event.key == K_a:
                unit1_group.update(-80,0)
            if event.key == K_w:
                unit1_group.update(0,-80)
            if event.key == K_s:
                unit1_group.update(0,80)

## Lowering Unit Health
    for enemy in pygame.sprite.groupcollide(unit1_group, unit2_group, False, True):
        enemy.hurt(1)
    
    for enemy in pygame.sprite.groupcollide(unit2_group, unit1_group, False, True):
        enemy.hurt(1)

## Lowering City Health
    for enemy in pygame.sprite.groupcollide(unit1_group, city2_group, False, True):
        enemy.hurt(1)
    
    for enemy in pygame.sprite.groupcollide(unit2_group, city1_group, False, True):
        enemy.hurt(1)

## Draw ##   
    tile_group.draw(SCREEN)
    unit1_group.draw(SCREEN)
    unit2_group.draw(SCREEN)
    city1_group.draw(SCREEN)
    city2_group.draw(SCREEN)

## Update ##
    pygame.display.flip()

