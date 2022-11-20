class User:
    def __init__(self, name:str, id:int):
        self.name=str(name.lower())
        self.id=id
        self.displayname=name
        self.admin=False