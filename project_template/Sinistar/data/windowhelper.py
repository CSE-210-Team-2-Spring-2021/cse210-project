import arcade
from data import constants
from data.ai import AI
from data.enemies import EnemyManager
from data.difficulty import Difficulty


class WindowHelper():
    """
    Assistant to the SinistarWindow class. Provides helpful classes to 
    improve the flow of sinistar window
    Stereotype:
        Service Provider
    """

    def __init__(self, player_sprite):
        """Class constructor
        Args:
            self - An instance of WindowHelper
        """
        self._ai = AI()
        self._enemy_manager = EnemyManager(player_sprite)
        self._text = ''

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

    def update_enemy_actions(self, all_sprites, player_sprite, enemy_sprites, enemy_lasers,
                             asteroids, crystal_sprites):
        """Processes enemy ai, movement, and lasers

        Args:
            self - an instance of WindowHelper
            all_sprites - SpriteList of all sprites
            player_sprite - the player's sprite
            enemy_sprites - SpriteList of all enemies
            enemy_lasers - SpriteList of all enemy lasers
            asteroids - SpriteList of asteroids
        """
        barriers = self._ai.find_barriers(enemy_sprites, all_sprites)
        for enemy in enemy_sprites:
            if enemy.enemy_type == 'Worker':
                if crystal_sprites:
                    enemy.crystal_exists(True)
                    if enemy.has_crystal == False:
                        closest_crystal = self._ai.find_closest(
                            enemy, crystal_sprites, all_sprites)
                        self._ai.face_crystal(enemy, closest_crystal)

                        enemy.process_move(self._ai.do_pathing(enemy.position, closest_crystal, barriers),
                                           enemy_lasers, all_sprites)
                    else:
                        self._ai.face_away_from_player(enemy, player_sprite)
                        enemy.process_move(self._ai.do_pathing(enemy.position, player_sprite.position, barriers),
                                   enemy_lasers, all_sprites)

                else:
                    """avoid the player"""
                    enemy.crystal_exists(False)
                    self._ai.face_away_from_player(enemy, player_sprite)
                    enemy.process_move(self._ai.do_pathing(enemy.position, player_sprite.position, barriers),
                                   enemy_lasers, all_sprites)

            elif enemy.enemy_type == 'Warrior':
                self._ai.face_player(enemy, player_sprite)

                enemy.process_move(self._ai.do_pathing(enemy.position, player_sprite.position, barriers),
                                   enemy_lasers, all_sprites)
        enemy_lasers.delete_laser()
        self.respawn(player_sprite, asteroids, enemy_sprites, all_sprites)

    def respawn(self, player_sprite, asteroids, enemy_sprites, all_sprites):
        """Runs the respawn code for asteroids and enemies

        Args:
            self - an instance of WindowHelper
            all_sprites - SpriteList of all sprites
            player_sprite - the player's sprite
            enemy_sprites - SpriteList of all enemies
        """
        asteroids.respawn_asteroids(player_sprite,
                                    all_sprites)
        enemy_sprites.respawn_enemies(player_sprite,
                                      all_sprites)

    def get_enemy_manager(self):
        """ Returns EnemyManager """
        return self._enemy_manager

    def input_text(self, key):
        """Appends keyboard text into a string

        Args:
            self - an instance of WindowHelper

        Returns:
            string - letter typed
        """
        if self._text != '':
            if key == arcade.key.BACKSPACE:
                self._text = str.rstrip(self._text[-1])
                return

        letter = ''
        letter = self._keyboard(key)
        if letter != '':
            self._text += letter

    def _keyboard(self, key):
        """Receives keyboard input returns a string

        Args:
            self - an instance of WindowHelper

        Returns:
            string - letter typed
        """
        if key == arcade.key.A:
            return 'A'
        elif key == arcade.key.B:
            return 'B'
        elif key == arcade.key.C:
            return 'C'
        elif key == arcade.key.D:
            return 'D'
        elif key == arcade.key.E:
            return 'E'
        elif key == arcade.key.F:
            return 'F'
        elif key == arcade.key.G:
            return 'G'
        elif key == arcade.key.H:
            return 'H'
        elif key == arcade.key.I:
            return 'I'
        elif key == arcade.key.J:
            return 'J'
        elif key == arcade.key.K:
            return 'K'
        elif key == arcade.key.L:
            return 'L'
        elif key == arcade.key.M:
            return 'M'
        elif key == arcade.key.N:
            return 'N'
        elif key == arcade.key.O:
            return 'O'
        elif key == arcade.key.P:
            return 'P'
        elif key == arcade.key.Q:
            return 'Q'
        elif key == arcade.key.R:
            return 'R'
        elif key == arcade.key.S:
            return 'S'
        elif key == arcade.key.T:
            return 'T'
        elif key == arcade.key.U:
            return 'U'
        elif key == arcade.key.V:
            return 'V'
        elif key == arcade.key.W:
            return 'W'
        elif key == arcade.key.X:
            return 'X'
        elif key == arcade.key.Y:
            return 'Y'
        elif key == arcade.key.Z:
            return 'Z'

    def get_text(self):
        """Returns text

        Args:
            self - Instance of WindowHelper

        Return:
            self._text - Text to hold player name
        """
        return self._text
