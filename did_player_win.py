board = [["[ ]", "[ ]", "[X]"], ["[ ]", "[X]", "[ ]"], ["[X]", "[ ]", "[ ]"]]


def did_player_win(board, s):
    ##### winning conditions #####

    # if they have three in one row
    for row in board:
        if all(cell == f"[{s}]" for cell in row):
            print(f"Player {s} wins! - row")
            return True

    # if they have three in one column
    for col in range(3):
        if all(row[col] == f"[{s}]" for row in board):
            print(f"Player {s} wins! - column")
            return True

    # for three in first diagonal
    if all(row[i] == f"[{s}]" for i, row in enumerate(board)):
        print(f"Player {s} wins! - first diagonal")
        return True

    # for three in second diagonal
    if all(row[2 - i] == f"[{s}]" for i, row in enumerate(board)):
        print(f"Player {s} wins! - second diagonal")
        return True

    return False


did_player_win(board, "X")
