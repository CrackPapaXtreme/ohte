from datetime import datetime
import csv
import os
from dir import src


class ScoreMgr:
    def add_score(self, gameid, userid, score):
        """Adds score to scores.csv with the current date.

        Args:
            gameid : Specifies the game to submit the score to.
            userid : Specifies which user is submitting the score.
            score : Score to submit.
        """
        time_now = datetime.now().strftime("%d.%m.%Y")
        with open(src(f"games/{gameid}/scores.csv"), "a", encoding="utf-8") as scoresheet:
            writer = csv.writer(scoresheet)
            writer.writerow([userid, time_now, score])
            scoresheet.close()

    def get_sorted_highscores_list(self, gameid):
        """Generates the complete or incomplete list of the top scores of any specific game.
        It reads the scores.csv file into a list, sorts it based on score, generates new list
        without duplicate users, then returns a list with a maxmimum length of 10.

        Args:
            gameid : Specifies which game dir to fetch list from.

        Returns:
            list : List of elements with a format of [userid,date,score]
        """
        with open(src(f"games/{gameid}/scores.csv"), "r", encoding="utf-8") as scoresheet:
            reader = csv.reader(scoresheet)
            templist = []
            for row in reader:
                templist.append(row)
            templist.sort(key=lambda a: int(a[2]), reverse=True)
        already = []
        highscorelist = []
        for listing in templist:
            if not listing[0] in already:
                highscorelist.append(listing)
                already.append(listing[0])
        try:
            return highscorelist[:10]
        except IndexError:
            return highscorelist

    def delete_all_scores(self):
        """Function used for setting up the program and tests.
        """
        for gamedir in os.listdir(src("games")):
            with open(src(f"games/{gamedir}/scores.csv"), "w", encoding="utf-8") as file:
                file.close()
