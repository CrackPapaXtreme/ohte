import tkinter as tk
from tkinter import font as tkfont
from menus import Scoreboard, MainMenu
from gamemgmt import GameMgr

GMgr = GameMgr


class UI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.fonts_and_config()

        self.load_frames()

        self.show_frame(0)

    def fonts_and_config(self):
        """Sets the different fonts for each text type(used by the UI classes in menus.py),
        and configures the container for the sub-frames to all be conatined in column 0 row 0
        """
        self.title_font = tkfont.Font(family='Ubuntu', size=20, weight="bold")
        self.subtitle_font = tkfont.Font(family='Ubuntu', size=18)
        self.normal_font = tkfont.Font(family='Ubuntu', size=12)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def load_frames(self):
        """Loads all the different frames for each game and the main menu. The list
        self.frames is used by the function self.show.frame()
        """
        self.frames = [MainMenu(parent=self.container, controller=self)]
        self.frames[0].grid(row=0, column=0, sticky="nsew")

        for game in GMgr.game_json_list(self):
            frame = Scoreboard(
                parent=self.container, controller=self, gameid=game["id"])
            self.frames.append(frame)

            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, gameid):
        """This function raises the desired frame

        Args:
            gameid (int): Frame to be raised to view
        """
        frame = self.frames[gameid]
        frame.tkraise()

    def reload_frame(self, gameid):
        """Refreshes the app by destroying it, initializing it, and showing the
        frame which was last in view.

        Upon executing the function, the app does appear on the screen to close
        and open up again by itself. I did not figure out how to make this refresh
        happen smoothly.

        Args:
            id (int): The frame that was in view before the app got closed.
        """
        self.destroy()
        self.__init__()
        self.title("Highscores!")
        self.show_frame(gameid)


if __name__ == "__main__":
    app = UI()
    app.title("Highscores!")
    app.mainloop()
