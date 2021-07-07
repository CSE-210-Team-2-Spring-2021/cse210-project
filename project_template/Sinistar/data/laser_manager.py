import arcade
from data import constants
from data.laser import Laser

class AsteroidManager(arcade.SpriteList):
    """This class manages the asteroid objects for use in Sinistar window"""

    def __init__(self):
        """Generate initial list of lasers
        
        Args:
            self - an instance of LaserManager
        """
        super().__init__()
        self._generate_list()
        

    def _generate_list(self):
        """Fills self with laser objects
        
        Args:
            self - instance of LaserManager
        """
        laser = Laser()
        self.append(laser)