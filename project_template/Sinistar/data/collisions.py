import arcade
from data import sinistarwindow
from data import constants
from data.laser import Laser
from data.asteroid import Asteroid
from data.enemies import EnemyManager


class Collisions():
    """This class handles all of the collisions between objects"""

    def handle_collisions(self):
        self._laser_sprites.delete_laser()
        _lasers = self._laser_sprites.get_lasers()
        for _laser in _lasers:
            asteroids = arcade.check_for_collision_with_list(self._laser_sprites,
                                                             self._asteroid_sprites)
            enemies = arcade.check_for_collision_with_list(self._laser_sprites,
                                                           self._enemy_sprites)
        for asteroid in asteroids:
            self._explosion.play(self._volume, 0, False)
            self._score += 50
            asteroid.kill()
            _laser.kill()
        for enemy in enemies:
            self._explosion.play(self._volume, 0, False)
            self._score += 200
            enemy.kill()
            _laser.kill()

    def is_ship_hit(self, player_sprite, asteroid_sprites, enemy_sprites, enemy_laser_sprites):
        asteroid_hit = arcade.check_for_collision_with_list(player_sprite,
                                                            asteroid_sprites)
        enemy_hit = arcade.check_for_collision_with_list(player_sprite,
                                                         enemy_sprites)
        enemy_laser_hit = arcade.check_for_collision_with_list(player_sprite,
                                                               enemy_laser_sprites)
        if asteroid_hit or enemy_hit or enemy_laser_hit:
            if enemy_laser_hit:
                enemy_laser_hit[0].kill()
            return True
        else:
            return False
