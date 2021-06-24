from game import constants


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._is_paused = False
        self._is_playing = True
        self._cast = cast
        self._script = script
        self._first_run = True

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        self._keep_playing()
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if self._cast[''][0].get_floor():
                self._keep_playing()
            elif self._cast[''] == []:
                self._keep_playing(1)

            (constants.FRAME_LENGTH)

    def pause_game(self):
        """ This will pause the game """
        pass

    def do_collisions(self):
        """ This will handle collisions """
        # game_over condition: if lives = 0, then self._is_playing = False
        pass

    def update_actors(self):
        """ This will update the Actors """
        pass

    def update_actions(self):
        """ This will update the Actions """
        pass
