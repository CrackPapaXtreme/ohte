import tkinter as tk
from gamemgmt import GameMgr
from usermgmt import UserMgr
from scoremgmt import ScoreMgr

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()


class Scoreboard(tk.Frame):
    def __init__(self, parent, controller, gameid):
        self._gameid=gameid
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self._notify = ""

        title = tk.Label(self, text="Highscores!", font=controller.title_font)
        title.grid(row=0, column=0, pady=10, padx=20)

        notify = tk.Label(self, text=self._notify)
        notify.grid(column=2, row=0)

        self.grid_columnconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(1, minsize=200, weight=1)
        self.grid_columnconfigure(2, minsize=200, weight=1)
        self.grid_columnconfigure(3, minsize=200, weight=1)
        self.grid_columnconfigure(4, minsize=200, weight=1)

        self._username_field = tk.Entry(self)
        self._submit_new_username = tk.Button(
            self,
            text="Create new user!",
            command=self.create_new_user
        )
        self._username_field.grid(row=0, column=3, sticky="e", padx=10)
        self._submit_new_username.grid(row=0, column=4, sticky="w", padx=10)

        self._game_title = tk.Label(
            self,
            text=GMgr.get_game_info(self._gameid)["title"],
            font=controller.subtitle_font
        )
        self._game_title.grid(row=1, column=0, sticky="w", padx=30, pady=20)

        tk.Label(
            self,
            text="Username:",
            font=controller.normal_font
        ).grid(row=2, column=0, sticky="w", padx=30)
        tk.Label(
            self,
            text="Score:",
            font=controller.normal_font
        ).grid(row=3, column=0, sticky="w", padx=30)

        self.submit_score_username = tk.Entry(self)
        self.submit_score_score = tk.Entry(self)

        self.submit_score_username.grid(row=2, column=1, sticky="w")
        self.submit_score_score.grid(row=3, column=1, sticky="w")

        submit_new_score_button = tk.Button(
            self,
            text="Submit new score"
        )
        submit_new_score_button.grid(
            row=4, column=0, padx=30, pady=10, columnspan=2, sticky="ew")

        self.list_best_scores

        self._backbutton = tk.Button(
            self,
            text="Back to Main Menu",
            command=lambda: controller.show_frame(0)
        )
        self._backbutton.grid(row=99,column=0,padx=20)
    def add_score_to_file(self, username, score):
        print(username)
        print(str(score))

    def create_new_user(self):
        if len(self._username_field.get()) < 32:
            if UMgr.create_user(self._username_field.get()):
                self._username_field.delete(0, "end")
                self._nofity = "Username created"
            else:
                self._notify = "Username taken"
        else:
            self._notify = "Username too long (max 24chars)"
        print(self._notify)

    def list_best_scores(self):
        scorelist = SMgr.get_sorted_highscores_list(self._gameid)
        scorerow=20
        for score in scorelist:
            if scorerow%2:
                fgcolor="white"
            else:
                fgcolor="yellow"
            tk.Label(
                self,
                text=UMgr.get_displayname(score[0]),
                font=self.controller.normal_font,
                fg=fgcolor
            ).grid(row=scorerow,column=0, padx= 10, sticky="e")
            tk.Label(
                self,
                text=score[1],
                font=self.controller.normal_font,
                fg=fgcolor
            ).grid(row=scorerow, column=2, sticky="ew")
            tk.Label(
                self,
                text=score[2],
                font=self.controller.normal_font,
                fg=fgcolor
            ).grid(row=scorerow, column=5, sticky="w")
            scorerow+=1


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self._notify = ""

        title = tk.Label(self, text="Highscores!", font=controller.title_font)
        title.grid(row=0, column=0, pady=10, padx=20)

        notify = tk.Label(self, text=self._notify)
        notify.grid(column=2, row=0)

        self.grid_columnconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(1, minsize=200, weight=1)
        self.grid_columnconfigure(2, minsize=200, weight=1)
        self.grid_columnconfigure(3, minsize=200, weight=1)
        self.grid_columnconfigure(4, minsize=200, weight=1)

        self._username_field = tk.Entry(self)
        submit_new_username = tk.Button(
            self,
            text="Create new user!",
            command=self.create_new_user
        )
        self._username_field.grid(row=0, column=3, sticky="e", padx=10)
        submit_new_username.grid(row=0, column=4, sticky="w", padx=10)

        col_num = 0
        row_num = 1
        for gameinfo in GMgr.game_json_list():
            #titlename = tk.Label(self, text=gameinfo["title"])
            self._gameselectbutton = tk.Button(
                self,
                text=gameinfo["title"],
                command=lambda id=gameinfo["id"]: controller.show_frame(id),
                height=5)
            self._gameselectbutton.grid(
                column=col_num, row=row_num, pady=10, padx=10, sticky="ew")
            if not col_num in range(4):
                col_num = 0
                row_num += 1
            else:
                col_num += 1

        # Create new game with admin passwd
        self._create_new_game_box = tk.Entry(self)
        self._create_new_game_admin_pwd_box = tk.Entry(self)
        self._create_new_game_button = tk.Button(
            self,
            text="Add new game(admin)",
            command=self.add_new_game(self._create_new_game_box.get(),self._create_new_game_admin_pwd_box.get())
        )
        self._create_new_game_box.grid(row=99,column=0,sticky="ew", padx=10)
        self._create_new_game_admin_pwd_box.grid(row=99,column=1, sticky="ew", padx=10)
        self._create_new_game_button.grid(row=99,column=2, sticky="w")

        # This is for visualising the column widths
        # for num in range(5):
        #    tk.Entry(self).grid(column=num,row=5, sticky="we")

    def create_new_user(self):
        if len(self._username_field.get()) < 32:
            if UMgr.create_user(self._username_field.get()):
                self._username_field.delete(0, "end")
                self._notify = "Username created"
            else:
                self._notify = "Username taken"
        else:
            self._notify = "Username too long (max 24chars)"
        print(self._notify)

    def add_new_game(self, title, adminpwd):
        pass