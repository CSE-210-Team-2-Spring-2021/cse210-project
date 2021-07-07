import math
from typing import Optional
import arcade, os, pathlib

SCREEN_TITLE = "Definitely Not a Sinistar Clone"

# How big are our image tiles?
SPRITE_IMAGE_SIZE = 128

GRID = 128

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_TILES = 0.5
SPRITE_SCALING_ASTEROIDS = 0.2
SPRITE_SCALING_ENEMIES = 1
SPRITE_SCALING_ENEMY_LASERS = 1
SPRITE_SCALING_LASERS = .04
SPRITE_SCALING_MOUSE = 0.5
SPRITE_SCALING_MENU = 1
SPRITE_SCALING_DIFFICULTY = 0.2
SPRITE_SCALING_INSTRUCTIONS = 0.7

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

# Player/Laser Speeds
MOVEMENT_SPEED = 7
ANGLE_SPEED = 5
ACCELERATION_RATE = 1
DECELERATION_RATE = 0.1
ANGLE_DECAY = 0.2
LASER_SPEED = 7

#Number of Asteroids
ASTEROID_COUNT = 20

#Number of Enemies
WORKER_COUNT = 5
WARRIOR_COUNT = 5

#Sprites from assets
ASSET_PATH = pathlib.Path(__file__).resolve().parents[1] / 'assets' #path to parent directory
PLAYER_SPRITE = ASSET_PATH / 'basic-ship.png'
ASTEROID_SPRITE = ASSET_PATH / 'basic-astroid.png'
WARRIOR_SPRITE = ASSET_PATH / 'warrior.png'
WORKER_SPRITE = ASSET_PATH / 'worker.png'
WORKER_CRYSTAL_SPRITE = ASSET_PATH / 'worker-with-crystal.png'
LIVES_SPRITES = [ASSET_PATH / 'Lives0.png', ASSET_PATH / 'Lives1.png', ASSET_PATH / 'Lives2.png', ASSET_PATH / 'Lives3.png',
                ASSET_PATH / 'Lives4.png', ASSET_PATH / 'Lives5.png']
LASER_SPRITE = ASSET_PATH / 'laser.png'
ENEMY_LASER_SPRITE = ASSET_PATH / 'enemy-laser.png'

MOUSE = ASSET_PATH / 'mouse.png'

MENU_BACK = ASSET_PATH / 'Menu - Back.png'
MENU_HELP = ASSET_PATH / 'Menu - Help.png'
MENU_QUIT = ASSET_PATH / 'Menu - Quit.png'
MENU_RESUME = ASSET_PATH / 'Menu - Resume.png'
MENU_SETTINGS = ASSET_PATH / 'Menu - Settings.png'
MENU_START = ASSET_PATH / 'Menu - Start.png'
MENU_MAIN = ASSET_PATH / 'Menu - Main.png'
MENU_RESTART = ASSET_PATH / 'Menu - Restart.png'

DIFFICULTY_EASIEST = ASSET_PATH / 'Difficulty - Easiest.png'
DIFFICULTY_EASY = ASSET_PATH / 'Difficulty - Easy.png'
DIFFICULTY_NORMAL = ASSET_PATH / 'Difficulty - Normal.png'
DIFFICULTY_HARD = ASSET_PATH / 'Difficulty - Hard.png'
DIFFICULTY_SINISTAR = ASSET_PATH / 'Difficulty - Sinistar.png'
DIFFICULTY_SELECTOR = ASSET_PATH / 'Difficulty - Selector.png'
DIFFICULTY_LABEL = ASSET_PATH / 'Difficulty - Label.png'


VOLUME_SPRITE = ASSET_PATH / 'Volume.png'
VOLUME_LABEL = ASSET_PATH / 'Volume - Label.png'
VOLUME_SELECTOR = ASSET_PATH / 'Volume - Selector.png'
VOLUME_MUTE = ASSET_PATH / 'Mute.png'
VOLUME_INC = 10

INSTRUCTIONS = ASSET_PATH / 'Help_Menu.png'

#Sounds
sound_path = pathlib.Path(__file__).resolve().parents[1] / 'sounds'
THEME = sound_path / 'bensound-scifi.mp3'
EXPLOSION = sound_path / 'explosion.wav'
COMICAL_EXPLOSION = sound_path / 'boom.wav'
LASER = sound_path / 'laser.wav'
ENEMY_LASER = sound_path / 'laser-gun-19sf.mp3'