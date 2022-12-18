import json
import os
import shutil
from misc.objects import Game
from misc.dir import src


class GameMgr:
    def new_game(self, title: str):
        """Creates a new game directory names after whatever the id should be for
        the next game. Also generates gameinfo.json for information of the game and
        scores.csv for the scores.

        Args:
            title: the title name of whatever game you want to create
        """
        if self.check_if_game_exists(title):
            return None
        gameid = len(os.listdir(src("data/games/")))+1
        os.mkdir(src(f"data/games/{gameid}"))

        with open(src(f"data/games/{gameid}/gameinfo.json"), "w", encoding="utf-8") as info:
            json.dump(vars(Game(title, gameid)), info)

        with open(src(f"data/games/{gameid}/scores.csv"), "w", encoding="utf-8") as something:
            something.close()

    def game_json_list(self):
        """The function reads the games.json in each game folder and appends it to
        a list which gets sorted based on game id number and then returned.

        Returns:
            list: Sorted list of the content in each games.json.
        """
        templist = []
        listdir = os.listdir(src("data/games"))
        for gameid in listdir:
            with open(src(f"data/games/{gameid}/gameinfo.json"), "r", encoding="utf-8") as file:
                templist.append(json.load(file))
        return sorted(templist, key=lambda game: game["id"])

    def get_game_info(self, gameid):
        """Get the contents of the gameinfo.json for a specific game.

        Args:
            gameid: The id of the game(which corresponds to the name of the folder)

        Returns:
            list: Returns the variables in gameinfo.json in a list with only this element in it.
        """
        with open(src(f"data/games/{gameid}/gameinfo.json"), "r", encoding="utf-8") as gameinfo:
            return json.load(gameinfo)

    def delete_all_games(self):
        """This function is used for setting up the program and also in tests.
        """
        try:
            shutil.rmtree(src("data/games"))
        except:
            pass
        os.mkdir(src("data/games"))

    def check_if_game_exists(self, title:str):
        """Checks to see if a game has already been created with the same name

        Args:
            title (str): Title/name of the game

        Returns:
            Boolean : True of False depending on if it has been created
        """
        gamelist = self.game_json_list()
        for game in gamelist:
            if title.lower()==game["title"].lower():
                return True
        return False
