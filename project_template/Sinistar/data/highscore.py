import json
from data import constants

class HighScore():
    """
    
    """

    def __init__(self):
        """
        
        """

        self._names:list = []
        self._scores:list = []

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


    def write_new_score(self):
        """
        
        """

        #retrieves the name and score of the player if a top 5 has been achieved.


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

        #is this needed?


    def save_file(self):
        """
        
        """

        json_new:dict = "{}"

        #Compiling the lists into a dictionary for the json.
        for name in self._names["Name"]:
            json_new["Name"].append(name)

        for score in self._scores["Score"]:
            json_new["Score"].append(score)

        with open(constants.SCORE_DOC, 'w') as outfile:
            json.dump(json_new, outfile)
        constants.SCORE_DOC.close()