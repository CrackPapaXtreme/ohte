import json
from objects import User
from dir import src


class UserMgr:
    def reset_users_json(self):
        """Deletes all users by setting the contents of users.json to just [].
        """
        with open(src("users.json"), "w", encoding="utf-8") as userlist:
            json.dump([], userlist, indent=4)

    def username_taken(self, username: str):
        """Checks to see if a username is taken

        Args:
            username (str): Name of user to check

        Returns:
            boolean : True or false depending on if user is taken or not.
        """
        with open(src("users.json"), "r", encoding="utf-8") as users:
            userlist = json.load(users)
        for user in userlist:
            if user["name"] == username.lower():
                return True
        return False

    def create_user(self, name: str):
        """Creates new user if it is not taken already and if the length of the username is under 32
        characters

        Args:
            name (str): Name of new user to be created

        Returns:
            boolean : True if the username was created successfully, false if not.
        """
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

    def get_user_id(self, username: str):
        """Fetches the userid of a user

        Args:
            username (str): The username for which the ID needs to be given

        Returns:
            None if the user is not found, userID (int) if it is found.
        """
        with open(src("users.json"), "r", encoding="utf-8") as userlist:
            templist = json.load(userlist)
        for user in templist:
            if user["name"] == username.lower():
                return user["id"]
        return None

    def get_displayname(self, uid: int):
        """Fetches the displayname of a user

        Args:
            id (int): The userID to fetch displayname for.

        Returns:
            str: Displayname
        """
        with open(src("users.json"), "r", encoding="utf-8") as userlist:
            templist = json.load(userlist)
        return templist[uid]["displayname"]
