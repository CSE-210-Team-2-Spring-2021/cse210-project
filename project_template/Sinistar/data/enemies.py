import arcade
import random
from data import constants

class Enemy():
    """
    
    """

    def __init__(self): 
        """set default attributes of enemies."""

        _toughness = 1
        

    def generate_enemies(self, all_sprites): 
        """will decide which type of enemy will be outputted to the screen."""

        self._enemy_sprite = Enemy(constants.PLAYER_SPRITE, constants.SPRITE_SCALING_PLAYER)
        self._enemy_sprite.center_x = constants.SCREEN_WIDTH/2
        self._enemy_sprite.center_y = constants.SCREEN_HEIGHT/2
        all_sprites.append(self._enemy_sprite)

        for _ in range(constants.enemy_COUNT):
            enemy = enemy(constants.enemy_SPRITE, constants.SPRITE_SCALING_enemyS)

            #Set Position
            enemy.center_x = random.randrange(constants.SCREEN_WIDTH)
            while enemy.center_x in exclude_group_x:
                enemy.center_x = random.randrange(constants.SCREEN_WIDTH)

            enemy.center_y = random.randrange(constants.SCREEN_HEIGHT)
            while enemy.center_y in exclude_group_y:
                enemy.center_y = random.randrange(constants.SCREEN_WIDTH)
                
            #Set Speed
            enemy.change_x = random.randint(-2, 2)
            enemy.change_y = random.randint(-2, 2)

            all_sprites.append(enemy)
            self._enemys.append(enemy)

    def respawn_enemies(self): 
        """respawns enemies after they are killed off."""
    
    def get_enemies(self): 
        """retreives enemies to be added."""
    
    def set_toughness(self): 
        """determines the amount of damage each enemy can take."""
    
    def ai_destroy(self): 
        """creates the AI for enemies to shoot and chase after player."""