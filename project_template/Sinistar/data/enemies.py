import arcade
import math
import random
from data import constants
from data.difficulty import Difficulty
from data.worker import Worker
from data.warrior import Warrior


class EnemyManager(arcade.SpriteList):
    """This class manages the enemy objects for use in Sinistar window"""

    def __init__(self, player_sprite):
        """Generate initial list of enemies

        Args:
            self - an instance of EnemyManager
        """
        super().__init__()

        self._path = None
        self._war_count = constants.WARRIOR_COUNT
        self._work_count = constants.WORKER_COUNT

    def generate_list(self, player_sprite):
        """Fills self with enemy objects

        Args:
            self - instance of EnemyManager
        """
        for _ in range(round(self._work_count)):
            # Set Position
            worker = Worker(player_sprite)
            self.append(worker)

        for _ in range(round(self._war_count)):
            # Set Position
            warrior = Warrior(player_sprite)
            self.append(warrior)

    def respawn_enemies(self, player_sprite, all_sprites):
        """Checks if asteroids need to be respawned, 
        if so it has a chance of respawning

        Args:
            self - instance of AsteroidManager
            all_sprites - List of all sprites
        """
        war_count = self._war_count
        work_count = self._work_count
        count = war_count + work_count
        num_enemies = len(self)
        if num_enemies < count:
            odds = 400
            war_dif = 1 - ((war_count - num_enemies) / count)
            war_odds = math.ceil(odds * war_dif)
            work_dif = 1 - ((work_count - num_enemies) / count)
            work_odds = math.ceil(odds * work_dif)
            if random.randrange(war_odds) == 0:
                warrior = Warrior(player_sprite)
                self.append(warrior)
                all_sprites.append(warrior)

            elif random.randrange(work_odds) == 0:
                worker = Worker(player_sprite)
                self.append(worker)
                all_sprites.append(worker)

    def set_count(self, war_count, work_count):
        """ Sets the count of the number of warriors and workings depending on the difficulty """
        self._war_count = war_count
        self._work_count = work_count

    def get_count(self):
        """ Returns the count of enemies """
        return self._count
