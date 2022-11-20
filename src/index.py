from usermgmt import create_user,reset_users_json,users
from get_local_dir import src

commands={
    "x":"x  - exit",
    "n":"n  - create new user",
    "r":"r  - reformat user.json",
    "l":"l  - list all users and their IDs",
    "c":"c  - list commands",
    "g":"g  - select game(WIP)",
}
def main():
    while True:
        
        #Asks for a command, rejects is if it is not found in the dict of commands
        cmd=input("command (c to show commands):")
        if not cmd in commands:
            print("unknown command!")
        
        # Create new username with max length 24 characters
        # If input is admin, it will ask for the admin password.
        # Calls the function create_user() and gives user feedback based on frue/false result.
        if cmd=="n":
            name=str(input("username (max 24 chars): "))
            try:
                if len(name)>24:
                        raise Exception("Too long!")
            except Exception:
                print("username too long, max. 24 chars!")
            else:
                if name.lower()=="admin":
                    with open(src("adminpasswd.txt"),"r") as passwdfile:
                        passwd=passwdfile.read()
                    if input("admin password: ")==passwd:
                            print("password correct!(admin mode wip)")
                elif create_user(name):
                    print("username registered!")
                    continue
                else:
                    print("username taken, pick another one!")

        # dev command resets users.json to have only admin user
        elif cmd=="r": 
                reset_users_json()

        # prints registered users
        elif cmd == "l":
                users()

        # prints available commands
        elif cmd=="c":
            for command in commands:
                print(commands[command])

        # maybe instead of a letter as a command the game would be chosen with id
        elif cmd=="g":
            print("wip")

        # x to exit
        elif cmd=="x":
            break

main()