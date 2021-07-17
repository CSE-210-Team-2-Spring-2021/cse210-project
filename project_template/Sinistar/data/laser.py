import arcade
import random
import math
from data import constants


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
        self._player_laser_sprites = []

    def generate_laser(self, _player_sprite, all_sprites):
        """Generates each new instance of laser shooting from player ship
            Args:
                self - An instance of laser
                _player_sprite - player ship sprite
                all_sprites - List of all sprites from WinistarWindow
        """
        # set velocity based off front of player ship
        laser = arcade.Sprite(constants.LASER_SPRITE,
                              constants.SPRITE_SCALING_LASERS, hit_box_algorithm = "Detailed")
        laser.change_y = math.cos(math.radians(_player_sprite.angle - 90)) * 10
        laser.change_x = -math.sin(math.radians(_player_sprite.angle - 90)) * 10

        laser.center_x = _player_sprite.center_x
        laser.center_y = _player_sprite.center_y

        # add laser to laser list, and add to all sprites list
        laser.angle = _player_sprite.angle
        self.append(laser)
        all_sprites.append(laser)

    def update_player_lasers(self, player_sprite, player_laser_sprites, enemy_sprites, 
                asteroid_sprites, explosion, crystal, volume, all_sprites, crystal_sprites, score):
        """Update and check each player laser for collisions with asteroids, enemies, and screen boundaries
            Args:
                self - an instance of LaserManager
                player_laser_sprites - SpriteList of all player laser sprites
                enemy_sprites - SpriteList of all enemies
                asteroid_sprites - SpriteList of all asteroids
                explosion - Sound for enemy sprite death
                volume - Volume of explosion sound
                all_sprites - List of all sprites from sinistarwindow
                score - Total running score from sinistarwindow
        """
        odds = 2

        for laser in player_laser_sprites:
            asteroids = arcade.check_for_collision_with_list(
                laser, asteroid_sprites)
            enemies = arcade.check_for_collision_with_list(
                laser, enemy_sprites)
            for asteroid in asteroids:
                if random.randrange(odds) == 0:
                    crystal.play(volume + 4, 0, False)
                    crystal_sprites.generate_crystal(asteroid, crystal_sprites, all_sprites)
                else:
                    score += 50
                    explosion.play(volume, 0, False)
                    asteroid_sprites.split_asteroid(
                    player_sprite, asteroid, all_sprites)
                    laser.kill()

            for enemy in enemies:
                score += 200
                explosion.play(volume, 0, False)
                enemy.kill()
                laser.kill()
        return score
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
