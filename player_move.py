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


print(player_move("hi", "X"))
