import json
from objects import Game
from dir import src
import os

class GameMgr:
    def new_game(title:str, about:str=None):
        # Create new folder with id as name
        gameid = len(os.listdir(src("games/")))+1
        os.mkdir(src(f"games/{gameid}"))
                
        # Create gameinfo.json
        with open(src(f"games/{gameid}/gameinfo.json"), "w") as info:
            json.dump(vars(Game(title,gameid,about)),info)
        
        # Create empty csv
        with open(src(f"games/{gameid}/scores.csv"),"w") as something:
            pass
    
    def game_json_list(self):
        __templist = []
        for gameid in os.listdir(src("games")):
            with open(src(f"games/{gameid}/gameinfo.json")) as file:
                __templist.append(json.load(file))
        return __templist

    def get_game_info(self,gameid):
        with open(src(f"games/{gameid}/gameinfo.json")) as gameinfo:
            return json.load(gameinfo)

    def delete_all_games(self):
        os.remove(src("games"))

    # Plans

    # def remove_game_visibility(gameid):

    # def check_for_existing_game(title):


if __name__=="__main__":
    gmr=GameMgr
    gmr.new_game("Post Void", "FPS")
    gmr.new_game("Tetris", "Cool game")