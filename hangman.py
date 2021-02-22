import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word==get_guessed_word(secret_word, letters_guessed):
        return True
    return False 
# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

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
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    all_letters= string.ascii_lowercase
    letter_left=" "
    for i in all_letters:
        if i not in letters_guessed:
            letter_left+=i
    return letter_left

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
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
# level=input("easy/medium/high")
# if level==easy:
remaining_live=8
# elif level==medium:
# remaining_live=6
# elif:
# remaining=4
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
    while remaining_live>remaining and remaining_live>0:
        if letter not in secret_word and guess!="hint":
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            print(IMAGES[8-remaining_live])
            letters_guessed.append(letter)
            print("")
            remaining_live-=1
    if remaining_live==0:
        break
    remaining-=1
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
# hangman(secret_word)