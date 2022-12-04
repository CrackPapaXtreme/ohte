from usermgmt import UserMgr
from gamemgmt import GameMgr
from scoremgmt import ScoreMgr
from random import randint

GameMgr.delete_all_games()
UserMgr.reset_users_json(self=None)
for num in range(1, 5):
    GameMgr.new_game(f"Game{num}")
for num in range(1, 11):
    UserMgr.create_user_test(f"User{num}")
for gid in range(1, 5):
    for uid in range(10):
        ScoreMgr.add_score(
            self=None,
            gameid=gid,
            userid=uid,
            score=randint(1, 1000)
        )
