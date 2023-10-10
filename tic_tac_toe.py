# initiate the game, get player names
# display the board, let Player 1 move
# display the board again, let Player 2 move
# after 3rd+ move of Player 1/2, check if they won
# if won, print "player X wins" and exit
# winning conditions - have the same code for conditions and alternate between "O" and "X"


def main():
    board = [
        ["[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]"],
        ["[ ]", "[ ]", "[ ]"],
    ]
    # p1, p2 = get_player_names()
    # print(p1, p2)
    # game(p1, p2)
    game("ebe", "bebe")
    # display_board()


def get_player_names():
    player1 = input("Enter player 1('Xs') name: ")
    player2 = input("Enter player 2('Os') name: ")
    return player1, player2


def game(p1, p2):
    won_game = False
    board = [["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]]
    move_count = 0
    # all the game should be in some kind of loop, I guess
    while move_count <= 9:
        display_board(board)
        if move_count % 2 == 0:
            p1_move = player_move(p1, "X")
            display_board(board, p1_move, "X")
        elif move_count % 2 == 1:
            p2_move = player_move(p2, "O")
            display_board(board, p2_move, "O")
        move_count += 1
    print("*** FINISH ***")
    # # after each move above 6, check winning conditions
    # if move_count >= 5:
    #     if move_count % 2 == 1:
    #         did_player_win(board, "X")
    #     elif move_count % 2 == 0:
    #         did_player_win(board, "O")


def player_move(p, s):
    valid_move = False
    rows = ["a", "b", "c"]
    columns = ["1", "2", "3"]
    while valid_move == False:
        move = input(f"Your move, {p}:").strip().lower()
        if move[0] not in rows or move[1] not in columns:
            print("invalid move - a/b/c for rows, 1/2/3 for columns")
        else:
            break
    return move


def did_player_win(board, s):
    ##### winning conditions #####

    # if they have three in one row
    for row in board:
        three_in_row = True
        for cell in row:
            if s not in cell:
                three_in_row = False
        print(three_in_row)

    # if they have three in one column
    for i in range(3):
        three_in_column = True
        for row in board:
            pass


def display_board(board, move="", s=""):
    print(move)
    if len(move) > 0:
        row, column = [char for char in move]
        print(row)
        print(column)
        # convert row and column values
        if row == "a":
            row = 0
        elif row == "b":
            row = 1
        elif row == "c":
            row = 2
        column = int(column) - 1
        # print(row, column)

        # assign either X or O to the chosen cell
        board[row][column] = f"[{s}]"
    for row in board:
        print("".join(row))

    # saving the new value, and returning it(dunno if it's necessary tho)
    new_board = board
    return new_board


main()
