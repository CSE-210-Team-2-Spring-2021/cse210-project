import arcade
import random
from data import constants

class Ship(arcade.Sprite):
    """Subclass of Actors to create instances of Ship (Player)

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    def generate_ship(self, all_sprites):
        """Generates ship in the center of screen
            Args:
                self - An instance of Asteroid
                all_sprites - List of all sprites from WinistarWindow
        """
        
        self._player_sprite =  Ship(constants.PLAYER_SPRITE, constants.SPRITE_SCALING_PLAYER)
        self._player_sprite.center_x = constants.SCREEN_WIDTH/2
        self._player_sprite.center_y = constants.SCREEN_HEIGHT/2
        all_sprites.append(self._player_sprite)

    # add in each new instance of player ship
    def add_ship(self):
        player_ship = "S"
        x = int(constants.SCREEN_GRID_WIDTH / 2)
        y = int(constants.SCREEN_GRID_HEIGHT / 2)
        player_ship.set_location(x,y)
        player_ship.set_velocity(0,0)
        player_ship.set_toughness(1)
        player_ship.set_lives(constants.LIVES)
        self.player_ship.append(player_ship)
        self.all_sprites.append(player_ship)
    
    # Reset the ship
    def ship_reset(self):
        self.draw_ship()
        self.set_lives(constants.LIVES-1)

    
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
        return self._velocity

    def get_ship(self):
        """Returns player sprite
        
        Args:
            self - An instance of SHip
        """
        return self._player_sprite


   