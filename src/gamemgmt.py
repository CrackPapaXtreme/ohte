import json
from objects import Game
from dir import src
import os
import shutil


class GameMgr:
    def new_game(title: str):
        # Create new folder with id as name
        gameid = len(os.listdir(src("games/")))+1
        os.mkdir(src(f"games/{gameid}"))

        # Create gameinfo.json
        with open(src(f"games/{gameid}/gameinfo.json"), "w", encoding="utf-8") as info:
            json.dump(vars(Game(title, gameid)), info)

        # Create empty csv
        with open(src(f"games/{gameid}/scores.csv"), "w", encoding="utf-8") as something:
            something.close()

    def game_json_list(self):
        templist = []
        for gameid in os.listdir(src("games")):
            with open(src(f"games/{gameid}/gameinfo.json"), "r", encoding="utf-8") as file:
                templist.append(json.load(file))
        return sorted(templist, key=lambda game: game["id"])

    def get_game_info(self, gameid):
        with open(src(f"games/{gameid}/gameinfo.json"), "r", encoding="utf-8") as gameinfo:
            return json.load(gameinfo)

    def delete_all_games():
        for game in os.listdir(src("games")):
            shutil.rmtree(src(f"games/{game}"))

    # Plans

    # def remove_game_visibility(gameid):

    # def check_for_existing_game(title):
