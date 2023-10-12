import json
import os
import random

name = "Yukina"

if __name__ == "__main__":
    motions = {}

    # find all the files in the /assets folder
    assets = os.listdir("assets")
    # load the files in the /assets folder with json
    for asset in assets:
        data = json.load(open("assets/" + asset, "r", encoding="UTF-8"))
        talkdata = data["Base"]["talkData"]

        for i, talk in enumerate(talkdata):
            if talk["windowDisplayName"] == name:
                saying = talk["body"]
                if talk["motions"] == []:
                    continue
                motion = talk["motions"][0]["motionName"]
                if motion == "":
                    continue
                if motion not in motions:
                    motions[motion] = []
                motions[motion].append(saying)
    # output the motions to a file
    with open("motions.json", "w", encoding="UTF-8") as f:
        json.dump(motions, f, ensure_ascii=False, indent=4)
                
