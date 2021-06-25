import arcade
import random
from data import constants
from data import actors

class Asteroid(actors):
    """Subclass of Actors to create instances of asteroid

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    # instantiate as an Actor and inherit the init.
    def __init__(self):
        super().__init__()

    # add in each new instance of asteroid
    def add_asteroid(self):
        asteroid = arcade.Sprite("images/asteroid.png", constants.SPRITE_SIZE)
        asteroid.center_y = random.randrange(constants.SCREEN_HEIGHT) 
        asteroid.center_x = random.randrange(constants.SCREEN_WIDTH)
        asteroid.velocity = (random.randint(-5, 5), random.randint(5, -5))
        self.asteroids_list.append(asteroid)
        self.all_sprites.append(asteroid)
