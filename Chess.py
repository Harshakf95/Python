ImportError
ImportWarning
def main():
    board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
             ["P", "P", "P", "P", "P", "P", "P", "P"],
             [None]*8,
             [None]*8,
             [None]*8,
             [None]*8,
             ["p", "p", "p", "p", "p", "p", "p", "p"],
             ["r", "n", "b", "q", "k", "b", "n", "r"]]

    while True:
        display_board(board)
        move = input("Enter your move: ")
        if move.lower() == "quit":
            break
        if validate_move(move):
            start, end = parse_move(move)
            make_move(board, start, end)
        else:
            print("Invalid move. Please try again.")