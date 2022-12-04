from usermgmt import UserMgr
from gamemgmt import GameMgr
from scoremgmt import ScoreMgr
from random import randint
import os


def format_program():
    GameMgr.delete_all_games()
    UserMgr.reset_users_json(self=None)


format_program()
