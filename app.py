worder = None

cleaned_lines = []

'''
try: 
    with open('word.txt') as file: 
        print(file.read())
except FileNotFoundError:
    print("error: the file was not found. :<")
'''

# rewrote this loop
try: 
    with open('words.txt', 'r') as file:
        line = file.readlines()

        for line in file:
            clean_line = line.rstrip()

            #add clean lines to list.
            cleaned_lines.append(clean_line)
except FileNotFoundError:
        print("File was not found! :<")

print(cleaned_lines)
