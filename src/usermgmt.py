import json
from objects import User
from get_local_dir import src


def users():
    with open(src("users.json"),"r") as userlist:
        users = json.load(userlist)
    for user in users:
        print(f'{user["id"]} - {user["displayname"]}')

def reset_users_json():
    #users json init with admin as user 0
    with open(src("users.json"), "w") as file:
        json.dump([vars(User("admin",0))],file,indent=4)

def username_taken(userlist:list,username:str):
    for user in userlist:
        if user["name"]==username.lower():
            return True #Username is taken
    return False #username not taken

def create_user(name:str):
    if len(name)>24:
        return False
    with open(src("users.json"),"r") as userlist:
        users = json.load(userlist)
    if username_taken(users,name):
        return False
    users.append(vars(User(name,len(users))))
    with open(src("users.json"), "w") as userlist:
        json.dump(users,userlist,indent=4)
    return True

def get_user_id(username):
    with open(src("users.json"),"r") as userlist:
        list=json.load(userlist)
    for user in list:
        if user["name"]==username.lower():
            return user["id"]
    return None




if __name__=="__main__":
    reset_users_json()
    create_user("nati")
    create_user("nati")
