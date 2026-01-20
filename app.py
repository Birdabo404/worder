import random

# idk why i have this variable lol. worder = None

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
playerName = None
incorrectLettersPosition = None  # Tracks the letters that are in the incorrect postion.
correctLettersPosition = (
    None  # Tracks the letters the player guessed that are not in the word bank.)
)
maxTurn = None  # Max number of player's turn.
currentTurn = None  # Current number of player's turn.

# initialize word bank as empty.
word_Bank = []

# load the file content into a list and loop through words.txt line by line.
try:
    with open("words.txt", "r") as file:
        for line in file:
            clean_words = line.rstrip()

            # add clean lines to list.
            word_Bank.append(clean_words)

except FileNotFoundError:
    print("File was not found! :<")

# should now print the words because i removed the readlines() function.
# print(word_Bank) :commented to remove printed word list.

random_Words = random.choice(word_Bank)
# print(f"The chosen word is: {random_Words}")

while playerName == "":
    print("Enter your username before starting.")
    playerName = input("Enter your username >> ")

print(f"{welcomeMessage} \nHello {playerName}!")
print(f"There are {len(random_Words)} letters in the words to guess.")
print(f"there are {currentTurn} turns left.")
