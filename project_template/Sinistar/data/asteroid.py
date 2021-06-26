import arcade
import random
from data import constants
from data import actors

class Asteroid(arcade.Sprite):
    """Subclass of Actors to create instances of asteroid

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
        
    """
    def generate_astroids(self, all_sprites):
        """Creates astroid sprites with random location and velocity
        Args:
            self - An instance of Asteroid
            all_sprites - List of all sprites from WinistarWindow"""
        for _ in range(constants.ASTEROID_COUNT):
            asteroid = Asteroid(constants.ASTEROID_SPRITE, constants.SPRITE_SCALING_ASTEROIDS)

            #Set Position
            asteroid.center_x = random.randrange(constants.SCREEN_WIDTH)
            asteroid.center_y = random.randrange(constants.SCREEN_HEIGHT)
            #Set Speed
            asteroid.change_x = random.randint(-2, 2)
            asteroid.change_y = random.randint(-2, 2)

            all_sprites.append(asteroid)

    # add in each new instance of asteroid
    def add_asteroid(self):
        """Adds an astroid when 1 is destroyed (will need more work later"""
        asteroid = "*"    # arcade.Sprite("images/asteroid.png", constants.SPRITE_SIZE)
        asteroid.center_y = random.randrange(constants.SCREEN_HEIGHT) 
        asteroid.center_x = random.randrange(constants.SCREEN_WIDTH)
        asteroid.velocity = (random.randint(-5, 5), random.randint(5, -5))
        self.asteroids_list.append(asteroid)
        self.all_sprites.append(asteroid)

    def get_astroids(self):
        """Returns astroids sprite list
        Args:
            self - an instance of Astroid"""

        return self._asteroids
    