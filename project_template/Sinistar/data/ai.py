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
        if enemy_sprites:
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

        return arcade.has_line_of_sight(enemy_location,
                                                            player_location, all_sprites, 100)

    def calc_distance(self, enemy_location, destination):
        """
        
        """

        distance = destination - enemy_location
        return distance

    def find_closest(self, enemy_sprite, crystal_sprites, all_sprites):
        """
        
        """

        enemy_location = (enemy_sprite.center_x, enemy_sprite.center_y)
        
        closest = 10000
        distances = []
        marker = -1
        
        for crystal in crystal_sprites:
            crystal_location = (crystal.center_x, crystal.center_y)
            if self.calc_sight_line(enemy_location, crystal_location, all_sprites):
                distance = self.calc_distance(enemy_location, crystal_location)
                distances.append(distance)

        for i, distance in enumerate(distances):
            if distance < closest:
                closest = distance
                marker = i

        closest_crystal = (crystal_sprites[marker].center_x, crystal_sprites[marker].center_y)
        return closest_crystal

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

    def face_away_from_player(self, enemy_sprite, player_sprite):
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
        enemy_sprite.angle = -(math.degrees(angle) - 90)

    def face_crystal(self, enemy_sprite, closest_crystal):
        """Makes the enemy sprite face the crystal sprite
        
        Args:
            self - Instance of ai
            enemy_sprite - An enemy Sprite
            closest_crystal(tuple) - The coordinates of the closest crystal
        """
        

        
        # Position the start at the enemy's current location
        start_x = enemy_sprite.center_x
        start_y = enemy_sprite.center_y

        # Get the destination location for the bullet
        (dest_x, dest_y) = closest_crystal

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Set the enemy to face the crystal.
        enemy_sprite.angle = math.degrees(angle) - 90