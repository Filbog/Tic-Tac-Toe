board = [
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
]


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

        #assign either X or O to the chosen cell
        board[row][column] = f"[{s}]"
    for row in board:
        print("".join(row))
        
    #saving the new value, and returning it(dunno if it's necessary tho)
    new_board = board
    return new_board


board = display_board(board, "a2", "X")
board = display_board(board, "c1", "O")
board = display_board(board, "b3", "X")
