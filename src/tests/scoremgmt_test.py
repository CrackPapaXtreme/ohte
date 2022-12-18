import unittest
from misc.setup import format_program
from services.scoremgmt import ScoreMgr
from services.gamemgmt import GameMgr
from misc.dir import src
import csv

smgr = ScoreMgr()
gmgr = GameMgr()


class TestScoreMgr(unittest.TestCase):
    def test_add_scores(self):
        format_program()
        gmgr.new_game("game1")
        smgr.add_score(1, 69, 420)
        smgr.add_score(1, 420, 69)
        csv_file = csv.reader(open(src(f"data/games/1/scores.csv"), "r"))
        current = next(csv_file)
        self.assertEqual(int(current[0]), 69)
        self.assertEqual(int(current[2]), 420)
        current = next(csv_file)
        self.assertEqual(int(current[0]), 420)
        self.assertEqual(int(current[2]), 69)

    def test_only_takes_integer_type(self):
        self.assertRaises(TypeError, smgr.add_score(1, 1, "abc"))
