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
    
    def set_path(self, path):
        """Sets the path attribute
        
        Args:
            self - instance of Enemies
            path - An astar path instance
        """
        self._path = path
        self._change_direction()

    def get_path(self):
        """Sets the path attribute
        
        Args:
            self - instance of Enemies
        """
        return self._path

    def _change_direction(self):
        """Sets the direciton to follow the path
        
        Args:
            self - instance of Warrior
        """
        if self._path:
            if len(self._path) > 2:
                print(self._path)
                start_x = self._path[0][0]
                start_y = self._path[0][1]
                end_x = self._path[1][0]
                end_y = self._path[1][1]
                direction = (end_x - start_x, end_y - start_y)


                self.change_x = direction[0]/constants.GRID * 2
                self.change_y = direction[1]/constants.GRID * 2
