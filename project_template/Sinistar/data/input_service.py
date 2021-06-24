import arcade

class InputService:
    """Responsible for receiving input for menu and game

    """
    
    def __init__(self):
        """Class constructor

        Args:
            self - an instance of InputService
        """
        self.MOVEMENT_SPEED = 5 #This can be changed to be in a constants file

    def on_key_press(self, key, player_sprite):
        """Called when a key is pressed for movement

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP:
            player_sprite.change_y = self.MOVEMENT_SPEED
        
        elif key == arcade.key.DOWN:
            player_sprite.change_y = -self.MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            player_sprite.change_x = -self.MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            player_sprite.change_x = self.MOVEMENT_SPEED

    def on_key_release(self, key, player_sprite):
        """Called when a key stops being pressed

        Args:
            self - an instance of InputService
            key - the key pressed
            player_sprite - the player's sprite object
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            player_sprite.change_y = 0

        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            player_sprite.change_x = 0