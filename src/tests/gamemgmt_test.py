import unittest
import json
from gamemgmt import GameMgr
from dir import src
import os

gmgr = GameMgr


class TestGameMgr(unittest.TestCase):
    def test_create_new_game(self):
        gmgr.delete_all_games()
        gmgr.new_game(None, "game1")
        gmgr.new_game(None, "game2")
        self.assertEqual(
            sorted(os.listdir(src("games")),
                   key=lambda element: int(element)), ["1", "2"])
        self.assertEqual(
            sorted(os.listdir(src("games/1"))),
            ["gameinfo.json", "scores.csv"])
        self.assertEqual(
            sorted(os.listdir(src("games/2"))),
            ["gameinfo.json", "scores.csv"])
