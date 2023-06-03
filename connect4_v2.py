from colorama import Fore
from collections import deque

ROWS, COLS = [6, 7]
board = [["0" for el in range(COLS)] for i in range(ROWS)]
def print_board():
    print(*board, sep="\n")

player_one = input(Fore.BLUE + "Player one please enter your Name: " + Fore.RESET)
player_two = input(Fore.RED + "Player two please enter your Name: " + Fore.RESET)
print_board()

total_counter = 0
symb_one = "*"
symb_two = "#"

turns = deque([(player_one, symb_one), (player_two, symb_two)])


def position_checker(col):
    for i in range(ROWS):

        if board[-i-1][col-1] == "0":
            position = ((-i-1),(col-1))
            board[-i-1][col-1] = turns[0][1]
            return position

        if board[0][col-1] != "0":
            print("no free slots- invalid choice!")
            break


def result_check(current_position):
    points = 1
    x = current_position[0]
    y = current_position[1]
    for i in range(1, 4):
        if 0 <= (x+ ROWS) + i < ROWS and 0 <= y < COLS:  # down
            if board[(x + ROWS)+ i][y] == turns[0][1]:
                points += 1

        if 0 <= (x + ROWS) - i < ROWS and 0 <= y < COLS:  # up
            if board[(x + ROWS)- i][y] == turns[0][1]:
                points += 1
        if points >= 4:
            return points

    points = 1

    for i in range(1, 4):
        if 0 <= (x+ ROWS) < ROWS and 0 <= y - i < COLS:  # left
            if board[x + ROWS ][y - i ] == turns[0][1]:
                points += 1

        if 0 <= (x+ ROWS) < ROWS and 0 <= y + i < COLS:  # right
            if board[(x+ ROWS)][y + i] == turns[0][1]:
                points += 1
        if points >= 4:
            return points

    points = 1

    for i in range(1, 4):
        if 0 <= (x+ ROWS) -i < ROWS and 0 <= y - i < COLS:  # top-left
            if board[(x+ ROWS) - i][y - 1] == turns[0][1]:
                points += 1

        if 0 <= (x+ ROWS) + i < ROWS and 0 <= y + i < COLS:  # bottom-right
            if board[(x+ ROWS) + i][y + i] == turns[0][1]:
                points += 1
    if points >= 4:
        return points

    points = 1
    for i in range(1, 4):
        if 0 <= (x+ ROWS) - i < ROWS and 0 <= y + i < COLS:  # top-right
            if board[(x+ ROWS) - i][y + i] == turns[0][1]:
                points += 1

        if 0 <= (x+ ROWS) + i < ROWS and 0 <= y - i < COLS:  # bottom-left
            if board[(x + ROWS) + i][y -i] == turns[0][1]:
                points += 1
    if points >= 4:
        return points

    return points


while True:
    try:
        if turns[0][1] == "*":
            play_position = int(input(Fore.BLUE + f"{turns[0][0]} choose your move: " + Fore.RESET))
        else:
            play_position = int(input(Fore.RED + f"{turns[0][0]} choose your move: " + Fore.RESET))

    except ValueError:
        play_position = int(input(f"{turns[0][0]} choose your valid move: "))
    try:
        position = position_checker(play_position)
    except IndexError:
        print("invalid move, try again!")
        continue
    if result_check(position) >= 4:
        print_board()
        print(Fore.BLUE + f"{turns[0][0]} wins the game!!!" + Fore.RESET)
        raise SystemExit()

    total_counter += 1
    if total_counter == ROWS * COLS:
        print(Fore.CYAN + "DRAW - GAME OVER!!!" + Fore.RESET)
        raise SystemExit()
    print_board()
    turns.rotate()
    
