import unittest
import json
from gamemgmt import GameMgr
from dir import src

gmgr = GameMgr()


class TestGameMgr(unittest.TestCase):
    def test_create_new_game(self):
        gmgr.new_game("game1")