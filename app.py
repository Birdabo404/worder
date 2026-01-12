
import random 

worder = None 

#initialize word bank as empty.
cleaned_lines = []


# load the file content into a list and loop through words.txt line by line.
try: 
    with open('words.txt', 'r') as file:
        for line in file:
            clean_line = line.rstrip()

            #add clean lines to list.
            cleaned_lines.append(clean_line)
    
except FileNotFoundError:
        print("File was not found! :<")

#should now print the words because i removed the readlines() function. 
print(cleaned_lines)


