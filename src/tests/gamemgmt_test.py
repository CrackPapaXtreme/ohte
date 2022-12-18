import unittest
from misc.setup import format_program
from services.gamemgmt import GameMgr
from misc.dir import src
import os

gmgr = GameMgr()


class TestGameMgr(unittest.TestCase):
    def test_create_new_game(self):
        format_program()
        gmgr.new_game("game1")
        gmgr.new_game("game2")
        self.assertEqual(
            sorted(os.listdir(src("data/games")),
                   key=lambda element: int(element)), ["1", "2"])
        self.assertEqual(
            sorted(os.listdir(src("data/games/1"))),
            ["gameinfo.json", "scores.csv"])
        self.assertEqual(
            sorted(os.listdir(src("data/games/2"))),
            ["gameinfo.json", "scores.csv"])

    def test_doesnt_create_duplicate_games(self):
        self.assertIsNone(gmgr.new_game("game1"))

    def test_game_exists_check_works(self):
        self.assertTrue(gmgr.check_if_game_exists("game1"))
