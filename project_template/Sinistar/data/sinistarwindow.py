import arcade, random
from data import constants
from data.ship import Ship
from data.asteroid import Asteroid

class SinistarWindow(arcade.Window):
    """
    Main application class.

    Stereotype:
        Controller/Service Provider
    """

    def __init__(self, width, height, title):
        """
        Class Constructor
        
        Args:
            self - an instance of SinistarWindow
            width - width of screen
            height - height of screen
            title - title of window
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self._all_sprites_list = None

        # Set up the player info
        self._player_sprite = None

        #Create Class objects
        self._asteroid = Asteroid()
        self._ship = Ship()

        # Set the background color
        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)

    def setup(self):
        """ Set up the game and initialize the variables. 
        
        Args:
            self - an instance of SinistarWindow
        """

        # Sprite lists
        self._all_sprites_list = arcade.SpriteList()

        #Create Asteroids
        self._asteroid.generate_astroids(self._all_sprites_list)

        #Set up the player
        self._ship.generate_ship(self._all_sprites_list)
        self._player_sprite = self._ship.get_ship()


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self._all_sprites_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Updte all sprites
        self._all_sprites_list.update()

    def on_key_press(self, key, modifier):
        """Called when a key is pressed for movement

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP:
            self._player_sprite.change_y = constants.MOVEMENT_SPEED
        
        elif key == arcade.key.DOWN:
            self._player_sprite.change_y = -constants.MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self._player_sprite.change_x = -constants.MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self._player_sprite.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifier):
        """Called when a key stops being pressed

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self._player_sprite.change_y = 0

        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self._player_sprite.change_x = 0