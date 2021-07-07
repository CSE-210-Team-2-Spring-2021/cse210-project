import arcade
from data import constants
from data.constants import LASER_SPRITE, SCREEN_HEIGHT, SCREEN_WIDTH
from data.laser import Laser

class LaserManager(arcade.SpriteList):
    """This class manages the asteroid objects for use in Sinistar window"""

    def __init__(self, _all_sprites_list, _player_sprite):
        """Generate initial list of lasers
        
        Args:
            self - an instance of LaserManager
        """
        super().__init__()
        self._laser_sprites = []
        self._generate_list(_all_sprites_list, _player_sprite)
        self._laser_sprites = Laser.get_lasers(self)
        self.delete_laser(self)
        

    def _generate_list(self, _all_sprites_list, _player_sprite):
        """Fills self with laser objects
        
        Args:
            self - instance of LaserManager
        """
        laser = Laser(_all_sprites_list, _player_sprite)
        self.append(laser)
        self._laser_sprites.append(self)
        _all_sprites_list.append(laser)
    
    def delete_laser(self, _laser_sprites):
        """ updates to check if each laser leaves viewed play space, then removes that laser if yes.
    #         Args:
    #             self - an instance of laser
    #     """
        super().update()  # init from arcade.Sprite update functionality
        lasers = _laser_sprites
        for _ in lasers:
            if self.right < 5:
                self.kill()
            elif self.left > constants.SCREEN_WIDTH - 5:
                self.kill()
            elif self.bottom > constants.SCREEN_HEIGHT - 5:
                self.kill() 
            elif self.top < 5:
                self.kill()