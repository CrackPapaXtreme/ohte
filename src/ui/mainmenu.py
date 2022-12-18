import tkinter as tk
from services.scoremgmt import ScoreMgr
from services.gamemgmt import GameMgr
from services.usermgmt import UserMgr
from misc.dir import src

UMgr = UserMgr()
GMgr = GameMgr()
SMgr = ScoreMgr()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        """Initializes the sub-window with content in it. The other arguments are for
        the frame and UI handler.

        Calls other functions to generate ui.

        Args:
            parent : The parent is the frame that the UI handler has given it, which
            is done inthe UI class in index.py.
            controller : The controller is a reference to the UI class which allows for
            the execution of show_frame() and reload_frame() functions from within the menu.
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.ui_title()

        self.ui_configure_columns()

        self.ui_username_creation()

        self.ui_game_buttons()

        self.ui_add_game()

    def ui_title(self):
        """Draws the app title on the top left "Highscores!"
        """
        title = tk.Label(self, text="Highscores!",
                         font=self.controller.title_font)
        title.grid(row=0, column=0, pady=10, padx=20)

    def ui_add_game(self):
        """Creates menu for adding games on the bottom of the screen. Labels, entryboxes and button.
        """
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
        """Draws UI for username creation
        """
        self._username_field = tk.Entry(self)
        submit_new_username = tk.Button(
            self,
            text="Create new user!",
            command=self.create_new_user
        )
        self._username_field.grid(row=0, column=3, sticky="e", padx=10)
        submit_new_username.grid(row=0, column=4, sticky="w", padx=10)

    def ui_game_buttons(self):
        """Using a for loop and variables, it draws 5 buttons each row for as long
        as there are games in the src/games directory.
        """
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
            if col_num not in range(4):
                col_num = 0
                row_num += 1
            else:
                col_num += 1

    def ui_configure_columns(self):
        """Column config for consistency
        """
        self.grid_columnconfigure(0, minsize=200, weight=1)
        self.grid_columnconfigure(1, minsize=200, weight=1)
        self.grid_columnconfigure(2, minsize=200, weight=1)
        self.grid_columnconfigure(3, minsize=200, weight=1)
        self.grid_columnconfigure(4, minsize=200, weight=1)

    def create_new_user(self):
        """Create new user button function. Calls on the UserManager.
        """
        if UMgr.create_user(self._username_field.get()):
            self._username_field.delete(0, "end")

    def add_new_game(self):
        """Function for new game creation. Calls on the GameManager.
        """
        name = self._create_new_game_box.get()
        pwd = self._create_new_game_admin_pwd_box.get()
        with open(src("data/adminpassword.txt"), "r", encoding="utf-8") as adminpasswordtxt:
            adminpassword = adminpasswordtxt.readline()
            adminpasswordtxt.close()
        if pwd == adminpassword:
            GMgr.new_game(name)
            self._create_new_game_admin_pwd_box.delete(0, "end")
            self._create_new_game_box.delete(0, "end")
            self.controller.reload_frame(0)
