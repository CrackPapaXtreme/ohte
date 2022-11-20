import json
import os
from user import User

usersjson=os.path.join(os.path.dirname(__file__),"users.json")

def reset_users_json():
    adminuser=User("admin",0)
    adminuser.admin=True
    with open(usersjson, "w") as file:
        json.dump([vars(adminuser)],file)

def username_taken(userlist:list,username:str):
    for user in userlist:
        print(user["name"])
        if user["name"]==username.lower():
            return True #Username is taken
    return False #username not taken

def create_user(name:str):
    with open(usersjson,"r") as userlist:
        users = json.load(userlist)
    if username_taken(users,name):
        return False
    users.append(vars(User(name,len(users))))
    with open(usersjson, "w") as userlist:
        json.dump(users,userlist)
    return True



if __name__=="__main__":
    reset_users_json()
    create_user("nati")
    create_user("nati")
