from datetime import datetime

class User:
    def __init__(self, name:str, userid:int):
        self.name=str(name.lower())
        self.id=userid
        self.displayname=name
        self.highscores={}
        self.submissions=[]

# Currently not in use
"""
class Game:
    def __init__(self, title:str, gameid:int):
        self.title=title
        self.id=gameid
        self.about=""
        self.first=None

class Score:
    def __init__(self, score:int, userid:int, time:datetime):
        self.score=score
        self.id=userid
        self.visible=True
        self.submission_time=time"""