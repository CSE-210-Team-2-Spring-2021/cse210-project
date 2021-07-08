from data import constants
from data.ai import AI

class WindowHelper:
    """
    Assistant to the SinistarWindow class. Provides helpful classes to 
    improve the flow of sinistar window

    Stereotype:
        Service Provider
    """
    def __init__(self):
        """Class constructor

        Args:
            self - An instance of WindowHelper
        """
        self._ai = AI()

    def wrap_sprites(self, sprites):
        """Wraps Sprite objects 

        Args:
            self - An instance of WindowHelper
            sprite - a sprite object
        """
        for sprite in sprites:
            if sprite.center_x <= 0:
                sprite.center_x = constants.SCREEN_WIDTH - 1

            elif sprite.center_y <= 0:
                sprite.center_y = constants.SCREEN_HEIGHT - 1

            elif sprite.center_x > constants.SCREEN_WIDTH:
                sprite.center_x = 1

            elif sprite.center_y > constants.SCREEN_HEIGHT:
                sprite.center_y = 1

    def update_enemy_actions(self, all_sprites, player_sprite, enemy_sprites, enemy_lasers):
        """Processes enemy ai, movement, and lasers
        
        Args:
            self - an instance of WindowHelper
            all_sprites - SpriteList of all sprites
            player_sprite - the player's sprite
            enemy_sprites - SpriteList of all enemies
            enemy_lasers - SpriteList of all enemy lasers
        """
        barriers = self._ai.find_barriers(enemy_sprites, all_sprites)
        for enemy in enemy_sprites:
            self._ai.face_player(enemy, player_sprite)
            
            enemy.process_move(self._ai.do_pathing(enemy.position, player_sprite.position, barriers),
                                enemy_lasers, all_sprites)  
        enemy_lasers.delete_laser()  
