import arcade, random
from data import constants
from data.ship import Ship
from data.asteroid import Asteroid

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
        self._score = 0

        #Create Class objects
        self._asteroid = Asteroid()
        self._ship = Ship()

        # Set the background color
        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)

        #Gameover Bool
        self._game_over = False
        
        #Immunity Timer
        self._immunity = 100

        #Sounds
        self._explosion = arcade.load_sound(constants.COMICAL_EXPLOSION, False)

    def setup(self):
        """ Set up the game and initialize the variables. 
        
        Args:
            self - an instance of SinistarWindow
        """

        # Sprite lists
        self._all_sprites_list = arcade.SpriteList()

        #Create Asteroids
        self._asteroid.generate_astroids(self._all_sprites_list)
        self._asteroid_sprites = self._asteroid.get_asteroids()

        #Set up the player
        self._ship.generate_ship(self._all_sprites_list)
        self._ship.set_lives(constants.LIVES)
        self._player_sprite = self._ship.get_ship()

        #Setup Lives Spritelist
        self._lives_sprites = [] #THis is a normal list
        for path in constants.LIVES_SPRITES:
            temp_sprite_list = arcade.SpriteList()
            sprite = arcade.Sprite(path, constants.SPRITE_SCALING_TILES)
            sprite.center_x = 80
            sprite.center_y = constants.SCREEN_HEIGHT - 20
            temp_sprite_list.append(sprite)
            self._lives_sprites.append(temp_sprite_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        score = "Score: " + str(self._score)

        if not self._game_over:
            # Draw all the sprites.
            self._all_sprites_list.draw()

            lives = self._ship.get_lives()
            if lives >= 0:
                self._lives_sprites[lives].draw()

            #Draw Score
            arcade.draw_text(score, constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)

        else:
            output = 'GAME OVER'
            arcade.draw_text(score, constants.SCREEN_WIDTH/2 - 10, constants.SCREEN_HEIGHT/2 - 10, arcade.color.WHITE, 14)
            arcade.draw_text(output, constants.SCREEN_WIDTH/2 - 30, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Updte all sprites
        self._all_sprites_list.update()

        if not self._game_over:
            #Wrap objects
            for sprite in self._all_sprites_list:
                self._wrap_sprite(sprite)

            #Check for collisions
            if self._immunity <= 0:
                ship_hit = []
                ship_hit = arcade.check_for_collision_with_list(self._player_sprite, self._asteroid_sprites)

                if ship_hit != []:
                    arcade.play_sound(self._explosion, 0.8, 0, False)
                    self._immunity = constants.IMMUNITY
                    self._score -= 100
                    lives = self._ship.get_lives()

                    if lives > 0:
                        self._ship.set_lives(lives - 1)

                        self._player_sprite.center_x = constants.SCREEN_WIDTH/2
                        self._player_sprite.center_y = constants.SCREEN_HEIGHT/2

                    else:
                        #GAME OVER
                        self._game_lost()
                else:
                    self._score += 1
                    
            else:
                self._immunity -= 1


    def _game_lost(self):
        """Removes Sprites and displays Game OVER
        
        Args:
            self - An Instance of SinistarWindow"""
        self._game_over = True
        
    def _wrap_sprite(self, sprite):
        """Wraps Sprite objects 
        
        Args:
            self - An instance of self
            sprite - a sprite object
        """

        if sprite.center_x <= 0:
            sprite.center_x = constants.SCREEN_WIDTH - 1

        elif sprite.center_y <= 0:
            sprite.center_y = constants.SCREEN_HEIGHT - 1

        elif sprite.center_x > constants.SCREEN_WIDTH:
            sprite.center_x = 1

        elif sprite.center_y > constants.SCREEN_HEIGHT:
            sprite.center_y = 1

    def on_key_press(self, key, modifier):
        """Called when a key is pressed for movement

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP:
            self._player_sprite.change_y = constants.MOVEMENT_SPEED
        
        elif key == arcade.key.DOWN:
            self._player_sprite.change_y = -constants.MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self._player_sprite.change_x = -constants.MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self._player_sprite.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifier):
        """Called when a key stops being pressed

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self._player_sprite.change_y = 0

        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self._player_sprite.change_x = 0