import arcade
import random, math
from data import constants

class Warrior(arcade.Sprite):

    def __init__(self):
        """
        Class Constructor
        """
        super().__init__(constants.WARRIOR_SPRITE, constants.SPRITE_SCALING_ENEMIES)
        self._setup_warrior()

    def _setup_warrior(self):
        """Responsible for assigning the position and velocity of warrior
        
        Args:
            self - An Instance of warrior
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

    # add in each new instance of warrior
    def add_warrior(self):
        """Adds a warrior when 1 is destroyed (will need more work later"""
        warrior = "*"    # arcade.Sprite("images/warrior.png", constants.SPRITE_SIZE)
        warrior.center_y = random.randrange(constants.SCREEN_HEIGHT) 
        warrior.center_x = random.randrange(constants.SCREEN_WIDTH)
        warrior.velocity = (random.randint(-5, 5), random.randint(5, -5))
        self.warriors_list.append(warrior)
        self.all_sprites.append(warrior)
    
    def get_warriors(self):
        """Returns astroids list"""

        return self._warriors