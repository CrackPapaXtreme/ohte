import tkinter as tk
from gamemgmt import GameMgr
from usermgmt import UserMgr
from scoremgmt import ScoreMgr
from dir import src

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()


class Scoreboard(tk.Frame):
    def __init__(self, parent, controller, gameid):
        self._gameid = gameid
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.ui_title_and_game_title()

        self.ui_configure_columns()

        self.ui_username_creation()

        self.ui_score_submission()

        self.ui_list_best_scores()

        self.ui_back_button()

    def ui_title_and_game_title(self):
        title = tk.Label(self, text="Highscores!",
                         font=self.controller.title_font)
        title.grid(row=0, column=0, pady=10, padx=20)

        self._game_title = tk.Label(
            self,
            text=GMgr.get_game_info(self._gameid)["title"],
            font=self.controller.subtitle_font
        )
        self._game_title.grid(row=1, column=0, sticky="w", padx=30, pady=20)

    def ui_score_submission(self):
        tk.Label(
            self,
            text="Username:",
            font=self.controller.normal_font
        ).grid(row=2, column=0, sticky="w", padx=30)
        tk.Label(
            self,
            text="Score:",
            font=self.controller.normal_font
        ).grid(row=3, column=0, sticky="w", padx=30)

        self.submit_score_username = tk.Entry(self)
        self.submit_score_score = tk.Entry(self)

        self.submit_score_username.grid(row=2, column=1, sticky="w")
        self.submit_score_score.grid(row=3, column=1, sticky="w")

        submit_new_score_button = tk.Button(
            self,
            text="Submit new score",
            command=self.add_new_score_to_scoreboard
        )
        submit_new_score_button.grid(
            row=4, column=0, padx=30, pady=10, columnspan=2, sticky="ew")

    def ui_username_creation(self):
        self._username_field = tk.Entry(self)
        self._submit_new_username = tk.Button(
            self,
            text="Create new user!",
            command=self.create_new_user
        )
        self._username_field.grid(row=0, column=3, sticky="e", padx=10)
        self._submit_new_username.grid(row=0, column=4, sticky="w", padx=10)

    def ui_configure_columns(self):
        self.grid_columnconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(1, minsize=200, weight=1)
        self.grid_columnconfigure(2, minsize=200, weight=1)
        self.grid_columnconfigure(3, minsize=200, weight=1)
        self.grid_columnconfigure(4, minsize=200, weight=1)

    def ui_back_button(self):
        self._backbutton = tk.Button(
            self,
            text="Back to Main Menu",
            command=lambda: self.controller.show_frame(0)
        )
        self._backbutton.grid(row=99, column=0, padx=20)

    def ui_list_best_scores(self):
        scorelist = SMgr.get_sorted_highscores_list(self._gameid)
        scorerow = 20
        for score in scorelist:
            if not scorerow % 2:
                bgcolor = "white"
            else:
                bgcolor = "light gray"
            tk.Label(
                self,
                text=score[1],
                font=self.controller.normal_font,
                bg=bgcolor
            ).grid(row=scorerow, column=0, sticky="ew", columnspan=5, padx=50)
            tk.Label(
                self,
                text=score[2],
                font=self.controller.normal_font,
                bg=bgcolor
            ).grid(row=scorerow, column=4, sticky="w")
            tk.Label(
                self,
                text=UMgr.get_displayname(int(score[0])),
                font=self.controller.normal_font,
                bg=bgcolor
            ).grid(row=scorerow, column=0, padx=10, sticky="e")
            scorerow += 1

    def add_new_score_to_scoreboard(self):
        try:
            thescore = int(self.submit_score_score.get())
        except: 
            return
        theuserid = UMgr.get_user_id(self.submit_score_username.get())
        if not theuserid==None:
            SMgr.add_score(self._gameid, theuserid, thescore)
            self.submit_score_score.delete(0, "end")
            self.submit_score_username.delete(0, "end")
            self.controller.reload_frame(self._gameid)
        else:
            pass
    def create_new_user(self):
        if UMgr.create_user(self._username_field.get()):
            self._username_field.delete(0, "end")


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # title
        title = tk.Label(self, text="Highscores!",
                         font=self.controller.title_font)
        title.grid(row=0, column=0, pady=10, padx=20)

        self.ui_configure_columns()

        self.ui_username_creation()

        self.ui_game_buttons()

        self.ui_add_game()

    def ui_add_game(self):
        self.grid_rowconfigure(97, minsize=300)
        tk.Label(
            self,
            text="Game name",
            font=self.controller.normal_font
        ).grid(row=98, column=0, sticky="sew")
        tk.Label(
            self,
            text="Admin password",
            font=self.controller.normal_font
        ).grid(row=98, column=1, sticky="sew")
        # Create new game with admin passwd
        self._create_new_game_box = tk.Entry(self)
        self._create_new_game_admin_pwd_box = tk.Entry(self)
        self._create_new_game_button = tk.Button(
            self,
            text="Add new game",
            command=self.add_new_game
        )
        self._create_new_game_box.grid(row=99, column=0, sticky="ew", padx=10)
        self._create_new_game_admin_pwd_box.grid(
            row=99, column=1, sticky="ew", padx=10)
        self._create_new_game_button.grid(row=99, column=2, sticky="w")

    def ui_username_creation(self):
        self._username_field = tk.Entry(self)
        submit_new_username = tk.Button(
            self,
            text="Create new user!",
            command=self.create_new_user
        )
        self._username_field.grid(row=0, column=3, sticky="e", padx=10)
        submit_new_username.grid(row=0, column=4, sticky="w", padx=10)

    def ui_game_buttons(self):
        col_num = 0
        row_num = 1
        for gameinfo in GMgr.game_json_list():
            self._gameselectbutton = tk.Button(
                self,
                text=gameinfo["title"],
                command=lambda id=gameinfo["id"]: self.controller.show_frame(
                    id),
                height=5)
            self._gameselectbutton.grid(
                column=col_num, row=row_num, pady=10, padx=10, sticky="ew")
            if not col_num in range(4):
                col_num = 0
                row_num += 1
            else:
                col_num += 1

    def ui_configure_columns(self):
        self.grid_columnconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(1, minsize=200, weight=1)
        self.grid_columnconfigure(2, minsize=200, weight=1)
        self.grid_columnconfigure(3, minsize=200, weight=1)
        self.grid_columnconfigure(4, minsize=200, weight=1)

    def create_new_user(self):
        if UMgr.create_user(self._username_field.get()):
            self._username_field.delete(0, "end")

    def add_new_game(self):
        name = self._create_new_game_box.get()
        pwd = self._create_new_game_admin_pwd_box.get()
        adminpassword = open(src("adminpassword.txt")).readline()
        if pwd == adminpassword:
            GMgr.new_game(name)
            self._create_new_game_admin_pwd_box.delete(0, "end")
            self._create_new_game_box.delete(0, "end")
            self.controller.reload_frame(0)
