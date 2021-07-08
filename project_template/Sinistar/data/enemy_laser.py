import arcade
import math
from data import constants
# from data.projectile import Projectile

# Laser class for projectiles shooting from front of ship.


class EnemyLaser(arcade.SpriteList):
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
        super().__init__()
        self._laser_speed = constants.LASER_SPEED

    def generate_laser(self, _enemy_sprite, all_sprites):
        """Generates each new instance of laser shooting from player ship
            Args:
                self - An instance of laser
                all_sprites - List of all sprites from WinistarWindow
        """
        # set velocity based off front of enemy ship
        laser = arcade.Sprite(constants.ENEMY_LASER_SPRITE, constants.SPRITE_SCALING_ENEMY_LASERS)
        laser.change_y = math.cos(math.radians(_enemy_sprite.angle)) * self._laser_speed
        laser.change_x = -math.sin(math.radians(_enemy_sprite.angle)) * self._laser_speed

        laser.center_x = _enemy_sprite.center_x
        laser.center_y = _enemy_sprite.center_y

        laser.angle = _enemy_sprite.angle
        self.append(laser)
        all_sprites.append(laser)
        
    def delete_laser(self):
        """ updates to check if each laser leaves viewed play space, then removes that laser if yes.
            Args:
                self - an instance of laser
        """
        for laser in self:
            if laser.right > constants.SCREEN_WIDTH - 5:
                laser.remove_from_sprite_lists()
                
            elif laser.left < 5:
                laser.remove_from_sprite_lists()
                
            elif laser.bottom < 5:
                laser.remove_from_sprite_lists()
                
            elif laser.top > constants.SCREEN_HEIGHT - 5:
                laser.remove_from_sprite_lists()
                
