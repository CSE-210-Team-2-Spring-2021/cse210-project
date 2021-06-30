import arcade
from data import constants
from data.asteroid import Asteroid

class AsteroidManager(arcade.SpriteList):
    """This class manages the asteroid objects for use in Sinistar window"""

    def __init__(self):
        """Generate initial list of asteroids
        
        Args:
            self - an instance of AsteroidManager
        """
        super().__init__()
        self._generate_list()
        

    def _generate_list(self):
        """Fills self with asteroid objects
        
        Args:
            self - instance of AsteroidManager
        """
        for _ in range(constants.ASTEROID_COUNT):
            #Set Position
            asteroid = Asteroid()
            self.append(asteroid)