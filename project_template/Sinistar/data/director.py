from data import constants


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
        self._draw_board()
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            if self._cast[''][0].get_board():
                self._draw_board()
            elif self._cast[''] == []:
                self._draw_board(1)

            (constants.FRAME_LENGTH)

    def pause_game(self):
        """ This will pause the game """
        pass

    def do_collisions(self):
        """ This will handle collisions """
        for asteroid in self._asteroid:
            if self._ship.alive and asteroid.alive and self._ship.shield == False:
                too_close = self._ship.radius + asteroid.radius
                if (abs(self._ship.center.x - asteroid.center.x) < too_close and abs(self._ship.center.y - asteroid.center.y) < too_close):
                    self._asteroids += asteroid.hit()
                    self._ship.lives -= 1
                    self._ship.shield = True
                    if self._ship.lives <= 0:
                        self._ship.alive = False
                        self._is_playing = False

    def update_actors(self, actors):
        """ This will update the Actors """
        self.actors.update()

    def update_actions(self, actions):
        """ This will update the Actions """
        self.actions.update()
