import arcade
from data import constants
from data.laser import Laser

class LaserManager(arcade.SpriteList):
    """This class manages the asteroid objects for use in Sinistar window"""

    def __init__(self, _all_sprites_list, _player_sprite):
        """Generate initial list of lasers
        
        Args:
            self - an instance of LaserManager
        """
        super().__init__()
        self._laser_sprites_list = []
        self._generate_list(_all_sprites_list, _player_sprite)
        self._laser_sprites_list = self.get_lasers()
        
    def _generate_list(self, _all_sprites_list, _player_sprite):
        """Fills self with laser objects
        
        Args:
            self - instance of LaserManager
        """
        laser = Laser(_all_sprites_list, _player_sprite)
        self.append(laser)
        self._laser_sprites_list.append(self)
        _all_sprites_list.append(laser)
    
    def get_lasers(self):
        """Returns laser list"""

        return self._laser_sprites_list