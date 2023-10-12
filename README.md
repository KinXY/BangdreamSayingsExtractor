(This repository Works as helper for [CyberDiva project](https://github.com/KinXY/CyberDiva).)

This repository helps to extract all the sayings as short sample dialogues of certain character in Bangdream from band stories. The extracted dialogues can be utilized to train llm models, prompt engineering and further usage.

## Usage

### Preparation

Open `main.py` and modify the following variables:
- `band_id` The id of the band that the character belongs to.
   
| ID | Band Name           |
|----|---------------------|
| 1  | Poppin'Party        |
| 2  | Afterglow           |
| 3  | Hello, Happy World! |
| 4  | Pastel*Palettes     |
| 5  | Roselia             |
| 6  | Morfonica           |
| 7  | RAISE A SUILEN      |

- `name` The name of the character to be extracted. **Only the full name is supported, and the first character should be capitalized.** (e.g. "Yukina", "Kasumi")

- `need_download` If the assets of band stories need to be downloaded. When running the script for the first time, set it to `True`. After that, if you only want to find the sayings of another character from the same band, set it to `False` to save time. 

### How to run

Run `python main.py` in the command line.

All the extracted dialogues will be saved in `sayings.txt` under root directory. A sample of 100 dialogues will be saved in `sample_sayings.txt` under root directory.

