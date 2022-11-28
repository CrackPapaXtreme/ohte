import tkinter as tk
from gamemgmt import GameMgr
from usermgmt import UserMgr
from scoremgmt import ScoreMgr

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()


class Scoreboard(tk.Frame):
    def __init__(self, parent, controller, gameid):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title = tk.Label(self, text="Highscores!", font=controller.title_font)
        title.grid(row=0, column=0, pady=10, padx=10)

        self.grid_columnconfigure(1, weight=1, minsize=500)
        self._username_field = tk.Entry(self, textvariable="Username")
        submit_new_username = tk.Button(
            self,
            text="Create new user!",
            command=lambda: UMgr.create_user(self._username_field.get()))
        self._username_field.grid(
            row=0, column=2, sticky="e", padx=20, pady=20)
        submit_new_username.grid(row=0, column=3, sticky="e", padx=20, pady=20)

        for gameinfo in GMgr.game_json_list():
            titlename = tk.Label(self, text=gameinfo["title"])
            titlename.grid()
            gameselectbutton = tk.Button(
                self,
                text=gameinfo["title"],
                command=lambda: controller.show_frame(gameinfo["id"]))
            gameselectbutton.grid()
