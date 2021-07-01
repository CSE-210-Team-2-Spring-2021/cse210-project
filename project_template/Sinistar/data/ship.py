import arcade
import random, math
from data import constants

class Ship(arcade.Sprite):
    """Subclass of Actors to create instances of Ship (Player)

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    def __init__(self, all_sprites):
        """
        Class Constructor"""
        super().__init__(constants.PLAYER_SPRITE, constants.SPRITE_SCALING_PLAYER)
        self._player_sprite = None
        self._lives = None
        self.speed = 0
        self.angle = 90
        self.generate_ship(all_sprites)

    def generate_ship(self, all_sprites):
        """Generates ship in the center of screen
            Args:
                self - An instance of Asteroid
                all_sprites - List of all sprites from WinistarWindow
        """
        self.center_x = constants.SCREEN_WIDTH/2
        self.center_y = constants.SCREEN_HEIGHT/2
        self.set_lives(constants.LIVES)
        all_sprites.append(self)

    #def update(self):
    #    """Updates the ship sprite
    #    
    #    Args:
    #        self - an instance of Ship
    #    """
    #    # Convert angle in degrees to radians.
    #    angle_rad = math.radians(self.angle)
#
    #    # Rotate the ship
    #    self.angle += self.change_angle
#
    #    # Use math to find our change based on our speed and angle
    #    self.center_x += -self.speed * math.sin(angle_rad)
    #    self.center_y += self.speed * math.cos(angle_rad)


    
    def set_lives(self, lives):
        """Updates the ship's lives.
        
        Args:
            lives (int): How many lives
        """
        self._lives = lives

    
    def get_lives(self):
        """Gets the ship's lives.
        
        Returns:
            lives: The ship's lives.
        """
        return self._lives

    def get_ship(self):
        """Returns player sprite
        
        Args:
            self - An instance of SHip
        """
        return self


   