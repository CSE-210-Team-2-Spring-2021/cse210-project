import arcade


class Actors(arcade.Sprite):
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
        and velocity in 2d space.

        Stereotype:
            Information Holder

        Attributes:
             Lasers List (list) - sprite list variable for each instance to be added to
             Asteroids List (list) - sprite list variable for each instance to be added to
             All sprites List (list) - sprite list for each sprite list to be added to
    """

    def __init__(self):
        """The class constructor."""
        
        # Setup the empty sprite lists
        self.lasers_list = arcade.SpriteList()
        self.asteroids_list = arcade.SpriteList()   
        self.player_ship = arcade.SpriteList()     
        self.all_sprites = arcade.SpriteList()

    
   