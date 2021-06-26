import sys
import arcade
from data import constants


class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.

        Args:
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen

    def clear_screen(self):
        """Clears the Asciimatics buffer for the next rendering."""
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    def draw_board(self):
        """ Draws the board onto the screen. """
        window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        window.show_view()
        arcade.run()

    def draw_actor(self, actor):
        """Renders the given actor's sprite on the screen.

        Args:
            actor (Actor): The actor to render.
        """
        texture = actor.get_Sprite()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(texture, x, y)

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """
        for actor in actors:
            self.draw_actor.arcade.SpriteList(actor)

    def flush_buffer(self):
        """Renders the screen."""
        self._screen.refresh()
