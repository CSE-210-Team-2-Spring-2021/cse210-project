import arcade
from data import constants

class SinistarWindow(arcade.Window):
    """
    Main application class.

    Stereotype:
        Controller/Service Provider
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self._player_list = None

        # Set up the player info
        self._player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self._player_sprite = Player("<Sprite png here>", constants.SPRITE_SCALING_PLAYER)
        self._player_sprite.center_x = 50
        self._player_sprite.center_y = 50
        self._player_list.append(self._player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self._player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()