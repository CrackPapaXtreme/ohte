from usermgmt import UserMgr
from gamemgmt import GameMgr

UMgr = UserMgr()
GMgr = GameMgr()


def format_program():
    """Deletes all games and resets the users to make the program ready for first time use.
    """
    GMgr.delete_all_games()
    UMgr.reset_users_json()


# This is here so that the function gets executes with poetry run invoke setup
format_program()
