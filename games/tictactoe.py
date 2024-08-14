def check_win(board, p="X"):
    # a, b, c,
    # d, e, f,
    # g, h, i,
    a, b, c, d, e, f, g, h, i = board
    winning_boards = [
        [a, b, c], [d, e, f], [g, h, i],
        [a, d, g], [b, e, h], [c, f, i],
        [a, e, i], [c, e, g]
    ]

    for b in winning_boards:
        if b == [p,p,p]: return True
    return False

def swap_player(player):
    if player == "X": return "O"
    if player == "O": return "X"
    raise Exception(f"Unknown player '{player}'")

def perform_move(board, position, player): pass
    # TODO

def render_board(board):
    a, b, c, d, e, f, g, h, i = board
    line = "-" * 11
    print(f" {a} | {b} | {c} ")
    print(line)
    print(f" {d} | {e} | {f} ")
    print(line)
    print(f" {g} | {h} | {i} ")


def is_over(board):
    for b in board:
        if b == " ": return False
    return True

if __name__ == "__main__":
    board = [" "] * 9
    player = "X"

    while not is_over(board):
        try:
            render_board(board)

            field = int(input(f"[{player}] Podaj pole 1-9: ")) - 1

            if field < 0 or field > 8: raise Exception("Out of bounds")
            if field == -1: break
        except:
            print("Podano zle pole.")
            continue



        



