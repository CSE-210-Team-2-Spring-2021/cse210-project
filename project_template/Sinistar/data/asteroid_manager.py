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
        self._generate_list(player_sprite)
        self._boom = arcade.Sound(constants.COMICAL_EXPLOSION)

    def _generate_list(self, player_sprite):
        """Fills self with asteroid objects

        Args:
            self - instance of AsteroidManager
        """
        for _ in range(constants.ASTEROID_COUNT):
            # Set Position
            asteroid = Asteroid(player_sprite)
            self.append(asteroid)

    def respawn_asteroids(self, player_sprite, all_sprites):
        """Checks if asteroids need to be respawned, 
        if so it has a chance of respawning

        Args:
            self - instance of AsteroidManager
            all_sprites - List of all sprites
        """
        count = constants.ASTEROID_COUNT
        num_asteroids = len(self)
        if num_asteroids < count:
            odds = 200
            dif = 1 - ((count - num_asteroids) / count)
            odds = math.ceil(odds * dif)
            if random.randrange(odds) == 0:
                asteroid = Asteroid(player_sprite)
                self.append(asteroid)
                all_sprites.append(asteroid)

    def split_asteroid(self, player_sprite, mother_of_all_asteroids):
        """ Splits Asteroids into chuncks when collision happens """
        asteroid = Asteroid(
            player_sprite, constants.SPRITE_SCALING_ASTEROIDS)
        x = mother_of_all_asteroids.center.x
        y = mother_of_all_asteroids.center.y
        mother_of_all_asteroids.kill()

        if asteroid.size == 4:
            for _ in range(3):
                image_no = random.randrange(2)
                image_list = []

                enemy_sprite = Asteroid(
                    image_list[image_no], self.constants.SPRITE_ASTEROIDS * 1.5)
                enemy_sprite.center_x = x
                enemy_sprite.center_y = y

                enemy_sprite.change_x = random.random() * 2.5 - 1.25
                enemy_sprite.change_y = random.random() * 2.5 - 1.25

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 3
                self.asteroid_list.append(enemy_sprite)
                self._boom

        elif asteroid.size == 3:
            for _ in range(3):
                image_no = random.randrange(2)
                image_list = []

                enemy_sprite = Asteroid(
                    image_list[image_no], self.constants.SPRITE_ASTEROIDS * 1.5)
                enemy_sprite.center_x = x
                enemy_sprite.center_y = y

                enemy_sprite.change_x = random.random() * 3 - 1.5
                enemy_sprite.change_y = random.random() * 3 - 1.5

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 2
                self.asteroid_list.append(enemy_sprite)
                self._boom

        elif asteroid.size == 2:
            for _ in range(3):
                image_no = random.randrange(2)
                image_list = []

                enemy_sprite = Asteroid(
                    image_list[image_no], self.constants.SPRITE_ASTEROIDS * 1.5)
                enemy_sprite.center_x = x
                enemy_sprite.center_y = y

                enemy_sprite.change_x = random.random() * 3.5 - 1.75
                enemy_sprite.change_y = random.random() * 3.5 - 1.75

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 2
                self.asteroid_list.append(enemy_sprite)
                self._boom

        else:
            self._boom
