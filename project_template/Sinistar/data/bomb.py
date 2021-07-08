import arcade
from data import constants

class Bomb(arcade.SpriteList):
    """Class to track the list of all Bombs in play

        Stereotype: Information Holder
    """

    def __init__(self):
        """Class Constructor"""
        super().__init__()

    def generate_crystal(self, asteroid, crystal_sprites, all_sprites):
        """When an asteroid explodes, it has a chance to drop a crystal. 
            Enemy Worker to pick it up later.
            Args:
                self - An instance of Bomb
                asteroid_sprites - SpriteList of all asteroids
                all_sprites - List of all sprites from sinistarwindow
        """
        # Set position and zero velocity based off destroyed asteroid position.
        crystal = arcade.Sprite(constants.CRYSTAL_SPRITE, constants.SPRITE_SCALING_CRYSTALS)
        crystal.center_x = asteroid.center_x
        crystal.center_y = asteroid.center_y

        crystal_sprites.append(crystal)
        all_sprites.append(crystal)