class User:
    def __init__(self, name: str, userid: int):
        """User class

        Args:
            name (str): Name inputted by the user. A variation of this is turned in to all lowercase
            and set as displayname. This is to prevent duplicate names.
            userid (int): UserID assigned by UserManager
        """
        self.name = str(name.lower())
        self.id = userid
        self.displayname = name


class Game:
    def __init__(self, title: str, gameid: int):
        """Game class

        Args:
            title (str): Name of the game
            gameid (int): Gameid given by GameManager
        """
        self.title = title
        self.id = gameid
