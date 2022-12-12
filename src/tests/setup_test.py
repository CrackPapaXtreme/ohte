import unittest
from dir import src
import os
import json
from setup import format_program


class TestSetup(unittest.TestCase):
    def test_setup_works(self):
        format_program()
        self.assertEqual(os.listdir(src("games")), [])
        with open(src("users.json")) as jsonfile:
            emptyjson = json.load(jsonfile)
        self.assertEqual(emptyjson, [])
