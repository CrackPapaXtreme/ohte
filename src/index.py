from tkinter import Tk, ttk
from datetime import datetime
from objects import Score
from usermgmt import UserMgr

umgr=UserMgr()

class UI:
    def __init__(self,root):
        self._root=root
        self._username_field= None

    def start(self):

        title = ttk.Label(master=self._root,text="Highscores!")

        self._username_field = ttk.Entry(master=self._root)
        submit_new_username = ttk.Button(
            master=self._root,
            text="Create new user!",
            command=self._click_submit_new_username)

        # score list to test
        scorelist=[Score(1000,1,datetime.now()),Score(1001,1,datetime.now()),Score(1100,1,datetime.now()),Score(1010,1,datetime.now())]

        # Title on the left
        title.grid(padx=13,pady=10)

        # Blank spacer column
        self._root.grid_columnconfigure(1, weight=1, minsize=500)

        # Username field and button next to each other
        self._username_field.grid(row=0,column=2,sticky="en",pady=14)
        submit_new_username.grid(row=0,column=3,sticky="en",padx=10,pady=10)

        """# Fuck yeah this works omg
        for listing in scorelist:
            scorename=ttk.Label(
                master=self._root,
                text=umgr.get_username(listing.id))
            scorename.grid()
        #############################"""


        reset_json = ttk.Button(
            master=self._root,
            text="reset json",
            command=umgr.reset_users_json()
        )
        reset_json.grid(column=3,sticky="e",padx=10,pady=10)
    
    def _click_submit_new_username(self):
        username = self._username_field.get()
        umgr.create_user(username)

window=Tk()
window.title("Highscores!")

ui = UI(window)
ui.start()
window.mainloop()