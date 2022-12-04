import tkinter as tk
from tkinter import font as tkfont
from menus import Scoreboard, MainMenu
from gamemgmt import GameMgr

GMgr = GameMgr


class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Ubuntu', size=20, weight="bold")
        self.subtitle_font = tkfont.Font(family='Ubuntu', size=18)
        self.normal_font = tkfont.Font(family='Ubuntu', size=12)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = [MainMenu(parent=self.container, controller=self)]
        self.frames[0].grid(row=0, column=0, sticky="nsew")

        for game in GMgr.game_json_list(self):
            frame = Scoreboard(
                parent=self.container, controller=self, gameid=game["id"])
            self.frames.append(frame)

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(0)

    def show_frame(self, gameid):
        frame = self.frames[gameid]
        frame.tkraise()

    def reload_frame(self, id):
        self.destroy()
        self.__init__()
        self.title("Highscores!")
        self.show_frame(id)


if __name__ == "__main__":
    app = UI()
    app.title("Highscores!")
    app.mainloop()
