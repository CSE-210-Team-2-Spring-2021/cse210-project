from os import X_OK
import arcade
import random, math
from data import constants

class Asteroid(arcade.Sprite):
    """Subclass of Actors to create instances of asteroid

    Stereotype: Information Holder

    Attributes:
         
        
    """
    def __init__(self):
        """
        Class Constructor"""
        super().__init__(constants.ASTEROID_SPRITE, constants.SPRITE_SCALING_ASTEROIDS)
        self._setup_asteroid()

    def _setup_asteroid(self):
        """Responsible for assigning the position and velocity of asteroid
        
        Args:
            self - An Instance of Asteroid
        """
        x = constants.SCREEN_WIDTH
        y = constants.SCREEN_HEIGHT
        speed = 2
        exclude_group_x = range(math.ceil(x/2) - 200, math.ceil(x/2) + 200)
        exclude_group_y = range(math.ceil(y/2) - 200, math.ceil(y/2) + 200)

        self.center_x = random.randrange(x)
        while self.center_x in exclude_group_x:
            self.center_x = random.randrange(x)

        self.center_y = random.randrange(y)
        while self.center_y in exclude_group_y:
            self.center_y = random.randrange(x)

        #Set Speed
        self.change_x = random.randint(-speed, speed)
        self.change_y = random.randint(-speed, speed)

    # add in each new instance of asteroid
    def add_asteroid(self):
        """Adds an astroid when 1 is destroyed (will need more work later"""
        asteroid = "*"    # arcade.Sprite("images/asteroid.png", constants.SPRITE_SIZE)
        asteroid.center_y = random.randrange(constants.SCREEN_HEIGHT) 
        asteroid.center_x = random.randrange(constants.SCREEN_WIDTH)
        asteroid.velocity = (random.randint(-5, 5), random.randint(5, -5))
        self.asteroids_list.append(asteroid)
        self.all_sprites.append(asteroid)
    
    def get_asteroids(self):
        """Returns astroids list"""

        return self._asteroids