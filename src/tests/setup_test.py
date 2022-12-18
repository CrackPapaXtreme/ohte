import unittest
from misc.dir import src
import os
import json
from misc.setup import format_program


class TestSetup(unittest.TestCase):
    def test_setup_works(self):
        format_program()
        self.assertEqual(os.listdir(src("data/games")), [])
        with open(src("data/users.json")) as jsonfile:
            emptyjson = json.load(jsonfile)
            jsonfile.close()
        self.assertEqual(emptyjson, [])
