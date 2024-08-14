import os
from random import randint
import datetime
import json

highscore_file = "highscores.json"
min = 1
max = 1000

def clear(): os.system("cls" if os.name == "nt" else "clear")

def get_date(): return datetime.datetime.now().isoformat()

def load_highscores():
    try:
        with open(highscore_file, "r") as f: return json.loads(f.read())
    except:
        return []

def save_highscore(name, tries):
    highscore = { "date": get_date() , "name": name, "tries": tries }
    previous_data = load_highscores()
    previous_data.append(highscore)
    serialized_data = json.dumps(previous_data, indent=4)

    with open(highscore_file, "w") as file:
        file.write(serialized_data)

def display_highscores():
    highscores = load_highscores().sort(key=lambda hs: hs["tries"])
    if highscores == None or len(highscores) == 0:
        return print("No saved highscores yet!")
    for i, hs in enumerate(highscores[:10]):
        # print(f"{i+1}. {hs["name"]} {hs["date"]} {hs["tries"]}")
        print(f"{i+1}. {hs}")


while True:
    os.system("clear") # clear()
    name = input("Jak masz na imie? ")
    secret = randint(min, max + 1)
    value = None
    tries = 0

    while value != secret:
        tries += 1

        try:
            value = int(input("Podaj liczbe: "))
            if value < min or value > max:
                raise Exception(f"Podana liczba musi byc w zakresie od {min}-{max}")
        except Exception as e:
            print(f"Wystapil blad: {str(e)}")

        if value > secret:
            print("Mniej...")
        elif value < secret:
            print("Więcej...")

    print(f"Wygrales! Sekretny numer to {secret}.\nIlosc prob: {tries}")
    save_highscore(name, tries)
    
    display_highscores()

    play_again = input("Czy chcesz zagrac jeszcze raz?\nY/N\n")
    if play_again.upper() != "Y":
        break
