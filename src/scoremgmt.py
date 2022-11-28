from dir import src
from datetime import datetime
import csv

#dev
from random import randint

class ScoreMgr:
    def add_score(gameid,userid,score):
        time_now = datetime.now().strftime("%d.%m.%Y")
        with open(src(f"games/{gameid}/scores.csv"), "a") as scoresheet:
            writer = csv.writer(scoresheet)
            writer.writerow([userid,time_now,score])
            scoresheet.close()

    def get_sorted_highscores_list(gameid):
        with open(src(f"games/{gameid}/scores.csv"), "r") as scoresheet:
            reader = csv.reader(scoresheet)
            list = []
            for row in reader:
                list.append(row)
            list.sort(key=lambda a : a[2], reverse=True)
        already=[]
        highscorelist = []
        for listing in list:
            if not listing[0] in already:
                highscorelist.append(listing)
                already.append(listing[0])
        return highscorelist

if __name__=="__main__":
    sm = ScoreMgr
    for num in range(50):
        sm.add_score(1,randint(1,15),randint(1,1000))
    for a in sm.get_sorted_highscores_list(1):
        print(str(a))