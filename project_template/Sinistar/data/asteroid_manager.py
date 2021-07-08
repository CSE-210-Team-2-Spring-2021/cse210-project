import arcade, random, math
from data import constants
from data.asteroid import Asteroid

class AsteroidManager(arcade.SpriteList):
    """This class manages the asteroid objects for use in Sinistar window"""

    def __init__(self, player_sprite):
        """Generate initial list of asteroids
        
        Args:
            self - an instance of AsteroidManager
        """
        super().__init__()
        self._generate_list(player_sprite)
        

    def _generate_list(self, player_sprite):
        """Fills self with asteroid objects
        
        Args:
            self - instance of AsteroidManager
        """
        for _ in range(constants.ASTEROID_COUNT):
            #Set Position
            asteroid = Asteroid(player_sprite)
            self.append(asteroid)

    def respawn_asteroids(self, player_sprite, all_sprites):
        """Checks if asteroids need to be respawned, 
        if so it has a chance of respawning
        
        Args:
            self - instance of AsteroidManager
            all_sprites - List of all sprites
        """
        count =  constants.ASTEROID_COUNT
        num_asteroids = len(self)
        if num_asteroids < count:
            odds = 200
            dif = 1 - ((count - num_asteroids) / count)
            odds = math.ceil(odds * dif)
            if random.randrange(odds) == 0:
                asteroid = Asteroid(player_sprite)
                self.append(asteroid)
                all_sprites.append(asteroid)