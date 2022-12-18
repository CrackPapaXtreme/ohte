from random import randint
from services.scoremgmt import ScoreMgr
from services.gamemgmt import GameMgr
from services.usermgmt import UserMgr
from misc.setup import format_program

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()

"""Function deletes all games and users, creates 4 games and 10 users with a submission in each game
of a random value between 1 and 1000.
"""


def gen():
    format_program()
    for num in range(1, 5):
        GMgr.new_game(f"Game{num}")
    for num in range(1, 11):
        UMgr.create_user(f"User{num}")
    for gid in range(1, 5):
        for uid in range(10):
            SMgr.add_score(
                gameid=gid,
                userid=uid,
                score=randint(1, 1000)
            )


if __name__ == "__main__":
    gen()
