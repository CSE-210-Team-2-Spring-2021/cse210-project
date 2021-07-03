import arcade
import math
from data import constants
# from data.projectile import Projectile

# Laser class for projectiles shooting from front of ship.


class EnemyLaser(arcade.Sprite):
    """Subclass of Actors to create instances of asteroid

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    # instantiate as a projectile sprite and inherit the init from arcade.Sprite.

    def __init__(self):
        """
        Class Constructor"""
        super().__init__(constants.ENEMY_LASER_SPRITE, constants.SPRITE_SCALING_ENEMY_LASERS)
        self._enemy_laser_sprites = []
        self._laser_speed = constants.LASER_SPEED

    def generate_laser(self, all_sprites, _enemy_sprite):
        """Generates each new instance of laser shooting from player ship
            Args:
                self - An instance of laser
                all_sprites - List of all sprites from WinistarWindow
        """
        # set velocity based off front of player ship
        self.change_y = math.cos(math.radians(_enemy_sprite.angle - 90)) * self._laser_speed
        self.change_x = -math.sin(math.radians(_enemy_sprite.angle - 90)) * self._laser_speed

        self.center_x = _enemy_sprite.center_x
        self.center_y = _enemy_sprite.center_y

        # add laser to laser list, and add to all sprites list
        self._enemy_laser_sprites.append(self)
        all_sprites.append(self)

    def delete_laser(self):
        """ updates to check if each laser leaves viewed play space, then removes that laser if yes.
            Args:
                self - an instance of laser
        """
        super().update()  # init from arcade.Sprite update functionality
        _enemy_laser_sprites = self._enemy_laser_sprites
        for _ in _enemy_laser_sprites:
            if self.center_x < 0 or self.center_x > constants.SCREEN_WIDTH or \
                    self.center_y > constants.SCREEN_HEIGHT or self.center_y < 0:
                self.kill()

    def get_lasers(self):
        """Returns laser list"""

        return self._enemy_laser_sprites
