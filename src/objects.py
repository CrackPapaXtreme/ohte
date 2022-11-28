class User:
    def __init__(self, name: str, userid: int):
        self.name = str(name.lower())
        self.id = userid
        self.displayname = name
        self.highscores = {}
        self.submissions = []

# Currently not in use


class Game:
    def __init__(self, title: str, gameid: int, about: str):
        self.title = title
        self.id = gameid
        self.about = about
        self.first = None
        self.visible = True


class Score:
    def __init__(self, score: int, userid: int, submission_time: str):
        self.score = score
        self.id = userid
        self.visible = True
        self.submission_time = submission_time
