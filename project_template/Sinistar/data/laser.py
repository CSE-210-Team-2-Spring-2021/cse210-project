import arcade
import random
from data import constants
from data import actors

#test

class Laser(actors):
    """Subclass of Actors to create instances of asteroid

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    # instantiate as an Actor and inherit the init.
    def __init__(self):
        super().__init__()

    # add in each new instance of laser shooting from player ship
    def add_laser(self):
        laser = "!"     # arcade.Sprite("images/laser.png", constants.SPRITE_SIZE)

        # need to modify this for shooting from the front of player ship

        # laser.center_y = random.randrange(constants.SCREEN_HEIGHT) 
        # laser.center_x = random.randrange(constants.SCREEN_WIDTH)
        # laser.velocity = (random.randint(-5, 5), random.randint(5, -5))
        self.lasers_list.append(laser)
        self.all_sprites.append(laser)
