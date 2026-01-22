import random
import os
import time

welcomeMessage = """ 
 /$$      /$$           /$$                                                     /$$                     /$$      /$$                           /$$                    
| $$  /$ | $$          | $$                                                    | $$                    | $$  /$ | $$                          | $$                    
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$       | $$ /$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$      | $$/$$ $$ $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$  \ $$      | $$$$_  $$$$| $$  \ $$| $$  \__/| $$  | $$| $$$$$$$$| $$  \__/
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$      | $$  | $$| $$_____/| $$      
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$| $$      
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         \___/   \______/       |__/     \__/ \______/ |__/       \_______/ \_______/|__/      
                                                                                                                                                                      
                                                                                                                                                                      
                                                                                                                                                                      """
# ------- CONSTANT GAME VARIABLES ---------
incorrectLettersPosition = None
correctLettersPosition = None
currentTurn = None
maxTurnAllowed = 3
turnTaken = 0
turnLeft = maxTurnAllowed - turnTaken


def clear_screen():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")


# initialize word bank as empty.
word_Bank = []

# --------- DATA WORKING? ---------
# load the file content into a list and loop through words.txt line by line.
try:
    with open("words.txt", "r") as file:
        for line in file:
            clean_words = line.rstrip()

            # add clean lines to list.
            word_Bank.append(clean_words)

except FileNotFoundError:
    print("File was not found! :<")

random_Words = random.choice(word_Bank)
# print(f"The chosen word is: {random_Words}")

# --------- START GAME ---------
playerName = input("\n Input username >> ")

while playerName != "":
    print(f"{welcomeMessage} \nHello {playerName}!")
    break
print("The system has chosen a word! ")
print(f"There are {len(random_Words)} letters in the chosen word to guess.")
print(f"You have a total of {turnLeft} turns left.\n")

user_Input = "start"
user_Input = input("please type 'start' to start the game.\n>> ").lower()
while user_Input != "start":
    print("Invalid Command. Try again")
    user_Choice = input(">> ").lower()

clear_screen()
print("Game S T A R T I N G. ")
