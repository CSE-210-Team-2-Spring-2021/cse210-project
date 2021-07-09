import arcade
from data import sinistarwindow
from data import constants
from data.laser import Laser
from data.asteroid import Asteroid
from data.enemies import EnemyManager


class Collisions():
    """This class handles all of the collisions between objects"""

    def __init__(self):
        self._laser_sprites = Laser()
        self._enemy_sprites = EnemyManager()
        self._asteroid_sprites = Asteroid()
        #self._crystal_sprites = Bomb()

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
        if self._immunity <= 0:
            ship_hit = []

            asteroid_hit = arcade.check_for_collision_with_list(self._player_sprite,
                                                                self._asteroid_sprites)
            enemy_hit = arcade.check_for_collision_with_list(self._player_sprite,
                                                            self._enemy_sprites)
            ship_hit = asteroid_hit + enemy_hit

            if ship_hit != []:
                self._boom.play(self._volume, 0, False)
                self._immunity = constants.IMMUNITY
                self._score -= 100
                lives = self._ship.get_lives()
                if lives > 0:
                    self._ship.set_lives(lives - 1)
                    self._player_sprite.center_x = constants.SCREEN_WIDTH/2
                    self._player_sprite.center_y = constants.SCREEN_HEIGHT/2
                else:
                    # GAME OVER
                    self._menu.game_lost()
            else:
                self._score += 1
        else:
            self._immunity -= 1
