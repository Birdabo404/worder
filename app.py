import random 

worder = None 

#initialize word bank as empty.
word_Bank = []


# load the file content into a list and loop through words.txt line by line.
try: 
    with open('words.txt', 'r') as file:
        for line in file:
            clean_words = line.rstrip()

            #add clean lines to list.
            word_Bank.append(clean_words)
    
except FileNotFoundError:
        print("File was not found! :<")

#should now print the words because i removed the readlines() function. 
#print(word_Bank) :commented to remove printed word list. 

random_Words = random.choice(word_Bank)
print(f"The chosen word is: {random_Words}")


