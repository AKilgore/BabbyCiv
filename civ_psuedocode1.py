"""

## UNIT CLASSES ##

class Unit(Sprite)
   knows what type of tile its on
   knows unit health
   knows unit movement speed
   knows unit production speed
   knows unit damage against other untis
   knows unit damage against cities 
   knows unit attack range

class Melee(Unit)
   health = 10
   movement speed = 3 squares per turn
   production speed = 3 turns
   damage against units = 



## MAP TILES CLASSES ##

class Map_Tile(Sprite)
   stores what's currently on the tile
   108x108 pixels

   def slow_unit:
      pass

class Field_Tile(Map_Tile) 
   def slow_unit:
      units lose no movement speed

class Forest_Tile(Map_Tile)
   def slow_unit:
      unit moving from forest tile loses one movement speed

class Mountain_Tile(Map_Tile)
   def slow_unit:
      units can't go onto this tile


"""
