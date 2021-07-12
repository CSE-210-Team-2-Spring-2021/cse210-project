class Difficulty():
    """ This class will determine the difficulty of the game based on user input from the menu. 

        Args:

    """

    def set_difficulty(self, difficulty, asteroid_manager, enemies):
        if difficulty == 1:
            asteroid_manager.set_count(5)
            enemies.set_count(1, 1)
        elif difficulty == 2:
            asteroid_manager.set_count(7)
            enemies.set_count(2, 2)
        elif difficulty == 3:
            asteroid_manager.set_count(10)
            enemies.set_count(2, 4)
        elif difficulty == 4:
            asteroid_manager.set_count(15)
            enemies.set_count(4, 6)
        else:
            asteroid_manager.set_count(20)
            enemies.set_count(8, 10)
