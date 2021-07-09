from data import constants
from data import sinistarwindow
from data import asteroid
from data import enemies
from data import menu
from data import warrior


class Difficulty():
    """ This class will determine the difficulty of the game based on user input from the menu. 

        Args:

    """

    def __init__(self):
        self._enemy_difficulty = 3
        self._asteroid_difficulty = 3

    def _set_difficulty(self):
        if self._menu._change_difficulty() == 1:
            self._asteroid_difficulty = self._asteroid._
            self._enemy_difficulty = self._enemies._retrieve_difficulty
            self._difficulty = 1
        elif self._menu._change_difficulty() == 2:
            self._enemies._retrieve_difficulty
            self._difficulty = 2
        elif self._menu._change_difficulty() == 3:
            self._enemies._retrieve_difficulty
            self._difficulty = 3
        elif self._menu._change_difficulty() == 4:
            self._enemies._retrieve_difficulty
            self._difficulty = 4
        else:
            self._enemies._retrieve_difficulty
            self._difficulty = 5

    def _get_difficulty(self):
        """Returns the difficulty"""
        return self._difficulty
