import string
import random

def load_words():

    f = open("words.txt","r")
    seek=0
    word = f.readline()
    word_list = word.split()
    return word_list 

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
