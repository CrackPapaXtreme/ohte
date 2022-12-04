import unittest
import json
from scoremgmt import ScoreMgr
from gamemgmt import GameMgr
from dir import src
import csv

smgr = ScoreMgr
gmgr = GameMgr


class TestScoreMgr(unittest.TestCase):
    def test_add_scores(self):
        gmgr.delete_all_games()
        gmgr.new_game(None, "game1")
        smgr.add_score(None, 1, 69, 420)
        smgr.add_score(None, 1, 420, 69)
        csv_file = csv.reader(open(src(f"games/1/scores.csv"), "r"))
        current = next(csv_file)
        self.assertEqual(int(current[0]), 69)
        self.assertEqual(int(current[2]), 420)
        current = next(csv_file)
        self.assertEqual(int(current[0]), 420)
        self.assertEqual(int(current[2]), 69)
