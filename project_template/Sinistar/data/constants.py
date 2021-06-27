import math
from typing import Optional
import arcade, os, pathlib

SCREEN_TITLE = "Definitely Not a Sinistar Clone"

# How big are our image tiles?
SPRITE_IMAGE_SIZE = 128

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_TILES = 0.5
SPRITE_SCALING_ASTEROIDS = 0.2

# Scaled sprite size for tiles
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_TILES)

# Size of grid to show on screen, in number of tiles
SCREEN_GRID_WIDTH = 25
SCREEN_GRID_HEIGHT = 15

# Size of screen to show, in pixels
SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT

# How many lives has the Player?
LIVES = 5
IMMUNITY = 100 #TIME spent invincible after damage

#Player Speed
MOVEMENT_SPEED = 5

#Number of Asteroids
ASTEROID_COUNT = 20

#Sprites from assets
asset_path = pathlib.Path(__file__).resolve().parents[1] / 'assets' #path to parent directory
PLAYER_SPRITE = asset_path / 'basic-ship.png'
ASTEROID_SPRITE = asset_path / 'basic-astroid.png'
LIVES_SPRITES = [asset_path / 'Lives0.png', asset_path / 'Lives1.png', asset_path / 'Lives2.png', asset_path / 'Lives3.png',
                asset_path / 'Lives4.png', asset_path / 'Lives5.png']

#Sounds
sound_path = pathlib.Path(__file__).resolve().parents[1] / 'sounds'
THEME = sound_path / 'bensound-scifi.mp3'
EXPLOSION = sound_path / 'explosion.wav'
COMICAL_EXPLOSION = sound_path / 'boom.wav'
