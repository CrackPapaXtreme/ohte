from random import randint
from usermgmt import UserMgr
from gamemgmt import GameMgr
from scoremgmt import ScoreMgr

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()

"""Function deletes all games and users, creates 4 games and 10 users with a submission in each game
of a random value between 1 and 1000.
"""


def gen():
    GMgr.delete_all_games()
    UMgr.reset_users_json()
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


gen()
