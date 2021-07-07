import arcade
from data import constants
from data.menu import Menu
from data.worker import Worker
from data.warrior import Warrior

class EnemyManager(arcade.SpriteList):
    """This class manages the enemy objects for use in Sinistar window"""

    def __init__(self):
        """Generate initial list of enemies
        
        Args:
            self - an instance of EnemyManager
        """
        super().__init__()
        
        self.menu = Menu()
        difficulty_mod = self._retrieve_difficulty()
        self._generate_list(difficulty_mod)
        self._path = None
        

    def _generate_list(self, difficulty_mod):
        """Fills self with enemy objects
        
        Args:
            self - instance of EnemyManager
        """
        for _ in range(round(constants.WARRIOR_COUNT * difficulty_mod)):
            #Set Position
            worker = Worker()
            self.append(worker)

        for _ in range(round(constants.WORKER_COUNT * difficulty_mod)):
            #Set Position
            warrior = Warrior()
            self.append(warrior)

    def _retrieve_difficulty(self):
        """
        
        """

        diff_temp = self.menu.get_difficulty()

        if diff_temp == 1:
            difficulty_modifier = .2
        elif diff_temp == 2:
            difficulty_modifier = .4
        elif diff_temp == 3:
            difficulty_modifier = .6
        elif diff_temp == 4:
            difficulty_modifier = .8
        else:
            difficulty_modifier = 1

        return difficulty_modifier