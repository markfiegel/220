from random import randint
def get_words(file_name):
    file_open = open(file_name,'r')
    words = file_open.readlines()
    return words

def get_random_word(words):
    randomizer = randint(0,len(words))
    new_word = words[randomizer-2]
    print(new_word)
    return new_word

def letter_in_secret_word(letter, secret_word):
    if secret_word.count(letter)>=1:
        return True
    else:
        return False

def already_guessed(letter, guesses):
    if guesses.count(letter) == 0:
        return False
    else:
        return True


def make_hidden_secret(secret_word, guesses):
    secret = ['_']* len(secret_word)
    replacer = secret_word.index(guesses)
    if letter_in_secret_word(guesses,secret_word):
        new_string = secret.pop(replacer)
        new_string = secret.insert(replacer,guesses)
    print(new_string)
    print(secret)
    return new_string

def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
