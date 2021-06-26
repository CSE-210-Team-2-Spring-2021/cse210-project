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

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. 
        
        Args:
            self - an instance of SinistarWindow
        """

        # Sprite lists
        self._all_sprites_list = arcade.SpriteList()

        # Set up the player
        self._player_sprite =  Ship(constants.PLAYER_SPRITE, constants.SPRITE_SCALING_PLAYER)
        self._player_sprite.center_x = constants.SCREEN_WIDTH/2
        self._player_sprite.center_y = constants.SCREEN_HEIGHT/2
        self._all_sprites_list.append(self._player_sprite)

        #Create Asteroids
        for _ in range(constants.ASTEROID_COUNT):
            asteroid = Asteroid(constants.ASTEROID_SPRITE, constants.SPRITE_SCALING_ASTEROIDS)

            #Set Position
            asteroid.center_x = random.randrange(constants.SCREEN_WIDTH)
            asteroid.center_y = random.randrange(constants.SCREEN_HEIGHT)
            #Set Speed
            asteroid.change_x = random.randint(-2, 2)
            asteroid.change_y = random.randint(-2, 2)

            self._all_sprites_list.append(asteroid)


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