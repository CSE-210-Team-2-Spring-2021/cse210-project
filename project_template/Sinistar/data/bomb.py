import arcade
from data import constants

class Bomb(arcade.SpriteList):
    """Class to track the list of all Bombs in play

        Stereotype: Information Holder
    """

    def __init__(self):
        """Class Constructor"""
        super().__init__()
        self._bomb_count = 0

    def generate_crystal(self, asteroid, crystal_sprites, all_sprites):
        """When an asteroid explodes, it has a chance to drop a crystal. 
            Enemy Worker to pick it up later.
            Args:
                self - An instance of Bomb
                asteroid_sprites - SpriteList of all asteroids
                all_sprites - List of all sprites from sinistarwindow
        """
        # Set position and zero velocity based off destroyed asteroid position.
        crystal = arcade.Sprite(constants.CRYSTAL_SPRITE, constants.SPRITE_SCALING_CRYSTALS)
        crystal.center_x = asteroid.center_x
        crystal.center_y = asteroid.center_y

        crystal_sprites.append(crystal)
        all_sprites.append(crystal)

    def crystal_to_bomb(self, crystal_sprites, player_sprite):
        """When the ship collides with crystal, a bomb is added to inventory for shooting.

            Args:
                self - An instance of Bomb
                crystal_sprites - list of all crystal sprites
                player_sprite - Player ship to collide with crystal
        """
        
        #print("running crystal to bomb")
        crystal_hit = arcade.check_for_collision_with_list(player_sprite, crystal_sprites)
        if crystal_hit:
            for crystal in crystal_hit:
                crystal.kill()
                if self._bomb_count < 5:
                    self._bomb_count += 1

    def get_bomb_count(self, _bomb_count):
        """ Returns the bomb count available"""

        return _bomb_count