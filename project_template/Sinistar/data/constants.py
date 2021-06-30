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
SPRITE_SCALING_MOUSE = 0.5
SPRITE_SCALING_MENU = 1

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
IMMUNITY = 10 #TIME spent invincible after damage

#Player Speed
MOVEMENT_SPEED = 5

#Number of Asteroids
ASTEROID_COUNT = 20

#Sprites from assets
ASSET_PATH = pathlib.Path(__file__).resolve().parents[1] / 'assets' #path to parent directory
PLAYER_SPRITE = ASSET_PATH / 'basic-ship.png'
ASTEROID_SPRITE = ASSET_PATH / 'basic-astroid.png'
LIVES_SPRITES = [ASSET_PATH / 'Lives0.png', ASSET_PATH / 'Lives1.png', ASSET_PATH / 'Lives2.png', ASSET_PATH / 'Lives3.png',
                ASSET_PATH / 'Lives4.png', ASSET_PATH / 'Lives5.png']

MOUSE = ASSET_PATH / 'mouse.png'

MENU_BACK = ASSET_PATH / 'Menu - Back.png'
MENU_HELP = ASSET_PATH / 'Menu - Help.png'
MENU_QUIT = ASSET_PATH / 'Menu - Quit.png'
MENU_RESUME = ASSET_PATH / 'Menu - Resume.png'
MENU_SETTINGS = ASSET_PATH / 'Menu - Settings.png'
MENU_START = ASSET_PATH / 'Menu - Start.png'
MENU_MAIN = ASSET_PATH / 'Menu - Main.png'
MENU_RESTART = ASSET_PATH / 'Menu - Restart.png'

#Sounds
sound_path = pathlib.Path(__file__).resolve().parents[1] / 'sounds'
THEME = sound_path / 'bensound-scifi.mp3'
EXPLOSION = sound_path / 'explosion.wav'
COMICAL_EXPLOSION = sound_path / 'boom.wav'
