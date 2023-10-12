import json
import os
from download import download
import random

band_id = 5
name = "Yukina"
need_download = True

if __name__ == "__main__":
    if need_download:
        download(band_id)

    sayings = []

    # find all the files in the /assets folder
    assets = os.listdir("assets")
    # load the files in the /assets folder with json
    for asset in assets:
        data = json.load(open("assets/" + asset, "r", encoding="UTF-8"))
        talkdata = data["Base"]["talkData"]

        for i, talk in enumerate(talkdata):
            if talk["windowDisplayName"] == name:
                # get the previous saying
                if i > 0:
                    prev_saying = talkdata[i - 1]["body"]
                chara_saying = talk["body"]
                # consist the sample dialogue using two sayings
                saying = f'Others: "{prev_saying}"\t{name}: "{chara_saying}"'
                sayings.append(saying)

    # output the sayings to a file
    with open("sayings.txt", "w", encoding="UTF-8") as f:
        # translate the sayings into a single string
        result = ""
        for saying in sayings:
            # translate the \n in the saying into a space
            saying = saying.replace("\n", " ")
            # now translate the \t into a \n
            saying = saying.replace("\t", "\n")
            result += f"{saying},\n\n"
        # remove the last comma
        result = result[:-3]
        f.write(result)
    
    # output random 100 sayings to another file
    with open("sample_sayings.txt", "w", encoding="UTF-8") as f:
        # translate the sayings into a single string
        result = ""
        for saying in random.sample(sayings, 100):
            # translate the \n in the saying into a space
            saying = saying.replace("\n", " ")
            # now translate the \t into a \n
            saying = saying.replace("\t", "\n")
            result += f"{saying},\n\n"
        # remove the last comma
        result = result[:-3]
        f.write(result)
