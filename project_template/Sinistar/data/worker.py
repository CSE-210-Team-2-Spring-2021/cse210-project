import arcade
import random, math
from data import constants

class Worker(arcade.Sprite):

    def __init__(self):
        """
        Class Constructor
        """
        super().__init__(constants.WORKER_SPRITE, constants.SPRITE_SCALING_ENEMIES)
        self._setup_worker()

    def _setup_worker(self):
        """Responsible for assigning the position and velocity of worker
        
        Args:
            self - An Instance of Worker
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