class User:
    def __init__(self, name: str, userid: int):
        self.name = str(name.lower())
        self.id = userid
        self.displayname = name


class Game:
    def __init__(self, title: str, gameid: int):
        self.title = title
        self.id = gameid
