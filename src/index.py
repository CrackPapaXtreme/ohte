from usermgmt import create_user,reset_users_json

while True:
    try:
        cmd=int(input("[0-Exit | 1-Add new user | 2-Reset users.json]->"))
    except:
        print("not a cmd")
        continue
    if cmd==1:
        name=str(input("username: "))
        if create_user(name):
            print("username registered!")
            continue
        else:
            print("username taken, pick another one!")
    elif cmd==2: 
        reset_users_json()
    else:break