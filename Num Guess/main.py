import random as rd
import pickle

def diff_choose():
    difficulties = {"easy", "medium", "hard", "expert", "insane"}
    difficulty = input("""This is a number guessing game, Choose your difficulty:
Easy: 1 - 100
Medium: 1 - 750
Hard: 1 - 2500
Expert: 1 - 10000
Insane: 1 - 50000

Difficulty: """)
    difficulty = difficulty.lower()
    if difficulty not in difficulties:
        while difficulty not in  difficulties:
            print(f"no such difficulty as {difficulty}")
            difficulty = input("choose difficulty: ")
    print(f"ok got it, {difficulty}")
    return difficulty


def num_guess(difficulty):
   tries = 0
   if difficulty == "easy":
       chance = 100
   elif difficulty == "medium":
       chance = 750
   elif difficulty == "hard":
       chance = 2500
   elif difficulty == "expert":
       chance = 10000
   elif difficulty == "insane":
       chance = 50000
       print("good luck")
   number = rd.randint(1, chance)
   guess = None
   while guess != number:
        try:
            guess = int(input("Guess: "))
        except (TypeError, ValueError):
            print("actual number please")
        if guess < number:
           print("Number is higher")
        elif guess > number:
           print("Number is lower")
        tries += 1
   print(f"you win, took about {tries} tries")
   return tries


def misc():
    if difficulty == "easy" and tries < highscores.get("Easy"):
        highscores.update({"Easy": tries})
    elif difficulty == "medium" and tries < highscores.get("Medium"):
        highscores.update({"Medium": tries})
    elif difficulty == "hard" and tries < highscores.get("Hard"):
        highscores.update({"Hard": tries})
    elif difficulty == "expert" and tries < highscores.get("Expert"):
        highscores.update({"Expert": tries})
    elif difficulty == "insane" and tries < highscores.get("Insane"):
        highscores.update({"Insane": tries})
    stats = input("Do you want to see your stats? ")
    if "Y" in stats:
        print(highscores)
    play_again = input("Do you want to play again? ")
    play_again = play_again.capitalize()
    if "Y" in play_again:
        return True
    elif "N" in play_again:
        return False
    else:
        return False

def savegame():
    try:
        open("savefile.dat", "x")
    except FileExistsError:
        pass
    with open("savefile.dat", "wb") as save:
        pickle.dump(highscores, save, protocol = 4)
def loadgame():
    global highscores
    try:
        with open("savefile.dat", "rb") as save:
            highscores = pickle.load(save)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    highscores = {
"Easy": float("inf"),
"Medium": float("inf"),
"Hard": float("inf"),
"Expert": float("inf"),
"Insane": float("inf")}
    loadgame()
    play_again = None
    while play_again is None or play_again == True:
        difficulty = diff_choose()
        tries = num_guess(difficulty)
        play_again = misc()
    print("goodbye")
    savegame()