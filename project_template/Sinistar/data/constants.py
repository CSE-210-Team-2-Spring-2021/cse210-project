import math
from typing import Optional
import arcade, os, pathlib

SCREEN_TITLE = "Definitely Not a Sinistar Clone"

# How big are our image tiles?
SPRITE_IMAGE_SIZE = 128

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_TILES = 0.5

# Scaled sprite size for tiles
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

# Size of grid to show on screen, in number of tiles
SCREEN_GRID_WIDTH = 25
SCREEN_GRID_HEIGHT = 15

# Size of screen to show, in pixels
SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT

# How many lives has the Player?
LIVES = 5

#Sprites from assets
path = pathlib.Path(__file__).resolve().parents[0] / 'assets' #path to parent directory
PLAYER_SPRITE = path / 'basic-ship.jpg'