import arcade
import random
import math

from pyglet.libs.win32.constants import FALSE
from data import constants
from data.ship import Ship
from data.asteroid import Asteroid
from data.asteroid_manager import AsteroidManager
from data.enemies import EnemyManager
from data.enemy_laser import EnemyLaser
from data.laser import Laser
from data.menu import Menu
from data.ai import AI
from data.windowhelper import WindowHelper
# from data.difficulty import Difficulty
# from data.collisions import Collisions


class SinistarWindow(arcade.Window):
    """
    Main application class.

    Stereotype:
        Controller/Service Provider
    """

    def __init__(self, width, height, title):
        """
        Class Constructor

        Args:
            self - an instance of SinistarWindow
            width - width of screen
            height - height of screen
            title - title of window
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self._all_sprites_list = None

        # Set up the player info
        self._player_sprite = None
        self._score = None

        self._mouse_sprite = None
        self._mouse_list = None

        # Setup Menu
        self._menu = Menu()
        self._generate_menu()

        #Setup Helper
        self._helper = WindowHelper()

        #Background
        self._background = arcade.load_texture(constants.BACKGROUND)

        # Create Class objects
        self._asteroid_sprites = None
        self._ship = None
        self._player_laser_sprites = None

        self._enemy_sprites = None
        self._enemy_laser_sprites = None

        self._status = []

        # Create sound objects
        self._volume = 0.5
        self._theme = arcade.Sound(constants.THEME, True)
        self._theme_player = self._theme.play(self._volume, 0, True)
        self._boom = arcade.Sound(constants.COMICAL_EXPLOSION, False)
        self._player_laser_effect = arcade.Sound(constants.LASER, False)
        self._enemy_laser_effect = arcade.Sound(constants.ENEMY_LASER, False)
        self._explosion = arcade.Sound(constants.EXPLOSION, False)

        # Movement Bool
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        # Set the background color
        arcade.set_background_color(arcade.color.EERIE_BLACK)

        # Immunity Timer
        self._immunity = constants.IMMUNITY

        # Hide Mouse
        self.set_mouse_visible(False)

        # Create Difficulty
        # self._difficulty = Difficulty()

        # Collisions check
        # self._collisions = Collisions()

    def setup(self):
        """ Set up the game and initialize the variables. 

        Args:
            self - an instance of SinistarWindow
        """
        self._all_sprites_list = arcade.SpriteList()
        self._ship = Ship(self._all_sprites_list)
        self._status = self._menu.get_status()
        self._score = 0

        # Create mouse
        self._mouse_list = arcade.SpriteList()
        self._mouse_sprite = arcade.Sprite(
            constants.MOUSE, constants.SPRITE_SCALING_MOUSE)
        self._mouse_list.append(self._mouse_sprite)

        # Set up the player
        self._player_sprite = self._ship.get_ship()

        # Create Asteroids
        self._asteroid_sprites = AsteroidManager(self._player_sprite)
        self._all_sprites_list.extend(self._asteroid_sprites)

        # Create Enemies
        self._enemy_sprites = EnemyManager(self._player_sprite)
        self._all_sprites_list.extend(self._enemy_sprites)

        # Setup the lasers
        self._player_laser_sprites = Laser()
        self._all_sprites_list.extend(self._player_laser_sprites)

        self._enemy_laser_sprites = EnemyLaser()

        # Setup Lives Spritelist
        self._lives_sprites = []  # THis is a normal list of SpriteList objects
        for path in constants.LIVES_SPRITES:
            temp_sprite_list = arcade.SpriteList()
            sprite = arcade.Sprite(path, constants.SPRITE_SCALING_TILES)
            sprite.center_x = 80
            sprite.center_y = constants.SCREEN_HEIGHT - 20
            temp_sprite_list.append(sprite)
            self._lives_sprites.append(temp_sprite_list)

    def _generate_menu(self):
        """
        Sets up the menu sprite lists

        Args:
            self - An instane of SinistarWindow"""

        # Setup menu SpriteLists
        self._main_menu = self._menu.get_main_menu()
        self._pause_menu = self._menu.get_pause_menu()
        self._settings_menu = self._menu.get_settings_menu()
        self._help_menu = self._menu.get_help_menu()
        self._game_over_menu = self._menu.get_game_over_menu()
        # self._change_difficulty = self._menu._change_difficulty()

    def _change_volume(self, volume):
        """
        Changes volume of game

        Args:
            self - An instane of SinistarWindow"""
        self._theme.set_volume(volume, self._theme_player)
        self._volume = volume

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        #draw background
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH,
                                            constants.SCREEN_HEIGHT,
                                            self._background)

        score = "Score: " + str(self._score)

        # self._status (0 - Main, 1 - Pause, 2 - Settings, 3 - Help, 4 - Game Over)
        if self._status[0]:  # Main menu bool
            # self._mouse_list.draw() #This draws the mouse under menu items due to location

            if self._status[2]:  # Settings
                self._settings_menu.draw()
                self._mouse_list.draw()

            elif self._status[3]:  # Help
                self._help_menu.draw()
                self._mouse_list.draw()

            else:  # Main Menu
                self._main_menu.draw()
                self._mouse_list.draw()

        elif self._status[1]:  # Paused
            # ADD IF STATEMENT HERE IF MORE OPTIONS ARE ADDED TO PAUSE
            self._pause_menu.draw()
            self._mouse_list.draw()

        else:
            # Game over (Will need more options for restart)
            if self._status[4]:
                self._game_over_menu.draw()
                output = 'GAME OVER'
                arcade.draw_text(score, constants.SCREEN_WIDTH/2 - 50,
                                 constants.SCREEN_HEIGHT/2 + 90, arcade.color.WHITE, 14)
                arcade.draw_text(output, constants.SCREEN_WIDTH/2 - 70,
                                 constants.SCREEN_HEIGHT/2 + 100, arcade.color.WHITE, 20)
                self._mouse_list.draw()

            else:  # Game playing
                # Draw all the sprites.
                self._all_sprites_list.draw()
                lives = self._ship.get_lives()
                if lives >= 0:
                    self._lives_sprites[lives].draw()
                # Draw Score
                arcade.draw_text(score, constants.SCREEN_WIDTH/2,
                                 constants.SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)
                
                #for enemy in self._enemy_sprites:
                #    if enemy.get_path():
                #        arcade.draw_line_strip(enemy.get_path(), arcade.color.BLUE, 2)

    def on_update(self, delta_time):
        """ Movement and game logic """
        # update status
        self._status = self._menu.get_status()
        # self._status (0 - Main, 1 - Pause, 2 - Settings, 3 - Help, 4 - Game Over)
        if self._status[0]:  # Main
            self._mouse_list.update()

            if self._status[2]:  # Settings
                self._settings_menu.update()

            elif self._status[3]:  # Help
                self._help_menu.update()

            else:
                self._main_menu.update()

        elif self._status[1]:
            self._mouse_list.update()

        else:
            # Game Over (Will need more options for restart)
            if self._status[4]:
                self._mouse_list.update()
            else:  # Gameplay
                # Update all sprites
                self._all_sprites_list.update()
                self._player_sprite.move(self.up_pressed, self.down_pressed, 
                                        self.left_pressed, self.right_pressed)

                # Wrap objects
                self._helper.wrap_sprites(self._all_sprites_list)

                # Check for collisions
                # self._collisions.handle_collisions()

                Laser.update_player_lasers(self, self._player_laser_sprites, self._enemy_sprites, 
                                            self._asteroid_sprites, self._explosion, self._volume)
                Laser.delete_laser(self._player_laser_sprites)
              
                if self._immunity <= 0:
                    self._player_sprite.set_normal_texture()
                    ship_hit = []

                    asteroid_hit = arcade.check_for_collision_with_list(self._player_sprite,
                                                                        self._asteroid_sprites)
                    enemy_hit = arcade.check_for_collision_with_list(self._player_sprite,
                                                                     self._enemy_sprites)
                    enemy_laser_hit = arcade.check_for_collision_with_list(self._player_sprite,
                                                                            self._enemy_laser_sprites)
                    ship_hit = asteroid_hit + enemy_hit + enemy_laser_hit

                    if ship_hit != []:
                        self._boom.play(self._volume, 0, False)
                        self._immunity = constants.IMMUNITY
                        self._score -= 100
                        lives = self._ship.get_lives()
                        if lives > 0:
                            self._ship.set_lives(lives - 1)
                            self._player_sprite.center_x = constants.SCREEN_WIDTH/2
                            self._player_sprite.center_y = constants.SCREEN_HEIGHT/2
                        else:
                            # GAME OVER
                            self._menu.game_lost()
                else:
                    self._immunity -= 1
                    self._player_sprite.set_shield_texture()

                #enemy movement/ respawns
                self._helper.update_enemy_actions(self._all_sprites_list, self._player_sprite,
                                                    self._enemy_sprites, self._enemy_laser_sprites,
                                                    self._asteroid_sprites)

    def on_key_press(self, key, modifier):
        """Called when a key is pressed for movement

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        elif key == arcade.key.ESCAPE:
            if self._status[1]:
                self._menu.start_pressed()
            else:
                self._menu.game_paused()
        # Adding spacebar for shooting a laser. Can be done same time as directional keys. Reason for separate if statement.
        if key == arcade.key.SPACE:
            self._player_laser_sprites = Laser.get_player_lasers(self)
            Laser.generate_laser(self._player_laser_sprites, self._ship, self._all_sprites_list)
            self._player_laser_effect.play(self._volume, 0, False)

    def on_key_release(self, key, modifier):
        """Called when a key stops being pressed

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def on_mouse_motion(self, x, y, dx, dy):
        """Handles Mouse Motion"""

        # Move the center of the player sprite to match the mouse x, y
        self._mouse_sprite.center_x = x
        self._mouse_sprite.center_y = y

    def on_mouse_release(self, x, y, dx, dy):
        """Handles clicking menu"""

        buttons = self._menu.get_menu()
        clicked = []
        # self._status (0 - Main, 1 - Pause, 2 - Settings, 3 - Help, 4 - Game Over)
        if self._status[0]:  # main menu
            if self._status[2]:
                clicked = arcade.check_for_collision_with_list(
                    self._mouse_sprite, self._settings_menu)
            elif self._status[3]:
                clicked = arcade.check_for_collision_with_list(
                    self._mouse_sprite, self._help_menu)
            else:
                clicked = arcade.check_for_collision_with_list(
                    self._mouse_sprite, self._main_menu)

        elif self._status[1]:  # Pause menu
            clicked = arcade.check_for_collision_with_list(
                self._mouse_sprite, self._pause_menu)

        elif self._status[4]:
            clicked = arcade.check_for_collision_with_list(self._mouse_sprite, self._game_over_menu)
        else: #Gameplay
            return

        if clicked == []: #prevents index errors
            return
        else:
            if clicked[0] == buttons[0]: #Start
                self._menu.start_pressed()
            elif clicked[0] == buttons[1]: #Settings
                self._menu.settings_pressed()
            elif clicked[0] == buttons[2]: #Help
                self._menu.help_pressed()
            elif clicked[0] == buttons[3]: #Quit
                self._menu.quit(self)

            elif clicked[0] == buttons[4]: #Resume
                self._menu.start_pressed()
            elif clicked[0] == buttons[5]: #Back
                self._menu.back_pressed()

            elif clicked[0] == buttons[6]: #Restart
                self._menu.restart(self)
            elif clicked[0] == buttons[7]: #Main
                self._menu.go_to_main(self)

            elif clicked[0] == buttons[8]: #Easiest
                self._menu.change_difficulty(1)
            elif clicked[0] == buttons[9]: #Easy
                self._menu.change_difficulty(2)
            elif clicked[0] == buttons[10]: #Normal
                self._menu.change_difficulty(3)
            elif clicked[0] == buttons[11]: #Hard
                self._menu.change_difficulty(4)
            elif clicked[0] == buttons[12]: #Sinistar
                self._menu.change_difficulty(5)

            elif clicked[0] == buttons[15]: #Volume 0
                self._menu.volume_select(0)
                self._change_volume(0)
            elif clicked[0] == buttons[16]: #Volume 0
                self._menu.volume_select(1)
                self._change_volume(0.1)
            elif clicked[0] == buttons[17]: #Volume 0
                self._menu.volume_select(2)
                self._change_volume(0.2)
            elif clicked[0] == buttons[18]: #Volume 0
                self._menu.volume_select(3)
                self._change_volume(0.3)
            elif clicked[0] == buttons[19]: #Volume 0
                self._menu.volume_select(4)
                self._change_volume(0.4)
            elif clicked[0] == buttons[20]: #Volume 0
                self._menu.volume_select(5)
                self._change_volume(0.5)
            elif clicked[0] == buttons[21]: #Volume 0
                self._menu.volume_select(6)
                self._change_volume(0.6)
            elif clicked[0] == buttons[22]: #Volume 0
                self._menu.volume_select(7)
                self._change_volume(0.7)
            elif clicked[0] == buttons[23]: #Volume 0
                self._menu.volume_select(8)
                self._change_volume(0.8)
            elif clicked[0] == buttons[24]: #Volume 0
                self._menu.volume_select(9)
                self._change_volume(0.9)
            elif clicked[0] == buttons[25]: #Volume 0
                self._menu.volume_select(10)
                self._change_volume(1)
            else:
                return
        
