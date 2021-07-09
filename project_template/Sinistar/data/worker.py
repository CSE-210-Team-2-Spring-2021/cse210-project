import arcade
import random, math
from data import constants

class Worker(arcade.Sprite):

    def __init__(self, player_sprite):
        """
        Class Constructor
        """
        self.enemy_type = "Worker"
        super().__init__(constants.WORKER_SPRITE, constants.SPRITE_SCALING_ENEMIES)
        self._setup_worker(player_sprite)
        self.has_crystal = False

    def _setup_worker(self, player_sprite):
        """Responsible for assigning the position and velocity of worker
        
        Args:
            self - An Instance of Worker
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

    # add in each new instance of worker
    def add_worker(self):
        """Adds a worker when 1 is destroyed (will need more work later"""
        worker = "*"    # arcade.Sprite("images/worker.png", constants.SPRITE_SIZE)
        worker.center_y = random.randrange(constants.SCREEN_HEIGHT) 
        worker.center_x = random.randrange(constants.SCREEN_WIDTH)
        worker.velocity = (random.randint(-5, 5), random.randint(5, -5))
        self.workers_list.append(worker)
        self.all_sprites.append(worker)
    
    def get_workers(self):
        """Returns astroids list"""

        return self._workers

    def process_move(self, path, laser = None, all_sprites = None):
        """Updates path and movement
        
        Args:
            self - instance of Enemies
            path - the path from sprite to player
            laser - used if the sprite shoots a laser
        """
        self._set_path(path)
    
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

    def get_enemy_type(self):
        """
        
        """

        return self.enemy_type

    def receive_crystal_collision(self, collision):
        """Receive the collision with a crystal and update the texture.
        
        """

        if collision == True:
            self.has_crystal = True
            arcade.append_texture(constants.WORKER__CRYSTAL_SPRITE)
            arcade.set_texture(2)