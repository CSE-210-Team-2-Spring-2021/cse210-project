import arcade
import random, math
from data import constants
from data.enemy_laser import EnemyLaser

class Warrior(arcade.Sprite):

    def __init__(self, player_sprite):
        """
        Class Constructor
        """
        self.enemy_type = "Warrior"
        super().__init__(constants.WARRIOR_SPRITE, constants.SPRITE_SCALING_ENEMIES)
        self._setup_warrior(player_sprite)
        self.has_crystal = False

    def _setup_warrior(self, player_sprite):
        """Responsible for assigning the position and velocity of warrior
        
        Args:
            self - An Instance of warrior
        """
        x = constants.SCREEN_WIDTH
        y = constants.SCREEN_HEIGHT
        speed = 2
        exclude_group_x = range(math.ceil(player_sprite.center_x - 200),
                                math.ceil(player_sprite.center_x + 200))
        exclude_group_y = range(math.ceil(player_sprite.center_y - 200), 
                                math.ceil(player_sprite.center_y + 200))

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

    def process_move(self, path, enemy_lasers, all_sprites):
        """Updates path and movement
        
        Args:
            self - instance of Enemies
            path - the path from sprite to player
            enemy_lasers - Enemy laser object
        """
        self._set_path(path)
        self._change_direction()
        self._shoot_at_player(enemy_lasers, all_sprites)
    
    def _set_path(self, path):
        """Sets the path attribute
        
        Args:
            self - instance of Enemies
            path - An astar path instance
        """
        self._path = path

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
                start_x = self._path[0][0]
                start_y = self._path[0][1]
                end_x = self._path[1][0]
                end_y = self._path[1][1]
                direction = (end_x - start_x, end_y - start_y)


                self.change_x = direction[0]/constants.GRID * 2
                self.change_y = direction[1]/constants.GRID * 2
    
    def _shoot_at_player(self, enemy_lasers, all_sprites):
        """Decides if the enemy should shoot at the player
        
        Args:
            self - Instance of ai
            enemy_sprite - An enemy Sprite
        """
        odds = 200

        if random.randrange(odds) == 0:
            enemy_lasers.generate_laser(self, all_sprites)

    def get_enemy_type(self):
        """
        
        """

        return self._enemy_type
