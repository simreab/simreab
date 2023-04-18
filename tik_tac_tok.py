import random

def display_board(board):
    for n in range(1,9,3):
        print(board[n], board[n+1], board[n+2])

def player_input():
    
    choice = 'WRONG'
    acceptable_range = range(1,10)  
    within_range = False
    
    while ((choice.isdigit() == False) or (within_range == False)):
        choice = input('please enter a number between (1-9) ')

        if choice.isdigit() == False:
            print('Sorry that is not a digit')

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, you are out of acceptable range (1-9)')
                within_range = False
    return int(choice)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if ((board[1] == board[2] == board[3]) and (board[1] != ' ')):
        return True
    elif ((board[4] == board[5] == board[6]) and (board[4] != ' ')):
        return True
    elif ((board[7] == board[8] == board[9]) and (board[7] != ' ')):
        return True
    elif ((board[1] == board[5] == board[9])) and (board[1] != ' '):
        return True
    elif ((board[3] == board[5] == board[7]) and (board[3] != ' ')):
        return True

def choose_first():
    return random.randint(1,2)

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    for pos in board:
        if pos == ' ':
            return False
    return True

def player_choice(board):
    pos = player_input()
    if space_check(board, pos):
        return pos
    else:
        return False
        
def replay():
    rp = input('Would you like to play again? (Answer yes or no)')
    if rp[0].lower() == 'y':
        return True
    else:
        return False

board_map = ['x','1','2','3','4','5','6','7','8','9']

test_board = ['#','X','O','X','O','X','O','X','O','X']

print('Welcome to Tic Tac Toe!\n')
game_start = input('Press any key then enter to start the game.')

while game_start:
    initial_board = [' ']*10
    fp = choose_first()
    print(f'player {fp} will go first.')
    fpm = input('would you like to be X or O?').upper()
    if fpm == 'X':
        spm = 'O'
    elif fpm == 'O':
        spm = 'X'
    if fp == 1:
        sp = 2
    else:
        sp = 1

    while not win_check(initial_board, fpm):
        print(f"Player {fp}'s turn.")
        fpp = player_choice(initial_board)
        place_marker(initial_board, fpm, fpp)
        display_board(initial_board)

        
        if not win_check(initial_board, spm):
            print(f"Player {sp}'s turn.")
            spp =  player_choice(initial_board)
            place_marker(initial_board, spm, spp)
            display_board(initial_board)
        elif win_check(initial_board, spm):
            print(f'congratulation! Player {sp} won this game.')
            
    print(f'congratulation! Player {fp} won this game.')
    if not replay():
        break
