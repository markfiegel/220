"""
mark fiegel
lab9.py
"""


def build_board():
    board = ['1','2','3','4','5','6','7','8','9']
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position-1]).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    board[position-1] = character.lower()

def winning_game(board):
    length = len(board)
    for i in range(0,length,3):
        if board[i]== board[i+1] == board[i+2]:
             return True
    if board[0] == board[4] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False
def game_over(board):
    if winning_game(board) or board.count('x') == 5:
        return True
    else:
        return False

def get_winner(board):
    if game_over(board) and board.count('x')> board.count('y'):
        return 'x'
    if game_over(board) and board.count('o') == board.count('x'):
        return 'o'
    else:
        return None
def play(board):
    print('get 3 in a row to win ')
    print_board(board)
    turn_counter = 2
    keep_playing = True
    while keep_playing:
        while not game_over(board):
            if turn_counter%2 == 0:
                position = eval(input('x pick a spot '))
                character = 'x'
                if is_legal(board,position):
                    fill_spot(board,position,character)
                    turn_counter = turn_counter+1
                    print_board(board)
            else:
                position = eval(input('o pick a spot '))
                if is_legal(board,position):
                    character = 'o'
                    fill_spot(board,position,character)
                    turn_counter = turn_counter+1
                    print_board(board)
            if game_over(board):
                print(get_winner(board),"wins!!")
            still_playing = input("do you want to play again? ")
            keep_playing = still_playing[0]
            if keep_playing == 'y':
                keep_playing == True
            else:
                keep_playing == False
play(build_board())