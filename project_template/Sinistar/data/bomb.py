import arcade
import math
from data import constants

class Bomb(arcade.SpriteList):
    """Class to track the list of all Bombs in play
        Stereotype: Information Holder
    """

    def __init__(self):
        """Class Constructor"""
        super().__init__()
        self._bombs_amount = 0

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

    def crystal_to_bomb(self, crystal_sprites, player_sprite):
        """When the ship collides with crystal, a bomb is added to inventory for shooting.
            Args:
                self - An instance of Bomb
                crystal_sprites - list of all crystal sprites
                player_sprite - Player ship to collide with crystal
        """
        
        crystal_hit = arcade.check_for_collision_with_list(player_sprite, crystal_sprites)
        if crystal_hit:
            for crystal in crystal_hit:
                crystal.kill()
                if self._bombs_amount < 5:
                    self._bombs_amount += 1

    def generate_bomb(self, _player_sprite, all_sprites):
        """Generates each new instance of bomb shooting from player ship
            Args:
                self - An instance of bomb
                _player_sprite - player ship sprite
                all_sprites - List of all sprites from WinistarWindow
        """
        # set velocity based off front of player ship
        bomb = arcade.Sprite(constants.BOMB_SPRITE, constants.SPRITE_SCALING_BOMB)
        bomb.change_y = math.cos(math.radians(_player_sprite.angle - 90)) * 10
        bomb.change_x = -math.sin(math.radians(_player_sprite.angle - 90)) * 10

        bomb.center_x = _player_sprite.center_x
        bomb.center_y = _player_sprite.center_y

        # add bomb to bomb list, and add to all sprites list
        bomb.angle = _player_sprite.angle
        self.append(bomb)
        all_sprites.append(bomb)

    def get_bombs_amount(self):
        """ Returns the bomb count available"""

        return self._bombs_amount

    def get_bombs_list(self):
        """ Returns the list of bomb sprites"""

        return self._bomb_sprites