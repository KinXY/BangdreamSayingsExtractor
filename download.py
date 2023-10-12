import requests
import os

def download(band_id):
    base_url = f"https://bestdori.com/assets/en/scenario/band/00{band_id}_rip/Scenarioband{band_id}-"
    num_files = 0

    # clear all the ./assets directory
    for file in os.listdir("assets"):
        os.remove(f"assets/{file}")
    for i in range(1, 101):
        url = f"{base_url}{i:03}.asset"
        response = requests.get(url)

        with open(f"assets/scenario{i:03}.json", "wb") as f:
            f.write(response.content)
        # open the file and examine if the beginning of the file is "{"Base":{"talkData":["
        is_valid = True
        with open(f"assets/scenario{i:03}.json", "r", encoding="UTF-8") as f:
            line = f.readline()
            if not line.startswith('{"Base"'):
                is_valid = False
        if not is_valid:
            os.remove(f"assets/scenario{i:03}.json")
            print("All files downloaded.")
            break
        # if the file is valid
        print(f"Found file: {url}")
        num_files += 1

    print(f"Total number of files found: {num_files}")
