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
CAPTION = pygame.display.set_caption('Space Bunnies vs. Steampunk(?) Foxes')
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

mtntile = Group()

class Forest_Tile(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('Tiletest.bmp')
        self.rect.topleft = x, y

class Mountain_Tile(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image, self.rect = load_graphics('volcano_tile2.bmp')
        self.rect.topleft = x, y
        self.add(mtntile)
        self.health = 10

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount

## TILE PLACEMENT ##

## Forest Tiles
tile = Group()
for y in range(0, HEIGHT, 80):
    for x in range(0, WIDTH, 80):
        tile.add(Forest_Tile(x,y))

## Volcano Tiles
mtn1 = Mountain_Tile(320,0)
mtn2 = Mountain_Tile(400,0)
mtn3 = Mountain_Tile(480,0)
mtn4 = Mountain_Tile(400,80)
mtn5 = Mountain_Tile(480,80)
mtn6 = Mountain_Tile(560,80)
mtn7 = Mountain_Tile(480,160)
mtn8 = Mountain_Tile(560,160)
mtn9 = Mountain_Tile(560,240)
mtn10 = Mountain_Tile(640,240)
mtn11 = Mountain_Tile(400,320)

mtn14 = Mountain_Tile(240,560)
mtn15 = Mountain_Tile(320,560)
mtn16 = Mountain_Tile(640,560)
mtn17 = Mountain_Tile(0,640)
mtn18 = Mountain_Tile(160,640)
mtn19 = Mountain_Tile(400,640)
mtn20 = Mountain_Tile(480,640)
mtn21 = Mountain_Tile(560,640)
mtn22 = Mountain_Tile(0,160)
mtn23 = Mountain_Tile(880,160)
mtn24 = Mountain_Tile(960,0)

## Player class
## tracks everything about a player like a city or unit

class Player(object):
    def __init__(self):
        self.units = Group()
        self.cities = Group()

player1u1 = Player()
player1u2 = Player()
player1u3 = Player()

player2u1 = Player()
player2u2 = Player()
player2u3 = Player()

## Units ##

class PlayerUnit(Sprite):
    def __init__(self, x, y, group):
        Sprite.__init__(self)

        if group == 1 or group == 2 or group == 3:
            self.image, self.rect = load_graphics("Bunny2_bg.bmp")
        if group == 4 or group == 5 or group == 6:
            self.image, self.rect = load_graphics("fox_new2_bg.bmp")
        self.rect.x = x
        self.rect.y = y
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


    def attack(self, enemies):
        for enemy in pygame.sprite.spritecollide(self, enemies, False):
            enemy.hurt(1)

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount



player1u1.units.add(PlayerUnit(0,400, 1))
player1u2.units.add(PlayerUnit(0,240, 2))
player1u3.units.add(PlayerUnit(80,320, 3))

player2u1.units.add(PlayerUnit(1040,400, 4))
player2u2.units.add(PlayerUnit(1040,240, 5))
player2u3.units.add(PlayerUnit(960,320, 6))


## Cites ##


class PlayerCity(Sprite):
    def __init__(self, x, y, group):
        Sprite.__init__(self)
        if group == 1:
            self.image, self.rect = load_graphics('city1-2.bmp')
        else: 
            self.image, self.rect = load_graphics('city2-1.bmp')
        self.rect.x = x
        self.rect.y = y
        self.health = 10

    def hurt(self, amount):
        if self.health - amount <= 0:
            self.kill()
        else:
            self.health -= amount


player1u1.cities.add(PlayerCity(0, 320, 1))
player2u1.cities.add(PlayerCity(1040, 320, 2))




#-------------------------------------------------------------------------------
# Refresh Display
pygame.display.flip()
#-------------------------------------------------------------------------------

def take_turn(event, player):
    if event.key == K_d:
        player.units.update(80,0)
        return True
    elif event.key == K_a:
        player.units.update(-80,0)
        return True
    elif event.key == K_w:
        player.units.update(0,-80)
        return True
    elif event.key == K_s:
        player.units.update(0,80)
        return True

    # else return no turn change
    return False

## Text
font = pygame.font.Font(None, 40)
bigfont = pygame.font.Font(None, 80)

p1win_text = bigfont.render("Player One Wins!!! Yay. ", True, (0,0,0), WHITE)
p2win_text = bigfont.render("Player Two Wins!!! Yay. ", True, (0,0,0), WHITE)

#To make in between turn screen; try adding another player
turn_order = [ player1u1, player1u1, player1u2, player1u2, player1u3, player1u3, player2u1, player2u1, player2u2, player2u2, player2u3, player2u3 ]
turn = 0
done = False
player1win = False
player2win = False

## Main Loop ##
while done == False:


## Player One Move
    nextturn = False  # checks if you need to switch players
    for event in pygame.event.get():
        if event.type == QUIT: 
            done = True
        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        elif event.type == KEYDOWN:
            nextturn = take_turn(event, turn_order[turn])

    # calculate whos turn it is
    if nextturn:
        turn += 1
        turn %= len(turn_order)

## Lowering Unit Health

    #Player one Attacking
    for unit in pygame.sprite.groupcollide(player1u1.units, player2u1.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player1u1.units, player2u2.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player1u1.units, player2u3.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player1u2.units, player2u1.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player1u2.units, player2u2.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player1u2.units, player2u3.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player1u3.units, player2u1.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player1u3.units, player2u2.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player1u3.units, player2u3.units, False, True):
        unit.hurt(1)

    #Player two Attacking
    for unit in pygame.sprite.groupcollide(player2u1.units, player1u1.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player2u1.units, player1u2.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player2u1.units, player1u3.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player2u2.units, player1u1.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player2u2.units, player1u2.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player2u2.units, player1u3.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player2u3.units, player1u1.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(player2u3.units, player1u2.units, False, True):
        unit.hurt(1)
    
    for unit in pygame.sprite.groupcollide(player2u3.units, player1u3.units, False, True):
        unit.hurt(1)


## Lowering City Health
    for city in pygame.sprite.groupcollide(player1u1.units, player2u1.cities, False, True):
        city.hurt(1)
        player1win == True
    
    for city in pygame.sprite.groupcollide(player1u2.units, player2u1.cities, False, True):
        city.hurt(1)
        player1win == True

    for city in pygame.sprite.groupcollide(player1u3.units, player2u1.cities, False, True):
        city.hurt(1)
        player1win == True
    
    for city in pygame.sprite.groupcollide(player2u1.units, player1u1.cities, False, True):
        city.hurt(1)
        player2win == True

    for city in pygame.sprite.groupcollide(player2u2.units, player1u1.cities, False, True):
        city.hurt(1)
        player2win == True

    for city in pygame.sprite.groupcollide(player2u3.units, player1u1.cities, False, True):
        city.hurt(1)
        player2win == True

## Running into Volcanoes
    for unit in pygame.sprite.groupcollide(mtntile, player1u1.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(mtntile, player2u1.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(mtntile, player1u2.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(mtntile, player2u2.units, False, True):
        unit.hurt(1)

    for unit in pygame.sprite.groupcollide(mtntile, player1u3.units, False, True):
        unit.hurt(1)
        
    for unit in pygame.sprite.groupcollide(mtntile, player2u3.units, False, True):
        unit.hurt(1)

## Draw ##    

    tile.draw(SCREEN)
    mtntile.draw(SCREEN)

    if player1win == True:
        SCREEN.blit(p1win_text, (320,160))

    if player2win == True:
        SCREEN.blit(p2win_text, (320,160))

    player1u1.cities.draw(SCREEN)
    player2u1.cities.draw(SCREEN)
    player1u1.units.draw(SCREEN)
    player2u1.units.draw(SCREEN)
    player1u2.units.draw(SCREEN)
    player2u2.units.draw(SCREEN)
    player1u3.units.draw(SCREEN)
    player2u3.units.draw(SCREEN)

## Update ##
    pygame.display.flip()

