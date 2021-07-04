from data import constants
from data import sinistarwindow
from data import asteroid
from data import enemies
from data import menu


class Difficulty():
    """ This class will determine the difficulty of the game based on user input from the menu. 

        Args:

    """

    def __init__(self):
        self._difficulty = constants.NORMAL

    def _set_difficulty(self):
        if self._menu._change_difficulty() == 1:
            self._difficulty = self._asteroid.add_asteroid(
                1) & self._enemies.retrieve_difficulty(1)
        elif self._menu._change_difficulty() == 2:
            self._difficulty = self._asteroid.add_asteroid(
                2) & self._enemies.retrieve_difficulty(2)
        elif self._menu._change_difficulty() == 3:
            self._difficulty = self._asteroid.add_asteroid(
                3) & self._enemies.retrieve_difficulty(3)
        elif self._menu._change_difficulty() == 4:
            self._difficulty = self._asteroid.add_asteroid(
                4) & self._enemies.retrieve_difficulty(4)
        else:
            self._difficulty = self._asteroid.add_asteroid(
                5) & self._enemies.retrieve_difficulty(5)

    def _get_difficulty(self):
        """Returns the difficulty"""
        return self._difficulty
