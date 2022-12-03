import tkinter as tk
from tkinter import Toplevel
from gamemgmt import GameMgr
from usermgmt import UserMgr
from scoremgmt import ScoreMgr

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()


class Scoreboard(tk.Frame):
    def __init__(self, parent, controller, gameid):
        self._gameid = gameid
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

    def open_add_score_window(self):
        window = Toplevel()
        window.title("Add score")

        title = tk.Label(window, text="Submit score")
        usernamebox = tk.Entry(window)
        scorebox = tk.Entry(window)
        submitbutton = tk.Button(
            window,
            text="Submit score",
            command=self.add_score_to_file(usernamebox.get(), scorebox.get())
        )

        title.grid()
        usernamebox.grid()
        scorebox.grid()
        submitbutton.grid()

    def add_score_to_file(self, username, score):
        print(username)
        print(str(score))

    def create_new_user(self):
        if len(self._username_field.get()) < 32:
            if UMgr.create_user(self._username_field.get()):
                self._username_field.delete(0, "end")
            else:
                self._notify = "Username taken"
        else:
            self._notify = "Username too long (max 24chars)"
        print(self._notify)


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
            gameselectbutton = tk.Button(
                self,
                text=gameinfo["title"],
                command=lambda: controller.show_frame(gameinfo["id"]),
                height=5)
            gameselectbutton.grid(
                column=col_num, row=row_num, pady=10, padx=10, sticky="ew")
            if not col_num in range(4):
                col_num = 0
                row_num += 1
            else:
                col_num += 1

        # This is for visualising the column widths
        # for num in range(5):
        #    tk.Entry(self).grid(column=num,row=5, sticky="we")

    def create_new_user(self):
        if len(self._username_field.get()) < 32:
            if UMgr.create_user(self._username_field.get()):
                self._username_field.delete(0, "end")
            else:
                self._notify = "Username taken"
        else:
            self._notify = "Username too long (max 24chars)"
        print(self._notify)
