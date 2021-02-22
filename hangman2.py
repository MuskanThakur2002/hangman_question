import string
from words import choose_word
from images import IMAGES

def is_word_guessed(secret_word, letters_guessed):

    if secret_word==get_guessed_word(secret_word, letters_guessed):
        return True
    return False 


def get_guessed_word(secret_word, letters_guessed):
    
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    import string
    all_letters= string.ascii_lowercase
    letter_left=" "
    for i in all_letters:
        if i not in letters_guessed:
            letter_left+=i
    return letter_left

def hangman(secret_word):
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

letters_guessed = []
def get_hint(secret_word, letters_guessed):
    import random
    letter_not_guessed=[]
    i=0
    while i<len(secret_word):
        letter=secret_word[i]
        if letter not in letters_guessed:
            if letter not in letter_not_guessed:
                letter_not_guessed.append(letter)
        i+=1
    return random.choice(letter_not_guessed )

def valid_user(num):
    if len(num)!=1:
        return False
    if (num>="a" and num<="z") or num<="A" and num>="Z":
        return True
    return False

secret_word = choose_word()
hangman(secret_word)
level=input("easy\nmedium\nhard\n")
if level=="easy":
    print("you have 8 remaining live")
    remaining_live=8
    remaining=7

elif level=="medium":
    print("you have 6 remaining live")
    remaining_live=7
    remaining=6

elif level=="hard":
    print("you have 4 remaining live")
    remaining_live=8
    remaining=7

while True:
    available_letters = get_available_letters(letters_guessed)
    print("Available letters: ",  available_letters)

    guess =input("Please guess a letter: ")
    letter = guess.lower()

    if guess=="hint":
        letters_guessed.append(get_hint(secret_word, letters_guessed))
        print("hint: " , get_guessed_word(secret_word, letters_guessed))
        print("")

        if is_word_guessed(secret_word, letters_guessed) == True:
            print(" * * Congratulations, you won! * * ")
            print("")
            break
        else:
            continue
    else:
        letter = guess.lower()
    

        if (valid_user(letter))!=True:
            print("not valid later again choose one letter")
            continue

    if letter in secret_word:
        letters_guessed.append(letter)
        print("Good guess: " , get_guessed_word(secret_word, letters_guessed))
        print("")
        
        if is_word_guessed(secret_word, letters_guessed) == True:
            print(" * * Congratulations, you won! * * ")
            print("")
            break
        else:
            continue
    if level=="easy":
        while remaining_live>remaining and remaining_live>0:
            if letter not in secret_word and guess!="hint":
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                print(IMAGES[8-remaining_live])
                letters_guessed.append(letter)
                print("")
                remaining_live-=1
        remaining-=1
        if remaining_live==0:
            break
    
    elif level=="medium":
        while remaining_live>remaining and remaining_live>0:
            if letter not in secret_word and guess!="hint":
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                print(IMAGES[8-remaining_live+1])
                letters_guessed.append(letter)
                print("")
                remaining_live-=1
        remaining-=1
        if remaining_live==1:
            break
    elif level=="hard":
        while remaining_live>remaining and remaining_live>0:
            if letter not in secret_word and guess!="hint":
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                print(IMAGES[8-remaining_live+1])
                letters_guessed.append(letter)
                print("")
                remaining_live-=2
        remaining-=2
    if remaining_live==0:
        break