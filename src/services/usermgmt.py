import json
from misc.objects import User
from misc.dir import src


class UserMgr:
    def reset_users_json(self):
        """Deletes all users by setting the contents of users.json to just [].
        """
        with open(src("data/users.json"), "w", encoding="utf-8") as userlist:
            json.dump([], userlist, indent=4)

    def username_taken(self, username: str):
        """Checks to see if a username is taken

        Args:
            username (str): Name of user to check

        Returns:
            boolean : True or false depending on if user is taken or not.
        """
        with open(src("data/users.json"), "r", encoding="utf-8") as users:
            userlist = json.load(users)
            users.close()
        for user in userlist:
            if user["name"] == username.lower():
                return True
        return False

    def create_user(self, inputname: str):
        """Creates new user if it is not taken already and if the length of the username is under 32
        characters

        Args:
            name (str): Name of new user to be created

        Returns:
            boolean : True if the username was created successfully, false if not.
        """
        name = self.remove_whitespace(inputname)
        with open(src("data/users.json"), "r", encoding="utf-8") as userlist:
            users = json.load(userlist)
            userlist.close()
        if name == "":
            self.list_users(users)
            return False
        if not self.check_if_allowed(name):
            return False
        if self.username_taken(name):
            return False
        users.append(vars(User(name, len(users))))
        with open(src("data/users.json"), "w", encoding="utf-8") as userlist:
            json.dump(users, userlist, indent=4)
            userlist.close()
        return True

    def get_user_id(self, username: str):
        """Fetches the userid of a user

        Args:
            username (str): The username for which the ID needs to be given

        Returns:
            None if the user is not found, userID (int) if it is found.
        """
        with open(src("data/users.json"), "r", encoding="utf-8") as userlist:
            templist = json.load(userlist)
            userlist.close()
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
        with open(src("data/users.json"), "r", encoding="utf-8") as userlist:
            templist = json.load(userlist)
            userlist.close()
        return templist[uid]["displayname"]

    def remove_whitespace(self, userinput: str):
        """Returns string without whitespace to prevent similar names from being created " "

        Args:
            input (str): string to remove whitespace from

        Returns:
            string : without whitespace
        """
        return userinput.replace(" ", "")

    def check_if_allowed(self, userinput: str):
        """Checks if username is too long or on blacklist

        Args:
            input (str): username to check

        Returns:
            Boolean : True of false depending on if it is allowed
        """
        if len(userinput) > 16:
            return False
        with open(src("data/usernameblacklist.txt"), "r", encoding="utf-8") as blacklist:
            for line in blacklist:
                if line in userinput:
                    return False
            blacklist.close()
        return True

    def list_users(self, ulist):
        print("Registered usernames:")
        for user in ulist:
            print(user["displayname"])
        print("")
