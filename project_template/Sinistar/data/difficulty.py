class Difficulty():
    """ This class will determine the difficulty of the game based on user input from the menu. 

        Args:

    """

    def _set_difficulty(self, menu, asteroid_manager, enemies):
        if menu.get_difficulty() == 1:
            asteroid_manager.set_count(10)
            enemies.set_count(2, 2)
        elif menu.get_difficulty() == 2:
            asteroid_manager.set_count(15)
            enemies.set_count(3, 3)
        elif menu.get_difficulty() == 3:
            asteroid_manager.set_count(20)
            enemies.set_count(5, 5)
        elif menu.get_difficulty() == 4:
            asteroid_manager.set_count(25)
            enemies.set_count(8, 8)
        else:
            asteroid_manager.set_count(30)
            enemies.set_count(10, 10)