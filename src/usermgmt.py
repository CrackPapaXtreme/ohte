import json
from objects import User
from dir import src


class UserMgr:
    def reset_users_json(self):
        with open(src("users.json"), "w", encoding="utf-8") as userlist:
            json.dump([], userlist, indent=4)

    def username_taken(self, username: str):
        with open(src("users.json"), "r", encoding="utf-8") as users:
            userlist = json.load(users)
        for user in userlist:
            if user["name"] == username.lower():
                return True
        return False

    def create_user(self, name: str):
        with open(src("users.json"), "r", encoding="utf-8") as userlist:
            users = json.load(userlist)
        if len(name) > 32:
            return False
        if self.username_taken(name):
            return False
        users.append(vars(User(name, len(users))))
        with open(src("users.json"), "w", encoding="utf-8") as userlist:
            json.dump(users, userlist, indent=4)
        return True

    def create_user_test(name: str):
        with open(src("users.json"), "r", encoding="utf-8") as userlist:
            users = json.load(userlist)
        users.append(vars(User(name, len(users))))
        with open(src("users.json"), "w") as userlist:
            json.dump(users, userlist, indent=4)
        return True

    def get_user_id(self, username: str):
        with open(src("users.json"), "r", encoding="utf-8") as userlist:
            list = json.load(userlist)
        for user in list:
            if user["name"] == username.lower():
                return user["id"]
        return None

    def get_displayname(self, id: int):
        with open(src("users.json"), "r", encoding="utf-8") as userlist:
            list = json.load(userlist)
        return list[id]["displayname"]
