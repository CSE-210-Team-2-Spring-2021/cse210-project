import arcade
import sys
from data import constants
import gc
# from data.difficulty import Difficulty


class Menu:
    """
    This class is responsible for the menu, sprites and commands relating to the menu's operation.

    Attributes:

    """

    def __init__(self):
        """
        The Class constructor

        Args:
            self - an Instance of Menu
        """
        self._menu_sprites = arcade.SpriteList()

        self._main_sprites = arcade.SpriteList()
        self._pause_sprites = arcade.SpriteList()
        self._settings_sprites = arcade.SpriteList()
        self._help_sprites = arcade.SpriteList()
        self._game_over_sprites = arcade.SpriteList()

        self._main_menu = True
        self._is_paused = False
        self._is_settings = False
        self._is_help = False
        self._game_over = False
        self._difficulty = 3  # self.difficulty._get_difficulty()  # RANGE 1-5 inclusive

        self._set_menu_sprites()
        self._create_menu_lists()

    def _set_menu_sprites(self):
        """
        Sets up the menu sprites/locations

        Args:
            self - An instance of Menu
        """
        menu_scaling = constants.SPRITE_SCALING_MENU
        difficulty_scaling = constants.SPRITE_SCALING_DIFFICULTY
        x = constants.SCREEN_WIDTH
        y = constants.SCREEN_HEIGHT

        # Create sprite objects
        # Same location as RESUME
        START = arcade.Sprite(constants.MENU_START, menu_scaling)
        START.center_x = x/2
        START.center_y = y/2 + 100

        SETTINGS = arcade.Sprite(constants.MENU_SETTINGS, menu_scaling)
        SETTINGS.center_x = x/2
        SETTINGS.center_y = y/2

        HELP = arcade.Sprite(constants.MENU_HELP, menu_scaling)
        HELP.center_x = x/2
        HELP.center_y = y/2 - 100

        # Same location as BACK
        QUIT = arcade.Sprite(constants.MENU_QUIT, menu_scaling)
        QUIT.center_x = x/2
        QUIT.center_y = y/2 - 200

        RESUME = arcade.Sprite(constants.MENU_RESUME, menu_scaling)
        RESUME.center_x = x/2
        RESUME.center_y = y/2 + 100

        BACK = arcade.Sprite(constants.MENU_BACK, menu_scaling)
        BACK.center_x = x/2
        BACK.center_y = y/2 - 200

        RESTART = arcade.Sprite(constants.MENU_RESTART, menu_scaling)
        RESTART.center_x = x/2
        RESTART.center_y = y/2

        MAIN = arcade.Sprite(constants.MENU_MAIN, menu_scaling)
        MAIN.center_x = x/2
        MAIN.center_y = y/2 - 100

        # Difficulty
        EASIEST = arcade.Sprite(
            constants.DIFFICULTY_EASIEST, difficulty_scaling)
        EASIEST.center_x = x/2 - 300
        EASIEST.center_y = y/2 + 300

        EASY = arcade.Sprite(constants.DIFFICULTY_EASY, difficulty_scaling)
        EASY.center_x = x/2 - 150
        EASY.center_y = y/2 + 300

        NORMAL = arcade.Sprite(constants.DIFFICULTY_NORMAL, difficulty_scaling)
        NORMAL.center_x = x/2
        NORMAL.center_y = y/2 + 300

        HARD = arcade.Sprite(constants.DIFFICULTY_HARD, difficulty_scaling)
        HARD.center_x = x/2 + 150
        HARD.center_y = y/2 + 300

        SINISTAR = arcade.Sprite(
            constants.DIFFICULTY_SINISTAR, difficulty_scaling)
        SINISTAR.center_x = x/2 + 300
        SINISTAR.center_y = y/2 + 300

        SELECTOR = arcade.Sprite(
            constants.DIFFICULTY_SELECTOR, difficulty_scaling)
        SELECTOR.center_x = x/2
        SELECTOR.center_y = y/2 + 300

        D_LABEL = arcade.Sprite(constants.DIFFICULTY_LABEL, menu_scaling)
        D_LABEL.center_x = x/2
        D_LABEL.center_y = y/2 + 400

        menu = [START, SETTINGS, HELP, QUIT, RESUME, BACK, RESTART, MAIN,
                EASIEST, EASY, NORMAL, HARD, SINISTAR, SELECTOR, D_LABEL]  # 0-14

        for i in range(11):
            if i == 0:
                temp = arcade.Sprite(constants.VOLUME_MUTE,
                                     difficulty_scaling * (0.6 + i * 0.04))
            else:
                temp = arcade.Sprite(
                    constants.VOLUME_SPRITE, difficulty_scaling * (0.6 + i * 0.04))
            temp.center_x = x/2 + (i - 5) * 70
            temp.center_y = y/2 + 100
            menu.append(temp)  # indexes 15-25

        V_SELECTOR = arcade.Sprite(
            constants.VOLUME_SELECTOR, difficulty_scaling * 0.8)
        V_SELECTOR.center_x = x/2
        V_SELECTOR.center_y = y/2 + 100
        menu.append(V_SELECTOR)  # 26

        V_LABEL = arcade.Sprite(constants.VOLUME_LABEL, menu_scaling)
        V_LABEL.center_x = x/2
        V_LABEL.center_y = y/2 + 200
        menu.append(V_LABEL)  # 27

        INSTRUCTIONS = arcade.Sprite(constants.INSTRUCTIONS, menu_scaling)
        INSTRUCTIONS.center_x = x/2
        INSTRUCTIONS.center_y = y/2 + 50
        menu.append(INSTRUCTIONS)  # 28

        for sprite in menu:
            self._menu_sprites.append(sprite)

    def _create_menu_lists(self):
        """Creates SpriteLists from the menu sprites

        Args:
            self - an instance of Menu
        """
        # MAIN MENU (Start)
        for i, item in enumerate(self._menu_sprites):
            if i < 4:
                self._main_sprites.append(item)  # START, SETTINGS, HELP, QUIT

        # PAUSE MENU
        self._pause_sprites.append(self._menu_sprites[4])  # RESUME
        self._pause_sprites.append(self._menu_sprites[3])  # QUIT

        # SETTINGS MENU
        for i, item in enumerate(self._menu_sprites):
            if i == 5 or (i > 7 and i < 28):
                self._settings_sprites.append(item)

        # HELP MENU
        self._help_sprites.append(self._menu_sprites[5])  # BACK
        self._help_sprites.append(self._menu_sprites[28])

        # HELP MENU
        self._help_sprites.append(self._menu_sprites[5])  # BACK

        # GAME OVER
        self._game_over_sprites.append(self._menu_sprites[3])
        self._game_over_sprites.append(self._menu_sprites[6])
        self._game_over_sprites.append(self._menu_sprites[7])

    def get_menu(self):
        """
        Returns _menu_sprites List

        Args:
            self - an Instance of Menu
        """
        return self._menu_sprites

    def get_main_menu(self):
        """Returns main menu Spritelist

        Args:
            self - an Instance of Menu
        """
        return self._main_sprites

    def get_pause_menu(self):
        """Returns a pause menu Spritelist

        Args:
            self - an Instance of Menu
        """
        return self._pause_sprites

    def get_settings_menu(self):
        """Returns a menu Spritelist

        Args:
            self - an Instance of Menu
        """
        return self._settings_sprites

    def get_help_menu(self):
        """Returns a menu Spritelist

        Args:
            self - an Instance of Menu
        """
        return self._help_sprites

    def get_game_over_menu(self):
        """Returns a menu Spritelist

        Args:
            self - an Instance of Menu
        """
        return self._game_over_sprites

    def start_pressed(self):
        """
        Code that runs when Start is pressed

        Args:
            self - an Instance of Menu
        """
        self._main_menu = False
        self._is_paused = False
        self._is_settings = False
        self._is_help = False

    def settings_pressed(self):
        """
        Settings is pressed

        Args:
            self - an Instance of Menu
        """
        self._main_menu = True
        self._is_paused = False
        self._is_settings = True
        self._is_help = False

    def help_pressed(self):
        """
        Help is pressed

        Args:
            self - an Instance of Menu
        """
        self._menu_sprites[5].center_y = constants.SCREEN_HEIGHT / \
            2 - 400  # Lower Back button
        self._is_settings = False
        self._is_help = True

    def quit(self, window):
        """
        Quit is pressed, exit program

        Args:
            self - an Instance of Menu
        """
        if window is None:
            return

        window.close()
        window = None
        gc.collect()

    def back_pressed(self):
        """
        Quit is pressed, exit program

        Args:
            self - an Instance of Menu
        """
        self._menu_sprites[5].center_y = constants.SCREEN_HEIGHT / \
            2 - 200  # move back button back
        self._is_settings = False
        self._is_help = False

    def game_lost(self):
        """
        Game lost

        Args:
            self - an Instance of Menu
        """
        self._game_over = True

    def restart(self, window):
        """
        Restart Game

        Args:
            self - an Instance of Menu
        """
        window.setup()
        self._game_over = False

    def go_to_main(self, window):
        """
        Opens the main menu

        Args:
            self - an Instance of Menu
        """
        window.setup()
        self._main_menu = True
        self._is_paused = False
        self._is_settings = False
        self._is_help = False
        self._game_over = False

    def game_paused(self):
        """
        Game is paused, esc typed

        Args:
            self - an Instance of Menu
        """
        self._main_menu = False
        self._is_paused = True
        self._is_settings = False
        self._is_help = False

    def change_difficulty(self, difficulty):
        """Changes the int value of difficulty and moves the selector circle

        Args:
            self - an Instance of Menu
        """
        self._difficulty = difficulty
        x = constants.SCREEN_WIDTH
        y = constants.SCREEN_HEIGHT

        if difficulty == 1:
            cx = x/2 - 300
            cy = y/2 + 300
        elif difficulty == 2:
            cx = x/2 - 150
            cy = y/2 + 300
        elif difficulty == 3:
            cx = x/2
            cy = y/2 + 300
        elif difficulty == 4:
            cx = x/2 + 150
            cy = y/2 + 300
        else:
            cx = x/2 + 300
            cy = y/2 + 300

        self._menu_sprites[13].center_x = cx
        self._menu_sprites[13].center_y = cy

    def volume_select(self, volume):
        """Moves the selector to the proper position

        Args:
            self - an Instance of Menu
        """
        scale = constants.SPRITE_SCALING_DIFFICULTY
        x = constants.SCREEN_WIDTH
        y = constants.SCREEN_HEIGHT

        self._menu_sprites[26]._set_scale(scale * (0.6 + volume * 0.04))
        self._menu_sprites[26].center_x = x/2 + (volume - 5) * 70
        self._menu_sprites[26].center_y = y/2 + 100

    def get_status(self):
        """
        Returns list of boolean

        Args:
            self - an Instance of Menu
        """
        return [self._main_menu, self._is_paused, self._is_settings, self._is_help, self._game_over]

    def get_difficulty(self):
        """
        Returns difficulty

        Args:
            self - an Instance of Menu
        """
        return self._difficulty
