from shutil import rmtree
from os import mkdir
try:
    from misc.dir import src
except ModuleNotFoundError:
    from dir import src


def format_program():
    """Deletes all games and resets the users to make the program ready for first time use.
    """
    try:
        rmtree(src("data"))
    except FileNotFoundError:
        pass
    mkdir(src("data"))
    mkdir(src("data/games"))
    with open(src("data/users.json"), "w", encoding="utf-8") as usersjson:
        usersjson.write("[]")
        usersjson.close()
    with open(src("data/adminpassword.txt"), "w", encoding="utf-8") as adminpasswordfile:
        adminpasswordfile.write("yay")
        adminpasswordfile.close()
    with open(src("data/usernameblacklist.txt"), "w", encoding="utf-8") as blacklist:
        blacklist.write("admin")
        blacklist.close()


# This is here so that the function gets executes with poetry run invoke setup
if __name__ == "__main__":
    format_program()
