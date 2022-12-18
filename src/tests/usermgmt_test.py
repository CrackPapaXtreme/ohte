import unittest
import json
from services.usermgmt import UserMgr
from misc.dir import src

umgr = UserMgr()


class TestUserMgr(unittest.TestCase):
    def test_reset_users_json(self):
        umgr.reset_users_json()
        with open(src("data/users.json"), "r") as file:
            content = json.load(file)
        self.assertEqual([], content)

    def test_create_user(self):
        umgr.reset_users_json()
        # creates two users and checks if they are written
        self.assertTrue(umgr.create_user("nati"))
        self.assertTrue(umgr.create_user("CrackPapaXtreme"))
        with open(src("data/users.json"), "r") as file:
            content = json.load(file)
        self.assertEqual(
            [
                {
                    "name": "nati",
                    "id": 0,
                    "displayname": "nati"
                },
                {
                    "name": "crackpapaxtreme",
                    "id": 1,
                    "displayname": "CrackPapaXtreme"
                }
            ], content)

    def test_username_too_long(self):
        umgr.reset_users_json()
        self.assertFalse(umgr.create_user(
            "this_username_is_longer_than_24_characters"))

    def test_username_taken(self):
        umgr.reset_users_json()
        umgr.create_user("username_taken")
        self.assertFalse(umgr.create_user("username_taken"))

    def test_get_user_id_from_name(self):
        umgr.reset_users_json()
        umgr.create_user("name")
        umgr.create_user("eman")
        self.assertEqual(umgr.get_user_id("name"), 0)
        self.assertEqual(umgr.get_user_id("eman"), 1)

    def test_get_user_id_from_nonexistent_user_returns_none(self):
        umgr.reset_users_json()
        self.assertIsNone(umgr.get_user_id("this user doesn't exist"))
