def main():
    p1, p2 = get_player_names()
    rules()
    print("*** START ***")
    game(p1, p2)


def get_player_names():
    player1 = input("Enter player 1('Xs') name: ")
    player2 = input("Enter player 2('Os') name: ")
    return player1, player2


def game(p1, p2):
    board = [["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]]
    move_count = 0
    move_list = []
    display_board(board)
    # all the game should be in some kind of loop, I guess
    while move_count < 9:
        if move_count % 2 == 0:
            p1_move = player_move(p1, "X", move_list)
            display_board(board, p1_move, "X")
            if did_player_win(board, "X"):
                print(f"{p1} WON")
                return
        elif move_count % 2 == 1:
            p2_move = player_move(p2, "O", move_list)
            display_board(board, p2_move, "O")
            if did_player_win(board, "O"):
                print(f"{p2} WON")
                return
        move_count += 1
    print("*** DRAW ***")
    return


def player_move(p, s, move_list):
    valid_move = False
    rows = ["a", "b", "c"]
    columns = ["1", "2", "3"]
    while valid_move == False:
        move = input(f"Your move, {p}: ").strip().lower()
        if move[0] not in rows or move[1] not in columns:
            print("invalid move - a/b/c for rows, 1/2/3 for columns")
        elif len(move) != 2:
            print("incorrect values")
        elif move in move_list:
            print("Cell already populated")
        else:
            move_list.append(move)
            valid_move == True
            break
    return move


def did_player_win(board, s):
    ##### winning conditions #####

    # if they have three in one row
    for row in board:
        if all(cell == f"[{s}]" for cell in row):
            # print(f"Player {s} wins! - row")
            return True

    # if they have three in one column
    for col in range(3):
        if all(row[col] == f"[{s}]" for row in board):
            # print(f"Player {s} wins! - column")
            return True

    # for three in first diagonal
    if all(row[i] == f"[{s}]" for i, row in enumerate(board)):
        # print(f"Player {s} wins! - first diagonal")
        return True

    # for three in second diagonal
    if all(row[2 - i] == f"[{s}]" for i, row in enumerate(board)):
        # print(f"Player {s} wins! - second diagonal")
        return True

    return False


def display_board(board, move="", s=""):
    if len(move) > 0:
        row, column = [char for char in move]
        row, column = convert_move(row, column)
        # assign either X or O to the chosen cell, but first validate if it's empty
        board[row][column] = f"[{s}]"
    print_board(board)


def convert_move(row, column):
    # convert row and column values
    if row == "a":
        row = 0
    elif row == "b":
        row = 1
    elif row == "c":
        row = 2
    column = int(column) - 1
    return row, column


def print_board(board):
    for row in board:
        print("".join(row))


def rules():
    board_with_explanation = [
        ["  1 ", " 2 ", " 3 "],
        ["a", "[ ]", "[ ]", "[ ]"],
        ["b", "[ ]", "[ ]", "[ ]"],
        ["c", "[ ]", "[ ]", "[ ]"],
    ]
    print("*** RULES ***")
    print("Input the move with two characters: a/b/c for rows and 1/2/3 for columns.")
    print("Here's how the board looks:")
    print_board(board_with_explanation)
    print("___________ \n")


if __name__ == "__main__":
    main()
