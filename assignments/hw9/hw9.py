"""
Mark Fiegel
hw9.py

I certify that this assignment is entirely my own work.
"""
from random import randint
def get_words(file_name):
    file_open = open(file_name,'r')
    words = file_open.readlines()
    return words
def get_random_word(words):
    randomizer = randint(0,len(words))
    new_word = words[randomizer-1]
    actual_word = new_word.strip('\n')
    return actual_word
def letter_in_secret_word(letter, secret_word):
    secret= bool(secret_word.count(letter)>=1)
    return secret
def already_guessed(letter, guesses):
    if guesses.count(letter) == 0:
        return False
    else:
        return True
def make_hidden_secret(secret_word, guesses):
    new_thing = ['_']*len(secret_word)
    for i_val in range(len(guesses)):
        if letter_in_secret_word(guesses[i_val],secret_word):
            x_find = secret_word.find(guesses[i_val])
            y_find = secret_word.rfind(guesses[i_val])
            new_thing.pop(x_find)
            new_thing.insert(x_find, guesses[i_val])
            new_thing.pop(y_find)
            new_thing.insert(y_find, guesses[i_val])
    new_string = ''
    for x_val in range(len(new_thing)):
        new_string = new_string + str(new_thing[x_val])+' '
    new_string = new_string.strip()
    return new_string
def won(guessed):
    if guessed.count('_') ==0:
        won = True
    else:
        won = False
    return won

def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
