import arcade
import random, math

from arcade.texture import load_texture
from data import constants

class Ship(arcade.Sprite):
    """Subclass of Actors to create instances of Ship (Player)

    Stereotype: Information Holder

    Attributes:
        _location (coordinate) - the actors position in 2D space
        _velocity (coordinate) - the actors speed and direction 
    """
    def __init__(self, all_sprites):
        """
        Class Constructor"""
        super().__init__(constants.PLAYER_SPRITE, constants.SPRITE_SCALING_PLAYER)
        self._lives = None
        self.speed = 0
        self.angle = 90
        self._toggle = False
        self._timer = 3
        self._norm_texture = load_texture(constants.PLAYER_SPRITE)
        self._shield_texture = load_texture(constants.SHIELD_PLAYER_SPRITE)
        self.generate_ship(all_sprites)

    def generate_ship(self, all_sprites):
        """Generates ship in the center of screen
            Args:
                self - An instance of Asteroid
                all_sprites - List of all sprites from WinistarWindow
        """
        self.center_x = constants.SCREEN_WIDTH/2
        self.center_y = constants.SCREEN_HEIGHT/2
        self.set_lives(constants.LIVES)
        all_sprites.append(self)

    def set_lives(self, lives):
        """Updates the ship's lives.
        
        Args:
            lives (int): How many lives
        """
        self._lives = lives

    
    def get_lives(self):
        """Gets the ship's lives.
        
        Returns:
            lives: The ship's lives.
        """
        return self._lives

    def get_ship(self):
        """Returns player sprite
        
        Args:
            self - An instance of SHip
        """
        return self

    def move(self, up_pressed, down_pressed, left_pressed, right_pressed):
        """Controls the movement of the ship
        
        Args:
            self - An instance of ship
        """
        FRICTION = constants.DECELERATION_RATE
        ACCELERATION_RATE = constants.ACCELERATION_RATE
        ANGLE_DECAY = constants.ANGLE_DECAY
        ANGLE_RATE = constants.ANGLE_SPEED
        MAX_SPEED = constants.MOVEMENT_SPEED
        angle = self.angle
        angle_rad = math.radians(angle)
        speed = math.sqrt(self.change_x **
                          2 + self.change_y ** 2)

        # Find angle in radians that the ship is moving in (not where it is facing)
        if self.change_x != 0:  # No division by 0
            velocity_rad = math.atan(
                self.change_y/self.change_x)
        else:
            if self.change_y > 0:  # Player moving up
                velocity_rad = math.pi/2
            else:
                velocity_rad = -math.pi/2

        # Slows down the ship as it drifts
        if speed > FRICTION:
            if self.change_x > 0:
                self.change_x -= abs(
                    FRICTION * math.cos(velocity_rad))
            elif self.change_x < 0:
                self.change_x += abs(
                    FRICTION * math.cos(velocity_rad))
            else:
                self.change_x = 0
            if self.change_y > 0:
                self.change_y -= abs(
                    FRICTION * math.sin(velocity_rad))
            elif self.change_y < 0:
                self.change_y += abs(
                    FRICTION * math.sin(velocity_rad))
            else:
                self.change_y = 0
        else:
            self.change_x = 0
            self.change_y = 0

        # Slows down ships rotation
        if self.change_angle > ANGLE_DECAY:
            self.change_angle -= ANGLE_DECAY
        elif self.change_angle < -ANGLE_DECAY:
            self.change_angle += ANGLE_DECAY
        else:
            self.change_angle = 0

        angle = self.angle  # Update values
        angle_rad = math.radians(angle)

        # Apply acceleration based on the keys pressed
        if up_pressed and not down_pressed:
            self.change_x += ACCELERATION_RATE * \
                math.cos(angle_rad)
            self.change_y += ACCELERATION_RATE * \
                math.sin(angle_rad)
        elif down_pressed and not up_pressed:
            self.change_x -= ACCELERATION_RATE * \
                math.cos(angle_rad)
            self.change_y -= ACCELERATION_RATE * \
                math.sin(angle_rad)
        if left_pressed and not right_pressed:
            self.change_angle = ANGLE_RATE
        elif right_pressed and not left_pressed:
            self.change_angle = -ANGLE_RATE

        # Stop the ship from moving beyond max speed
        speed = math.sqrt(self.change_x **
                          2 + self.change_y ** 2)
        if speed > MAX_SPEED:
            velocity_rad = math.atan(
                self.change_y/self.change_x)
            angle_rad = math.radians(angle)
            if self.change_x > 0:
                self.change_x = abs(
                    MAX_SPEED * math.cos(velocity_rad))
            elif self.change_x < 0:
                self.change_x = - \
                    abs(MAX_SPEED * math.cos(velocity_rad))
            if self.change_y > 0:
                self.change_y = abs(
                    MAX_SPEED * math.sin(velocity_rad))
            elif self.change_y < 0:
                self.change_y = - \
                    abs(MAX_SPEED * math.sin(velocity_rad))
   
    def set_normal_texture(self):
        """Makes the ship its normal texture
        
        Args:
            self - an instance of Ship
        """
        if self._toggle:
            self._texture = self._norm_texture
            self._toggle = False

    def set_shield_texture(self):
        """Makes the ship its inverted texture
        
        Args:
            self - an instance of Ship
        """
        if self._toggle == False:
            self._texture = self._shield_texture
            self._toggle = True