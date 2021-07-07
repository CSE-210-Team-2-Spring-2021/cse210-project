import arcade
import random
import math
from data import constants
# from data.projectile import Projectile

# Laser class for projectiles shooting from front of ship.


class Laser(arcade.Sprite):
    """Subclass of Actors to create instances of asteroid

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    # instantiate as a projectile sprite and inherit the init from arcade.Sprite.

    def __init__(self, _all_sprites_list, _player_sprite):
        """
        Class Constructor"""
        super().__init__(constants.LASER_SPRITE, constants.SPRITE_SCALING_LASERS)
        self._laser_speed = constants.LASER_SPEED
        self.generate_laser(_all_sprites_list, _player_sprite)

    def generate_laser(self, _all_sprites_list, _player_sprite):
        """Generates each new instance of laser shooting from player ship
            Args:
                self - An instance of laser
                all_sprites - List of all sprites from WinistarWindow
        """
        # set velocity based off front of player ship
        self.change_y = math.cos(math.radians(_player_sprite.angle - 90)) * self._laser_speed
        self.change_x = -math.sin(math.radians(_player_sprite.angle - 90)) * self._laser_speed

        self.center_x = _player_sprite.center_x
        self.center_y = _player_sprite.center_y

        # add laser to laser list, and add to all sprites list
        # self._laser_sprites.append(self)
        # all_sprites.append(self)

    def delete_laser(self, _laser_sprites_list):
        """ updates to check if each laser leaves viewed play space, then removes that laser if yes.
            Args:
                self - an instance of laser
        """
        #super().update(self)  # init from arcade.Sprite update functionality
        lasers = _laser_sprites_list
        for _ in lasers:
            if self.right < 5:
                self.kill()
            elif self.left > constants.SCREEN_WIDTH - 5:
                self.kill()
            elif self.bottom > constants.SCREEN_HEIGHT - 5:
                self.kill() 
            elif self.top < 5:
                self.kill()
