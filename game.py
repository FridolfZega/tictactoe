WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def get_cell(x, y, w, h):
    col = min(x // (w // 3), 2)
    row = min(y // (h // 3), 2)
    return int(row * 3 + col)


def check_winner(board_state):
    for combo in WINNING_COMBINATIONS:
        a, b, c = combo
        if board_state[a] != "" and board_state[a] == board_state[b] == board_state[c]:
            return board_state[a], combo
    if all(cell != "" for cell in board_state):
        return "Draw", None
    return None, None


def reset_board():
    return [""] * 9


def make_move(board, cell, player):
    if 0 <= cell < 9 and board[cell] == "":
        board[cell] = player
        return True
    return False
