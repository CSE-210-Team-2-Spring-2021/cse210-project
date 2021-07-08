import arcade, math, random
from data import constants
from data.laser import Laser

class AI():
    """Class used for handling the enemy AI
    
    Sterotypes:
        Information Holder?
    """

    def __init__(self):
        """
        
        """
        t = 5 #this is just to stop errors

    def find_barriers(self, enemy_sprites, all_sprites):
        """Returns a list of barriers to be used to find pathing.

        Args:
            enemy_sprites: the list of all enemy sprites.
            all_sprites: the list of all sprites in the game.
        """
        sprite = enemy_sprites[0] #if enemies are same size this only needs to be done once
        barriers = arcade.AStarBarrierList(sprite, all_sprites,
                            constants.GRID, 0, constants.SCREEN_WIDTH, 
                            0, constants.SCREEN_HEIGHT)

        #for sprite in enemy_sprites:
        #    barriers.append(arcade.AStarBarrierList(sprite, all_sprites,
        #                    128, 0, constants.SCREEN_WIDTH, 
        #                    0, constants.SCREEN_HEIGHT))
        return barriers

    def do_pathing(self, enemy_location, destination, barriers):
        """Returns a list to be used as a path.
        
        Args:
            enemy_location (tuple): the location of the enemy to be given a path.
            destination (tuple): where the path is headed towards.
            barriers (list): the list of barriers
        """

        enemy_path = []
        enemy_path = arcade.astar_calculate_path(enemy_location, destination,
                                    barriers, True)
        return enemy_path

    def calc_sight_line(self, enemy_location, player_location,
                        all_sprites):
        """Returns a tuple with a bool to indicate whether there is sight or not
        and a list containing the coordinates within the sight line.
        
        Args:
            enemy_location (tuple): The location of the enemy to be given sight.
            player_location (tuple): The location of the player ship.
            all_sprites (list): The list of all sprites in the game, used to check for obstacles.
        """

        (tuple_bool, tuple_list) = arcade.has_line_of_sight(enemy_location,
                                                            player_location, all_sprites, 100)
        return (tuple_bool, tuple_list)

    def get_path_vector(self, enemy_location, enemy_path):
        """
        
        """

        vector = enemy_path - enemy_location
        return vector

    def face_player(self, enemy_sprite, player_sprite):
        """Makes the enemy sprite face the player sprite
        
        Args:
            self - Instance of ai
            enemy_sprite - An enemy Sprite
            player_sprite - The player Sprite
        """
        # Position the start at the enemy's current location
        start_x = enemy_sprite.center_x
        start_y = enemy_sprite.center_y

        # Get the destination location for the bullet
        dest_x = player_sprite.center_x
        dest_y = player_sprite.center_y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Set the enemy to face the player.
        enemy_sprite.angle = math.degrees(angle) - 90