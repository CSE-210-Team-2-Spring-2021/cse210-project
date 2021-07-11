from os import X_OK
import arcade
import random
import math
from data import constants


class Asteroid(arcade.Sprite):
    """Subclass of Actors to create instances of asteroid

    Stereotype: Information Holder

    Attributes:


    """

    def __init__(self, player_sprite, size):
        """
        Class Constructor"""
        super().__init__(constants.ASTEROID_SPRITE,
                         (constants.SPRITE_SCALING_ASTEROIDS * size / 3))
        self._setup_asteroid(player_sprite)
        self._size = size

    def _setup_asteroid(self, player_sprite):
        """Responsible for assigning the position and velocity of asteroid

        Args:
            self - An Instance of Asteroid
        """
        x = constants.SCREEN_WIDTH
        y = constants.SCREEN_HEIGHT
        speed = 2
        exclude_group_x = range(math.floor(player_sprite.center_x - 200),
                                math.ceil(player_sprite.center_x + 200))
        exclude_group_y = range(math.floor(player_sprite.center_y - 200),
                                math.ceil(player_sprite.center_y + 200))

        self.center_x = random.randrange(x)
        while self.center_x in exclude_group_x:
            self.center_x = random.randrange(x)

        self.center_y = random.randrange(y)
        while self.center_y in exclude_group_y:
            self.center_y = random.randrange(x)

        # Set Speed
        self.change_x = random.randint(-speed, speed)
        self.change_y = random.randint(-speed, speed)

    def get_size(self):
        return self._size
