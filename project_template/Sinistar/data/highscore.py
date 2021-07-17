import json
import arcade
from arcade.key import N
from data import constants
from data.windowhelper import WindowHelper

class HighScore():
    """
    
    """

    def __init__(self, player_sprite):
        """
        
        """

        self._helper = WindowHelper(player_sprite)

        self._names:list = []
        self._scores:list = []
        self._score_marker = -1
        self._has_highscore = False

        json_in_temp: str = ""
        json_in:str = ""
        json_new:dict = "{}"

        #Loading the json into something more easily read by python.
        json_in_temp = open(constants.SCORE_DOC, "r")
        json_in = json_in_temp.read()
        json_new = json.loads(json_in)
        json_in_temp.close()

        #Compiling the json parts into two lists that can easily be referenced.
        for name in json_new["Name"]:
            self._names.append(name)

        for score in json_new["Score"]:
            self._scores.append(score)

    def retrieve_name(self, name):
        """
        
        """

        name_in = name

        congratulatory_text = "Congratulations! You achieved a highscore. Please input your name, then press enter."

        arcade.draw_text(congratulatory_text, constants.SCREEN_WIDTH/2 - 300,
                        constants.SCREEN_HEIGHT/2 + 80, arcade.color.WHITE, 20)
        arcade.draw_text(name_in, constants.SCREEN_WIDTH/2 - 300,
                        constants.SCREEN_HEIGHT/2 + 40, arcade.color.WHITE, 20)

        return name_in

    def check_highscore(self, score_in):
        """
        
        """

        #retrieves the name and score of the player if a top 5 has been achieved.
        for i in range(0, 5):
            if score_in > self._scores[i]:
                self._score_marker = i
                self._has_highscore = True
                return self._has_highscore

    def save_highscore(self, name_in, score_in):
        """
        
        """

        self._names[self._score_marker] = name_in
        self._scores[self._score_marker] = score_in

    def get_names(self):
        """
        
        """

        return self._names


    def get_scores(self):
        """
        
        """

        return self._scores


    def display_scores(self):
        """
        
        """

        start_x_1 = constants.SCREEN_WIDTH/2 - 70
        start_x_2 = constants.SCREEN_WIDTH/2 + 70
        start_y = constants.SCREEN_HEIGHT - 20
        for i in range(0, 5):
            

            arcade.draw_text(self._names[i], start_x_1,
                                    start_y, arcade.color.WHITE, 14)

            arcade.draw_text(str(self._scores[i]), start_x_2,
                                    start_y, arcade.color.WHITE, 14)

            start_y -= 20


    def save_file(self):
        """
        
        """

        json_new:dict = {
            "Name": [],
            "Score": []
            }

        #Compiling the lists into a dictionary for the json.
        for i, name in enumerate(self._names):
            json_new["Name"].append(name)

        for i, score in enumerate(self._scores):
            json_new["Score"].append(score)

        with open(constants.SCORE_DOC, 'w') as outfile:
            json.dump(json_new, outfile)