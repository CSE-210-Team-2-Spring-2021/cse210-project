import math
from typing import Optional
import arcade
import os
import pathlib

SCREEN_TITLE = "Definitely Not a Sinistar Clone"

# How big are our image tiles?
SPRITE_IMAGE_SIZE = 128

GRID = 128

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_TILES = 0.5
SPRITE_SCALING_ASTEROIDS = 0.6
SPRITE_SCALING_ENEMIES = 1
SPRITE_SCALING_ENEMY_LASERS = 1
SPRITE_SCALING_LASERS = .04
SPRITE_SCALING_MOUSE = 0.5
SPRITE_SCALING_MENU = 1
SPRITE_SCALING_DIFFICULTY = 0.2
SPRITE_SCALING_INSTRUCTIONS = 0.7
SPRITE_SCALING_CRYSTALS = 1
SPRITE_SCALING_BOMB = .1

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
IMMUNITY = 100  # TIME spent invincible after damage
BOMBS = 0

# Player/Laser Speeds
MOVEMENT_SPEED = 7
ANGLE_SPEED = 5
ACCELERATION_RATE = 1
DECELERATION_RATE = 0.1
ANGLE_DECAY = 0.2
LASER_SPEED = 10

# Set Difficulty
EASIEST = .25
EASY = .5
NORMAL = 1
HARD = 1.25
SINISTAR = 1.5

# Number of Asteroids
ASTEROID_COUNT = 10

# Number of Enemies
WORKER_COUNT = 5
WARRIOR_COUNT = 5

# Highscore doc path
SCORE_DOC = os.path.abspath('./data/highscores.json')

# Sprites from assets
#ASSET_PATH = pathlib.Path(__file__).resolve(
#).parents[1] / 'assets'  # path to parent directory
#ASSET_PATH = os.path.abspath('../assets')  # path to parent directory
PLAYER_SPRITE = os.path.abspath('./assets/basic-ship.png')
SHIELD_PLAYER_SPRITE = os.path.abspath('./assets/shield-basic-ship.png')
ASTEROID_SPRITE = os.path.abspath('./assets/asteroid.png')  # 'basic-astroid.png'
WARRIOR_SPRITE = os.path.abspath('./assets/warrior.png')
WORKER_SPRITE = os.path.abspath('./assets/worker.png')
CRYSTAL_SPRITE = os.path.abspath('./assets/crystal.png')
WORKER_CRYSTAL_SPRITE = os.path.abspath('./assets/worker-with-crystal.png')
LIVES_SPRITES = [os.path.abspath('./assets/Lives0.png'), os.path.abspath('./assets/Lives1.png'),
                 os.path.abspath('./assets/Lives2.png'), os.path.abspath('./assets/Lives3.png'),
                 os.path.abspath('./assets/Lives4.png'), os.path.abspath('./assets/Lives5.png')]
LASER_SPRITE = os.path.abspath('./assets/laser.png')
ENEMY_LASER_SPRITE = os.path.abspath('./assets/enemy-laser.png')
BOMBS_AMOUNT_SPRITES = [os.path.abspath('./assets/BombsAmount0.png'), os.path.abspath('./assets/BombsAmount1.png'),
                        os.path.abspath('./assets/BombsAmount2.png'), os.path.abspath('./assets/BombsAmount3.png'),
                        os.path.abspath('./assets/BombsAmount4.png'), os.path.abspath('./assets/BombsAmount5.png')]
BOMB_SPRITE = os.path.abspath('./assets/bomb.png')

MOUSE = os.path.abspath('./assets/mouse.png')

MENU_BACK = os.path.abspath('./assets/Menu - Back.png')
MENU_HELP = os.path.abspath('./assets/Menu - Help.png')
MENU_QUIT = os.path.abspath('./assets/Menu - Quit.png')
MENU_RESUME = os.path.abspath('./assets/Menu - Resume.png')
MENU_SETTINGS = os.path.abspath('./assets/Menu - Settings.png')
MENU_START = os.path.abspath('./assets/Menu - Start.png')
MENU_MAIN = os.path.abspath('./assets/Menu - Main.png')
MENU_RESTART = os.path.abspath('./assets/Menu - Restart.png')

DIFFICULTY_EASIEST = os.path.abspath('./assets/Difficulty - Easiest.png')
DIFFICULTY_EASY = os.path.abspath('./assets/Difficulty - Easy.png')
DIFFICULTY_NORMAL = os.path.abspath('./assets/Difficulty - Normal.png')
DIFFICULTY_HARD = os.path.abspath('./assets/Difficulty - Hard.png')
DIFFICULTY_SINISTAR = os.path.abspath('./assets/Difficulty - Sinistar.png')
DIFFICULTY_SELECTOR = os.path.abspath('./assets/Difficulty - Selector.png')
DIFFICULTY_LABEL = os.path.abspath('./assets/Difficulty - Label.png')


VOLUME_SPRITE = os.path.abspath('./assets/Volume.png')
VOLUME_LABEL = os.path.abspath('./assets/Volume - Label.png')
VOLUME_SELECTOR = os.path.abspath('./assets/Volume - Selector.png')
VOLUME_MUTE = os.path.abspath('./assets/Mute.png')
VOLUME_INC = 10

INSTRUCTIONS = os.path.abspath('./assets/Help_Menu.png')

BACKGROUND = os.path.abspath('./assets/Star Background.png')

# Sounds
#sound_path = pathlib.Path(__file__).resolve().parents[1] / 'sounds'
THEME = os.path.abspath('./sounds/bensound-scifi.mp3')
EXPLOSION = os.path.abspath('./sounds/explosion.wav')
COMICAL_EXPLOSION = os.path.abspath('./sounds/boom.wav')
LASER = os.path.abspath('./sounds/laser.wav')
ENEMY_LASER = os.path.abspath('./sounds/laser-gun-19sf.mp3')
CRYSTAL_SOUND = os.path.abspath('./sounds/crystal_sound.ogg')
BOMB_EFFECT = os.path.abspath('./sounds/bomb_effect.wav')
CRYSTAL_PICKUP = os.path.abspath('./sounds/Crystal_Pickup.wav')
