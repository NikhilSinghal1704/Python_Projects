import random
import string

def get_word():  #guess a randomm word
    fp = open("Common_english_words.txt", "r")
    words = fp.readlines()
    word = random.choice(words)
    word = word.replace("\n", "")
    fp.close()
    return word

a = """
||||||||||||||
|            |
|            |
|          |||||
|        ||     ||
|        ||     ||
|          |||||    
|     ||     |     ||       
|       |||  |  |||
|          |||||
|            |
|            |
|            |
|            |
|          || ||
|       |||     |||
|     ||           ||
|
|||||||||||||||||||||||||||||||
"""

b = """
||||||||||||||
|            |
|            |
|          |||||
|        ||     ||
|        ||     ||
|          |||||    
|     ||     |     ||       
|       |||  |  |||
|          |||||
|            |
|            |
|            |
|            |
|          
|
|
|
|||||||||||||||||||||||||||||||
"""

c = """
||||||||||||||
|            |
|            |
|          |||||
|        ||     ||
|        ||     ||
|          |||||    
|            |           
|            |  
|            |
|            |
|            |
|            |
|            |
|    
|
|
|
|||||||||||||||||||||||||||||||
"""

d = """
||||||||||||||
|            |
|            |
|          |||||
|        ||     ||
|        ||     ||
|          |||||    
|     
|
|
|
|
|
|
|
|
|
|
|||||||||||||||||||||||||||||||
"""

e = """
||||||||||||||
|            |
|            |
|          
|
|
|    
|     
|
|
|
|
|
|
|
|
|
|
|||||||||||||||||||||||||||||||
"""

def condition(stage):  #prints the hangman 
    stages = [e, d, c, b, a]
    print(stages[stage])
    
def result(word, user, stage):
    mesage = ""
    if user in word:
        correct_guess.append(user)
        guessed.append(user)
        message = f"'{user}' is present in the word"
    else:
        guessed.append(user)
        stage += 1
        message = f"'{user}' is not present in the word"
    
    condition(stage)
    print("\n\n\n")    
    
    temp = ""
    #print(word)
    for ch in word:
        if ch in correct_guess:
            temp += (ch  + " ")
        else:
            temp += "_ "
    print(temp)
    print(message)
    user_view = ", ".join(guessed)
    print(f"Total letters guessed: {user_view}")
    return temp, stage

print("Guess the letter which may be in the word\nIf your letter in the word then its all occurence will be revealed\nUse this information to guess the next letter until you find the word\nYou have four chances, you may guess 4 letters that are not in the word\nthere is no pnelty on guessing the word already guessed twice")

word = get_word().upper()
length = len(word) # Let's store length of the choosen word
valid = string.ascii_uppercase
stage = 0
correct_guess = []  # A list of coreectly guessed letters
guessed = []
display_word = "_ " * length
print(display_word)
while True:
    #print(word)
    #print(stage)
    if display_word == word:
        print(f"Congratulations! You have found the word: {word}")
        break
        
    elif stage >= 4:
        print(f"You lost! the word was: {word}")
        break
    
    ch_input = input("Enter a character: ").upper()
    
    if ch_input in valid and ch_input not in guessed:
        display_word, stage = result(word, ch_input, stage)
        display_word = display_word.replace(" ", "")
        
    elif ch_input in guessed:
        print(f"You have already guessed this '{ch_input}'")
        
    else:
        print("Invalid input, choose only a single letter")
        


