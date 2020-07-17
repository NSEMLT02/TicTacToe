def pwin_check(board):
    # wining combinations
    combinations = [[0, 1, 2], [3, 4, 5],
                    [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
    options = ["X", "O"]

    # check current game for matches

    for char in options:
        for x in range(8):
            if board[combinations[x][0]] == char and board[combinations[x][1]] == char and board[combinations[x][2]] == char:
                print(f'{char} wins')
                return True
    if not "_" in c:
        print("Draw")
        return True
    return False


def handle_input():
    global c, turn
    while True:
        #Loop for validating user input
        x, y = input("Enter the coordinates:").split()
        try:
            #Type checker
            x = int(x)
            y = int(y)
            #Check if coords are in range
            if x in range(1, 4) and y in range(1, 4):
                #Checks if cell is not occupied
                if c[game_matrix[x][y]] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    break
            else:
                print("Coordinates should be from 1 to 3!")
                continue
        except ValueError:
            print("You should enter numbers!")
            continue
#Add move depending who is playing
    if turn == "X":
        c[game_matrix[x][y]] = turn
        turn = "O"
    elif turn == "O":
        c[game_matrix[x][y]] = turn
        turn = "X"
    print_game()


def print_game():
    print(f"""---------
    | {c[0]} {c[1]} {c[2]} |
    | {c[3]} {c[4]} {c[5]} |
    | {c[6]} {c[7]} {c[8]} |
    ---------""")
    print(f"Turn {turn}")


game_matrix = [None, [None, 6, 3, 0], [None, 7, 4, 1], [None, 8, 5, 2]]
c = ["_"] * 9
turn = "X"
while not pwin_check(c):
    print_game()
    handle_input()
    pwin_check(c)
