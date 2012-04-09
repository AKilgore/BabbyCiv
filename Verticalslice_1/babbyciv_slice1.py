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
WHITE = 255, 255, 255
GRAY = 80, 80, 80
GREEN = 0, 192, 0

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

#-------------------------------------------------------------------------------
## Tiles n Stuff ##

mtntile_group = Group()

class Forest_Tile(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Tiletest.bmp')
        self.rect.topleft = x, y

class Mountain_Tile(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Mountain_tile.bmp')
        self.rect.topleft = x, y
        self.add(mtntile_group)


## TILE PLACEMENT ##

## Forest Tiles
tile_group = Group()
for y in range(0, HEIGHT, 80):
    for x in range(0, WIDTH, 80):
        tile_group.add(Forest_Tile(x,y))

## Mountain Tiles
mtn0 = Mountain_Tile(0,0)
mtn1 = Mountain_Tile(160,0)
mtn2 = Mountain_Tile(240,0)
mtn3 = Mountain_Tile(320,0)
mtn4 = Mountain_Tile(160,80)


## PLAYER CHARACTERS ##

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
        if dx > 0 and self.rect.x + dx < 1200-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x + dx > -80:
            self.rect.x += dx
        if dy > 0 and self.rect.y + dy < 1200-self.rect.h:
            self.rect.y += dy 
        if dy < 0 and self.rect.y + dy > -80:
            self.rect.y += dy 

    def key_event(self, event):
        if event.key == pygame.K_d:
            self.update(80,0)
        elif event.key == pygame.K_a:
            self.update(-80,0)
        elif event.key == pygame.K_w:
            self.update(0,-80)
        elif event.key == pygame.K_s:
            self.update(0,80)

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
        if dx > 0 and self.rect.x + dx < 1200-self.rect.w:
            self.rect.x += dx
        if dx < 0 and self.rect.x + dx > -80:
            self.rect.x += dx
        if dy > 0 and self.rect.y + dy < 1200-self.rect.h:
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


bunny1 = Player1_Unit(0,400)
bunny2 = Player1_Unit(0,240)

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
clicked = False
done = False
game_over = False

pressed = pygame.key.get_pressed()
move_count = 0
font = pygame.font.Font(None, 40)
bigfont = pygame.font.Font(None, 80)

# Text 
text1 = font.render("Player One Move First Character", True, (0,0,0), WHITE)
text1_rect = text1.get_rect()

text2 = font.render("Player One Move Second Character", True, (0,0,0), WHITE)
text2_rect = text2.get_rect()

p2lose_text = bigfont.render("Player One Wins!!! Yay. ", True, (0,0,0), WHITE)

## Main Loop ##
while done == False: 

    tile_group.draw(SCREEN)
    mtntile_group.draw(SCREEN)

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            done = True

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

## Player Movement Controls
        elif event.type == pygame.KEYDOWN and move_count != 2:
            bunny1.key_event(event)
            move_count += 1
            print move_count

        elif event.type == pygame.KEYDOWN and move_count == 2:
            bunny2.key_event(event)
            move_count -= 1
            print move_count
           
    if move_count == 1 and game_over == False:           
        SCREEN.blit(text1, (320,160))

    if move_count == 2 and game_over == False:
        SCREEN.blit(text2, (320,160))

## Lowering Unit Health
    for enemy in pygame.sprite.groupcollide(unit1_group, unit2_group, False, True):
        enemy.hurt(1)
    
    for enemy in pygame.sprite.groupcollide(unit2_group, unit1_group, False, True):
        enemy.hurt(1)

## Lowering City Health
    for enemy in pygame.sprite.groupcollide(unit1_group, city2_group, False, True):
        enemy.hurt(1)
        game_over = True
        
    
    for enemy in pygame.sprite.groupcollide(unit2_group, city1_group, False, True):
        enemy.hurt(1)

## Draw ##   
    if game_over == True:
        SCREEN.blit(p2lose_text, (320,160)) 

    unit1_group.draw(SCREEN)
    unit2_group.draw(SCREEN)
    city1_group.draw(SCREEN)
    city2_group.draw(SCREEN)

## Update ##
    pygame.display.flip()

