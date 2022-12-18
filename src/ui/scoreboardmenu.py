import tkinter as tk
from services.scoremgmt import ScoreMgr
from services.gamemgmt import GameMgr
from services.usermgmt import UserMgr

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()


class Scoreboard(tk.Frame):
    def __init__(self, parent, controller, gameid):
        """Initializes the sub-window with content in it. The content depents on
        the gameid argument. The other arguments are for the frame and UI handler.

        Calls other functions to generate ui.

        Args:
            parent : The parent is the frame that the UI handler has given it, which
            is done inthe UI class in index.py.
            controller : The controller is a reference to the UI class which allows for
            the execution of show_frame() and reload_frame() functions from within the menu.
            gameid : This variable determines from which game the data gets pulled.
        """
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
        """Draws the title for the app and game with different fonts.
        """
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
        """Draws the labels to indicate what data to input and where. Inits the entry boxes
        and the button for score submission.
        """
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
        """Configures the columns to make the app look consistent
        """
        self.grid_columnconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(1, minsize=200, weight=1)
        self.grid_columnconfigure(2, minsize=200, weight=1)
        self.grid_columnconfigure(3, minsize=200, weight=1)
        self.grid_columnconfigure(4, minsize=200, weight=1)

    def ui_back_button(self):
        """Back button for returning to the main menu with gameid=0
        """
        self._backbutton = tk.Button(
            self,
            text="Back to Main Menu",
            command=lambda: self.controller.show_frame(0)
        )
        self._backbutton.grid(row=99, column=0, padx=20)

    def ui_list_best_scores(self):
        """Creates the list of the top 10 scores in the game, and the top labels
        (name, date, score) for each column. The bgcolor is made to vary between
        lightgray to white, to make each submission stand out. Scorerow starts at
        20 to make it easier to add stuff in between if wanted. Added rowconfig
        for padding on top and bottom of list.
        """
        self.rowconfigure(10, minsize=10)
        tk.Label(
            self,
            text="Username",
            font=self.controller.normal_font
        ).grid(row=11, column=0, sticky="e")
        tk.Label(
            self,
            text="Date",
            font=self.controller.normal_font
        ).grid(row=11, column=2, sticky="ew")
        tk.Label(
            self,
            text="Score",
            font=self.controller.normal_font
        ).grid(row=11, column=4, sticky="w")

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

        self.rowconfigure(scorerow, minsize=20)

    def add_new_score_to_scoreboard(self):
        """Adds an integer type score to the scoreboard with the ScoreManager, clears the
        entry boxes, and executes the reload_frame() function of the controller. Before
        calling on the ScoreManager, it fetches the userid with UserManager. If the user
        doesn't exist, it doesn't do anything.
        """
        try:
            thescore = int(self.submit_score_score.get())
        except ValueError:
            return
        theuserid = UMgr.get_user_id(self.submit_score_username.get())
        if not theuserid is None:
            SMgr.add_score(self._gameid, theuserid, thescore)
            self.submit_score_score.delete(0, "end")
            self.submit_score_username.delete(0, "end")
            self.controller.reload_frame(self._gameid)
        else:
            pass

    def create_new_user(self):
        """Creates a new user via the UserManager
        """
        if UMgr.create_user(self._username_field.get()):
            self._username_field.delete(0, "end")