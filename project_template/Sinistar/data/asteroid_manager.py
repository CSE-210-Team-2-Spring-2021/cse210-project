import arcade
import random
import math
from data import constants
from data.asteroid import Asteroid


class AsteroidManager(arcade.SpriteList):
    """This class manages the asteroid objects for use in Sinistar window"""

    def __init__(self, player_sprite):
        """Generate initial list of asteroids

        Args:
            self - an instance of AsteroidManager
        """
        super().__init__()
        self._boom = arcade.Sound(constants.COMICAL_EXPLOSION)
        self._start_size = 3
        self._count = constants.ASTEROID_COUNT
        self._generate_list(player_sprite)

    def _generate_list(self, player_sprite):
        """Fills self with asteroid objects

        Args:
            self - instance of AsteroidManager
        """
        for _ in range(self._count):
            # Set Position
            asteroid = Asteroid(player_sprite, self._start_size)
            self.append(asteroid)

    def respawn_asteroids(self, player_sprite, all_sprites):
        """Checks if asteroids need to be respawned, 
        if so it has a chance of respawning

        Args:
            self - instance of AsteroidManager
            all_sprites - List of all sprites
        """
        count = self._count
        num_asteroids = len(self)
        if num_asteroids < count:
            odds = 200
            dif = 1 - ((count - num_asteroids) / count)
            odds = math.ceil(odds * dif)
            if random.randrange(odds) == 0:
                asteroid = Asteroid(player_sprite, self._start_size)
                self.append(asteroid)
                all_sprites.append(asteroid)

    def split_asteroid(self, player_sprite, mother_of_all_asteroids, all_sprites_list):
        """ Splits Asteroids into chuncks when collision happens """
        broken_size = mother_of_all_asteroids.get_size()
        if broken_size > 1:
            for _ in range(random.randint(1, 3)):
                asteroid = Asteroid(player_sprite, broken_size - 1)
                asteroid.center_x = mother_of_all_asteroids.center_x
                asteroid.center_y = mother_of_all_asteroids.center_y
                self.append(asteroid)
                all_sprites_list.append(asteroid)

        mother_of_all_asteroids.kill()

    def set_count(self, count):
        self._count = count

    def get_count(self):
        return self._count
