import tkinter as tk
from tkinter import font as tkfont
from menus import Scoreboard, MainMenu
from gamemgmt import GameMgr

gmgr = GameMgr

class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Ubuntu', size=18, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = [MainMenu(parent=container, controller=self)]
        self.frames[0].grid(row=0, column=0, sticky="nsew")
        
        for game in gmgr.game_json_list():
            frame = Scoreboard(parent=container,controller=self, gameid=game["id"])
            self.frames.append(frame)

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(0)

    def show_frame(self, gameid):
        frame = self.frames[gameid]
        frame.tkraise()


if __name__=="__main__":
    app = UI()
    app.title("Highscores!")
    app.mainloop()
