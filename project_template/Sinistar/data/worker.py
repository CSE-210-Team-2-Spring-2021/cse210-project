import arcade
import random, math
from data import constants

class Worker(arcade.Sprite):

    def __init__(self, player_sprite):
        """
        Class Constructor
        """
        self.enemy_type = "Worker"
        super().__init__(constants.WORKER_SPRITE, constants.SPRITE_SCALING_ENEMIES, hit_box_algorithm = "Detailed")
        self._setup_worker(player_sprite)
        self.has_crystal = False
        self._crystals_exist = False

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
        """Adds a worker when 1 is destroyed (will need more work later
        """
        worker = "*"    # arcade.Sprite("images/worker.png", constants.SPRITE_SIZE)
        worker.center_y = random.randrange(constants.SCREEN_HEIGHT) 
        worker.center_x = random.randrange(constants.SCREEN_WIDTH)
        worker.velocity = (random.randint(-5, 5), random.randint(5, -5))
        self.workers_list.append(worker)
        self.all_sprites.append(worker)
    
    def get_workers(self):
        """Returns workers list
        """

        return self._workers

    def process_move(self, path, laser = None, all_sprites = None):
        """Updates path and movement
        
        Args:
            self - instance of Enemies
            path - the path from sprite to player
            laser - used if the sprite shoots a laser
        """
        self._set_path(path)
        self._change_direction()

    def _change_direction(self):
        """Sets the direciton to follow the path
        
        Args:
            self - instance of Warrior
        """
        if ((self.center_x - constants.SCREEN_WIDTH) > 2) and ((0 - self.center_x) < -2):
            if ((self.center_y - constants.SCREEN_HEIGHT) > 2) and ((0 - self.center_y) < -2):
                if self._path:
                    if len(self._path) > 2:
                        start_x = self._path[0][0]
                        start_y = self._path[0][1]
                        end_x = self._path[1][0]
                        end_y = self._path[1][1]
                    
                        if self._crystals_exist and self.has_crystal == False:
                            direction = (end_x - start_x, end_y - start_y)

                        else:
                            direction = (-(end_x - start_x), -(end_y - start_y))

                        self.change_x = direction[0]/constants.GRID * 2
                        self.change_y = direction[1]/constants.GRID * 2
    
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
        """Returns the type of enemy of this object
        
        Args:
            self - instance of Enemies
        """

        return self.enemy_type

    def receive_crystal_collision(self, crystal_sprites, enemy_sprites):
        """Receive the collision with a crystal and update the texture.
        
        Args:
            self - an instance of the worker object.
            crystal_sprites(list) - a list of all crystal sprites in play
            enemy_sprites(list) - a list of all enemy sprites
        """

        worker_crystal_texture = arcade.load_texture(constants.WORKER_CRYSTAL_SPRITE)
        for enemy in enemy_sprites:
            if enemy.enemy_type == "Worker" and enemy.has_crystal == False:
                crystal_hit = arcade.check_for_collision_with_list(enemy, crystal_sprites)
                if crystal_hit:
                    self._texture = worker_crystal_texture
                    enemy.has_crystal = True
                    for crystal in crystal_hit:
                        crystal.kill()

    def crystal_exists(self, exists):
        """Sets attribute to True if Crystal exists
        
        Args:
            self - an instance of Worker
            exists - Bool if crystals exist"""

        self._crystals_exist = exists