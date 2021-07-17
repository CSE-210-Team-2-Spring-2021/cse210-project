import json
import arcade
from data import constants

class HighScore():
    """A class of object designed to keep track of and save scores to a file.
    
    Archetype: Information Holder
    
    Attributes:
        _names(list): A list of all names in the score file
        _scores(list): A list of all scores in the score file.
        _score_marker(int): An index to indicate where the players highscore is.
    """

    def __init__(self):
        """Setup the object and organize the file into appropriate lists.
        
        Args:
            self
        """

        self._names:list = []
        self._scores:list = []
        self._score_marker = -1

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
        """Get the user's name to be added to the list.
        
        Args:
            self
            name(str): The user's name.
        """

        name_in = name

        congratulatory_text = "Congratulations! You achieved a highscore. Please input your name, then press enter."

        arcade.draw_text(congratulatory_text, constants.SCREEN_WIDTH/2 - 300,
                        constants.SCREEN_HEIGHT/2 + 80, arcade.color.WHITE, 20)
        arcade.draw_text(name_in, constants.SCREEN_WIDTH/2 - 300,
                        constants.SCREEN_HEIGHT/2 + 40, arcade.color.WHITE, 20)

        return name_in

    def check_highscore(self, score_in):
        """Check if the user achieved a highscore.
        
        Args:
            self
            score_in(int): The user's score.
        """

        #retrieves the name and score of the player if a top 5 has been achieved.
        for i in range(0, 5):
            if score_in > self._scores[i]:
                self._score_marker = i
                return self._has_highscore

    def save_highscore(self, name_in, score_in):
        """Add the player highscore and name to the corresponding lists.
        
        Args:
            self
            name_in(str): The user's name.
            score_in(int): The user's score.
        """

        self._names[self._score_marker] = name_in
        self._scores[self._score_marker] = score_in

    def get_names(self):
        """Return the list of all names.
        
        Args:
            self
        """

        return self._names


    def get_scores(self):
        """Return the list of all scores.
        
        Args:
            self
        """

        return self._scores


    def display_scores(self):
        """Outputs the scores to the screen
        
        Args:
            self
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
        """Save the file with the new scores.
        
        Args:
            self
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