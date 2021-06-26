import arcade
import random
from data import constants
from data import actors

class Ship(actors):
    """Subclass of Actors to create instances of Ship (Player)

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    # instantiate as an Actor and inherit the init.
    def __init__(self):
        super().__init__()
        self._lives = 0

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


   