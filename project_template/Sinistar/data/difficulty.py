from data import constants
from data import asteroid
from data import enemies
from data import menu
from data import sinistarwindow


class Difficulty():
    """ This class will determine the difficulty of the game based on user input from the menu. 

        Args:

    """

    def __init__(self):
        self._difficulty = constants.NORMAL

    def set_difficulty(self):
        if self._change_difficulty() == 1:
            self._difficulty = self._add_asteroid(
                1) & self._retrieve_difficulty(1)
        elif self._change_difficulty() == 2:
            self._difficulty = self._add_asteroid(
                2) & self._retrieve_difficulty(2)
        elif self._change_difficulty() == 3:
            self._difficulty = self._add_asteroid(
                3) & self._retrieve_difficulty(3)
        elif self._change_difficulty() == 4:
            self._difficulty = self._add_asteroid(
                4) & self._retrieve_difficulty(4)
        else:
            self._difficulty = self._add_asteroid(
                5) & self._retrieve_difficulty(5)
