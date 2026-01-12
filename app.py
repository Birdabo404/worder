import random 

worder = None 

#initialize word bank as empty.
cleaned_lines = []

'''
try: 
    with open('word.txt') as file: 
        print(file.read())
except FileNotFoundError:
    print("error: the file was not found. :<")
'''
#ignore


# load the file content into a list and loop through words.txt line by line.
try: 
    with open('words.txt', 'r') as file:
        line = file.readlines()

        for line in file:
            clean_line = line.rstrip()

            #add clean lines to list.
            cleaned_lines.append(clean_line)
except FileNotFoundError:
        print("File was not found! :<")

        random_Word = random.choice(cleaned_lines)

        print(f"The random word is: {random_Word}")
# print(cleaned_lines) 

words_minimum_Val = 0
words_maximum_Val = 5

#required condition to do the random number genration.
adjusted_Value = words_maximum_Val -1

random_Number = random.randint(words_minimum_Val, adjusted_Value)



