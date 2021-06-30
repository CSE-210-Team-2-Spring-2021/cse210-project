import arcade, sys
from data import constants
import gc

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

        self._set_menu_sprites()
        self._create_menu_lists()

    def _set_menu_sprites(self):
        """
        Sets up the menu sprites/locations
        
        Args:
            self - An instance of Menu
        """
        scaling = constants.SPRITE_SCALING_MENU
        x = constants.SCREEN_WIDTH
        y = constants.SCREEN_HEIGHT

        #Create sprite objects
        START = arcade.Sprite(constants.MENU_START, scaling) #Same location as RESUME
        START.center_x = x/2
        START.center_y = y/2 + 100

        SETTINGS = arcade.Sprite(constants.MENU_SETTINGS, scaling)
        SETTINGS.center_x = x/2
        SETTINGS.center_y = y/2

        HELP = arcade.Sprite(constants.MENU_HELP, scaling)
        HELP.center_x = x/2
        HELP.center_y = y/2 - 100

        QUIT = arcade.Sprite(constants.MENU_QUIT, scaling) #Same location as BACK
        QUIT.center_x = x/2
        QUIT.center_y = y/2 - 200

        RESUME = arcade.Sprite(constants.MENU_RESUME, scaling)
        RESUME.center_x = x/2
        RESUME.center_y = y/2 + 100

        BACK = arcade.Sprite(constants.MENU_BACK, scaling)
        BACK.center_x = x/2
        BACK.center_y = y/2 - 200

        RESTART = arcade.Sprite(constants.MENU_RESTART, scaling)
        RESTART.center_x = x/2
        RESTART.center_y = y/2

        MAIN = arcade.Sprite(constants.MENU_MAIN, scaling)
        MAIN.center_x = x/2
        MAIN.center_y = y/2 - 100

        menu = [START, SETTINGS, HELP, QUIT, RESUME, BACK, RESTART, MAIN]

        for sprite in menu:
            self._menu_sprites.append(sprite)

    def _create_menu_lists(self):
        """Creates SpriteLists from the menu sprites
        
        Args:
            self - an instance of Menu
        """
        #MAIN MENU (Start)
        for i, item in enumerate(self._menu_sprites):
            if i < 4:
                self._main_sprites.append(item) #START, SETTINGS, HELP, QUIT

        #PAUSE MENU
        self._pause_sprites.append(self._menu_sprites[4]) #RESUME
        self._pause_sprites.append(self._menu_sprites[3]) #QUIT

        #SETTINGS MENU
        self._settings_sprites.append(self._menu_sprites[5]) #BACK

        #HELP MENU
        self._help_sprites.append(self._menu_sprites[5]) #BACK

        #GAME OVER
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

    def get_status(self):
        """
        Returns list of boolean
        
        Args:
            self - an Instance of Menu
        """
        return [self._main_menu, self._is_paused, self._is_settings, self._is_help, self._game_over]
        


        


