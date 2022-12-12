import json
import os
import shutil
from objects import Game
from dir import src


class GameMgr:
    def new_game(self, title: str):
        """Creates a new game directory names after whatever the id should be for
        the next game. Also generates gameinfo.json for information of the game and
        scores.csv for the scores.

        Args:
            title: the title name of whatever game you want to create
        """
        gameid = len(os.listdir(src("games/")))+1
        os.mkdir(src(f"games/{gameid}"))

        with open(src(f"games/{gameid}/gameinfo.json"), "w", encoding="utf-8") as info:
            json.dump(vars(Game(title, gameid)), info)

        with open(src(f"games/{gameid}/scores.csv"), "w", encoding="utf-8") as something:
            something.close()

    def game_json_list(self):
        """The function reads the games.json in each game folder and appends it to
        a list which gets sorted based on game id number and then returned.

        Returns:
            list: Sorted list of the content in each games.json.
        """
        templist = []
        listdir = os.listdir(src("games"))
        for gameid in listdir:
            with open(src(f"games/{gameid}/gameinfo.json"), "r", encoding="utf-8") as file:
                templist.append(json.load(file))
        return sorted(templist, key=lambda game: game["id"])

    def get_game_info(self, gameid):
        """Get the contents of the gameinfo.json for a specific game.

        Args:
            gameid: The id of the game(which corresponds to the name of the folder)

        Returns:
            list: Returns the variables in gameinfo.json in a list with only this element in it.
        """
        with open(src(f"games/{gameid}/gameinfo.json"), "r", encoding="utf-8") as gameinfo:
            return json.load(gameinfo)

    def delete_all_games(self):
        """This function is used for setting up the program and also in tests.
        """
        try:
            shutil.rmtree(src("games"))
        except:
            pass
        os.mkdir(src("games"))
