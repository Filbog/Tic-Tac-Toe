from tic_tac_toe import convert_move, did_player_win, player_move, get_player_names


def test_convert_move():
    assert convert_move("a", 2) == (0, 1)
    assert convert_move("c", 3) == (2, 2)


def test_did_player_win():
    board1 = [["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]]
    assert did_player_win(board1, "X") == False

    board2 = [["[X]", "[ ]", "[ ]"], ["[X]", "[ ]", "[ ]"], ["[X]", "[ ]", "[ ]"]]
    assert did_player_win(board2, "X") == True
    assert did_player_win(board2, "O") == False

    board3 = [["[ ]", "[O]", "[ ]"], ["[ ]", "[O]", "[ ]"], ["[ ]", "[O]", "[ ]"]]
    assert did_player_win(board3, "O") == True

    board4 = [["[X]", "[ ]", "[ ]"], ["[ ]", "[X]", "[ ]"], ["[ ]", "[ ]", "[X]"]]
    assert did_player_win(board4, "X") == True


#testing with a function using input - for this we use monkeypatch object
def test_player_move_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "c2")

    assert player_move("Mark", "X", ["a1", "b2"]) == "c2"

#testing a function using multiple inputs
def test_get_player_names(monkeypatch):
    names = iter(["Habibi", "Ebebebe"])
    monkeypatch.setattr("builtins.input", lambda _: next(names))
    assert get_player_names() == ("Habibi", "Ebebebe")
