import arcade
from data import constants
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
        self._generate_list()
        

    def _generate_list(self):
        """Fills self with enemy objects
        
        Args:
            self - instance of EnemyManager
        """
        for _ in range(constants.WARRIOR_COUNT):
            #Set Position
            worker = Worker()
            self.append(worker)

        for _ in range(constants.WORKER_COUNT):
            #Set Position
            warrior = Warrior()
            self.append(warrior)