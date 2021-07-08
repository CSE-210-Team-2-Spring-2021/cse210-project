import arcade
import math
from data import constants
# from data.projectile import Projectile

# Laser class for projectiles shooting from front of ship.


class Laser(arcade.SpriteList):
    """Subclass of arcade to create instances of laser

    Stereotype: Information Holder
    """
    # instantiate as a sprite and inherit the init from arcade.SpriteList.

    def __init__(self):
        """
        Class Constructor"""
        super().__init__()
        self._laser_speed = constants.LASER_SPEED

    def generate_laser(self, _player_sprite, all_sprites):
        """Generates each new instance of laser shooting from player ship
            Args:
                self - An instance of laser
                all_sprites - List of all sprites from WinistarWindow
        """
        # set velocity based off front of player ship
        laser = arcade.Sprite(constants.LASER_SPRITE, constants.SPRITE_SCALING_LASERS)
        laser.change_y = math.cos(math.radians(_player_sprite.angle - 90)) * 9
        laser.change_x = -math.sin(math.radians(_player_sprite.angle - 90)) * 9

        laser.center_x = _player_sprite.center_x
        laser.center_y = _player_sprite.center_y

        # add laser to laser list, and add to all sprites list
        laser.angle = _player_sprite.angle
        self.append(laser)
        all_sprites.append(laser)

    def update_player_lasers(self, player_laser_sprites, enemy_sprites, asteroid_sprites, explosion, volume):
        """Update and check each player laser for collisions with asteroids, enemies, and screen boundaries

            Args:
                self - an instance of LaserManager
                player_laser_sprites - SpriteList of all player laser sprites
                enemy_sprites - SpriteList of all enemies
                asteroid_sprites - SpriteList of all asteroids
                explosion - Sound for enemy sprite death
                volume - Volume of explosion sound
        """
        for laser in player_laser_sprites:
            asteroids = arcade.check_for_collision_with_list(laser, asteroid_sprites)
            enemies = arcade.check_for_collision_with_list(laser, enemy_sprites)
            for asteroid in asteroids:
                explosion.play(volume, 0, False)
                self._score += 50
                asteroid.kill()
                laser.kill()
            for enemy in enemies:
                explosion.play(volume, 0, False)
                self._score += 200
                enemy.kill()
                laser.kill()

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

    def get_player_lasers(self):
        """Returns list of all player lasers
        """
        return self._player_laser_sprites