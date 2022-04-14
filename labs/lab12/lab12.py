"""
Mark Fiegel
lab12.py
I did a series of challenges without being able to use a for loop
I certify that this assignment is entirely my own work.
"""
from random import randint
def find_and_remove_first(list,value):
    new_list = list
    list_index = new_list.index(value)
    new_list.pop(list_index)
    new_list.insert(list_index,'mark')
    return new_list
def good_input():
    good = eval(input("input a number "))
    good_input = False
    while good_input == False:
         if 10>= good >= 1:
            good_input = True
            print("Good input")
         else:
            print('not a valid input, try between 1 and 10 ')
            good = eval(input("input a new number "))
def num_digits():
    is_negative = False
    while is_negative == False:
        num = eval(input('enter a number '))
        if num <=0:
            is_negative = True
        counter = 0
        while num != 0:
            num = num//10
            counter = counter+1
        if counter >=1:
            print(counter)
def hi_lo_game():
    game_on = True
    num = randint(1,99)
    print(num)
    counter = 1
    while game_on == True:
        guess = eval(input("guess "))
        if guess == num:
            print('congratulations! you guessed right')
            print('you got it in attempt # ', counter)
            game_on = False
        elif counter == 7:
            print('Sorry, you lose. The number was ', num)
            game_on = False
        elif guess < num:
            print('guess higher ')
            counter += 1
        elif guess > num:
            print("guess lower ")
            counter += 1
