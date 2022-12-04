from dir import src
from datetime import datetime
import csv
import os

# dev
from random import randint


class ScoreMgr:
    def add_score(self, gameid, userid, score):
        time_now = datetime.now().strftime("%d.%m.%Y")
        with open(src(f"games/{gameid}/scores.csv"), "a", encoding="utf-8") as scoresheet:
            writer = csv.writer(scoresheet)
            writer.writerow([userid, time_now, score])
            scoresheet.close()

    def get_sorted_highscores_list(gameid):
        with open(src(f"games/{gameid}/scores.csv"), "r", encoding="utf-8") as scoresheet:
            reader = csv.reader(scoresheet)
            list = []
            for row in reader:
                list.append(row)
            list.sort(key=lambda a: a[2], reverse=True)
        already = [] # List to keep track of what userids have been added to returnable list
        highscorelist = [] # List to be returned with 10 best scores
        for listing in list:
            # Loop which makes sure duplicate names don't appear
            # Checks if userid (listing[0]) is already added, skips if true
            if not listing[0] in already:
                highscorelist.append(listing)
                already.append(listing[0])
        try: # Returns 10 best scores. If list hass less than 10 scores, it returns the list as is.
            return highscorelist[:10]
        except IndexError:
            return highscorelist

    def delete_all_scores():
        for gamedir in os.listdir(src("games")):
            file = open(
                src(f"games/{gamedir}/scores.csv"), "w", encoding="utf-8")
            file.close()


if __name__ == "__main__":
    sm = ScoreMgr
    sm.delete_all_scores()
    # for num in range(50):
    #    sm.add_score(1,randint(1,15),randint(1,1000))
    # for a in sm.get_sorted_highscores_list(1):
    #    print(str(a))
